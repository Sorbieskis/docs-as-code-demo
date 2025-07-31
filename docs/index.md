---
title: Documentation Demo
author: Demo Project
date: 2024
---

# Documentation Demo

This demonstrates a docs-as-code workflow with automated builds and web-based editing.

## Features

- Markdown-based content
- Web-based editing interface  
- Automated website generation
- PDF export capability

## Getting Started

1. Edit content through the admin interface at `/admin/`
2. Changes trigger automatic rebuilds
3. View results at the published site

## Architecture

The system combines:

- **MkDocs** for static site generation
- **Decap CMS** for web-based editing
- **GitHub Actions** for automation
- **LaTeX** for PDF generation

## Sample Content

### Code Example

```python
def build_docs():
    """Generate documentation from Markdown."""
    return "Documentation built successfully"
```

### Table

| Output | Format | Status |
|--------|--------|--------|
| Website | HTML | ✅ |
| PDF | LaTeX | ✅ |

This demonstrates professional documentation workflow capabilities.