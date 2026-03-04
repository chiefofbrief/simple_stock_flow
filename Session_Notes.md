# Session Notes
*(Temporary scratchpad for active session commands, thoughts, and feedback. Wiped regularly.)*

## Session Status / Next Steps

---

## Pending Updates

### Discovery
- **prompt_digest.md**: Apply the sequential "Active Workflow" (Read -> Analyze -> Ask -> Write), and match the format (e.g., role) to `prompt_price.md` and `prompt_earnings.md`. See `prompt_price.md` and `prompt_earnings.md` as examples. 
- **prompt_digest.md**: Leverage new GEMINI.md analysis section. We want to point to this, not repeat it. 
- **prompt_discovery.md**: Apply the sequential "Active Workflow" (Read -> Analyze -> Ask -> Write), and match the format (e.g., role) to `prompt_price.md` and `prompt_earnings.md`. See `prompt_price.md` and `prompt_earnings.md` as examples.
- **prompt_discovery.md**: Leverage new GEMINI.md analysis section. We want to point to this, not repeat it.
- **prompt_discovery.md**: Incorporate new `[TAILWIND]` tagging logic for newly identified candidates.

### Screening
- **Earnings Prompt Alignment:** Implement the same descriptive summary, examples, and `GEMINI.md` integration for `prompt_earnings.md` as was done for the Price phase (FOR CONTEXT:  Added 10 high-signal analysis examples to `prompt_price.md` to distinguish between "Temporary" and "Permanent" losers. Integrated a mandatory step to read `GEMINI.md` at the start of the workflow to ensure foundational analysis philosophy (e.g., Margin of Safety) is applied before data analysis. Updated Price summaries to be more descriptive and metric-heavy.)
- Are `prompt_price.md` and `prompt_earnings.md` appending the full Q&A to the screening files?

### Deep Dive
-  Deep Dive prompts need to be updated to write full Q&A reports to Thesis files instead of just summary paragraphs (e.g., HIMS).

### Thesis:
- Create a dedicated `prompt_thesis_synthesis.md` (or similar) to standardize the final review and recommendation step.

---

## Future Updates & Considerations (NOT TO BE ADDRESSED NOW)

**Immediate Items**
- Properly leverage the Indexes
    - Use planning – have the llm describe the sequence of actions it will take.
- Peer comparisons.

**Skills Marketplace** 
- /plugins for skills marketplace

**Autonomous Agents & Tools**
- Make it autonomous. Give it a list of tools and general structure, but let it decide which tools to use when. Tools and Skills and Agents: Consider turning the scripts into tools (?) and prompts into skills/agents(?)
- Skill should have yaml with name and description. Also good to have overview section.
- /skills to see skills you have
- Launch subagents to work in parallel/divide tasks. Subagents get their own context window and can return results to a main agent.
- /agents to create agent.
- Agents can get their own prompt and skills and tools (you ned to specify the tools), even model (have agents assigned to different roles).
- You can include shell commands in files (aka commands).

**Evaluation (Responses & Tools)** 
- Don't focus on just the final output. Rate the intetmediate ouputs: Use reflection (consider using diff models for initial output and eval/refined output). 
- Look at what tools are doing (steps, calls, errors).
- Look at other prompts for ideas. 

**Search & Database Capabilities**
- Web search is not necessarily an LLM function only. RAG may not be either
- https://docs.cloud.google.com/generative-ai-app-builder/docs/migrate-from-cse
- SQL database: use a function that turns your natural-language questions into SQL queries. You provide your question and the database schema as input. The LLM then generates the SQL query that answers your question.

**Tools & Libraries to Consider**:
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

## Tools

### Options APIs
* https://www.marketdata.app/pricing/
* https://alpaca.markets/
* https://tradier.com/individuals/pricing
