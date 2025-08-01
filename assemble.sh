#!/bin/bash

# Simple Manual Assembly Script for Project Unidoc
# Replaces complex Python orchestration with straightforward shell script

# Remove set -e to see all errors
# set -e  # Exit on any error

DOCS_DIR="docs"
MANUALS_DIR="$DOCS_DIR/manuals"
ASSEMBLED_DIR="assembled"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 Project Unidoc Simple Assembly${NC}"
echo "========================================"

# Create assembled directory
mkdir -p "$ASSEMBLED_DIR"

# Function to extract YAML field value
get_yaml_field() {
    local file="$1"
    local field="$2"
    grep "^$field:" "$file" | sed 's/^[^:]*: *"\?//' | sed 's/"\?$//'
}

# Function to extract chapters list from YAML
get_yaml_chapters() {
    local file="$1"
    sed -n '/^chapters:/,/^[^ ]/p' "$file" | \
    grep '^ *-' | \
    sed 's/^ *- *//' | \
    sed 's/^docs\///'  # Remove docs/ prefix if present
}

# Function to assemble a single manual
assemble_manual() {
    local manual_file="$1"
    local manual_name=$(basename "$manual_file" .yml)
    
    echo -e "\n${BLUE}📚 Processing: $manual_name${NC}"
    
    # Extract metadata
    local title=$(get_yaml_field "$manual_file" "title")
    local author=$(get_yaml_field "$manual_file" "author")
    local date=$(get_yaml_field "$manual_file" "date")
    local description=$(get_yaml_field "$manual_file" "description")
    
    echo "  Title: $title"
    echo "  Author: $author"
    echo "  Date: $date"
    
    # Create assembled markdown file
    local output_file="$ASSEMBLED_DIR/${manual_name}.md"
    
    # Write frontmatter
    cat > "$output_file" << EOF
---
title: "$title"
author: "$author"
date: "$date"
description: "$description"
---

EOF
    
    # Process each chapter
    echo "  Chapters:"
    
    # Use process substitution to avoid subshell issues
    while IFS= read -r chapter_path; do
        if [ -n "$chapter_path" ]; then
            local full_path="$DOCS_DIR/$chapter_path"
            echo "    - $chapter_path"
            
            if [ -f "$full_path" ]; then
                # Add chapter content
                echo "" >> "$output_file"
                cat "$full_path" >> "$output_file" 
                echo -e "\n\n---\n" >> "$output_file"
            else
                echo -e "    ${RED}⚠️ Warning: Chapter file not found: $full_path${NC}"
            fi
        fi
    done < <(get_yaml_chapters "$manual_file")
    
    echo -e "  ${GREEN}✓ Assembled: $output_file${NC}"
    
    # Also copy to docs/ for MkDocs (but only the assembled content)
    cp "$output_file" "$DOCS_DIR/"
    echo -e "  ${GREEN}✓ Copied to docs/ for MkDocs${NC}"
}

# Main execution
if [ ! -d "$MANUALS_DIR" ]; then
    echo -e "${RED}❌ Error: Manuals directory not found: $MANUALS_DIR${NC}"
    exit 1
fi

# Find all YAML files in manuals directory
manual_count=0
echo -e "\n${BLUE}🔍 Discovering manuals in $MANUALS_DIR${NC}"
for manual_file in "$MANUALS_DIR"/*.yml; do
    echo "  Checking: $manual_file"
    if [ -f "$manual_file" ]; then
        echo "  Processing: $manual_file"
        assemble_manual "$manual_file"
        ((manual_count++))
        echo "  Manual count now: $manual_count"
    else
        echo "  Not a file: $manual_file"
    fi
done

if [ $manual_count -eq 0 ]; then
    echo -e "${RED}❌ No manual assembly files found in $MANUALS_DIR${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}🎉 Assembly Complete!${NC}"
echo "  Processed: $manual_count manuals"
echo "  Output: $ASSEMBLED_DIR/"
echo "  MkDocs: docs/"
echo ""
echo "Next steps:"
echo "  📖 Build website: mkdocs serve"
echo "  📄 Generate PDFs: pandoc assembled/manual-name.md -o manual-name.pdf"