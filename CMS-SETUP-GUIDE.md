# Complete Decap CMS Setup Guide

## Why CMS Isn't Working

The CMS admin panel loads but can't edit content because it needs:
1. **Authentication** - GitHub OAuth or local backend server
2. **Repository Access** - Permission to read/write files
3. **CORS Configuration** - Proper headers for local development

## 🚀 Solution 1: GitHub OAuth Setup (Recommended)

### Step 1: Create GitHub OAuth App

1. **Go to GitHub Settings**:
   - Visit: https://github.com/settings/developers
   - Click "OAuth Apps"
   - Click "New OAuth App"

2. **Fill in OAuth App Details**:
   ```
   Application name: Docs CMS
   Homepage URL: http://localhost:8000
   Application description: Documentation CMS
   Authorization callback URL: https://api.netlify.com/auth/done
   ```

3. **Get Client ID**:
   - After creating, copy the "Client ID"
   - Keep the Client Secret secure (don't share)

### Step 2: Update CMS Configuration

Edit `docs/admin/config.yml`:

```yaml
backend:
  name: github
  repo: YOUR-USERNAME/docs-as-code-demo  # ← Replace with your repo
  branch: main
  
# Remove local_backend for production
# local_backend: true
```

### Step 3: Add GitHub OAuth Client ID

Add to your repository secrets or environment:
```bash
# For local development, you can temporarily add:
# In docs/admin/config.yml:
# backend:
#   name: github
#   repo: your-username/docs-as-code-demo
#   client_id: your-oauth-client-id  # Add this line
```

## 🧪 Solution 2: Test Mode (Immediate Testing)

For testing without GitHub setup:

### Option A: Direct File Editing
```bash
# Edit files directly and see live changes:
echo "# New Content" > docs/new-page.md

# Add to mkdocs.yml navigation:
# nav:
#   - Home: index.md
#   - New Page: new-page.md

# Changes appear instantly at:
# http://localhost:8000/docs-as-code-demo/
```

### Option B: Alternative CMS (Prose.io)
```bash
# Use prose.io for GitHub file editing:
# 1. Go to http://prose.io
# 2. Authorize with GitHub
# 3. Navigate to your repository
# 4. Edit markdown files directly
```

## 🎯 Solution 3: Netlify Identity (Easiest for Demo)

If you deploy to Netlify, you can use Netlify Identity:

```yaml
# In docs/admin/config.yml:
backend:
  name: git-gateway
  branch: main

# Add to docs/admin/index.html:
# <script src="https://identity.netlify.com/v1/netlify-identity-widget.js"></script>
```

## 🔧 Solution 4: Local Development Server

For advanced local development:

```bash
# Install Node.js, then:
npm install -g @decaporg/decap-server
npx @decaporg/decap-server

# In another terminal:
mkdocs serve

# The CMS will work at localhost:8000/admin/
```

## ✅ Quick Test to Verify CMS

1. **Access CMS**: http://localhost:8000/docs-as-code-demo/admin/
2. **Expected Behavior**:
   - ✅ CMS interface loads
   - ✅ Shows "Content Manager" title
   - ⚠️ Shows login screen or error (needs auth)
   - ✅ Can navigate the interface

3. **With GitHub OAuth**:
   - ✅ "Login with GitHub" button works
   - ✅ Can see content collections
   - ✅ Can edit markdown files
   - ✅ Live preview panel works
   - ✅ Changes save to Git automatically

## 🚨 Common Issues & Fixes

### Issue: "Cannot read config.yml"
**Fix**: Verify file exists at `docs/admin/config.yml`

### Issue: "Repository not found" 
**Fix**: Update repo name in config.yml to match your GitHub repo

### Issue: "Authentication failed"
**Fix**: Check OAuth app callback URL and client ID

### Issue: "CORS error"
**Fix**: Use proper domain (localhost:8000) not 127.0.0.1

## 🎯 Recommended Setup for You

**For immediate testing**:
1. Keep current `test-repo` backend
2. Use direct file editing: Edit `docs/*.md` files
3. Watch live reload in browser

**For full CMS experience**:
1. Create GitHub repository from this project
2. Set up GitHub OAuth app (5 minutes)
3. Update CMS config with your repo details
4. Deploy to GitHub Pages
5. CMS works fully at yourusername.github.io/docs-as-code-demo/admin/

## 📊 What Each Solution Gives You

| Solution | Live Edit | Git Integration | Rich Editor | Authentication |
|----------|-----------|----------------|-------------|----------------|
| Direct Files | ✅ Instant | Manual commits | VS Code/etc | None needed |
| GitHub OAuth | ✅ Live | ✅ Automatic | ✅ Rich CMS | GitHub account |
| Netlify Identity | ✅ Live | ✅ Automatic | ✅ Rich CMS | Email signup |
| Local Server | ✅ Live | ✅ Automatic | ✅ Rich CMS | None needed |

The system is fully functional for direct editing. The CMS adds a web interface layer that's perfect for non-technical users!