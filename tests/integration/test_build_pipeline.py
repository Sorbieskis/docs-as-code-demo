#!/usr/bin/env python3
"""
Integration tests for the complete build pipeline.
"""

import os
import subprocess
import tempfile
import shutil
import pytest
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent


class TestBuildPipeline:
    """Test the complete build pipeline integration."""

    def setup_method(self):
        """Set up test environment."""
        self.original_dir = os.getcwd()
        os.chdir(PROJECT_ROOT)

    def teardown_method(self):
        """Clean up after tests."""
        os.chdir(self.original_dir)
        
        # Clean up build artifacts
        site_dir = PROJECT_ROOT / "site"
        if site_dir.exists():
            shutil.rmtree(site_dir)

    def test_mkdocs_build_succeeds(self):
        """Test that MkDocs builds successfully."""
        result = subprocess.run(
            ["python", "-m", "mkdocs", "build", "--strict"],
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT
        )
        
        assert result.returncode == 0, f"MkDocs build failed: {result.stderr}"
        
        # Check that site directory was created
        site_dir = PROJECT_ROOT / "site"
        assert site_dir.exists(), "Site directory not created"
        
        # Check that index.html was generated
        index_html = site_dir / "index.html"
        assert index_html.exists(), "index.html not generated"

    def test_mkdocs_serves_locally(self):
        """Test that MkDocs can serve the site locally."""
        # First build the site
        build_result = subprocess.run(
            ["python", "-m", "mkdocs", "build"],
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT
        )
        
        assert build_result.returncode == 0, f"MkDocs build failed: {build_result.stderr}"
        
        # Start server in background and test it can start
        server_process = subprocess.Popen(
            ["python", "-m", "mkdocs", "serve", "--dev-addr", "127.0.0.1:8001"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=PROJECT_ROOT
        )
        
        try:
            # Give server time to start
            import time
            time.sleep(3)
            
            # Check if process is still running (didn't crash)
            poll_result = server_process.poll()
            assert poll_result is None, "MkDocs server crashed on startup"
            
        finally:
            # Clean up server process
            server_process.terminate()
            try:
                server_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                server_process.kill()

    def test_html_content_quality(self):
        """Test that generated HTML meets quality standards."""
        # Build the site
        result = subprocess.run(
            ["python", "-m", "mkdocs", "build"],
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT
        )
        
        assert result.returncode == 0, f"MkDocs build failed: {result.stderr}"
        
        # Read generated HTML
        index_html = PROJECT_ROOT / "site" / "index.html"
        with open(index_html, 'r') as f:
            html_content = f.read()
        
        # Check for essential HTML elements
        quality_checks = [
            '<title>',
            '<meta charset="utf-8">',
            'Ventil Docs Demo',
            '<h1',
            '<nav',
            'material'  # Material theme elements
        ]
        
        for check in quality_checks:
            assert check in html_content, f"HTML quality check failed: missing '{check}'"

    def test_assets_generation(self):
        """Test that CSS/JS assets are properly generated."""
        # Build the site
        result = subprocess.run(
            ["python", "-m", "mkdocs", "build"],
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT
        )
        
        assert result.returncode == 0, f"MkDocs build failed: {result.stderr}"
        
        # Check that assets directory exists
        assets_dir = PROJECT_ROOT / "site" / "assets"
        assert assets_dir.exists(), "Assets directory not created"
        
        # Check for CSS files (Material theme should generate CSS)
        css_files = list(assets_dir.glob("**/*.css"))
        assert len(css_files) > 0, "No CSS files generated"
        
        # Check for JS files
        js_files = list(assets_dir.glob("**/*.js"))
        assert len(js_files) > 0, "No JavaScript files generated"

    def test_search_functionality_setup(self):
        """Test that search functionality is properly set up."""
        # Build the site
        result = subprocess.run(
            ["python", "-m", "mkdocs", "build"],
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT
        )
        
        assert result.returncode == 0, f"MkDocs build failed: {result.stderr}"
        
        # Check for search index
        search_files = list((PROJECT_ROOT / "site").glob("**/search_index.json"))
        assert len(search_files) > 0, "Search index not generated"
        
        # Verify search index is not empty
        search_index = search_files[0]
        with open(search_index, 'r') as f:
            search_content = f.read()
        
        assert len(search_content) > 10, "Search index appears to be empty"
        assert "Ventil" in search_content, "Search index doesn't contain expected content"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])