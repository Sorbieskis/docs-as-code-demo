#!/usr/bin/env python3
"""
Integration tests for PDF generation pipeline.
"""

import os
import subprocess
import shutil
import yaml
import pytest
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent


class TestPDFGeneration:
    """Test PDF generation functionality."""

    def setup_method(self):
        """Set up test environment."""
        self.original_dir = os.getcwd()
        os.chdir(PROJECT_ROOT)

    def teardown_method(self):
        """Clean up after tests."""
        os.chdir(self.original_dir)
        
        # Clean up test PDF files
        test_pdfs = ["test-manual.pdf", "manual.pdf"]
        for pdf_file in test_pdfs:
            pdf_path = PROJECT_ROOT / pdf_file
            if pdf_path.exists():
                pdf_path.unlink()

    def test_pandoc_available(self):
        """Test that Pandoc is available for PDF generation."""
        result = subprocess.run(
            ["pandoc", "--version"],
            capture_output=True,
            text=True
        )
        
        assert result.returncode == 0, "Pandoc not available"
        assert "pandoc" in result.stdout.lower(), "Pandoc version check failed"

    def test_latex_engine_available(self):
        """Test that LaTeX engine is available."""
        result = subprocess.run(
            ["xelatex", "--version"],
            capture_output=True,
            text=True
        )
        
        # XeLaTeX might not be available in CI, so we'll make this a soft check
        if result.returncode == 0:
            assert "xetex" in result.stdout.lower() or "xelatex" in result.stdout.lower()
        else:
            pytest.skip("XeLaTeX not available in test environment")

    def test_metadata_extraction(self):
        """Test that metadata can be extracted from Markdown files."""
        docs_index = PROJECT_ROOT / "docs" / "index.md"
        
        with open(docs_index, 'r') as f:
            content = f.read()
        
        # Check if file has frontmatter
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                try:
                    frontmatter = yaml.safe_load(parts[1])
                    
                    # Check for required metadata
                    assert 'title' in frontmatter, "Title missing from frontmatter"
                    assert 'author' in frontmatter, "Author missing from frontmatter"
                    assert 'date' in frontmatter, "Date missing from frontmatter"
                    
                    # Validate metadata values
                    assert isinstance(frontmatter['title'], str), "Title should be string"
                    assert isinstance(frontmatter['author'], str), "Author should be string"
                    
                except yaml.YAMLError as e:
                    pytest.fail(f"Invalid YAML frontmatter: {e}")
            else:
                pytest.fail("Frontmatter format is invalid")
        else:
            pytest.fail("No frontmatter found in docs/index.md")

    @pytest.mark.skipif(
        subprocess.run(["which", "xelatex"], capture_output=True).returncode != 0,
        reason="XeLaTeX not available"
    )
    def test_pdf_generation_with_pandoc(self):
        """Test PDF generation using Pandoc and LaTeX template."""
        docs_index = PROJECT_ROOT / "docs" / "index.md"
        latex_template = PROJECT_ROOT / "template.latex"
        output_pdf = PROJECT_ROOT / "test-manual.pdf"
        
        # Extract metadata
        with open(docs_index, 'r') as f:
            content = f.read()
        
        if content.startswith('---'):
            parts = content.split('---', 2)
            frontmatter = yaml.safe_load(parts[1])
        else:
            frontmatter = {}
        
        title = frontmatter.get('title', 'Test Title')
        author = frontmatter.get('author', 'Test Author')
        date = str(frontmatter.get('date', '2024-01-01'))
        
        # Run Pandoc
        cmd = [
            "pandoc", str(docs_index),
            "--template", str(latex_template),
            "--pdf-engine", "xelatex",
            f"--variable=title:{title}",
            f"--variable=author:{author}",
            f"--variable=date:{date}",
            "--toc",
            "--number-sections",
            "-o", str(output_pdf)
        ]
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT
        )
        
        if result.returncode != 0:
            pytest.fail(f"PDF generation failed: {result.stderr}")
        
        # Verify PDF was created
        assert output_pdf.exists(), "PDF file was not created"
        
        # Check PDF file size (should be reasonable)
        pdf_size = output_pdf.stat().st_size
        assert pdf_size > 10240, f"PDF file too small ({pdf_size} bytes), likely generation failed"
        assert pdf_size < 10485760, f"PDF file too large ({pdf_size} bytes), might indicate an issue"

    def test_latex_template_compilation(self):
        """Test that LaTeX template can compile without errors."""
        latex_template = PROJECT_ROOT / "template.latex"
        
        # Read template
        with open(latex_template, 'r') as f:
            template_content = f.read()
        
        # Check for common LaTeX syntax errors
        syntax_checks = [
            (r'\\begin{document}', r'\\end{document}'),
            (r'\\documentclass', None),
        ]
        
        for begin_pattern, end_pattern in syntax_checks:
            assert begin_pattern in template_content, f"Template missing: {begin_pattern}"
            if end_pattern:
                assert end_pattern in template_content, f"Template missing: {end_pattern}"
        
        # Check for Pandoc variables
        pandoc_vars = ['$title$', '$author$', '$date$', '$body$']
        for var in pandoc_vars:
            assert var in template_content, f"Template missing Pandoc variable: {var}"

    def test_pdf_metadata_variables(self):
        """Test that PDF metadata variables are properly set up."""
        latex_template = PROJECT_ROOT / "template.latex"
        
        with open(latex_template, 'r') as f:
            template_content = f.read()
        
        # Check for hypersetup configuration
        assert '\\hypersetup{' in template_content, "PDF metadata setup missing"
        
        metadata_fields = ['pdftitle', 'pdfauthor', 'pdfsubject']
        for field in metadata_fields:
            assert field in template_content, f"PDF metadata field missing: {field}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])