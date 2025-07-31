
***

# CLAUDE.md

This file provides guidance to you, Claude, for working within the docs-as-code repository. It is your primary instruction set and master index.

---

## 📋 Project Overview

**docs-as-code-demo** is an Automated Technical Documentation System.

Its primary purpose is to solve a business problem by replacing an inefficient, error-prone manual process with a centralized, automated system that ensures consistency, quality, and safe collaboration.

* **Core Features:** A central Git repository as a "single source of truth," a web-based editor (Decap CMS) for non-technical users, a pull-request-based review workflow, and automated generation of both a static website (MkDocs) and a print-ready PDF (Pandoc/LaTeX).
* **Technology Stack:** Markdown, Git/GitHub, Decap CMS, GitHub Actions, MkDocs, Pandoc, LaTeX.

---

## 🏗️ System Architecture

The project uses a **CI/CD-Driven Documentation Pipeline**. This architecture ensures that every change to the source content automatically and consistently regenerates the final outputs.

1.  **Stage A (Content Contribution):** Content is created or edited. Technical users push commits directly via Git. Non-technical users submit changes via the Decap CMS web interface, which creates a pull request.
2.  **Stage B (Review & Merge):** All changes proposed by non-technical users are reviewed and approved via the GitHub pull request workflow, ensuring quality control before they are merged into the `main` branch.
3.  **Stage C (Automated Build & Deploy):** The merge to `main` triggers a GitHub Actions workflow. This workflow runs two parallel jobs: one builds the MkDocs website and deploys it, while the other uses Pandoc/LaTeX to generate the final PDF and export it.

The directory structure provides a map of the codebase.

---

## 📝 Critical Development Principles

Adherence to these principles is non-negotiable. They guide all file generation and modification.

### 🛡️ Single Source of Truth & Process Integrity

This is the most important rule for this project. The entire system is built on this foundation.

* **The Git Repository is Absolute.** All content and configuration must live in the central GitHub repository. There are no alternative, "official" sources.
* **All Changes Go Through the Process.** All modifications must be introduced to the `main` branch via a direct commit (for technical owners) or an approved Pull Request (for all other contributors). Out-of-band changes (e.g., emailing a "fixed" PDF) are invalid and must be rejected.
* **Outputs are Disposable Artifacts.** The generated website and PDFs are temporary build products. They are never to be edited directly. The system must be able to delete and perfectly regenerate them at any time from the source files.

### 📐 Software Design Principles

These principles ensure the system is maintainable, scalable, and robust.

* **SRP & Clear Interfaces:** Focus each component (e.g., a specific workflow, a configuration file) on a single, well-defined purpose.
* **KISS (Keep It Simple, Stupid):** Always prefer the simplest solution that correctly solves the problem. Avoid unnecessary complexity in workflows and scripts.
* **DRY (Don't Repeat Yourself):** Ensure every piece of knowledge (like a reusable content snippet or a configuration setting) has a single, authoritative representation.
* **YAGNI (You Aren't Gonna Need It):** Generate only what is strictly necessary to meet the requirements defined in the PRD.

For a detailed breakdown, refer to `docs/CODE_GUIDELINES.md`.

---

## 🔒 Governance & File Permissions

To maintain project integrity, a strict governance model is in place.

* **Level 1: Read/Write (Your Working Memory):**
    * **Files:** `session-*.md`, temporary `topic-*.md` files.
    * **Rule:** You are encouraged to write to these files to log progress, update checklists, and maintain conversational state.

* **Level 2: Strictly Read-Only (The Project's Constitution):**
    * **Files:** This file (`CLAUDE.md`), `docs/PRD.md`, `docs/CODE_GUIDELINES.md`.
    * **Rule:** You are not authorized to modify these foundational documents. They are your immutable instructions.

* **Level 3: Write by Explicit Command (Living Documents):**
    * **Files:** `README.md`, `mkdocs.yml`, `.github/workflows/*.yml`.
    * **Rule:** You may only modify these files when you receive a direct and specific command from the user to do so (e.g., "Add this plugin to the mkdocs.yml file."). You are acting as a scribe, not an author.

> **Critical Safeguard:** You must treat all Level 2 documents as strictly read-only. Do not modify them under any circumstances unless you receive an explicit override command from the user that acknowledges they are changing a foundational document.

---

## 🤝 How to Interact

1.  **Start Here:** Always begin a work session by reviewing this file and the latest `session-*.md` file to understand the project's state and your immediate tasks.
2.  **Use On-Demand Context:** Do not guess. If a task requires knowledge about features or configuration, state that you need to reference the relevant file (`PRD.md`, `mkdocs.yml`, etc.).
3.  **Act as an Assistant:** Your role is to execute tasks and provide solutions within this established framework. Architectural and product decisions are made by the human developer.