## Workflow Update

We finished version 0.5 of the workflow on 02-23-2026. Changes mades included: 
   * Workflow V1 Setup: Created WORKFLOW v1 directory structure.
   * Script Migration: Moved peters_digest.py, price.py, earnings.py, shared_utils.py and all digest scripts to WORKFLOW v1/Scripts/.
   * Path Updates: Updated peters_digest.py to point to the new location of digest scripts and save output to WORKFLOW v1/Peter's Digest/. Updated docs/COMMANDS.md.
   * Prompt Creation: Created WORKFLOW v1/Prompts/price_analysis_prompt.md.
   * Execution: Ran Peter's Digest for today.
   * Analysis: Generated and prepended the market analysis to the daily digest file.
   * Git Sync: Pushed all changes to the remote repository.
   * Stock Tracker Update: Added "Earnings/Valuation Analysis" section to WORKFLOW v1/Stock Tracker.md.
   * Earnings Prompt: Created WORKFLOW v1/Prompts/earnings_analysis_prompt.md with specific analysis questions and data inputs.
   * Financials Script: Created WORKFLOW v1/Scripts/financials.py to fetch FMP data (Annual & Quarterly), calculate Earnings Risk, Quality, and ROI metrics, and generate detailed
     markdown reports with statistical analysis (CAGR, CV, Deltas).
   * Script Validation: Verified financials.py accuracy against AAPL SEC filings and confirmed manual TTM calculation logic.
   * Tracker Enhancements: Added "Earnings Risk", "Earnings Quality", and "ROI" subsections to WORKFLOW v1/Stock Tracker.md.
   * Script Update (Quarterly Data): Enhanced financials.py to output "Recent Quarterly Trends" (last 4 quarters + deltas) alongside the annual data tables.
   * Script Testing: Verified the enhanced financials.py output with AAPL.
   * Metrics Prompts: Created WORKFLOW v1/Prompts/earnings_risk_prompt.md, earnings_quality_prompt.md, and roi_prompt.md with interchangeable roles and specific metrics.
   * Prompt Consolidation: Consolidated earnings_risk, earnings_quality, and roi prompts into a single WORKFLOW v1/Prompts/prompt_financials.md, updated with a refined metrics list
     and embedded guidance.
   * Prompt Renaming: Renamed all analysis prompts to follow the prompt_.md convention (prompt_price.md, prompt_earnings.md, prompt_financials.md).
   * Financials Script Update: Updated WORKFLOW v1/Scripts/financials.py to match the new prompt_financials.md structure (flattened JSON, single table output, updated metrics).
     Verified with AAPL.
   * Sentiment Prompt Creation: Created WORKFLOW v1/Prompts/prompt_sentiment.md for analyzing news and social media sentiment.
   * Sentiment Script Migration: Migrated scripts/sentiment.py and dependencies (news.py, reddit.py, etc.) to WORKFLOW v1/Scripts/ and WORKFLOW v1/Scripts/Sentiment Scripts/.
   * Sentiment Script Optimization: Fixed a bug in the YouTube script and lowered Reddit engagement thresholds (10 upvotes, 0 comments) to capture more data. Verified with AAPL.
   * Archive Cleanup: Archived old sentiment scripts to archive/scripts/ with _old suffixes to prevent confusion.
   * Sentiment Lookback Update: Updated WORKFLOW v1/Scripts/Sentiment Scripts/reddit.py and WORKFLOW v1/Scripts/sentiment.py to use a 90-day (3-month) lookback period by default.
   * Footnotes Prompt Creation: Created WORKFLOW v1/Prompts/prompt_footnotes.md for analyzing MD&A and footnotes, ensuring consistency with other analysis prompts.
   * SEC Filings Script Migration: Migrated sec_filings.py to WORKFLOW v1/Scripts/ and updated it to use the new shared_utils location.
   * SEC Filings Script Optimization: Enhanced sec_filings.py with robust extraction logic (whitespace normalization, flexible regex) to correctly handle 10-Q Notes sections, fixing a failure on AAPL. Verified successful extraction for both AAPL and AMZN.
   * Earnings Call Prompt Creation: Created WORKFLOW v1/Prompts/prompt_earnings_calls.md for analyzing earnings call transcripts, focusing on management tone shifts and alignment
     with previous financial/sentiment analyses.
   * Earnings Call Script Implementation: Developed WORKFLOW v1/Scripts/earnings_calls.py to fetch the two most recent quarterly transcripts via AlphaVantage, processing them into a
     consolidated markdown file with clear "Prepared Remarks" and "Q&A" sections for LLM analysis.
   * Earnings Call Script Testing: Verified earnings_calls.py functionality with IBM and AMZN, confirming correct quarter detection (2025Q4/2025Q3), file generation, and markdown
     structure.


-----------------------------------------

## Future Updates/Considerations

**Immediate items**
- Properly leverage the Indexes
      - Use planning – have the llm describe the sequence of actions it will take.
- Peer comparisons.

**There is a Skills marketplace** 
- /plugins for skills marketplace

**Make it autonomous. Give it a list of tools and general structure, but let it decide which tools to use when. Tools and Skills and Agents: Consider turning the scripts into tools (?) and prompts into skills/agents(?)**
- Skill should have yaml with name and description. Also good to have overview section.
- /skills to see skills you have
- Launch subagents to work in parallel/divide tasks. Subagents get their own context window and can return results to a main agent.
- /agents to create agent.
- Agents can get their own prompt and skills and tools (you ned to specify the tools), even model (have agents assigned to different roles).
- You can include shell commands in files (aka commands).

**Evaluate responses, tools, etc** 
- Don't focus on just the final output. Rate the intetmediate ouputs: Use reflection (consider using diff models for initial output and eval/refined output). 
- Look at what ools are doing (steps, calls, errors).
- Look at other prompts for ideas. 

**Web search is not necessarily an LLM function only. RAG may not be either**
- https://docs.cloud.google.com/generative-ai-app-builder/docs/migrate-from-cse
- SQL database: use a function that turns your natural-language questions into SQL queries. You provide your question and the database schema as input. The LLM then generates the SQL query that answers your question.

**Tools to Consider**:
- Github Actions: Can be setup with a command: /setup github-actions.
- Google: Big query database on google cloud.
- Google: Flask dashboard.
- Andrew's pakacge (lets you use multiple models): aisuite==0.1.11.
- vertexai (agents?)
- sqlalchemy
- pydantic
- uvicorn
- notebook experience: ipywidgets, jupyter_server, nbclassic, notebook.
- data analysis/display: duckdb, matplotlib, pandas, seaborn, tabulate, tinydb.
- Machine Learning / NLP: jinja2, psycopg2-binary, scikit-learn.
- json for handling structured data.
- pandas for working with tabular data.
- dotenv to load environment variables (e.g., API keys)
- Google workspace extensions (or gmail) for emails








4. Notes (financial statments) / MD&A:
    - What do the filings reveal about questions/concerns raised by prior analyses?
    - Do the filings align with prior analyses, or are there areas of divergence?
    - Are there risks that were not identified in prior analyses?

