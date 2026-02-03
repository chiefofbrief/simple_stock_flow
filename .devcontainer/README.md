# GitHub Codespaces Setup

This configuration automatically sets up your development environment when you open the repository in GitHub Codespaces.

## What Gets Installed

- **Python 3.11** with all project dependencies from `setup/requirements.txt`
- **Claude Code CLI** - Anthropic's CLI tool
- **Gemini CLI** - Google's generative AI SDK (`google-generativeai`)
- **Git & GitHub CLI** - Version control and GitHub integration
- **VS Code Extensions** - Python, Pylance, Jupyter support
- **Development Tools** - iPython, pytest

## Required API Keys

Before opening the Codespace, configure your API keys as **GitHub Codespaces Secrets**:

### How to Add Secrets

1. Go to your GitHub repository
2. Navigate to **Settings → Secrets and variables → Codespaces**
3. Click **New repository secret**
4. Add the following secrets:

| Secret Name | Description |
|-------------|-------------|
| `PERIGON_API_KEY` | Perigon news API key |
| `ALPHAVANTAGE_API_KEY` | AlphaVantage market data API key |
| `FMP_API_KEY` | Financial Modeling Prep API key |
| `SOCIAVAULT_API_KEY` | SociaVault social media API key |

These will be automatically available as environment variables in your Codespace.

## First Time Setup

When you first open the Codespace:

1. The environment will automatically run `.devcontainer/setup.sh`
2. All dependencies will be installed
3. Data directories will be created
4. You'll see a setup completion message

## Verifying Installation

After setup completes, verify everything is working:

```bash
# Check Python environment
python --version
pip list

# Check API keys are set
echo $PERIGON_API_KEY  # Should show your key (or at least confirm it exists)

# Test a simple script
python scripts/discovery.py --help
```

## Manual Setup (if needed)

If you need to re-run setup:

```bash
bash .devcontainer/setup.sh
```

## Troubleshooting

**API Keys Not Available:**
- Check that secrets are added in GitHub → Settings → Codespaces Secrets
- Rebuild the container: Command Palette (Cmd/Ctrl+Shift+P) → "Codespaces: Rebuild Container"

**Package Installation Fails:**
- Check `setup/requirements.txt` is present
- Run manually: `pip install -r setup/requirements.txt`

**Claude/Gemini CLI Not Working:**
- These may need manual installation or authentication
- Check their respective documentation for latest install methods
