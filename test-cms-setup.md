# Testing Decap CMS Live Editing

## Method 1: Direct File Editing with Live Reload

**Current Setup (Easiest)**:
1. Open: http://127.0.0.1:8000/docs-as-code-demo/
2. In another terminal/editor, edit: `docs/index.md`  
3. Save the file
4. Watch the website auto-reload with changes!

## Method 2: CMS Interface Testing

**Access CMS**: http://127.0.0.1:8000/docs-as-code-demo/admin/

**For local testing without GitHub auth**:
1. The CMS will load the interface
2. You can preview content structure
3. For full editing, you need GitHub OAuth setup

## Method 3: Full CMS with GitHub (Production-like)

**Setup GitHub OAuth**:
1. Go to GitHub Settings → Developer settings → OAuth Apps
2. Create new OAuth App:
   - Application name: "Docs CMS Local"
   - Homepage URL: "http://localhost:8000"
   - Authorization callback URL: "https://api.netlify.com/auth/done"
3. Copy Client ID to CMS config

## Live Preview Testing Steps:

### Test 1: Direct File Editing
```bash
# Terminal 1: Server running (already started)
# Terminal 2: Edit content
echo "# Updated Content

This content was updated at $(date)

## New Section
Testing live reload functionality!" > docs/test-page.md

# Add to navigation in mkdocs.yml:
# nav:
#   - Home: index.md  
#   - Test: test-page.md
```

### Test 2: Multiple Format Testing
```bash
# Test website
curl http://127.0.0.1:8000/docs-as-code-demo/

# Test PDF generation
ENABLE_PDF_EXPORT=1 mkdocs build
ls -la site/pdf/manual.pdf
```

### Test 3: Content Validation
```bash
# Test with various content types
cp tests/fixtures/sample_page.md docs/
# Update navigation
# Watch auto-reload
```

## Expected Behavior:

✅ **File changes** → **Auto-reload** → **Instant preview**
✅ **CMS interface** → **Rich editor** → **Live preview panel**  
✅ **Save changes** → **Git commit** → **Deploy pipeline**

## Troubleshooting:

If CMS doesn't load:
1. Check browser console for errors
2. Verify `docs/admin/index.html` exists
3. Check `docs/admin/config.yml` syntax

If live reload doesn't work:
1. Server must be running with `mkdocs serve`
2. Check file permissions
3. Verify MkDocs watching the right directories