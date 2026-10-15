from datetime import datetime

MODEL_NAME = "gemma4:e2b"

def create_capsule(dependency, dependency_file, version, usage, baseline, ai_text, test_after=None):
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    if test_after is None:
        test_after = "Not executed"

    usage_text = "\n".join(f"- {item}" for item in usage) if usage else "- No direct imports found"

    capsule = f"""# Dependency Exit Capsule

Generated on: {date}  
AI model: {MODEL_NAME}  
Access method: Local Ollama

## 1. Dependency Details
- Name: {dependency}
- Version: {version if version else "Not detected"}
- Declared in: {dependency_file if dependency_file else "Not detected"}

## 2. Usage Locations
{usage_text}

## 3. Verified Repository Evidence
- Import scan was performed on Python files.
- Baseline test result:
{baseline}

## 4. AI-GENERATED RECOMMENDATION
{ai_text}

## 5. Test Evidence
- Baseline tests: recorded above.
- Tests after proposed replacement: {test_after}

## 6. Evidence Separation
- Verified facts: repository scan and pytest execution.
- AI-generated recommendations: Gemma output only.

## 7. Limitations
- This capsule covers the selected dependency only.
- AI recommendations require manual review.
- Test results depend on the repository's available test suite.
"""

    with open("dependency_exit_capsule.md", "w", encoding="utf-8") as f:
        f.write(capsule)

    print("Created dependency_exit_capsule.md")