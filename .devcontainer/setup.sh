#!/bin/bash
set -e

echo "=========================================="
echo "Setting up Stock Analysis Environment"
echo "=========================================="

# Install Python dependencies
echo ""
echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Install Claude Code CLI
echo ""
echo "Installing Claude Code CLI..."
if ! command -v claude &> /dev/null; then
    curl -fsSL https://claude.ai/install.sh | bash || echo "⚠️  Claude Code installation failed - check internet connection"
else
    echo "✓ Claude Code already installed"
fi

# Install Gemini CLI (Google AI)
echo ""
echo "Installing Gemini CLI..."
if ! command -v gemini &> /dev/null; then
    npm install -g @google/gemini-cli || echo "⚠️  Gemini CLI installation failed - check internet connection"
else
    echo "✓ Gemini CLI already installed"
fi

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
pip list | grep -E "requests|tabulate|rich|beautifulsoup4" || true
echo ""
echo "CLI tools:"
if command -v claude &> /dev/null; then echo "  ✓ Claude Code"; else echo "  ✗ Claude Code (not installed)"; fi
if command -v gemini &> /dev/null; then echo "  ✓ Gemini CLI"; else echo "  ✗ Gemini CLI (not installed)"; fi
echo ""
echo "Environment variables configured:"
if [ -n "$PERIGON_API_KEY" ]; then echo "  ✓ PERIGON_API_KEY"; else echo "  ✗ PERIGON_API_KEY (not set)"; fi
if [ -n "$ALPHAVANTAGE_API_KEY" ]; then echo "  ✓ ALPHAVANTAGE_API_KEY"; else echo "  ✗ ALPHAVANTAGE_API_KEY (not set)"; fi
if [ -n "$FMP_API_KEY" ]; then echo "  ✓ FMP_API_KEY"; else echo "  ✗ FMP_API_KEY (not set)"; fi
if [ -n "$SOCIAVAULT_API_KEY" ]; then echo "  ✓ SOCIAVAULT_API_KEY"; else echo "  ✗ SOCIAVAULT_API_KEY (not set)"; fi
echo ""
echo "Ready to start analyzing stocks!"
echo "See docs/CLAUDE.md for workflow overview"
echo "See docs/COMMANDS.md for command reference"
echo "=========================================="
