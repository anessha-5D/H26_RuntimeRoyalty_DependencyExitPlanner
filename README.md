# Dependency Exit Planner

An AI-powered developer tool that helps open-source maintainers identify dependency risks, understand code usage, plan migrations, verify changes, and generate a reusable Dependency Exit Capsule.

## Problem Statement

Software projects rely on third-party packages that may become outdated, unmaintained, deprecated, or incompatible with newer Python versions. Replacing these packages without proper analysis can introduce new problems.

## Our Solution

Dependency Exit Planner analyzes the organizer-provided LinkWatch repository. It identifies dependency metadata and import locations, uses Gemma 4 to suggest migration approaches, runs available tests, and generates a Dependency Exit Capsule.

## Key Features

- Dependency metadata discovery
- Python import and usage-location scanning
- AI-generated risk analysis and replacement recommendations
- Baseline test execution
- Replacement verification where feasible
- Dependency Exit Capsule generation
- Separation of verified evidence and AI recommendations

## Technology Stack

- Python 3.12 / 3.13
- Gemma 4
- Ollama or the actual supported model access method used
- pytest
- Git and GitHub

## How It Works

1. Provide the LinkWatch repository path.
2. Scan dependency files and Python imports.
3. Analyze the collected findings using Gemma 4.
4. Run relevant repository tests.
5. Generate `dependency_exit_capsule.md`.

## How to Run

Use Python 3.12 or 3.13.

```bash
pip install -r requirements.txt
python main.py --repo path/to/LinkWatch --dependency package_name
```

Replace the repository path and package name with actual values.

## AI Model Details

- Model name: Gemma 4
- Exact model version: To be confirmed
- Model source: To be confirmed
- Access method: To be confirmed
- License or usage terms: Verify the selected model's applicable terms
- Role: Risk analysis, replacement suggestions, migration planning, and suggested tests

## Verification

The tool records actual repository inspection and test results. AI-generated recommendations are not treated as verified results. Checks that cannot be executed are reported honestly.

## Known Limitations

- Replacement recommendations require developer review.
- Not all dependencies can be replaced automatically.
- Test coverage may not reveal every compatibility issue.
- Results depend on available repository metadata and successful model access.

## License

See the LICENSE file for the project's licensing terms.

   

