# Project Unidoc Style Guide

**Version 1.0 - Definitive Writing and Formatting Standards**

## 📋 Overview

This style guide defines the writing tone, terminology, and formatting standards for all Project Unidoc technical documentation. Adherence to these standards ensures consistency, professionalism, and accessibility across all company manuals.

## 🎯 Writing Principles

### Tone and Voice
- **Professional yet approachable**: Clear, confident, and helpful
- **User-focused**: Always consider the reader's perspective and needs
- **Concise and direct**: Eliminate unnecessary words and complexity
- **Action-oriented**: Use active voice and clear imperatives

### Target Audience
- **Primary**: Workshop technicians and field engineers
- **Secondary**: System administrators and technical managers
- **Tertiary**: External customers and service partners

## 📝 Writing Standards

### Language Guidelines

**DO:**
- Use present tense for instructions ("Click Save" not "You will click Save")
- Use active voice ("The system generates reports" not "Reports are generated")
- Write in second person for procedures ("You configure the system")
- Use parallel structure in lists and headings
- Write concisely and eliminate filler words

**DON'T:**
- Use future tense unnecessarily
- Use passive voice without good reason
- Include unnecessary technical jargon
- Write overly long sentences (max 25 words)
- Use contractions in formal documentation

### Terminology Standards

#### Company Terms
- **Project Unidoc** (not "project unidoc" or "Unidoc")
- **Ventil Test Equipment** (official company name)
- **CRS10** (not "CRS-10" or "crs10")

#### Technical Terms
- **manual** (not "document" or "guide" unless specifically different)
- **component** (for reusable content pieces)
- **assembly** (for the process of combining components)
- **workflow** (not "work flow")
- **setup** (noun), **set up** (verb)
- **login** (noun), **log in** (verb)

#### Capitalization
- **Sentence case** for headings (not Title Case)
- **Initial caps** for proper nouns and official product names
- **Lowercase** for generic technical terms (unless starting a sentence)

### Numbers and Units
- Spell out numbers one through nine, use numerals for 10 and above
- Use numerals for all technical specifications and measurements
- Always include units of measurement (GB, MHz, seconds)
- Use consistent decimal notation (1.5, not 1,5)

## 🏗️ Formatting Standards

### Document Structure

#### Required Elements
All manuals must include:
1. **Title page** with manual name, version, and date
2. **Table of contents** (auto-generated)
3. **Introduction** explaining purpose and scope
4. **Main content** organized in logical sections
5. **Appendices** (if applicable)

#### Heading Hierarchy
```
# Level 1: Manual title (once per document)
## Level 2: Major sections
### Level 3: Subsections
#### Level 4: Detailed procedures (limit use)
```

#### Section Numbering
- Use automatic numbering through Pandoc/LaTeX
- Don't manually number sections in markdown
- Maximum 4 levels of nesting

### Content Elements

#### Procedures and Instructions
Format step-by-step procedures as numbered lists:

```markdown
1. **Action verb**: Descriptive explanation
   - Sub-step if needed
   - Additional clarification
   
2. **Next action**: Continue with clear steps
   
3. **Final action**: Complete the procedure
```

#### Code and Commands
- Use `inline code` for file names, commands, and short code
- Use code blocks for multi-line examples
- Always specify the language for syntax highlighting

```bash
# Example command with comment
./assemble.sh --verbose
```

#### Warnings and Notes

Use consistent formatting for callouts:

```markdown
> **⚠️ Warning**: Critical information that prevents damage or data loss

> **💡 Tip**: Helpful suggestions to improve workflow

> **📋 Note**: Additional context or clarification
```

#### Lists and Bullets
- Use **bold** for the key term or action in bullet lists
- Keep list items parallel in structure
- Use numbered lists for sequential procedures
- Use bullet lists for non-sequential items

### Tables and Diagrams

#### Table Formatting
- Include clear headers for all columns
- Align numerical data to the right
- Align text data to the left
- Keep tables simple and scannable

#### Images and Diagrams
- Include alternative text for all images
- Use consistent image sizing and placement
- Number figures if referenced in text
- Store images in `docs/assets/images/`

## 🎨 Visual Identity

### Color Scheme
- **Primary**: Blue (#2196F3) - headers and links
- **Secondary**: Light blue (#E3F2FD) - backgrounds and accents
- **Text**: Dark gray (#333333) - main content
- **Warning**: Orange (#FF9800) - cautions and warnings
- **Success**: Green (#4CAF50) - confirmations and tips

### Typography
- **Headings**: Clear, professional font (Material theme default)
- **Body text**: Readable serif font for PDFs, sans-serif for web
- **Code**: Monospace font with syntax highlighting
- **Emphasis**: Use **bold** for important terms, *italic* for emphasis

## 📄 PDF-Specific Standards

### Page Layout
- **Margins**: 1 inch on all sides
- **Font size**: 12pt for body text, scaled appropriately for headings
- **Line spacing**: 1.2x for optimal readability
- **Page numbers**: Bottom center, starting after title page

### Headers and Footers
- **Header**: Manual title (left), section name (right)
- **Footer**: Page number (center), date (right)
- **Title page**: No header/footer

### Professional Elements
- Company logo on title page
- Consistent branding throughout
- Professional color scheme
- Clear section breaks and white space

## 🔍 Quality Checklist

Before publishing any manual, verify:

**Content:**
- [ ] All information is accurate and up-to-date
- [ ] Procedures have been tested and verified
- [ ] Terminology follows the style guide
- [ ] Tone is consistent throughout

**Structure:**
- [ ] Logical organization and flow
- [ ] Proper heading hierarchy
- [ ] Complete table of contents
- [ ] All cross-references work

**Formatting:**
- [ ] Consistent formatting throughout
- [ ] Proper use of callouts and emphasis
- [ ] All images have alt text
- [ ] Tables are properly formatted

**Technical:**
- [ ] All links work (verified by lychee)
- [ ] No spelling errors (verified by cspell)
- [ ] PDF generates correctly
- [ ] Website displays properly

## 🚀 Implementation

### For Writers
1. Review this guide before writing new content
2. Use the component template for new components
3. Follow the assembly format for new manuals
4. Run quality checks before submitting

### For Reviewers
1. Check adherence to style guidelines
2. Verify technical accuracy
3. Test all procedures
4. Ensure professional presentation

### For Maintainers
1. Update this guide as standards evolve
2. Provide training on style standards
3. Monitor consistency across all manuals
4. Update templates to reflect changes

---

**Document History:**
- Version 1.0 (2025-01-30): Initial definitive style guide
- Approved for use in Project Unidoc V1 MVP

This style guide ensures that all Project Unidoc documentation maintains the highest standards of clarity, consistency, and professionalism.