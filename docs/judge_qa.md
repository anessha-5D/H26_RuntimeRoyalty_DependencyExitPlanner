# Judge Q&A

## 1. How do you identify dependencies?

The tool reads dependency declaration files in the target repository and identifies the packages declared there.

**To confirm with Member 1:** Which files does our tool actually read — requirements.txt, pyproject.toml, setup.py, or others?

## 2. How do you identify where a dependency is used?

The tool examines source code to find imports associated with the dependency and records where it is used.

**To confirm with Member 1:** Does our tool provide file names only, or file names with line numbers?

## 3. How is Gemma used meaningfully?

Gemma receives repository evidence and helps generate a risk assessment, replacement suggestions, migration steps, compatibility concerns, and suggested tests.

The recommendations are AI-generated and must be reviewed against the actual evidence.

## 4. How do you verify the recommendations?

We compare the tool's claims with repository files, package metadata, and actual test output. Our manually checked reference information is recorded in `docs/ground_truth.md`.

Tests are described as executed only when we have actual execution results. Anything not run is labelled "Not executed."

## 5. How do you distinguish AI recommendations from verified facts?

The capsule separates verified evidence, such as dependency declarations and captured test results, from AI-generated recommendations.

An AI suggestion is not treated as a verified fact merely because Gemma produced it.

## 6. What are the limitations?

- AI-generated recommendations can be incorrect and require human review.
- The usefulness of test results depends on the repository's existing test coverage.
- Some dependencies may receive only partial analysis within the available time.
- A replacement is not considered verified unless the relevant checks have actually been performed.
- Security vulnerability analysis is outside this project's stated scope.

Update these points if the team's actual implementation has additional limitations.

## 7. Which model do you use, and how is it accessed?

- Model: Gemma 4
- Exact version/tag: [Confirm from `ollama list` on the demo machine]
- Access method: [Confirm the actual local Ollama setup]
- Official terms/license: [Insert the applicable official Gemma terms link]

Do not present placeholders as confirmed facts. Update this answer after Member 1 or Member 4 confirms the exact details.

## 8. What happens if a replacement test fails or is not run?

We report the actual result. If a test was not executed, we say "Not executed." If it failed, we report the failure and investigate the cause instead of claiming the replacement works.

## 9. Does the tool automatically replace dependencies?

The tool's primary purpose is to analyze dependencies and prepare an exit plan. Any automated replacement or migration capability should be described according to what the implementation actually supports.

## 10. What is the final output?

The tool produces a Dependency Exit Capsule that combines repository evidence, test results when available, AI-generated recommendations, migration steps, and unresolved concerns.