# genpark-git-conventional-commit-changelog-generator-skill

Agent Skill implementing **Semantic Diff Analysis & Conventional Commit Synthesis** in 100% Python standard library.

## Architectural Flow
```mermaid
flowchart TD
    Diff["Git Staged Diff Buffer"] --> Scan["Keyword & AST Modification Scanner"]
    Scan --> Feat{"New Class/Methods?"}
    Scan --> Fix{"Bug/Error Patches?"}
    Scan --> Test{"Unit Test Assertions?"}
    Scan --> Docs{"Markdown/Documentation?"}
    Feat -->|Yes| M1["feat: ..."]
    Fix -->|Yes| M2["fix: ..."]
    Test -->|Yes| M3["test: ..."]
    Docs -->|Yes| M4["docs: ..."]
    M1 & M2 & M3 & M4 --> Commit["Conventional Commit Message"]
```
