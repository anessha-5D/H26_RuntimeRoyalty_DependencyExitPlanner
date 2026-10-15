import requests

URL = "http://localhost:11434/api/generate"
MODEL = "gemma4:e2b"

def analyze(dependency, usage_files, baseline_tests):
    prompt = f"""
You are a dependency maintenance assistant.

Dependency: {dependency}
Used in: {', '.join(usage_files) if usage_files else 'No imports found'}
Baseline tests: {baseline_tests}

Tasks:
1. Assess risk: Low, Medium, or High.
2. Say whether replacement is needed.
3. Suggest one replacement if needed.
4. Give migration steps.
5. List compatibility risks.
6. Suggest tests.

Label your answer as: AI-GENERATED RECOMMENDATION.
Do not invent files or test results.
"""

    response = requests.post(
        URL,
        json={"model": MODEL, "prompt": prompt, "stream": False},
        timeout=180
    )

    return response.json()["response"]