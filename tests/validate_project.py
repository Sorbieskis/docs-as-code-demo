#!/usr/bin/env python3
"""
Project validation script for comprehensive system check.
"""

import os
import sys
import yaml
import subprocess
from pathlib import Path
from typing import List, Tuple, Dict, Any

# ANSI color codes for output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

PROJECT_ROOT = Path(__file__).parent.parent


class ValidationResult:
    """Container for validation results."""
    
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.warnings = 0
        self.results: List[Tuple[str, bool, str]] = []
    
    def add_result(self, test_name: str, passed: bool, message: str = ""):
        """Add a test result."""
        self.results.append((test_name, passed, message))
        if passed:
            self.passed += 1
        else:
            self.failed += 1
    
    def add_warning(self, test_name: str, message: str):
        """Add a warning."""
        self.results.append((test_name, None, message))
        self.warnings += 1
    
    def print_summary(self):
        """Print validation summary."""
        print(f"\n{BLUE}=== VALIDATION SUMMARY ==={RESET}")
        print(f"{GREEN}✓ Passed: {self.passed}{RESET}")
        print(f"{RED}✗ Failed: {self.failed}{RESET}")
        print(f"{YELLOW}⚠ Warnings: {self.warnings}{RESET}")
        
        if self.failed > 0:
            print(f"\n{RED}Failed tests:{RESET}")
            for test_name, passed, message in self.results:
                if passed is False:
                    print(f"  {RED}✗{RESET} {test_name}: {message}")
        
        return self.failed == 0


def check_file_exists(filepath: Path, description: str) -> Tuple[bool, str]:
    """Check if a file exists."""
    if filepath.exists():
        return True, f"{description} exists"
    return False, f"{description} not found at {filepath}"


def check_yaml_valid(filepath: Path, description: str) -> Tuple[bool, str]:
    """Check if YAML file is valid."""
    try:
        with open(filepath, 'r') as f:
            yaml.safe_load(f)
        return True, f"{description} has valid YAML"
    except yaml.YAMLError as e:
        return False, f"{description} has invalid YAML: {e}"
    except FileNotFoundError:
        return False, f"{description} not found"


def check_command_available(command: str) -> Tuple[bool, str]:
    """Check if a command is available."""
    try:
        result = subprocess.run([command, "--version"], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            return True, f"{command} is available"
        return False, f"{command} returned non-zero exit code"
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False, f"{command} not found or not responding"


def validate_mkdocs_config() -> List[Tuple[str, bool, str]]:
    """Validate MkDocs configuration."""
    results = []
    mkdocs_file = PROJECT_ROOT / "mkdocs.yml"
    
    # Check file exists
    passed, msg = check_file_exists(mkdocs_file, "mkdocs.yml")
    results.append(("MkDocs config exists", passed, msg))
    
    if not passed:
        return results
    
    # Check YAML validity
    passed, msg = check_yaml_valid(mkdocs_file, "mkdocs.yml")
    results.append(("MkDocs config valid YAML", passed, msg))
    
    if not passed:
        return results
    
    # Check required fields
    try:
        with open(mkdocs_file, 'r') as f:
            config = yaml.safe_load(f)
        
        required_fields = ['site_name', 'theme', 'nav', 'plugins']
        for field in required_fields:
            if field in config:
                results.append((f"MkDocs has {field}", True, f"{field} configured"))
            else:
                results.append((f"MkDocs has {field}", False, f"{field} missing"))
        
        # Check theme
        if config.get('theme', {}).get('name') == 'material':
            results.append(("MkDocs uses Material theme", True, "Material theme configured"))
        else:
            results.append(("MkDocs uses Material theme", False, "Material theme not configured"))
            
    except Exception as e:
        results.append(("MkDocs config parsing", False, f"Error parsing config: {e}"))
    
    return results


def validate_cms_config() -> List[Tuple[str, bool, str]]:
    """Validate Decap CMS configuration."""
    results = []
    
    # Check admin interface
    admin_html = PROJECT_ROOT / "docs" / "admin" / "index.html"
    passed, msg = check_file_exists(admin_html, "CMS admin interface")
    results.append(("CMS admin interface", passed, msg))
    
    # Check CMS config
    cms_config = PROJECT_ROOT / "docs" / "admin" / "config.yml"
    passed, msg = check_file_exists(cms_config, "CMS config")
    results.append(("CMS config exists", passed, msg))
    
    if passed:
        passed, msg = check_yaml_valid(cms_config, "CMS config")
        results.append(("CMS config valid YAML", passed, msg))
        
        if passed:
            try:
                with open(cms_config, 'r') as f:
                    config = yaml.safe_load(f)
                
                # Check backend
                if 'backend' in config and config['backend'].get('name') == 'github':
                    results.append(("CMS GitHub backend", True, "GitHub backend configured"))
                else:
                    results.append(("CMS GitHub backend", False, "GitHub backend not configured"))
                
                # Check collections
                if 'collections' in config:
                    results.append(("CMS collections", True, "Collections configured"))
                else:
                    results.append(("CMS collections", False, "Collections not configured"))
                    
            except Exception as e:
                results.append(("CMS config parsing", False, f"Error parsing: {e}"))
    
    return results


def validate_latex_template() -> List[Tuple[str, bool, str]]:
    """Validate LaTeX template."""
    results = []
    
    template_file = PROJECT_ROOT / "template.latex"
    passed, msg = check_file_exists(template_file, "LaTeX template")
    results.append(("LaTeX template exists", passed, msg))
    
    if passed:
        try:
            with open(template_file, 'r') as f:
                content = f.read()
            
            # Check for essential LaTeX elements
            latex_elements = [
                ('\\documentclass', 'Document class declaration'),
                ('\\begin{document}', 'Document begin'),
                ('\\end{document}', 'Document end'),
                ('$title$', 'Title variable'),
                ('$author$', 'Author variable'),
                ('$date$', 'Date variable'),
                ('$body$', 'Body variable')
            ]
            
            for element, description in latex_elements:
                if element in content:
                    results.append((f"LaTeX {description.lower()}", True, f"{description} found"))
                else:
                    results.append((f"LaTeX {description.lower()}", False, f"{description} missing"))
                    
        except Exception as e:
            results.append(("LaTeX template parsing", False, f"Error reading template: {e}"))
    
    return results


def validate_github_actions() -> List[Tuple[str, bool, str]]:
    """Validate GitHub Actions workflows."""
    results = []
    
    workflows_dir = PROJECT_ROOT / ".github" / "workflows"
    passed, msg = check_file_exists(workflows_dir, "GitHub workflows directory")
    results.append(("GitHub workflows directory", passed, msg))
    
    if passed:
        # Check main workflows
        workflows = [
            ("build-and-deploy.yml", "Build and deploy workflow"),
            ("ci.yml", "CI workflow")
        ]
        
        for workflow_file, description in workflows:
            workflow_path = workflows_dir / workflow_file
            passed, msg = check_file_exists(workflow_path, description)
            results.append((description, passed, msg))
            
            if passed:
                passed, msg = check_yaml_valid(workflow_path, description)
                results.append((f"{description} valid YAML", passed, msg))
    
    return results


def validate_dependencies() -> List[Tuple[str, bool, str]]:
    """Validate system dependencies."""
    results = []
    
    # Check Python dependencies
    requirements_file = PROJECT_ROOT / "requirements.txt"
    passed, msg = check_file_exists(requirements_file, "Requirements file")
    results.append(("Requirements file", passed, msg))
    
    # Check key commands
    commands = [
        ("python", "Python interpreter"),
        ("pip", "Python package manager")
    ]
    
    for command, description in commands:
        passed, msg = check_command_available(command)
        results.append((description, passed, msg))
    
    # Check optional commands (warnings only)
    optional_commands = [
        ("pandoc", "Pandoc for PDF generation"),
        ("xelatex", "XeLaTeX for PDF compilation")
    ]
    
    for command, description in optional_commands:
        passed, msg = check_command_available(command)
        if not passed:
            results.append((description, None, f"Optional: {msg}"))
        else:
            results.append((description, True, msg))
    
    return results


def validate_content() -> List[Tuple[str, bool, str]]:
    """Validate content structure."""
    results = []
    
    # Check main content
    docs_dir = PROJECT_ROOT / "docs"
    passed, msg = check_file_exists(docs_dir, "Docs directory")
    results.append(("Docs directory", passed, msg))
    
    if passed:
        index_file = docs_dir / "index.md"
        passed, msg = check_file_exists(index_file, "Main index file")
        results.append(("Main index file", passed, msg))
        
        if passed:
            try:
                with open(index_file, 'r') as f:
                    content = f.read()
                
                # Check for frontmatter
                if content.startswith('---'):
                    results.append(("Index frontmatter", True, "Frontmatter present"))
                    
                    # Parse frontmatter
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        try:
                            frontmatter = yaml.safe_load(parts[1])
                            required_fields = ['title', 'author', 'date']
                            for field in required_fields:
                                if field in frontmatter:
                                    results.append((f"Index {field}", True, f"{field} in frontmatter"))
                                else:
                                    results.append((f"Index {field}", False, f"{field} missing from frontmatter"))
                        except yaml.YAMLError as e:
                            results.append(("Index frontmatter valid", False, f"Invalid YAML: {e}"))
                    else:
                        results.append(("Index frontmatter format", False, "Invalid frontmatter format"))
                else:
                    results.append(("Index frontmatter", None, "No frontmatter (optional)"))
                    
            except Exception as e:
                results.append(("Index file parsing", False, f"Error reading index: {e}"))
    
    return results


def main():
    """Run comprehensive project validation."""
    print(f"{BLUE}Validating Docs-as-Code Project{RESET}")
    print(f"Project root: {PROJECT_ROOT}")
    print("-" * 50)
    
    result = ValidationResult()
    
    # Run all validations
    validations = [
        ("MkDocs Configuration", validate_mkdocs_config),
        ("CMS Configuration", validate_cms_config),
        ("LaTeX Template", validate_latex_template),
        ("GitHub Actions", validate_github_actions),
        ("Dependencies", validate_dependencies),
        ("Content Structure", validate_content)
    ]
    
    for section_name, validation_func in validations:
        print(f"\n{YELLOW}{section_name}:{RESET}")
        
        try:
            section_results = validation_func()
            for test_name, passed, message in section_results:
                if passed is True:
                    print(f"  {GREEN}✓{RESET} {test_name}: {message}")
                    result.add_result(test_name, True, message)
                elif passed is False:
                    print(f"  {RED}✗{RESET} {test_name}: {message}")
                    result.add_result(test_name, False, message)
                else:  # Warning
                    print(f"  {YELLOW}⚠{RESET} {test_name}: {message}")
                    result.add_warning(test_name, message)
                    
        except Exception as e:
            error_msg = f"Validation error: {e}"
            print(f"  {RED}✗{RESET} {section_name}: {error_msg}")
            result.add_result(section_name, False, error_msg)
    
    # Print summary and return appropriate exit code
    success = result.print_summary()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()