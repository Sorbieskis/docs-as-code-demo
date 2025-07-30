#!/usr/bin/env python3
"""
Unit tests for Decap CMS configuration validation.
"""

import os
import yaml
import pytest
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
CMS_CONFIG = PROJECT_ROOT / "docs" / "admin" / "config.yml"


def test_cms_config_exists():
    """Test that CMS config file exists."""
    assert CMS_CONFIG.exists(), "docs/admin/config.yml file not found"


def test_cms_config_valid_yaml():
    """Test that CMS config is valid YAML."""
    with open(CMS_CONFIG, 'r') as f:
        try:
            config = yaml.safe_load(f)
            assert config is not None
        except yaml.YAMLError as e:
            pytest.fail(f"CMS config contains invalid YAML: {e}")


def test_cms_backend_configuration():
    """Test that CMS backend is properly configured."""
    with open(CMS_CONFIG, 'r') as f:
        config = yaml.safe_load(f)
    
    assert 'backend' in config, "Backend configuration missing"
    backend = config['backend']
    
    assert backend['name'] == 'github', "Backend should be 'github'"
    assert 'repo' in backend, "Repository must be specified"
    assert 'branch' in backend, "Branch must be specified"


def test_cms_collections_configuration():
    """Test that CMS collections are properly configured."""
    with open(CMS_CONFIG, 'r') as f:
        config = yaml.safe_load(f)
    
    assert 'collections' in config, "Collections must be defined"
    collections = config['collections']
    
    # Find pages collection
    pages_collection = None
    for collection in collections:
        if collection.get('name') == 'pages':
            pages_collection = collection
            break
    
    assert pages_collection is not None, "Pages collection must be defined"
    assert 'folder' in pages_collection, "Pages collection must specify folder"
    assert 'fields' in pages_collection, "Pages collection must have fields"


def test_cms_pages_collection_fields():
    """Test that pages collection has required fields."""
    with open(CMS_CONFIG, 'r') as f:
        config = yaml.safe_load(f)
    
    pages_collection = None
    for collection in config['collections']:
        if collection.get('name') == 'pages':
            pages_collection = collection
            break
    
    assert pages_collection is not None, "Pages collection not found"
    
    fields = pages_collection['fields']
    field_names = [field.get('name') for field in fields]
    
    required_fields = ['title', 'author', 'date', 'body']
    for field in required_fields:
        assert field in field_names, f"Required field '{field}' missing from pages collection"


def test_cms_media_configuration():
    """Test that media handling is configured."""
    with open(CMS_CONFIG, 'r') as f:
        config = yaml.safe_load(f)
    
    assert 'media_folder' in config, "Media folder must be specified"
    assert 'public_folder' in config, "Public folder must be specified"


def test_cms_admin_interface_exists():
    """Test that admin interface HTML file exists."""
    admin_html = PROJECT_ROOT / "docs" / "admin" / "index.html"
    assert admin_html.exists(), "docs/admin/index.html file not found"


def test_cms_admin_interface_content():
    """Test that admin interface has required content."""
    admin_html = PROJECT_ROOT / "docs" / "admin" / "index.html"
    
    with open(admin_html, 'r') as f:
        content = f.read()
    
    required_elements = [
        'decap-cms',
        'Content Manager',
        '<!DOCTYPE html>'
    ]
    
    for element in required_elements:
        assert element in content, f"Admin interface missing required element: {element}"


if __name__ == "__main__":
    pytest.main([__file__])