# Session Notes - February 2, 2026

## 1. Critical Environment Configuration
- **API Keys:** Stored in `setup_env.sh`. Sourced automatically in `~/.bashrc`.
- **PYTHONPATH:** Explicitly set in `setup_env.sh` to include `~/.local/lib/python3.11/site-packages` (required for user-installed pip packages in this Nix environment).
- **LD_LIBRARY_PATH (Fragile):** `setup_env.sh` exports a hardcoded Nix store path for `libstdc++.so.6` to fix `curl_cffi` imports.
    - **Warning:** This export breaks system tools like `date` due to libc version mismatch.
    - **Workaround:** Avoid using `$(date ...)` in subshells where `setup_env.sh` is sourced.

## 2. Permanent Code Changes
- **`scripts/discovery.py`:** Updated `get_command` to use `sys.executable` instead of `"python"`. This ensures all sub-processes inherit the correct Python interpreter and environment variables (essential for portability and venv support).
- **Error Handling:** `discovery.py` now captures and prints `stdout` on failure, exposing critical "Missing API Key" messages that were previously swallowed.

## 3. Persistent Issues / Watchlist
- **`curl_cffi`:** Highly sensitive to system libraries. If moved to a new environment (e.g., Codespaces), the hardcoded `LD_LIBRARY_PATH` in `setup_env.sh` MUST be removed or updated.
- **Output:** Internal report title is customized to "Peter's Daily Digest" within `discovery.py`.

## 4. Workflow Preferences
- **Cost Efficiency:** Always verify dependencies and environment (imports, keys) *before* executing scripts that consume API credits.
- **Automation:** User prefers persistence (modifying `.bashrc`) over repetitive manual setup steps.