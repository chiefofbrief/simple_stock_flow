# Project Setup: LLM Stock Analysis

## Phase 1: Discovery & Documentation
- [ ] **Identify Outputs:** Review `COMMANDS.md` and script executions to ensure *all* script outputs are documented and verified.
- [ ] **Index Codebase:** Create a "Context Map" (file index) for the LLM to understand the project structure and file purposes.
- [ ] **Review Guidance:** Audit existing files in `Guidance/` (Stock Analysis, News Analysis) and integrate external skill files (News Analysis, Statement Analysis) if available.

## Phase 2: Infrastructure & Setup
- [ ] **Setup Directory:** Populate the `setup/` directory with configuration and maintenance files.
- [ ] **Dependency Management:** Create a `requirements.txt` for all Python scripts (likely in `setup/` or root).
- [ ] **Commands Documentation:** Move/Refine `COMMANDS.md` into the `setup/` structure if appropriate.
- [ ] **Data Standardization:** Ensure all scripts save outputs to `data/` in a consistent format (JSON/Markdown) for LLM consumption.

## Phase 3: Automation (Master Commands)
*Note: Master command composition to be defined step-by-step.*
- [ ] **Define Workflows:** Collaboratively define the exact scripts and order for "Market News", "Stock Screening", and "Deep Dive" commands.
- [ ] **Implement Master Scripts:** Create the shell scripts or Python wrappers to execute these defined workflows.

## Phase 4: LLM Integration
- [ ] **Recurring Prompts:** Create specific prompt templates for analyzing the outputs of the Master Commands.
- [ ] **Pipeline Testing:** Run a full end-to-end test on a single stock to verify the flow.
