#!/usr/bin/env python3
"""
Reddit Top Posts Fetcher (via SociaVault API)
==============================================

Fetches top posts from investment subreddits.
Returns Title, Description, and Top 3 Comments by upvotes.
"""

import os
import sys
import argparse
import requests
import time

# ============================================================================
# CONFIGURATION
# ============================================================================

SOCIAVAULT_BASE_URL = "https://api.sociavault.com/v1"
MIN_SCORE_THRESHOLD = 0
SUBREDDITS = ["ValueInvesting", "stocks"]
MAX_POSTS_PER_SUB = 15

BOT_KEYWORDS = ["i am a bot", "action was performed automatically", "contact the moderators", "rule", "submission statement", "permalink"]

def is_bot_noise(text):
    if not text: return False
    return any(k in text.lower() for k in BOT_KEYWORDS)

def fetch_reddit(api_key, timeframe="day", limit_comments=None, limit_subs=None):
    headers = {"X-API-Key": api_key, "Content-Type": "application/json"}
    all_results = {}

    subs_to_run = SUBREDDITS[:limit_subs] if limit_subs else SUBREDDITS

    for sub in subs_to_run:
        try:
            params = {"subreddit": sub, "timeframe": timeframe, "sort": "top", "trim": False}
            r = requests.get(f"{SOCIAVAULT_BASE_URL}/scrape/reddit/subreddit", headers=headers, params=params, timeout=30)
            r.raise_for_status()
            
            raw = r.json().get('data', {}).get('posts', [])
            posts = raw if isinstance(raw, list) else list(raw.values()) if isinstance(raw, dict) else []
            filtered = [p for p in posts if p.get('score', 0) >= MIN_SCORE_THRESHOLD]
            filtered.sort(key=lambda x: x.get('score', 0), reverse=True)
            
            display_posts = filtered[:MAX_POSTS_PER_SUB]
            posts_for_comments = display_posts[:limit_comments] if limit_comments is not None else display_posts
            
            for p in display_posts:
                p['top_comments'] = []
                if p in posts_for_comments:
                    # SociaVault returns `url` as the full Reddit thread URL
                    thread_url = p.get('url')

                    try:
                        time.sleep(0.5)
                        c_r = requests.get(f"{SOCIAVAULT_BASE_URL}/scrape/reddit/post/comments", headers=headers, params={"url": thread_url, "trim": True}, timeout=20)
                        if c_r.status_code == 200:
                            c_raw = c_r.json().get('data', {}).get('comments', [])
                            comments = c_raw if isinstance(c_raw, list) else list(c_raw.values()) if isinstance(c_raw, dict) else []
                            comments.sort(key=lambda x: x.get('score', 0), reverse=True)
                            p['top_comments'] = comments[:3]
                    except:
                        pass
            
            all_results[sub] = display_posts
        except Exception as e:
            print(f"Error fetching r/{sub}: {e}", file=sys.stderr)
            
    return all_results

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--timeframe', default="day")
    parser.add_argument('--verify', action='store_true')
    args = parser.parse_args()

    api_key = os.environ.get('SOCIAVAULT_API_KEY')
    if not api_key:
        print("Error: Missing SOCIAVAULT_API_KEY", file=sys.stderr)
        return

    if args.verify:
        results = fetch_reddit(api_key, args.timeframe, limit_comments=1, limit_subs=1)
    else:
        results = fetch_reddit(api_key, args.timeframe)

    print("## Reddit Top Posts")
    for sub, posts in results.items():
        if not posts: continue
        print(f"### r/{sub}")
        for i, p in enumerate(posts, 1):
            title = p.get('title', 'No Title').strip()
            score = p.get('score', 0)
            url = p.get('url', '#')
            
            print(f"#### {i}. {title}")
            print(f"**Score:** ↑{score:,} — [View Thread]({url})")
            
            if p.get('selftext'):
                print(f"\n> {p.get('selftext').strip()}")

            comments = p.get('top_comments', [])
            if comments:
                print("\n**Top Comments:**")
                for c in comments:
                    author = c.get('author', 'unknown')
                    c_score = c.get('score', 0)
                    # Flatten to single line so bullet formatting stays intact
                    body = ' '.join(p for p in c.get('body', '').strip().splitlines() if p.strip())
                    if is_bot_noise(body):
                        print(f"* **[BOT] u/{author}** (↑{c_score}): {body}")
                    else:
                        print(f"* **u/{author}** (↑{c_score}): {body}")
            print("\n---")

if __name__ == "__main__":
    main()
