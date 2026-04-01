#!/usr/bin/env python3
"""
Automated Digest Workflow
=========================

This script exactly replicates the manual workflow:
1. Runs Scripts/peters_digest.py to generate the raw data file.
2. Dynamically locates the generated raw data file from stdout.
3. Feeds raw data + context (GEMINI.md, AI_Guidelines.md) into the prompt (prompt_digest.md).
4. Prepends analysis output directly into the file below the header.
5. Emails the final document.
"""

import os
import sys
import subprocess
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google import genai
from google.genai import types

# ============================================================================
# CONFIGURATION
# ============================================================================

# Using Flash Lite latest which is the most reliable option for Free Tier quotas
GEMINI_MODEL = "gemini-flash-lite-latest"
MAX_RETRIES = 5
RETRY_DELAY_BASE = 10 # Increased delay for better 429 recovery

# File Paths
PROMPT_PATH = "Prompts/prompt_digest.md"
GEMINI_CONTEXT_PATH = "GEMINI.md"
AI_GUIDELINES_PATH = "AI_Guidelines.md"

def load_file(path):
    try:
        if os.path.exists(path):
            with open(path, 'r') as f:
                content = f.read()
                print(f"✓ Loaded {path} ({len(content)} chars)")
                return content
        print(f"⚠️ Warning: File not found at {path}")
        return ""
    except Exception as e:
        print(f"❌ Error reading {path}: {e}")
        return ""

def send_email(subject, body, user, password, to_email):
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(user, password)
            server.send_message(msg)
        print("✓ Email sent successfully!")
        return True
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return False

def main():
    api_key = os.getenv("GEMINI_API_KEY")
    email_user = os.getenv("EMAIL_USER")
    email_pass = os.getenv("EMAIL_PASSWORD")
    email_to = os.getenv("EMAIL_TO", email_user)
    
    if not all([api_key, email_user, email_pass]):
        print("❌ Error: Missing required environment variables (GEMINI_API_KEY, EMAIL_USER, EMAIL_PASSWORD)")
        sys.exit(1)

    # 1. Determine Today's File Path for Cache Check
    import datetime
    today = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    digest_dir = "Peter's Digest"
    cached_path = os.path.join(digest_dir, f"Daily_Digest_{today}.md")

    # 2. Generate Raw Data (Only if not already present)
    digest_path = None
    if os.path.exists(cached_path):
        print(f"✓ Found existing digest at {cached_path}. Skipping raw data generation to save API calls.")
        digest_path = cached_path
    else:
        print("Step 1: Generating raw data via peters_digest.py...")
        try:
            result = subprocess.run(
                [sys.executable, "Scripts/peters_digest.py", "--daily"], 
                capture_output=True, 
                text=True, 
                check=True
            )
            print(result.stdout)
            
            # Extract generated file path from stdout
            for line in result.stdout.split('\n'):
                if "Digest generated and saved to:" in line:
                    digest_path = line.split(":", 1)[1].strip()
                    break
        except subprocess.CalledProcessError as e:
            print(f"❌ Error running peters_digest.py:\n{e.stderr}")
            sys.exit(1)

    if not digest_path or not os.path.exists(digest_path):
        # Final fallback check
        if os.path.exists(cached_path):
            digest_path = cached_path
        else:
            print("❌ Error: Could not find or generate the raw data file.")
            sys.exit(1)
        
    print(f"✓ Target file identified: {digest_path}")

    with open(digest_path, 'r') as f:
        digest_content = f.read()

    # 3. Prepare AI Environment
    prompt_digest = load_file(PROMPT_PATH)
    gemini_md = load_file(GEMINI_CONTEXT_PATH)
    ai_guidelines = load_file(AI_GUIDELINES_PATH)

    if not prompt_digest:
        print("❌ Error: prompt_digest.md is empty or missing.")
        sys.exit(1)

    client = genai.Client(api_key=api_key)
    
    system_instruction = f"""
{prompt_digest}

### REFERENCE FRAMEWORKS ###
---
{gemini_md}
---
{ai_guidelines}

### AUTOMATION OVERRIDE ###
You are running headlessly. Skip all 'STOP. Wait for user approval' steps. 
Generate the analysis output immediately based strictly on the provided raw data.
"""
    
    # 4. Run Analysis with Retry Logic
    print(f"Step 2: Executing prompt_digest.md via {GEMINI_MODEL}...")
    analysis = None
    
    for attempt in range(MAX_RETRIES):
        try:
            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=f"DATA INTAKE:\n\n{digest_content}",
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                    temperature=0.2,
                )
            )
            analysis = response.text
            if analysis:
                break
        except Exception as e:
            print(f"⚠️ Attempt {attempt + 1} failed: {e}")
            if attempt < MAX_RETRIES - 1:
                wait_time = RETRY_DELAY_BASE * (2 ** attempt)
                print(f"⏳ Retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                print("❌ Max retries reached. Exiting.")
                sys.exit(1)
    
    if not analysis:
        print("❌ Analysis failed: Empty response.")
        sys.exit(1)
    print(f"✓ Analysis received ({len(analysis)} chars)")

    # 5. Prepend Analysis (below 3-line header)
    lines = digest_content.split('\n')
    header = lines[:3]
    body = lines[3:]
    
    final_report = "\n".join(header) + "\n\n" + analysis + "\n\n---\n\n" + "\n".join(body)

    with open(digest_path, 'w') as f:
        f.write(final_report)
    print(f"✓ Analysis prepended to {digest_path}")

    # 6. Email Final Report
    print("Step 3: Emailing completed digest...")
    filename = os.path.basename(digest_path).replace(".md", "")
    subject = f"Peter's Market Digest & Screening - {filename}"
    send_email(subject, final_report, email_user, email_pass, email_to)

if __name__ == "__main__":
    main()
