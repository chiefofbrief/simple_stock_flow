#!/usr/bin/env python3
"""
Automated Tracker Priority Workflow
=====================================

1. Runs Scripts/tracker_update.py to refresh all market data columns in Stock_Tracker.md.
2. Feeds Stock_Tracker.md + context files into prompt_tracker_priority.md via Vertex AI.
3. Writes the priority section to the top of Stock_Tracker.md, replacing any existing
   priority section (identified by the <!-- PRIORITY_COMPLETE --> marker).
4. Emails the priority section as a formatted HTML email.
5. Commits the updated Stock_Tracker.md to git.
"""

import os
import sys
import subprocess
import time
import datetime
import smtplib
from email.message import EmailMessage

import markdown

try:
    import vertexai
    from vertexai.generative_models import GenerativeModel
except ImportError:
    print("❌ Error: google-cloud-aiplatform SDK not installed.")
    sys.exit(1)

# ============================================================================
# CONFIGURATION
# ============================================================================

GEMINI_MODEL = "gemini-2.5-pro"
MAX_RETRIES = 5
RETRY_DELAY_BASE = 10

PRIORITY_MARKER = "<!-- PRIORITY_COMPLETE -->"
TRACKER_HEADER = "# Ticker Tracker"

TRACKER_PATH = "Stock_Tracker.md"
PROMPT_PATH = "Prompts/prompt_tracker_priority.md"
GEMINI_MD_PATH = "GEMINI.md"
CONTEXT_MARKETS_PATH = "context_markets.md"
CONTEXT_AI_SC_PATH = "context_ai_supply_chain.md"


# ============================================================================
# HELPERS
# ============================================================================

def load_file(path):
    try:
        if os.path.exists(path):
            with open(path, 'r') as f:
                content = f.read()
            print(f"✓ Loaded {path} ({len(content)} chars)")
            return content
        print(f"⚠️  Warning: File not found at {path}")
        return ""
    except Exception as e:
        print(f"❌ Error reading {path}: {e}")
        return ""


def send_email(subject, body, user, password, to_email):
    user = user.strip()
    password = password.strip()
    to_email = to_email.strip()

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = user
    msg['To'] = to_email

    msg.set_content(body, cte='quoted-printable')

    html_style = """
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #333; max-width: 680px; margin: 0 auto; padding: 20px; }
        h1 { color: #1a365d; border-bottom: 2px solid #1a365d; padding-bottom: 10px; }
        h2 { color: #2c5282; margin-top: 30px; border-bottom: 1px solid #e2e8f0; padding-bottom: 6px; }
        h3 { color: #2b6cb0; margin-top: 20px; }
        li { margin-bottom: 8px; }
        strong { color: #1a202c; }
        hr { border: 0; border-top: 1px solid #e2e8f0; margin: 24px 0; }
        p { margin: 8px 0; }
    </style>
    """

    html_content = markdown.markdown(body, extensions=['fenced_code', 'nl2br'])
    full_html = f"<html><head>{html_style}</head><body>{html_content}</body></html>"
    msg.add_alternative(full_html, subtype='html')

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, [to_email], msg.as_string())
        server.quit()
        print("✓ Email sent successfully.")
        return True
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return False


# ============================================================================
# MAIN
# ============================================================================

def main():
    project_id = os.getenv("PROJECT_ID")
    location = os.getenv("LOCATION", "us-central1")
    email_user = os.getenv("EMAIL_USER")
    email_pass = os.getenv("EMAIL_PASSWORD")
    email_to = os.getenv("EMAIL_TO") or email_user

    if not project_id:
        print("❌ Error: Missing required environment variable PROJECT_ID")
        sys.exit(1)

    today = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")

    # ------------------------------------------------------------------
    # Step 1: Refresh market data
    # ------------------------------------------------------------------
    print("Step 1: Refreshing market data via tracker_update.py...")
    try:
        result = subprocess.run(
            [sys.executable, "Scripts/tracker_update.py"],
            capture_output=True,
            text=True,
            check=True,
            env=os.environ.copy(),
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"❌ tracker_update.py failed:\n{e.stderr}")
        sys.exit(1)
    print("✓ Market data refreshed.")

    # ------------------------------------------------------------------
    # Step 2: Load files
    # ------------------------------------------------------------------
    print("\nStep 2: Loading context files...")
    prompt = load_file(PROMPT_PATH)
    gemini_md = load_file(GEMINI_MD_PATH)
    context_markets = load_file(CONTEXT_MARKETS_PATH)
    context_ai_sc = load_file(CONTEXT_AI_SC_PATH)
    tracker_content = load_file(TRACKER_PATH)

    if not prompt:
        print("❌ Error: prompt_tracker_priority.md is empty or missing.")
        sys.exit(1)
    if not tracker_content:
        print("❌ Error: Stock_Tracker.md is empty or missing.")
        sys.exit(1)

    # Strip existing priority section so the model only sees the tracker data
    raw_tracker = tracker_content
    if PRIORITY_MARKER in tracker_content:
        idx = tracker_content.find(TRACKER_HEADER)
        if idx != -1:
            raw_tracker = tracker_content[idx:]
            print("✓ Stripped existing priority section from tracker input.")

    # ------------------------------------------------------------------
    # Step 3: Call Gemini
    # ------------------------------------------------------------------
    system_instruction = f"""{prompt}

### CONTEXT FILES ###

--- GEMINI.md ---
{gemini_md}

--- context_markets.md ---
{context_markets}

--- context_ai_supply_chain.md ---
{context_ai_sc}

### AUTOMATION OVERRIDE: HEADLESS EXECUTION ###
You are running in a fully automated, headless pipeline. There is NO human in the loop.
- Output ONLY the priority section content. Start directly with the `<!-- PRIORITY_COMPLETE -->` marker.
- DO NOT include any conversational filler, confirmation questions, or meta-commentary.
- Treat this as a direct write-to-file operation with zero conversational output.
"""

    print(f"\nStep 3: Running priority analysis via {GEMINI_MODEL} (Vertex AI)...")
    vertexai.init(project=project_id, location=location)
    model = GenerativeModel(
        model_name=GEMINI_MODEL,
        system_instruction=[system_instruction],
    )

    priority_output = None
    for attempt in range(MAX_RETRIES):
        try:
            response = model.generate_content(
                f"STOCK TRACKER DATA:\n\n{raw_tracker}",
                generation_config={"temperature": 0.2},
            )
            priority_output = response.text
            if priority_output:
                break
        except Exception as e:
            print(f"⚠️  Attempt {attempt + 1} failed: {e}")
            if attempt < MAX_RETRIES - 1:
                wait_time = RETRY_DELAY_BASE * (2 ** attempt)
                print(f"⏳ Retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                print("❌ Max retries reached. Exiting.")
                sys.exit(1)

    if not priority_output:
        print("❌ Analysis failed: Empty response.")
        sys.exit(1)
    print(f"✓ Priority output received ({len(priority_output)} chars)")

    # ------------------------------------------------------------------
    # Step 4: Write priority section to top of Stock_Tracker.md
    # ------------------------------------------------------------------
    print("\nStep 4: Writing priority section to Stock_Tracker.md...")
    final_content = priority_output.strip() + "\n\n---\n\n" + raw_tracker

    with open(TRACKER_PATH, 'w') as f:
        f.write(final_content)
    print(f"✓ Priority section written to {TRACKER_PATH}")

    # ------------------------------------------------------------------
    # Step 5: Email the priority section
    # ------------------------------------------------------------------
    if email_user and email_pass:
        print("\nStep 5: Emailing priority list...")
        # Strip the HTML marker line before emailing — just the markdown content
        email_body = priority_output.replace(PRIORITY_MARKER, "").strip()
        send_email(
            subject=f"Tracker Priority — {today}",
            body=email_body,
            user=email_user,
            password=email_pass,
            to_email=email_to,
        )
    else:
        print("\nStep 5: Skipping email (EMAIL_USER / EMAIL_PASSWORD not set).")

    # ------------------------------------------------------------------
    # Step 6: Commit to git
    # ------------------------------------------------------------------
    print("\nStep 6: Committing updated tracker...")
    try:
        subprocess.run(["git", "add", TRACKER_PATH], check=True)
        subprocess.run(
            ["git", "commit", "-m", f"chore: update tracker priority and market data {today} [skip ci]"],
            check=True,
        )
        print("✓ Committed.")
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Git commit step: {e} (may be no changes)")

    print("\n✓ Tracker priority workflow completed successfully.")


if __name__ == "__main__":
    main()
