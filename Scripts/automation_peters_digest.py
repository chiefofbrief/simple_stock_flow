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
import re
from email.message import EmailMessage

# Try to import google-genai
try:
    from google import genai
    from google.genai import types
except ImportError:
    print("❌ Error: google-genai SDK not installed.")
    sys.exit(1)

# ============================================================================
# CONFIGURATION
# ============================================================================

# Using Gemini 2.5 Pro for flagship reasoning quality (Paid Tier)
GEMINI_MODEL = "gemini-2.5-pro"
MAX_RETRIES = 5
RETRY_DELAY_BASE = 10 
ANALYSIS_MARKER = "<!-- ANALYSIS_COMPLETE -->"

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

import markdown

def send_email(subject, body, user, password, to_email):
    # Ensure no accidental whitespace from Secrets
    user = user.strip()
    password = password.strip()
    to_email = to_email.strip()
    
    # Create the modern EmailMessage object
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = user
    msg['To'] = to_email
    
    # Set the Plain Text version (Markdown)
    msg.set_content(body, cte='quoted-printable')
    
    # Generate and add the HTML version
    html_style = """
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; }
        h1 { color: #1a365d; border-bottom: 2px solid #1a365d; padding-bottom: 10px; }
        h2 { color: #2c5282; margin-top: 30px; border-bottom: 1px solid #e2e8f0; }
        h3 { color: #2b6cb0; margin-top: 20px; }
        table { border-collapse: collapse; width: 100%; margin: 20px 0; font-size: 14px; }
        th { background-color: #f7fafc; border: 1px solid #e2e8f0; padding: 12px; text-align: left; color: #4a5568; }
        td { border: 1px solid #e2e8f0; padding: 12px; text-align: left; }
        tr:nth-child(even) { background-color: #f8fafc; }
        li { margin-bottom: 8px; }
        hr { border: 0; border-top: 1px solid #e2e8f0; margin: 30px 0; }
        blockquote { border-left: 4px solid #e2e8f0; padding-left: 16px; color: #718096; font-style: italic; }
    </style>
    """
    
    # Convert Markdown to HTML
    html_content = markdown.markdown(body, extensions=['tables', 'fenced_code', 'nl2br'])
    full_html = f"<html><head>{html_style}</head><body>{html_content}</body></html>"
    
    msg.add_alternative(full_html, subtype='html')
    
    try:
        # Use Port 587 with STARTTLS
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(user, password)
        # Use sendmail for explicit envelope control
        server.sendmail(user, [to_email], msg.as_string())
        server.quit()
        print("✓ Email sent successfully!")
        return True
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return False

def main():
    api_key = os.getenv("GEMINI_API_KEY")
    email_user = os.getenv("EMAIL_USER")
    email_pass = os.getenv("EMAIL_PASSWORD")
    
    # Handle GitHub Actions passing empty strings for missing secrets
    email_to = os.getenv("EMAIL_TO")
    if not email_to:
        email_to = email_user
    
    if not all([api_key, email_user, email_pass]):
        print("❌ Error: Missing required environment variables (GEMINI_API_KEY, EMAIL_USER, EMAIL_PASSWORD)")
        sys.exit(1)

    # 1. Determine Today's File Path for Cache Check
    import datetime
    today = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    digest_dir = "Peter's Digest"
    cached_path = os.path.join(digest_dir, f"Daily_Digest_{today}.md")

    # 2. Generate Raw Data (Only if not already present AND clean)
    digest_path = None
    force_generation = False
    
    if os.path.exists(cached_path):
        with open(cached_path, 'r') as f:
            existing_data = f.read()
        
        if "Error running" in existing_data:
            print("⚠️ Existing digest contains module errors. Forcing re-generation to try Perigon key again.")
            force_generation = True
        else:
            print(f"✓ Found clean existing digest at {cached_path}. Skipping raw data generation.")
            digest_path = cached_path

    if not digest_path or force_generation:
        print("Step 1: Generating raw data via peters_digest.py...")
        try:
            result = subprocess.run(
                [sys.executable, "Scripts/peters_digest.py", "--daily"], 
                capture_output=True, 
                text=True, 
                check=True,
                env=os.environ.copy() # Explicitly share API keys with sub-scripts
            )
            print(result.stdout)
            
            for line in result.stdout.split('\n'):
                if "Digest generated and saved to:" in line:
                    digest_path = line.split(":", 1)[1].strip()
                    break
        except subprocess.CalledProcessError as e:
            print(f"❌ Error running peters_digest.py:\n{e.stderr}")
            sys.exit(1)

    if not digest_path or not os.path.exists(digest_path):
        if os.path.exists(cached_path):
            digest_path = cached_path
        else:
            print("❌ Error: Could not find or generate the raw data file.")
            sys.exit(1)
        
    print(f"✓ Target file identified: {digest_path}")

    with open(digest_path, 'r') as f:
        digest_content = f.read()

    # 3. Cleanup existing analysis if present (Prevent duplication)
    # We find the first occurrence of the separator and keep everything after it
    if ANALYSIS_MARKER in digest_content:
        print("✓ Analysis marker found. Cleaning up existing analysis blocks.")
        # Everything after the separator is the raw data
        parts = digest_content.split("---\n\n", 1)
        if len(parts) > 1:
            digest_content = parts[1]
            # Strip the remaining "---" if it was part of the old prepended block
            # (Matches the # Title, Date, --- pattern)
            lines = digest_content.split('\n')
            if len(lines) > 3 and "---" in lines[2]:
                digest_content = "\n".join(lines[3:])

    # 4. Prepare AI Environment
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

### AUTOMATION OVERRIDE: HEADLESS EXECUTION ###
You are running in a fully automated, headless pipeline. There is NO human in the loop.
- Output ONLY the final Markdown analysis. Start directly with the first header.
- DO NOT include any conversational filler, confirmation questions, or meta-commentary.
- DO NOT include phrases like "Action:", "Shall I proceed", or "Do you approve".
- Treat this as a direct write-to-file operation with zero conversational output.
"""
    
    # 5. Run Analysis with Retry Logic
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

    # 6. Reconstruct Digest (Prepend analysis below 3-line header)
    # We handle the header separately from the body to ensure clean prepending
    lines = digest_content.split('\n')
    header = lines[:3]
    body = lines[3:]
    
    final_report = ANALYSIS_MARKER + "\n" + "\n".join(header) + "\n\n" + analysis + "\n\n---\n\n" + "\n".join(body)

    with open(digest_path, 'w') as f:
        f.write(final_report)
    print(f"✓ Analysis prepended to {digest_path}")

    # 7. Email Final Report
    print("Step 3: Emailing completed digest...")
    subject = f"Peter's Digest - {today}"
    email_success = send_email(subject, final_report, email_user, email_pass, email_to)
    
    if not email_success:
        print("❌ Workflow failed at the email step.")
        sys.exit(1)
    
    print("✓ Workflow completed successfully.")

if __name__ == "__main__":
    main()
