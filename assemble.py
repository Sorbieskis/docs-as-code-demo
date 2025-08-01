#!/usr/bin/env python3
"""
Project Unidoc Manual Assembly System
====================================

A robust Python-based manual assembly system that combines YAML-defined 
component lists into complete documentation manuals.

Features:
- Proper YAML parsing with error handling
- Cross-platform compatibility
- Comprehensive logging and validation
- Clean, maintainable code architecture
"""

import os
import sys
import yaml
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ManualAssembler:
    """Handles the assembly of documentation manuals from component files."""
    
    def __init__(self, docs_dir: str = "docs", output_dir: str = "assembled"):
        self.docs_dir = Path(docs_dir)
        self.output_dir = Path(output_dir)
        self.manuals_dir = self.docs_dir / "manuals"
        self.components_dir = self.docs_dir / "content" / "components"
        
        # Ensure output directory exists
        self.output_dir.mkdir(exist_ok=True)
        
    def discover_manuals(self) -> List[Path]:
        """Discover all YAML manual definition files."""
        if not self.manuals_dir.exists():
            logger.error(f"Manuals directory not found: {self.manuals_dir}")
            return []
            
        manual_files = list(self.manuals_dir.glob("*.yml"))
        logger.info(f"Found {len(manual_files)} manual definition(s)")
        return manual_files
    
    def load_manual_config(self, manual_file: Path) -> Optional[Dict]:
        """Load and validate a manual configuration file."""
        try:
            with open(manual_file, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
                
            if not config:
                logger.warning(f"Empty configuration in {manual_file}")
                return None
                
            # Validate required fields
            required_fields = ['title', 'author', 'date', 'chapters']
            missing_fields = [field for field in required_fields if field not in config]
            
            if missing_fields:
                logger.error(f"Missing required fields in {manual_file}: {missing_fields}")
                return None
                
            return config
            
        except yaml.YAMLError as e:
            logger.error(f"YAML parsing error in {manual_file}: {e}")
            return None
        except FileNotFoundError:
            logger.error(f"Manual file not found: {manual_file}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error loading {manual_file}: {e}")
            return None
    
    def load_component(self, component_path: str) -> Optional[str]:
        """Load content from a component file."""
        # Handle both relative and absolute component paths
        if component_path.startswith('content/components/'):
            full_path = self.docs_dir / component_path
        else:
            full_path = self.components_dir / component_path
            
        if not full_path.exists():
            logger.error(f"Component file not found: {full_path}")
            return None
            
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                
            if not content:
                logger.warning(f"Empty component file: {full_path}")
                return ""
                
            return content
            
        except Exception as e:
            logger.error(f"Error reading component {full_path}: {e}")
            return None
    
    def assemble_manual(self, manual_file: Path) -> bool:
        """Assemble a single manual from its configuration."""
        config = self.load_manual_config(manual_file)
        if not config:
            return False
            
        manual_name = manual_file.stem
        logger.info(f"Assembling manual: {config['title']}")
        
        # Build the assembled content
        content_parts = []
        
        # Add YAML frontmatter
        frontmatter = f"""---
title: "{config['title']}"
author: "{config['author']}"
date: "{config['date']}"
description: "{config.get('description', '')}"
---

"""
        content_parts.append(frontmatter)
        
        # Process each chapter
        chapters = config.get('chapters', [])
        if not chapters:
            logger.warning(f"No chapters defined for {manual_name}")
            return False
            
        failed_components = []
        for i, chapter in enumerate(chapters, 1):
            # Handle both string and dict chapter formats
            if isinstance(chapter, dict):
                chapter_path = chapter.get('chapter', '')
            else:
                chapter_path = str(chapter)
                
            if not chapter_path:
                logger.warning(f"Empty chapter path in {manual_name}, chapter {i}")
                continue
                
            logger.info(f"  Loading chapter: {chapter_path}")
            component_content = self.load_component(chapter_path)
            
            if component_content is None:
                failed_components.append(chapter_path)
                continue
                
            # Add the component content with spacing
            content_parts.append(component_content)
            content_parts.append("\n\n")
        
        if failed_components:
            logger.error(f"Failed to load components for {manual_name}: {failed_components}")
            return False
            
        # Write assembled manual
        output_file = self.output_dir / f"{manual_name}.md"
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(''.join(content_parts))
                
            logger.info(f"✓ Assembled: {output_file}")
            
            # Copy to docs/ for MkDocs
            docs_copy = self.docs_dir / f"{manual_name}.md"
            with open(docs_copy, 'w', encoding='utf-8') as f:
                f.write(''.join(content_parts))
                
            logger.info(f"✓ Copied to docs/: {docs_copy}")
            return True
            
        except Exception as e:
            logger.error(f"Error writing assembled manual {output_file}: {e}")
            return False
    
    def run(self) -> int:
        """Run the complete assembly process."""
        logger.info("🚀 Project Unidoc Manual Assembly")
        logger.info("=" * 40)
        
        # Discover manual files
        manual_files = self.discover_manuals()
        if not manual_files:
            logger.error("No manual definition files found")
            return 1
            
        # Process each manual
        successful = 0
        failed = 0
        
        for manual_file in manual_files:
            if self.assemble_manual(manual_file):
                successful += 1
            else:
                failed += 1
                
        # Summary
        logger.info("")
        logger.info("🎉 Assembly Complete!")
        logger.info(f"  Successful: {successful} manuals")
        if failed > 0:
            logger.error(f"  Failed: {failed} manuals")
            return 1
            
        logger.info(f"  Output: {self.output_dir}/")
        logger.info(f"  MkDocs: {self.docs_dir}/")
        logger.info("")
        logger.info("Next steps:")
        logger.info("  📖 Build website: mkdocs serve")
        logger.info("  📄 Generate PDFs: pandoc assembled/manual-name.md -o manual-name.pdf")
        
        return 0

def main():
    """Main entry point for the assembly script."""
    try:
        assembler = ManualAssembler()
        exit_code = assembler.run()
        sys.exit(exit_code)
        
    except KeyboardInterrupt:
        logger.info("\nAssembly interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()