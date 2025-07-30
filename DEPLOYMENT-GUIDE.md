# 🚀 Deployment Guide for Sorbieskis/docs-as-code-demo

## 📋 Quick Setup Checklist

### 1. Create GitHub Repository
```bash
# Create new repository at: https://github.com/new
# Repository name: docs-as-code-demo
# Make it public (required for GitHub Pages)
# Initialize with this README: No (we have content)
```

### 2. Push Your Code
```bash
cd /home/sorbieskis/_projects/docs-as-code-demo

# Initialize git repository
git init
git add .
git commit -m "Initial commit: Complete docs-as-code system with web editor

🎉 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"

# Add your GitHub repository as remote
git remote add origin https://github.com/Sorbieskis/docs-as-code-demo.git
git branch -M main
git push -u origin main
```

### 3. Enable GitHub Pages
1. Go to: `https://github.com/Sorbieskis/docs-as-code-demo/settings/pages`
2. **Source**: Deploy from a branch
3. **Branch**: `gh-pages` (will be created automatically)
4. **Folder**: `/ (root)`
5. Click **Save**

### 4. Set Up GitHub OAuth for CMS (Optional but Recommended)

#### Step 4a: Create OAuth App
1. Go to: `https://github.com/settings/developers`
2. Click **"OAuth Apps"** → **"New OAuth App"**
3. Fill in details:
   ```
   Application name: Docs CMS - Sorbieskis
   Homepage URL: https://sorbieskis.github.io/docs-as-code-demo
   Description: Documentation CMS for docs-as-code-demo
   Authorization callback URL: https://api.netlify.com/auth/done
   ```
4. Click **"Register application"**
5. **Copy the Client ID** (keep Client Secret secure)

#### Step 4b: Add Client ID to CMS Config
Edit `docs/admin/config.yml` and add your client ID:

```yaml
backend:
  name: github
  repo: Sorbieskis/docs-as-code-demo
  branch: main
  client_id: your-oauth-client-id-here  # Add this line
```

## 🎯 What Happens Next

### Automatic Deployment
Once you push to GitHub:

1. **GitHub Actions triggers** (see `.github/workflows/build-and-deploy.yml`)
2. **Website builds** using MkDocs Material theme
3. **PDF generates** using LaTeX template  
4. **Deploys to** `https://sorbieskis.github.io/docs-as-code-demo/`
5. **CMS available at** `https://sorbieskis.github.io/docs-as-code-demo/admin/`

### URLs You'll Get
- **📖 Website**: `https://sorbieskis.github.io/docs-as-code-demo/`
- **✏️ CMS Editor**: `https://sorbieskis.github.io/docs-as-code-demo/admin/`
- **📄 PDF Download**: Available in GitHub Actions artifacts

## 🔧 Local Development Commands

```bash
# Install dependencies
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Start development server
mkdocs serve

# Generate PDF locally (optional)
ENABLE_PDF_EXPORT=1 mkdocs build

# Run tests
python -m pytest tests/ -v

# Run linting
python -m ruff check .
python -m ruff format .
```

## 📊 Features Overview

| Feature | Status | URL |
|---------|--------|-----|
| **Website** | ✅ Auto-deploy | https://sorbieskis.github.io/docs-as-code-demo/ |
| **CMS Interface** | ✅ Ready | https://sorbieskis.github.io/docs-as-code-demo/admin/ |
| **PDF Generation** | ✅ Auto-build | GitHub Actions artifacts |
| **Live Editing** | ✅ Works | Edit files directly or via CMS |
| **Search** | ✅ Enabled | Full-text search in website |
| **Themes** | ✅ Dark/Light | Material Design theme |

## 🚨 Troubleshooting

### "Repository not found" Error
- Ensure repository is **public**
- Check repository name matches exactly: `Sorbieskis/docs-as-code-demo`

### CMS Authentication Issues
- Verify OAuth app callback URL: `https://api.netlify.com/auth/done`
- Check client ID is added to `docs/admin/config.yml`
- Make sure repository is public

### GitHub Actions Failing
- Check **Actions** tab in your repository
- Ensure **GitHub Pages** is enabled
- Verify **workflow permissions** allow writing

### PDF Generation Issues
- PDFs generate in GitHub Actions (not locally by default)
- Download from **Actions** → **workflow run** → **Artifacts**
- To generate locally: `ENABLE_PDF_EXPORT=1 mkdocs build`

## 🎉 Success Indicators

You'll know everything is working when:

1. ✅ **Repository exists** at `https://github.com/Sorbieskis/docs-as-code-demo`
2. ✅ **GitHub Actions runs** (green checkmark in commits)
3. ✅ **Website loads** at `https://sorbieskis.github.io/docs-as-code-demo/`
4. ✅ **CMS loads** at `https://sorbieskis.github.io/docs-as-code-demo/admin/`
5. ✅ **You can login** to CMS with GitHub account
6. ✅ **Edits save** and website updates automatically

## 📝 Next Steps After Deployment

1. **Test CMS editing**: Login at `/admin/` and edit a page
2. **Customize content**: Replace demo content with your documentation
3. **Configure theme**: Adjust colors/branding in `mkdocs.yml`
4. **Add collaborators**: Invite team members to GitHub repository
5. **Set up branch protection**: Require reviews for main branch

## 💡 Pro Tips

- **Content editors** only need the CMS URL - no technical setup required
- **Developers** can edit files directly and push to trigger rebuilds
- **PDFs automatically generate** for each release
- **Search is automatic** - no configuration needed
- **Mobile responsive** - works perfectly on phones/tablets

Your docs-as-code system is ready for production use! 🚀