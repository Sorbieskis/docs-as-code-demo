# Docs-as-Code Demo

A complete demonstration of a modern documentation system that combines web-based editing with automated builds to produce both static websites and professional PDFs from the same Markdown source.

## 🚀 Features

- **Web-based Editing**: Edit content through Decap CMS interface
- **Automated Builds**: GitHub Actions workflow for continuous deployment
- **Multiple Output Formats**: Generate both website and PDF from same source
- **Professional Design**: Material Design theme and LaTeX typography
- **Comprehensive Testing**: 4-layer testing pipeline with CI/CD integration
- **Version Control**: Full Git workflow with collaborative editing

## 📋 Quick Start

### Prerequisites

- GitHub account with repository access
- Python 3.11+ installed locally
- Git installed

### 1. Repository Setup

1. **Fork or create a new repository** from this template
2. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/docs-as-code-demo.git
   cd docs-as-code-demo
   ```

3. **Update configuration files** with your repository details:
   - `docs/admin/config.yml`: Update `repo` and `site_domain`
   - `mkdocs.yml`: Update `site_url` and `repo_url`

### 2. Local Development

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Start local development server**:
   ```bash
   mkdocs serve
   ```

3. **Access the site**:
   - Website: http://localhost:8000
   - CMS Admin: http://localhost:8000/admin/

### 3. GitHub Setup

1. **Enable GitHub Actions**:
   - Go to your repository Settings → Actions → General
   - Enable "Allow all actions and reusable workflows"

2. **Configure GitHub Pages**:
   - Go to Settings → Pages
   - Source: "Deploy from a branch"
   - Branch: `gh-pages` (will be created by the workflow)

3. **Set up Decap CMS Authentication**:
   - Go to GitHub Settings → Developer settings → OAuth Apps
   - Create new OAuth App with:
     - Authorization callback URL: `https://api.netlify.com/auth/done`
   - Or use Netlify Identity for simpler setup

### 4. First Deployment

1. **Push to main branch**:
   ```bash
   git add .
   git commit -m "Initial setup"
   git push origin main
   ```

2. **Monitor deployment**:
   - Check Actions tab for workflow progress
   - Website will be available at `https://yourusername.github.io/docs-as-code-demo/`
   - PDF will be available as workflow artifact

## 🏗️ System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Editor    │    │  GitHub Repo    │    │ GitHub Actions  │
│  (Decap CMS)    │───▶│  (Git Storage)  │───▶│  (Automation)   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                        │
                       ┌─────────────────┐    ┌─────────────────┐
                       │  GitHub Pages   │◀───┤  Build Process  │
                       │   (Website)     │    │ (MkDocs+Pandoc) │
                       └─────────────────┘    └─────────────────┘
                                                        │
                                              ┌─────────────────┐
                                              │   PDF Output    │
                                              │  (Artifacts)    │
                                              └─────────────────┘
```

## 📁 Project Structure

```
docs-as-code-demo/
├── .github/workflows/           # GitHub Actions workflows
│   ├── build-and-deploy.yml    # Main deployment workflow  
│   └── ci.yml                   # Testing and validation
├── docs/                        # Documentation content
│   ├── admin/                   # Decap CMS configuration
│   │   ├── index.html          # CMS interface
│   │   └── config.yml          # CMS settings
│   └── index.md                # Main content file
├── tests/                       # Comprehensive test suite
│   ├── unit/                   # Unit tests
│   ├── integration/            # Integration tests
│   ├── fixtures/               # Test data
│   └── validate_project.py     # Project validation script
├── mkdocs.yml                  # MkDocs configuration
├── requirements.txt            # Python dependencies
├── template.latex              # LaTeX template for PDF
└── README.md                   # This file
```

## 🔧 Configuration

### MkDocs Configuration (`mkdocs.yml`)

Key settings to customize:

```yaml
site_name: Your Site Name
site_url: https://yourusername.github.io/your-repo-name/
repo_url: https://github.com/yourusername/your-repo-name

theme:
  name: material
  # Customize theme features, colors, etc.

plugins:
  - with-pdf:
      output_path: pdf/manual.pdf
      # PDF generation settings
```

### CMS Configuration (`docs/admin/config.yml`)

Update for your repository:

```yaml
backend:
  name: github
  repo: yourusername/your-repo-name  # ← Change this
  branch: main

site_url: https://yourusername.github.io/your-repo-name  # ← Change this
```

## 🧪 Testing

### Running Tests Locally

```bash
# Install test dependencies
pip install pytest pyyaml

# Run all tests
pytest

# Run specific test categories
pytest -m unit          # Unit tests only
pytest -m integration   # Integration tests only

# Run project validation
python tests/validate_project.py
```

### Test Categories

1. **Unit Tests**: Configuration validation, template syntax
2. **Integration Tests**: Build pipeline, PDF generation
3. **CI Pipeline**: Automated testing on every commit
4. **Validation Script**: Comprehensive project health check

### Testing Pipeline

The project includes a comprehensive 4-layer testing architecture:

- **Layer 1**: Linting & Static Analysis (YAML, Markdown)
- **Layer 2**: Build Verification (MkDocs, PDF generation)  
- **Layer 3**: Workflow & Smoke Tests (GitHub Actions, deployment)
- **Layer 4**: Quality Assurance (Performance, security)

## 🎨 Customization

### Theme Customization

1. **Colors and Fonts**: Edit `mkdocs.yml` theme section
2. **Custom CSS**: Add to `docs/assets/stylesheets/`
3. **Logo and Favicon**: Configure in theme settings

### PDF Styling

1. **LaTeX Template**: Modify `template.latex`
2. **Typography**: Adjust fonts and spacing
3. **Layout**: Change margins, headers, footers

### Content Structure

1. **Navigation**: Update `nav` section in `mkdocs.yml`
2. **New Pages**: Add Markdown files to `docs/`
3. **CMS Fields**: Modify `docs/admin/config.yml` collections

## 🚀 Deployment Options

### GitHub Pages (Default)

- Automatic deployment via GitHub Actions
- Free hosting for public repositories
- Custom domain support available

### Alternative Hosting

The generated `site/` directory can be deployed to:

- **Netlify**: Direct GitHub integration
- **Vercel**: Import GitHub repository  
- **AWS S3**: Static website hosting
- **Your Server**: Copy `site/` directory

## 🔍 Troubleshooting

### Common Issues

1. **Build Failures**:
   ```bash
   # Check MkDocs configuration
   mkdocs build --strict --verbose
   
   # Validate project setup
   python tests/validate_project.py
   ```

2. **PDF Generation Issues**:
   - Ensure LaTeX packages are installed
   - Check template syntax
   - Verify metadata in frontmatter

3. **CMS Authentication**:
   - Verify OAuth app configuration
   - Check repository permissions
   - Ensure correct callback URLs

### Debug Commands

```bash
# Test local build
mkdocs build --strict

# Validate configurations
yamllint mkdocs.yml docs/admin/config.yml

# Check Markdown formatting
markdownlint-cli2 "docs/**/*.md"

# Run comprehensive validation
python tests/validate_project.py
```

## 📚 Documentation Workflow

### For Content Editors

1. **Access CMS**: Navigate to `/admin/` on the deployed site
2. **Authenticate**: Log in with GitHub account
3. **Edit Content**: Use rich text editor with live preview
4. **Save Changes**: Content automatically commits to repository
5. **Automatic Deployment**: Site updates within minutes

### For Developers

1. **Local Development**: Use `mkdocs serve` for instant preview
2. **Testing**: Run test suite before committing
3. **CI/CD**: All changes validated automatically
4. **Monitoring**: Check Actions tab for deployment status

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Run tests: `pytest`
4. Commit changes: `git commit -m "Description"`
5. Push branch: `git push origin feature-name`
6. Create Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/docs-as-code-demo/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/docs-as-code-demo/discussions)
- **Documentation**: [Project Wiki](https://github.com/yourusername/docs-as-code-demo/wiki)

---

**Built with**: MkDocs Material, Decap CMS, GitHub Actions, LaTeX, and comprehensive testing pipeline.