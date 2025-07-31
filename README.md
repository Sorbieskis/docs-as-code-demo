# Demo Commands

## Start Development Servers

### For Fish Shell:
```fish
# Terminal 1: Start MkDocs server
source venv/bin/activate.fish
mkdocs serve

# Terminal 2: Start Decap CMS backend
npx decap-server
```

### For Bash/Zsh:
```bash
# Terminal 1: Start MkDocs server
source venv/bin/activate
mkdocs serve

# Terminal 2: Start Decap CMS backend
npx decap-server
```

## Troubleshooting

### Port Already in Use Error:
```fish
# Stop existing servers
pkill -f "mkdocs serve"
pkill -f "decap-server"

# Or use different port
mkdocs serve --dev-addr=127.0.0.1:8001
```

### Browser Console Warnings:
- CSP warnings about favicon.ico are normal and don't affect functionality
- "Content-Security-Policy" errors can be safely ignored during development

## Access Points

- **Documentation Site**: http://127.0.0.1:8000/
- **CMS Admin Interface**: http://127.0.0.1:8000/admin/

## Generate PDF

### Fish Shell:
```fish
source venv/bin/activate.fish
mkdocs build
```

### Bash/Zsh:
```bash
source venv/bin/activate
mkdocs build
```

PDF Output: `site/pdf/manual.pdf`

## Live Demo Workflow

1. Edit content via CMS at `/admin/`
2. See live changes at documentation site
3. Generate PDF with `mkdocs build`
4. Show both outputs from single source