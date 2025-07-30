#!/usr/bin/env python3
"""
Unit tests for MkDocs configuration validation.
"""

import os
import yaml
import pytest
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
MKDOCS_CONFIG = PROJECT_ROOT / "mkdocs.yml"


def test_mkdocs_config_exists():
    """Test that mkdocs.yml exists."""
    assert MKDOCS_CONFIG.exists(), "mkdocs.yml file not found"


def test_mkdocs_config_valid_yaml():
    """Test that mkdocs.yml is valid YAML."""
    with open(MKDOCS_CONFIG, 'r') as f:
        try:
            config = yaml.safe_load(f)
            assert config is not None
        except yaml.YAMLError as e:
            pytest.fail(f"mkdocs.yml contains invalid YAML: {e}")


def test_mkdocs_required_fields():
    """Test that mkdocs.yml contains required fields."""
    with open(MKDOCS_CONFIG, 'r') as f:
        config = yaml.safe_load(f)
    
    required_fields = ['site_name', 'theme', 'nav']
    for field in required_fields:
        assert field in config, f"Required field '{field}' missing from mkdocs.yml"


def test_mkdocs_theme_configuration():
    """Test that Material theme is properly configured."""
    with open(MKDOCS_CONFIG, 'r') as f:
        config = yaml.safe_load(f)
    
    assert config['theme']['name'] == 'material', "Theme should be 'material'"
    assert 'features' in config['theme'], "Theme features should be defined"


def test_mkdocs_plugins_configuration():
    """Test that required plugins are configured."""
    with open(MKDOCS_CONFIG, 'r') as f:
        config = yaml.safe_load(f)
    
    assert 'plugins' in config, "Plugins should be defined"
    plugin_names = []
    
    for plugin in config['plugins']:
        if isinstance(plugin, str):
            plugin_names.append(plugin)
        elif isinstance(plugin, dict):
            plugin_names.extend(plugin.keys())
    
    assert 'search' in plugin_names, "Search plugin should be enabled"
    assert 'with-pdf' in plugin_names, "PDF plugin should be enabled"


def test_mkdocs_markdown_extensions():
    """Test that required markdown extensions are configured."""
    with open(MKDOCS_CONFIG, 'r') as f:
        config = yaml.safe_load(f)
    
    assert 'markdown_extensions' in config, "Markdown extensions should be defined"
    
    required_extensions = ['admonition', 'pymdownx.details', 'pymdownx.superfences']
    extension_names = []
    
    for ext in config['markdown_extensions']:
        if isinstance(ext, str):
            extension_names.append(ext)
        elif isinstance(ext, dict):
            extension_names.extend(ext.keys())
    
    for req_ext in required_extensions:
        assert req_ext in extension_names, f"Required extension '{req_ext}' not found"


if __name__ == "__main__":
    pytest.main([__file__])