# VS Code Workspace Settings

This directory contains VS Code settings that apply specifically to the `platform-inspector` repository.

## Why is GitHub Copilot disabled?

GitHub Copilot is intentionally disabled for this project while working through the early stages of the Python learning roadmap.

The purpose of `platform-inspector` is not simply to produce working Python code. The project is being built incrementally to develop a practical understanding of Python for Platform Engineering.

The learning approach is:

> **One concept → one useful improvement → understand it → test it → commit it → move on.**

During the foundational stages, AI-generated code completions can make it too easy to skip the process of remembering Python syntax, making mistakes, debugging them, and understanding why the code works.

For that reason, `.vscode/settings.json` contains a workspace-level GitHub Copilot configuration:

```json
{
    "github.copilot.enable": {
        "*": false,
        "python": false
    }
}
```

This setting applies only when working in this VS Code workspace. It does **not** mean that GitHub Copilot needs to be disabled globally.

## What about Pylance?

Pylance should remain enabled.

Pylance provides useful Python development assistance such as:

- Syntax and type checking
- Import validation
- IntelliSense
- Function and variable information
- Detection of undefined variables
- Python-aware diagnostics

The distinction is intentional:

```text
Pylance
    ↓
Helps identify and understand problems in code I write.

GitHub Copilot
    ↓
Can generate the code for me before I have learned to write it myself.
```

During the learning stages of this project, the first type of assistance is encouraged while the second is intentionally limited.

## When should Copilot be enabled again?

There is no fixed roadmap step where Copilot must be re-enabled.

A good guideline is:

> Re-enable Copilot when Python syntax and the core concepts are familiar enough that its suggestions can be reviewed critically rather than accepted because they simply look correct.

At that point, Copilot becomes what it should be for this project:

**a productivity tool rather than a substitute for learning.**

Until then, writing the code manually is part of the exercise.

---

If Copilot appears to be unexpectedly disabled when revisiting this repository in the future, check:

```text
.vscode/settings.json
```

before troubleshooting the VS Code installation or GitHub Copilot extension.

The behavior may be completely intentional. 🙂