#!/usr/bin/env python3
"""
Analyze Market Digest & Send Email
==================================

This script:
1. Reads a generated market digest (Markdown).
2. Uses the Gemini API (google-genai SDK) to analyze the data.
3. Inserts the analysis into the digest.
4. Emails the final report via Gmail SMTP.

Requires:
    - GEMINI_API_KEY
    - EMAIL_USER (pyratecru@gmail.com)
    - EMAIL_PASSWORD (App Password)
    - EMAIL_TO (pyratecru@gmail.com)
"""

import os
import sys
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google import genai
from google.genai import types

# ============================================================================
# CONFIGURATION
# ============================================================================

# Using the latest model as requested
GEMINI_MODEL = "gemini-3.0-pro"

# File Paths
PROMPT_PATH = "guidance/prompts/news_analysis.md"
GENERAL_GUIDELINES_PATH = "guidance/frameworks/stock_analysis_guidelines.md"
AI_GUIDELINES_PATH = "guidance/frameworks/ai_stock_analysis.md"

def load_file(path):
    try:
        if os.path.exists(path):
            with open(path, 'r') as f:
                return f.read()
        return ""
    except Exception as e:
        print(f"Error reading {path}: {e}")
        return ""

def send_email(subject, body, user, password, to_email):
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(user, password)
        server.send_message(msg)
        server.quit()
        print("✓ Email sent successfully!")
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

def main():
    # 1. Verify Environment
    api_key = os.getenv("GEMINI_API_KEY")
    email_user = os.getenv("EMAIL_USER")
    email_pass = os.getenv("EMAIL_PASSWORD")
    email_to = os.getenv("EMAIL_TO", email_user)
    
    if not all([api_key, email_user, email_pass]):
        print("Error: Missing required environment variables (GEMINI_API_KEY, EMAIL_USER, EMAIL_PASSWORD)")
        sys.exit(1)

    # 2. Get Input Data (from stdin)
    digest_content = sys.stdin.read()
    if not digest_content:
        print("Error: No digest content found in stdin.")
        sys.exit(1)

    # 3. Prepare AI Client
    client = genai.Client(api_key=api_key)
    
    news_prompt = load_file(PROMPT_PATH)
    general_guidelines = load_file(GENERAL_GUIDELINES_PATH)
    ai_guidelines = load_file(AI_GUIDELINES_PATH)

    system_instruction = f"""
{news_prompt}

### REFERENCE FRAMEWORKS ###
---
{general_guidelines}
---
{ai_guidelines}
"""
    
    # 4. Analyze
    print(f"Analyzing market data with {GEMINI_MODEL}...")
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
    except Exception as e:
        print(f"Gemini API Error: {e}")
        sys.exit(1)
    
    if not analysis:
        print("Analysis failed: Empty response.")
        sys.exit(1)

    # 5. Reconstruct Digest
    lines = digest_content.split('\n')
    header = lines[:3]
    rest = lines[3:]
    
    final_report = "\n".join(header) + "\n\n" + analysis + "\n\n---\n\n" + "\n".join(rest)

    # 6. Save locally (backup)
    os.makedirs("data/discovery", exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"data/discovery/Daily_Digest_{today}.md"
    with open(filename, 'w') as f:
        f.write(final_report)
    print(f"✓ Saved locally to {filename}")

    # 7. Send Email
    subject = f"Market Analysis Digest - {today}"
    send_email(subject, final_report, email_user, email_pass, email_to)

if __name__ == "__main__":
    main()
