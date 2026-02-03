#!/bin/bash
set -e

echo "=========================================="
echo "Setting up Stock Analysis Environment"
echo "=========================================="

# Install Python dependencies
echo ""
echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r setup/requirements.txt

# Install Claude Code CLI
echo ""
echo "Installing Claude Code CLI..."
# Using npm installation method (most common for CLI tools)
if ! command -v claude &> /dev/null; then
    npm install -g @anthropic-ai/claude-cli 2>/dev/null || echo "⚠️  Claude CLI installation not available via npm - install manually if needed"
else
    echo "✓ Claude CLI already installed"
fi

# Install Gemini CLI (Google AI)
echo ""
echo "Installing Gemini CLI..."
# Using pip installation method for Google's generative AI SDK
pip install google-generativeai

# Install additional useful tools
echo ""
echo "Installing additional development tools..."
pip install ipython  # Better Python REPL
pip install pytest   # Testing framework (if needed later)

# Set up git configuration helpers
echo ""
echo "Configuring git..."
git config --global core.autocrlf input
git config --global pull.rebase false

# Display environment info
echo ""
echo "=========================================="
echo "✓ Environment setup complete!"
echo "=========================================="
echo ""
echo "Python version: $(python --version)"
echo "Pip version: $(pip --version)"
echo ""
echo "Installed packages:"
pip list | grep -E "requests|tabulate|rich|beautifulsoup4|google-generativeai" || true
echo ""
echo "Environment variables configured:"
if [ -n "$PERIGON_API_KEY" ]; then echo "  ✓ PERIGON_API_KEY"; else echo "  ✗ PERIGON_API_KEY (not set)"; fi
if [ -n "$ALPHAVANTAGE_API_KEY" ]; then echo "  ✓ ALPHAVANTAGE_API_KEY"; else echo "  ✗ ALPHAVANTAGE_API_KEY (not set)"; fi
if [ -n "$FMP_API_KEY" ]; then echo "  ✓ FMP_API_KEY"; else echo "  ✗ FMP_API_KEY (not set)"; fi
if [ -n "$SOCIAVAULT_API_KEY" ]; then echo "  ✓ SOCIAVAULT_API_KEY"; else echo "  ✗ SOCIAVAULT_API_KEY (not set)"; fi
echo ""
echo "Ready to start analyzing stocks!"
echo "See CLAUDE.md for workflow overview"
echo "See setup/COMMANDS.md for command reference"
echo "=========================================="
