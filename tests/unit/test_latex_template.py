#!/usr/bin/env python3
"""
Unit tests for LaTeX template validation.
"""

import os
import re
import pytest
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
LATEX_TEMPLATE = PROJECT_ROOT / "template.latex"


def test_latex_template_exists():
    """Test that template.latex exists."""
    assert LATEX_TEMPLATE.exists(), "template.latex file not found"


def test_latex_template_not_empty():
    """Test that template.latex is not empty."""
    with open(LATEX_TEMPLATE, 'r') as f:
        content = f.read().strip()
        assert len(content) > 0, "template.latex should not be empty"


def test_latex_document_structure():
    """Test that template has proper LaTeX document structure."""
    with open(LATEX_TEMPLATE, 'r') as f:
        content = f.read()
    
    # Check for essential LaTeX commands
    essential_commands = [
        r'\\documentclass',
        r'\\begin{document}',
        r'\\end{document}'
    ]
    
    for command in essential_commands:
        assert re.search(command, content), f"Template missing essential command: {command}"


def test_pandoc_variables():
    """Test that template contains required Pandoc variables."""
    with open(LATEX_TEMPLATE, 'r') as f:
        content = f.read()
    
    required_variables = ['$title$', '$author$', '$date$', '$body$']
    
    for var in required_variables:
        assert var in content, f"Template missing required Pandoc variable: {var}"


def test_latex_packages():
    """Test that template includes essential LaTeX packages."""
    with open(LATEX_TEMPLATE, 'r') as f:
        content = f.read()
    
    essential_packages = [
        'inputenc',
        'fontenc',
        'geometry',
        'graphicx',
        'hyperref'
    ]
    
    for package in essential_packages:
        package_pattern = rf'\\usepackage.*{{{package}.*}}'
        assert re.search(package_pattern, content), f"Template missing essential package: {package}"


def test_pdf_metadata_setup():
    """Test that template includes PDF metadata configuration."""
    with open(LATEX_TEMPLATE, 'r') as f:
        content = f.read()
    
    metadata_commands = [
        '\\hypersetup',
        'pdftitle',
        'pdfauthor'
    ]
    
    for command in metadata_commands:
        assert command in content, f"Template missing PDF metadata setup: {command}"


def test_title_page_setup():
    """Test that template includes title page configuration."""
    with open(LATEX_TEMPLATE, 'r') as f:
        content = f.read()
    
    title_elements = [
        r'\\title{',
        r'\\author{',
        r'\\date{'
    ]
    
    for element in title_elements:
        assert re.search(element, content), f"Template missing title page element: {element}"


if __name__ == "__main__":
    pytest.main([__file__])