# Project Unidoc - Simplified Documentation System

A clean, PRD-compliant automated technical documentation system with component-based manual assembly.

## 🎯 System Overview

**Project Unidoc** creates professional technical manuals through a simple component-based assembly system:

- **📝 Content Components**: Reusable markdown content pieces
- **📚 Manual Assembly**: YAML files define manual structure  
- **🚀 Automated Building**: Simple script + GitHub Actions pipeline
- **📄 Multiple Outputs**: Website (MkDocs) + PDFs (Pandoc)

## 🏗️ Quick Start

### 1. Manual Assembly

Create or edit manuals by running the assembly script:

```bash
# Assemble all manuals from components
./assemble.sh
```

This creates:
- `assembled/*.md` - PDF-ready files
- `docs/*.md` - Web-ready files  

### 2. Website Development

```bash
# Install dependencies
pip install -r requirements.txt

# Start development server
mkdocs serve
```

Access at: http://127.0.0.1:8000/

### 3. CMS Interface (Optional)

```bash
# Terminal 1: MkDocs server
mkdocs serve

# Terminal 2: CMS backend  
npx decap-server
```

Access CMS at: http://127.0.0.1:8000/admin/

## 📚 Current Manuals

The system includes 3 pilot manuals as specified in the PRD:

1. **CRS10 Software Manual** - Installation and operation guide
2. **System Architecture Guide** - Technical implementation details  
3. **Project Unidoc Overview** - System overview and business value

## 🔧 Manual Assembly System

### Component Structure
```
docs/content/components/
├── company-header.md          # Reusable header
├── crs10-introduction.md      # CRS10 intro
├── crs10-installation.md      # CRS10 install guide
└── ...                        # Other components
```

### Assembly Definition
```yaml
# docs/manuals/example-manual.yml
title: "Manual Title"
author: "Author Name"  
date: "2025-01-30"
description: "Manual description"
chapters:
  - content/components/header.md
  - content/components/introduction.md
  - content/components/conclusion.md
```

### Assembly Process
1. **Discovery**: Script finds all `docs/manuals/*.yml` files
2. **Validation**: Checks required fields and component files
3. **Assembly**: Combines components with frontmatter
4. **Output**: Creates both web and PDF versions

## 🚀 Deployment

### GitHub Actions (Automatic)
Pushes to `main` branch automatically:
1. Assemble manuals from components
2. Run quality gates (spell check + link check)  
3. Build and deploy website to GitHub Pages
4. Generate and upload PDF artifacts

### Manual PDF Generation
```bash
# Generate PDFs locally (requires pandoc)
for manual in assembled/*.md; do
  pandoc "$manual" --pdf-engine=xelatex -o "$(basename "$manual" .md).pdf"
done
```

## 🛡️ Quality Gates

The system includes automated quality checks:

- **Spell Check**: Uses `cspell` with custom dictionary
- **Link Check**: Uses `lychee` to verify all links work
- **Build Validation**: Ensures MkDocs builds successfully

## 📁 Project Structure

```
docs-as-code-demo/
├── docs/                          # MkDocs source
│   ├── content/components/         # Content components
│   ├── manuals/                    # Assembly definitions (.yml)
│   └── admin/                      # CMS interface
├── assembled/                      # Generated manual files
├── assemble.sh                     # Simple assembly script
├── .github/workflows/              # CI/CD automation
├── .cspell.json                    # Spell check config
└── mkdocs.yml                      # Site configuration
```

## 🔄 Development Workflow

1. **Edit Components**: Modify content in `docs/content/components/`
2. **Update Assembly**: Edit YAML files in `docs/manuals/`
3. **Test Locally**: Run `./assemble.sh && mkdocs serve`
4. **Commit Changes**: Push to main branch
5. **Automatic Deploy**: GitHub Actions handles the rest

## 📋 PRD Compliance

This simplified system meets all V1 MVP requirements:

- ✅ **3 Pilot Manuals**: CRS10 + 2 additional manuals
- ✅ **Component Assembly**: Simple YAML-driven "Lego block" system
- ✅ **CMS Interface**: Two-section interface (components + assembly)
- ✅ **Quality Gates**: Automated spell check and link validation
- ✅ **CI/CD Pipeline**: Full GitHub Actions automation
- ✅ **Multiple Outputs**: Website + PDF generation
- ✅ **Review Workflow**: GitHub PR process for changes

## 🎉 Next Steps

This clean V1 foundation enables future enhancements:
- Advanced Python orchestration
- Dynamic navigation updates  
- Multi-format outputs
- Enhanced validation and error handling

The simplified architecture preserves the core assembly concept while delivering immediate business value through stakeholder-ready manuals.