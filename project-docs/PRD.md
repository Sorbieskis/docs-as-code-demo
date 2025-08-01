Product Requirements Document: Project Unidoc

    Version: 1.0 (Minimum Viable Product)

    Status: Approved for Development

    Author: Deimonas Suchanka

    Stakeholders: Jan (General Manager), Rob (CEO/Software Lead), Ventil Engineering Team

1. Introduction & Vision
1.1. The Problem

Ventil's current documentation process is an ad-hoc system reliant on scattered, unversioned files (e.g., Word documents). This creates a high risk of using outdated information, results in inconsistent and unprofessional outputs, and causes significant internal inefficiency. Furthermore, there is no safe or structured process for non-technical subject matter experts to contribute.
1.2. Strategic Purpose of this V1 (MVP)

The primary goal of this first version is Stakeholder Buy-In. We will deliver a limited-scope but fully functional and automated pipeline to serve as a definitive proof-of-concept. The secondary goal is Product Delivery, using the pipeline to solve the urgent need for high-quality PDF manuals, starting with the CRS10 software manual and other key documents.
1.3. The Long-Term Vision

Project Unidoc will establish a scalable pattern for a "single source of truth" for all technical documentation at Ventil. This will enable a modular, "Lego block" system for the future automatic generation of machine-specific manuals and will be replicated across different documentation domains (e.g., internal policies, technical specifications) in separate repositories.
2. User Personas & Needs

    2.1. The Contributor (e.g., a Team Leader, external guest): Needs a simple, low-friction web interface to add or edit technical content without needing to understand Git. The experience should be as simple as using a word processor.

    2.2. The Reviewer (e.g., "Core Admin Team"): Needs a clear, auditable process on a centralized platform (GitHub) to review proposed changes, ensure quality, and give formal approval before content is published.

    2.3. The Consumer (e.g., Workshop Technician, Customer): Needs access to the most up-to-date, accurate, and professionally formatted version of a manual, primarily in a print-ready PDF format.

3. V1 (MVP) Scope & Key Deliverables
3.1. Pilot Projects

The V1 pipeline will be used to produce new, high-quality PDF manuals for:

    The CRS10 software manual.

    At least two other existing manuals, which will be converted from their current format to Markdown.

3.2. V1 Key Deliverables

In addition to the manuals, the V1 project will deliver the following foundational assets:

    A Definitive Style Guide defining the writing tone, terminology, and formatting standards.

    A professional, reusable LaTeX Template that defines the visual identity for all company PDF manuals.

    A fully configured and documented CI/CD Pipeline on GitHub Actions.

3.3. V1 Success Metrics

    Successfully publish the three pilot manuals as high-quality PDFs.

    Successfully deploy a private static website to Netlify with a functional Decap CMS editor.

    The entire process must be 100% version-controlled and auditable in the Git repository.

    The formal review and approval workflow via GitHub Pull Requests must be successfully used for at least one content change.

    The automated quality checks (spell check, link check) must successfully run as part of the CI pipeline.

4. Functional Requirements
4.1. Content Architecture (The "Lego Blocks")

The content will be structured modularly. Final manuals will be defined by simple YAML "assembly files" that list which content components to include.
4.2. The Review Workflow (Per Jan's Specification)

    The main branch of the repository will be protected. No direct commits will be allowed.

    All changes must be submitted as a Pull Request (PR). This is the central point for all reviews.

    A "Core Admin Team" (e.g., Team Leaders) will be established in GitHub. Branch protection rules will require at least one approval from a member of this team to merge a PR.

    Temporary Access: For V1, external or temporary contributors can be given standard "Write" access to the repository, allowing them to submit PRs. Their changes will still be subject to the mandatory review by the Core Admin Team.

    Approval UI: The approval of Pull Requests will take place exclusively within the GitHub.com web interface. The Decap CMS dashboard is for content editing only and will not have integrated approval buttons.

4.3. The Automated Pipeline (CI/CD)

    The pipeline must trigger automatically on every merge to the main branch.

    Automated Quality Gates: The pipeline must include automated checks for spelling (cspell) and broken links (lychee). A build will fail if these checks do not pass.

    Primary Output: It must successfully generate high-quality PDFs using Pandoc and the official LaTeX template. The final PDFs will be exported to a designated internal location.

    Secondary Output: It must successfully build a static website using MkDocs and deploy it to a private Netlify site.

4.4. The CMS Experience

    The Decap CMS editor must be configured for maximum simplicity, using a "rich text" (WYSIWYG) widget and a minimal set of formatting buttons.

    The CMS will feature two distinct sections: one for editing content "chapters" and another for assembling final manuals from those chapters using a simple dropdown interface.

5. V1 Tooling & Environment Specification

    Version Control: GitHub

    Project Management: GitHub Projects

    Automation: GitHub Actions

    PDF Generation: Pandoc with a custom LaTeX template.

    Static Site Generation: MkDocs with the "Material for MkDocs" theme.

    Content Management System (CMS): Decap CMS

    CMS Hosting: Netlify (free tier), connected to the GitHub repository via OAuth.

    Automated Quality Tools: cspell (spell checking), lychee (link checking).

6. Future Considerations (Post-V1)

    ChatOps Integration: To further simplify the review process, a future version could integrate with Microsoft Teams. This would allow the "Core Admin Team" to review and approve Pull Requests via interactive buttons directly within a Teams channel, removing the need for them to interact with the GitHub UI.

    Temporary Guest Access Model: A more formal system for temporary contributor access can be explored, potentially using features like GitHub Apps for more granular permissions.


     Evolution Path                                                                                                                                              │ │
│ │                                                                                                                                                             │ │
│ │ - V2: Add Python orchestration back with lessons learned                                                                                                    │ │
│ │ - V3: Add dynamic navigation and advanced features                                                                                                          │ │
│ │ - V4: Multi-format outputs and advanced validation                                                                                                          │ │
│ │                                                               