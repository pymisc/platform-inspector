# Platform Inspector — Python for Platform Engineering

A hands-on Python learning project built incrementally from basic Python fundamentals into a real-world Platform Engineering diagnostic tool.

The goal is **not to complete a Python course**.

The goal is to learn Python by continuously building, improving, testing, and operating a real project.

## Learning Philosophy

> **One concept → one useful improvement → understand it → test it → commit it → move on.**

Each step introduces a small concept or capability and applies it directly to the project.

We intentionally avoid building the entire architecture at the beginning.

The project should evolve naturally:

```text
Simple Python Script
        │
        ▼
Python Fundamentals
        │
        ▼
Linux Inspector
        │
        ▼
File Parser
        │
        ▼
Log Analyzer
        │
        ▼
Tested Python Application
        │
        ▼
AWS Inspector
        │
        ▼
Kubernetes Inspector
        │
        ▼
Platform Doctor
        │
        ▼
Production-Style Platform Engineering Tool
```

---

# Phase 1 — Python Foundations

- [ ] **STEP 1 — Hello Platform Inspector**  
  Create `platform_inspector.py` and print a simple welcome message.

- [ ] **STEP 2 — Strings**  
  Store platform-related values such as hostname, OS name, and environment name in string variables.

- [ ] **STEP 3 — Integers**  
  Represent values such as CPU count, node count, and restart count.

- [ ] **STEP 4 — Floats**  
  Represent values such as memory size, disk usage percentage, and load average.

- [ ] **STEP 5 — Booleans**  
  Represent states such as `docker_installed`, `cluster_reachable`, and `healthy`.

- [ ] **STEP 6 — Type Inspection**  
  Use `type()` to understand the types of variables being used.

- [ ] **STEP 7 — String Formatting**  
  Learn f-strings and produce cleaner status output.

- [ ] **STEP 8 — Basic String Methods**  
  Practice `.lower()`, `.upper()`, `.strip()`, `.replace()`, `.split()`, and similar methods with platform data.

- [ ] **STEP 9 — Numeric Operations**  
  Calculate free disk space, memory percentages, and simple health values.

- [ ] **STEP 10 — Build the First System Summary**  
  Combine variables into a small human-readable Platform Inspector report.

---

# Phase 2 — Python Collections

- [ ] **STEP 11 — Lists**  
  Create a list of tools such as Python, Docker, kubectl, Helm, Terraform, and AWS CLI.

- [ ] **STEP 12 — Accessing List Items**  
  Learn indexing and retrieve specific tools from the list.

- [ ] **STEP 13 — Modifying Lists**  
  Practice `append()`, `remove()`, `insert()`, `sort()`, and related operations.

- [ ] **STEP 14 — Tuples**  
  Represent fixed information such as `(tool_name, version)`.

- [ ] **STEP 15 — Dictionaries**  
  Represent a server or Kubernetes node with keys such as hostname, CPU, memory, and status.

- [ ] **STEP 16 — Nested Dictionaries**  
  Represent richer platform information inside nested structures.

- [ ] **STEP 17 — Sets**  
  Use sets to find unique namespaces, node names, or error types.

- [ ] **STEP 18 — Collection Length and Membership**  
  Use `len()`, `in`, and `not in`.

- [ ] **STEP 19 — Convert Between Collection Types**  
  Practice list → set → tuple conversions using real platform examples.

- [ ] **STEP 20 — Platform Inventory Structure**  
  Build an in-memory inventory containing several servers or Kubernetes nodes.

---

# Phase 3 — Decisions and Loops

- [ ] **STEP 21 — Basic `if` Statements**  
  Report whether a platform component is healthy.

- [ ] **STEP 22 — `if/else`**  
  Show different output for healthy versus unhealthy components.

- [ ] **STEP 23 — `if/elif/else`**  
  Classify CPU or disk usage as Healthy, Warning, or Critical.

- [ ] **STEP 24 — Comparison Operators**  
  Practice `>`, `<`, `>=`, `<=`, `==`, and `!=`.

- [ ] **STEP 25 — Boolean Logic**  
  Combine checks using `and`, `or`, and `not`.

- [ ] **STEP 26 — First `for` Loop**  
  Loop through installed platform tools.

- [ ] **STEP 27 — Loop Through Dictionaries**  
  Iterate through server or cluster properties.

- [ ] **STEP 28 — `enumerate()`**  
  Number resources while printing them.

- [ ] **STEP 29 — `break` and `continue`**  
  Skip irrelevant entries or stop when a condition is met.

- [ ] **STEP 30 — Mini Health Scanner**  
  Loop over several simulated systems and report their health.

---

# Phase 4 — Functions

- [ ] **STEP 31 — First Function**  
  Move repeated output into a function such as `display_header()`.

- [ ] **STEP 32 — Function Arguments**  
  Write `check_disk(usage)` and pass values into it.

- [ ] **STEP 33 — Return Values**  
  Return Healthy, Warning, or Critical instead of only printing.

- [ ] **STEP 34 — Multiple Arguments**  
  Pass name, status, and utilization values into a function.

- [ ] **STEP 35 — Default Arguments**  
  Add sensible defaults to functions.

- [ ] **STEP 36 — Type Hints**  
  Introduce annotations such as:

```python
def check_disk(usage: float) -> str:
    ...
```

- [ ] **STEP 37 — Docstrings**  
  Document what each function does.

- [ ] **STEP 38 — Variable Scope**  
  Understand local versus global variables.

- [ ] **STEP 39 — Lambda Functions**  
  Use a lambda to sort servers, pods, or errors.

- [ ] **STEP 40 — Refactor the Inspector into Functions**  
  Turn the original procedural script into several understandable functions.

---

# Phase 5 — Real Linux Inspection

- [ ] **STEP 41 — Hostname Discovery**  
  Retrieve the real hostname using Python.

- [ ] **STEP 42 — Operating System Information**  
  Read OS and kernel information.

- [ ] **STEP 43 — CPU Information**  
  Determine CPU count using Python libraries.

- [ ] **STEP 44 — Filesystem and Disk Information**  
  Read disk capacity and free space.

- [ ] **STEP 45 — Environment Variables**  
  Read values from Linux environment variables using `os.environ`.

- [ ] **STEP 46 — `pathlib` Basics**  
  Work with directories and paths using `Path`.

- [ ] **STEP 47 — Check Whether Commands Exist**  
  Detect tools such as `kubectl`, `docker`, `helm`, and `terraform`.

- [ ] **STEP 48 — Run Linux Commands**  
  Introduce `subprocess.run()`.

- [ ] **STEP 49 — Capture Command Output**  
  Capture stdout, stderr, and return codes.

- [ ] **STEP 50 — Real Local Platform Report**  
  Generate a real report describing the Linux machine running Platform Inspector.

---

# Phase 6 — File Handling

- [ ] **STEP 51 — Read a Text File**  
  Open and read a sample configuration or log file.

- [ ] **STEP 52 — Read Files Line by Line**  
  Process a large file without loading everything into memory.

- [ ] **STEP 53 — Write a File**  
  Save Platform Inspector output to a report.

- [ ] **STEP 54 — Append to a File**  
  Add historical inspection results without replacing existing data.

- [ ] **STEP 55 — File Metadata**  
  Determine file size, modification time, suffix, and filename.

- [ ] **STEP 56 — JSON Reading**  
  Load JSON data into Python dictionaries and lists.

- [ ] **STEP 57 — JSON Writing**  
  Export an inspection result as formatted JSON.

- [ ] **STEP 58 — CSV Parsing and Writing**  
  Read and generate infrastructure inventory in CSV format.

- [ ] **STEP 59 — YAML Parsing**  
  Read Kubernetes-style YAML using PyYAML.

- [ ] **STEP 60 — Universal File Inspector**  
  Allow Platform Inspector to recognize and inspect text, JSON, CSV, and YAML files.

---

# Phase 7 — Log Analysis

- [ ] **STEP 61 — Read a Log File**  
  Load a realistic Linux or application log.

- [ ] **STEP 62 — Find Simple Patterns**  
  Detect lines containing `ERROR`, `WARNING`, `FAILED`, or `TIMEOUT`.

- [ ] **STEP 63 — Case-Insensitive Searching**  
  Normalize strings before pattern matching.

- [ ] **STEP 64 — Count Log Severities**  
  Produce totals for INFO, WARNING, ERROR, and CRITICAL.

- [ ] **STEP 65 — Store Matching Log Entries**  
  Keep discovered errors in lists for further analysis.

- [ ] **STEP 66 — Count Repeated Errors**  
  Use dictionaries to identify recurring failure messages.

- [ ] **STEP 67 — Sort Error Frequency**  
  Find the most common errors using sorting and lambda functions.

- [ ] **STEP 68 — Regular Expressions**  
  Introduce `re` to identify timestamps, IP addresses, services, and structured patterns.

- [ ] **STEP 69 — Generate a Log Analysis Report**  
  Produce top errors, severity counts, and detected patterns.

- [ ] **STEP 70 — Export Log Reports**  
  Save analysis as text, JSON, or CSV.

---

# Phase 8 — Exceptions, Logging, and Code Organization

- [ ] **STEP 71 — Basic Exception Handling**  
  Handle `FileNotFoundError` and `PermissionError`.

- [ ] **STEP 72 — Command Exceptions**  
  Handle failed Linux commands and missing executables.

- [ ] **STEP 73 — Parsing Exceptions**  
  Gracefully handle malformed JSON and YAML.

- [ ] **STEP 74 — `finally` and Cleanup**  
  Understand cleanup behavior and resource handling.

- [ ] **STEP 75 — Python Logging**  
  Replace important `print()` debugging messages with the `logging` module.

- [ ] **STEP 76 — Logging Levels**  
  Use DEBUG, INFO, WARNING, ERROR, and CRITICAL appropriately.

- [ ] **STEP 77 — Split Code into Modules**  
  Introduce files such as `system.py`, `files.py`, and `logs.py`.

- [ ] **STEP 78 — Imports**  
  Learn importing functions and modules properly.

- [ ] **STEP 79 — `__name__ == "__main__"`**  
  Understand script execution versus module importing.

- [ ] **STEP 80 — Convert to a Python Package**  
  Create the first proper `platform_inspector/` package structure.

---

# Phase 9 — Testing and Python Development Practices

- [ ] **STEP 81 — Virtual Environments**  
  Create and understand `.venv`.

- [ ] **STEP 82 — `pip` and Dependencies**  
  Install external libraries deliberately.

- [ ] **STEP 83 — `requirements.txt`**  
  Capture project dependencies.

- [ ] **STEP 84 — First pytest Test**  
  Test a simple health-check function.

- [ ] **STEP 85 — Multiple Test Cases**  
  Test Healthy, Warning, and Critical scenarios.

- [ ] **STEP 86 — Test File Parsing**  
  Create controlled sample files and verify parser results.

- [ ] **STEP 87 — pytest Fixtures and Temporary Files**  
  Learn reusable test setup and safe filesystem testing.

- [ ] **STEP 88 — Mocking**  
  Mock system commands and external calls rather than depending on the real environment.

- [ ] **STEP 89 — Test Coverage**  
  Add `pytest-cov` and generate coverage reports.

- [ ] **STEP 90 — Code Quality Tooling**  
  Add Ruff linting/formatting, Bandit security checks, and `pip-audit`.

---

# Phase 10 — Platform Engineering Python

- [ ] **STEP 91 — Build a Real CLI**  
  Use `argparse` so commands such as these work cleanly:

```bash
platform-inspector system
platform-inspector files
platform-inspector logs
platform-inspector aws
platform-inspector kubernetes
platform-inspector doctor
```

- [ ] **STEP 92 — AWS with boto3**  
  Connect to AWS and identify the current account and region.

- [ ] **STEP 93 — AWS Resource Inspection**  
  Inspect EC2, S3, or EKS resources and summarize them using Python collections.

- [ ] **STEP 94 — AWS Exception Handling and Pagination**  
  Handle credential failures, API errors, and paginated AWS responses.

- [ ] **STEP 95 — Kubernetes Python Client**  
  Connect to a Kubernetes cluster without shelling out to `kubectl`.

- [ ] **STEP 96 — Kubernetes Health Inspection**  
  Inspect nodes, namespaces, pods, phases, restart counts, and unhealthy workloads.

- [ ] **STEP 97 — Kubernetes Log Analysis**  
  Retrieve pod logs through the Kubernetes API and run the existing pattern analyzer against them.

- [ ] **STEP 98 — Platform Doctor**  
  Combine Linux, AWS, Kubernetes, files, and logs into a single health-check command.

- [ ] **STEP 99 — GitHub Actions CI**  
  Automatically run Ruff, pytest, coverage, Bandit, and dependency auditing for every push and pull request.

- [ ] **STEP 100 — Production-Style Release**  
  Package and document the finished tool, add versioning and releases, containerize it if useful, create architecture documentation, and publish:

```text
Platform Inspector v1.0.0
```

---

# What STEP 100 Should Look Like

By STEP 100, Platform Inspector should have evolved from a tiny Python script into a useful Platform Engineering diagnostic utility.

For example:

```text
$ platform-inspector doctor

============================================================
                    PLATFORM INSPECTOR
============================================================

SYSTEM
------------------------------------------------------------
✓ Linux           Ubuntu
✓ CPU             8 cores
✓ Memory          43% used
⚠ Disk            84% used

TOOLS
------------------------------------------------------------
✓ Python          3.13
✓ Docker          installed
✓ kubectl         installed
✓ Helm            installed
✓ Terraform       installed
✓ AWS CLI         installed

AWS
------------------------------------------------------------
✓ Authentication  Successful
✓ Region          us-west-2
✓ EC2             4 running
✓ EKS             1 cluster

KUBERNETES
------------------------------------------------------------
✓ Cluster         reachable
✓ Nodes           3 / 3 Ready
✓ Pods            42 Running
⚠ Restarts        3 pods have > 5 restarts
✗ Failed Pods     1

LOG ANALYSIS
------------------------------------------------------------
ERROR             37
WARNING           82

Top patterns:
  14 × connection timeout
   9 × connection refused
   7 × permission denied
   4 × OOMKilled

REPORT
------------------------------------------------------------
reports/platform-inspector-2026-08-16.json

Overall Health Score: 86 / 100
Status: WARNING
```

---

# What We Should Know by STEP 100

Finishing the application is only part of the goal.

By STEP 100, we should be able to explain:

- Why and when to use strings, integers, floats, and booleans.
- When a list is appropriate.
- When a tuple makes more sense.
- How dictionaries represent structured platform data.
- Why sets are useful for unique values.
- How loops process infrastructure resources.
- How `if/elif/else` implements health decisions.
- How functions make code reusable and testable.
- What lambda functions are and when they are useful.
- How list comprehensions work.
- How Python reads, writes, and parses files.
- How JSON, CSV, YAML, and plain text map into Python structures.
- How to analyze logs and identify recurring patterns.
- How regular expressions help extract structured information.
- How exception handling protects applications from expected failures.
- How Python logging differs from simply using `print()`.
- How modules and packages organize larger applications.
- What `__init__.py` does.
- Why `__name__ == "__main__"` exists.
- What a Python virtual environment solves.
- What `pip` does.
- Why `requirements.txt` exists.
- How external Python libraries are managed.
- How pytest tests application behavior.
- How fixtures help create controlled test environments.
- Why mocking is important when testing AWS, Kubernetes, Linux commands, and APIs.
- What code coverage actually measures.
- What Ruff checks.
- What Bandit checks.
- What `pip-audit` checks.
- How `subprocess` interacts with Linux commands.
- How `pathlib` works with files and directories.
- How boto3 communicates with AWS.
- How AWS API responses are traversed and processed.
- How AWS pagination works.
- How the Kubernetes Python client communicates with a cluster.
- How Kubernetes objects can be inspected without relying on `kubectl`.
- How to retrieve and analyze Kubernetes logs.
- How to design a useful CLI.
- How GitHub Actions validates Python code automatically.
- How a Python application progresses from a script into a maintainable software project.

Most importantly:

> **We should be able to open almost any part of Platform Inspector and explain why the code exists, how it works, how to test it, and how we would troubleshoot it if it broke.**

---

# Progress Tracker

```text
Current Step : STEP 0
Completed    : 0 / 100
Progress     : 0%
```

The journey starts with:

```text
STEP 1 — Hello Platform Inspector
```

And ends with:

```text
STEP 100 — Platform Inspector v1.0.0
```

---

## Project Rule

We are deliberately **not** trying to learn everything at once.

If a future step contains something interesting, resist the temptation to jump ahead unless the project genuinely needs it.

The repository itself is the course.

The Git history is the learning journal.

And every step should leave the project slightly better than it was before.

> **Build it. Understand it. Test it. Commit it. Then move forward.**
