---
title: "Component Authoring"
component_type: "unique"
---

# 2. Component-Based Authoring Model

To adhere to the **DRY (Don't Repeat Yourself)** principle, our manuals are not written as single, monolithic files. Instead, they are assembled from smaller, reusable components.

## Types of Content Files

1.  **Master Assembly Files (`docs/manuals/*.yml`)**
    * **Purpose:** These are the master files for a complete manual. Their main job is to define the structure of a manual and *include* the other components in the correct order. **This architecture enables infinite scalability** - adding new manuals requires only creating new assembly files that reference existing or new components.
    * **Scalability Benefits:**
        - **Template-driven consistency**: All manuals inherit the same professional structure
        - **Component reuse**: Common sections (safety, maintenance, contact info) are written once, used everywhere
        - **Zero-effort standardization**: New products automatically follow established documentation patterns
        - **Automated cross-manual updates**: Changes to shared components propagate instantly across all manuals
    * **Example (`docs/manuals/pekos-v2.yml`):**
        ```yaml
        title: "Pekos V2 Clamping System Manual"
        author: "Project Unidoc Team"
        date: "2025-01-30"
        chapters:
          - content/includes/company-header.md
          - content/parts/pekos-v2-introduction.md
          - content/parts/pekos-v2-installation.md
          - content/includes/standard-maintenance-schedule.md
        ```

2.  **Unique Part Files (`docs/content/parts/`)**
    * **Purpose:** This directory holds content that is unique to a specific machine or component. These are the substantial chapters of a manual.
    * **Examples:** `pekos-v2-installation.md`, `crs10-software-guide.md`.

3.  **Reusable Include Files (`docs/content/includes/`)**
    * **Purpose:** This directory is for "Lego bricks"—small, persistent snippets of content that are identical across multiple manuals.
    * **Examples:** `standard-safety-warnings.md`, `company-contact-info.md`.

## How It Comes Together

The build process is configured to understand YAML assembly files. When it builds a manual, it starts with the **Master Assembly File**, reads the list of chapters, and stitches them together into a single, complete document before converting it to its final format.