This file provides guidance to you, the AI assistant, for working within the Project Unidoc repository. It is your primary instruction set and master index.
📋 Project Overview

Project Unidoc is an automated, enterprise-grade technical documentation system for Ventil Test Equipment.

Its primary purpose is to solve a business problem by replacing an inefficient, error-prone manual process with a centralized, automated system that ensures consistency, quality, and safe collaboration between technical and non-technical teams. The V1 (MVP) is detailed in the PRD: Project Unidoc (V1 - Final).

    Core Features: A central Git repository as a "single source of truth," a web-based editor (Decap CMS) for non-technical users, a pull-request-based review workflow, and automated generation of both a static website (for the CMS) and print-ready PDFs (for consumers).

    Technology Stack: Markdown, YAML, Git/GitHub, Decap CMS, GitHub Actions, MkDocs, Pandoc, LaTeX, and Python for the manual assembly script.

🏗️ System Architecture

The project uses a CI/CD-Driven Documentation Pipeline. This architecture ensures that every change to the source content automatically and consistently regenerates the final outputs.

    Stage A (Content Contribution): Content is created or edited. Technical users push commits directly via Git. Non-technical users submit changes via the Decap CMS web interface, which creates a pull request.

    Stage B (Review & Merge): All changes proposed by contributors are reviewed and approved via the GitHub Pull Request workflow by a "Core Admin Team," ensuring quality control before they are merged into the main branch.

    Stage C (Automated Build & Deploy): The merge to main triggers a GitHub Actions workflow. This workflow runs parallel jobs to build the MkDocs website (and deploy it to a private host for the CMS) and to generate the final PDF manuals (and export them to a shared drive).

The directory structure and component model are detailed in the "Project Structure Guide" page of the presentation site.
📝 Critical Development Principles

Adherence to these principles is non-negotiable. They guide all file generation and modification.
🛡️ Process Integrity Protocol

This is the most important rule for this project. The entire system is built on this foundation.

    The Git Repository is the Single Source of Truth. All content and configuration must live in the central GitHub repository. There are no alternative, "official" sources.

    All Changes Go Through the Process. All modifications must be introduced to the main branch via an approved Pull Request. Out-of-band changes (e.g., emailing a "fixed" PDF) are invalid and must be rejected.

    Outputs are Disposable Artifacts. The generated website and PDFs are temporary build products. They are never to be edited directly. The system must be able to delete and perfectly regenerate them at any time from the source files.

📐 Software Design Principles

These principles ensure the system is maintainable, scalable, and robust.

    SRP & Clear Interfaces: Focus each component (e.g., a workflow, a script, a config file) on a single, well-defined purpose.

    KISS (Keep It Simple, Stupid): Always prefer the simplest solution that correctly solves the problem. Avoid unnecessary complexity.

    DRY (Don't Repeat Yourself): Ensure every piece of knowledge has a single, authoritative representation. Avoid duplicated logic.

    YAGNI (You Aren't Gonna Need It): Generate only what is strictly necessary to meet the requirements defined in the PRD.

For a detailed breakdown, refer to the CODE_GUIDELINES.md file.
🔒 Governance & File Permissions

To maintain project integrity, a strict governance model is in place.

    Level 1: Read/Write (Your Working Memory):

        Files: session-*.md, temporary topic-*.md files.

        Rule: You are encouraged to write to these files to log progress, update checklists, and maintain conversational state.

    Level 2: Strictly Read-Only (The Project's Constitution):

        Files: This file (AI_GUIDELINES.md), PRD: Project Unidoc (V1 - Final), CODE_GUIDELINES.md.

        Rule: You are not authorized to modify these foundational documents. They are your immutable instructions.

    Level 3: Write by Explicit Command (Living Documents):

        Files: README.md, mkdocs.yml, .github/workflows/*.yml, assemble_manuals.py, template.latex, docs/admin/config.yml.

        Rule: You may only modify these files when you receive a direct and specific command from the user to do so (e.g., "Add the cspell check to the ci.yml workflow."). You are acting as a scribe, not an author.

    Critical Safeguard: You must treat all Level 2 documents as strictly read-only. Do not modify them under any circumstances unless you receive an explicit override command from the user that acknowledges they are changing a foundational document.

🤝 How to Interact

    Start Here: Always begin a work session by reviewing this file and the latest session-*.md file to understand the project's state and your immediate tasks.

    Use On-Demand Context: Do not guess. If a task requires knowledge about features or configuration, state that you need to reference the relevant file (PRD: Project Unidoc (V1 - Final), mkdocs.yml, etc.).

    Act as an Assistant: Your role is to execute tasks and provide solutions within this established framework. Architectural and product decisions are made by the human developer.