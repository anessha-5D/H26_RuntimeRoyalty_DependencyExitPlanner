import argparse
import os
import re
import subprocess
from scanner import find_dependency_files, find_imports
from gemma import analyze
from capsule import create_capsule


parser = argparse.ArgumentParser()
parser.add_argument("--repo", required=True)
parser.add_argument("--dependency", required=True)
args = parser.parse_args()

repo = args.repo
dependency = args.dependency

dependency_file = None
version = None

requirements_path = os.path.join(repo, "requirements.txt")

if os.path.exists(requirements_path):
    dependency_file = requirements_path

    with open(requirements_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.lower().startswith(dependency.lower()):
                match = re.search(r"==\s*([0-9][^,\s;#]*)", line)
                if match:
                    version = match.group(1)
                break

print(f"Dependency: {dependency}")
print(f"Version: {version}")
print(f"Declared in: {dependency_file}")

repo = args.repo
dependency = args.dependency

ground_truth_path = os.path.join(repo, "docs", "ground_truth.md")
ground_truth = "No ground truth file found."

if os.path.exists(ground_truth_path):
    with open(ground_truth_path, "r", encoding="utf-8") as f:
        ground_truth = f.read()

print("Ground truth loaded:")
print(ground_truth[:500])

print("Dependency files found:")
print(find_dependency_files(repo))


print("Finding imports...")
usage = find_imports(repo, dependency)
print(usage)


print("Running baseline tests...")

baseline = "Tests could not run."

try:
    result = subprocess.run(
        ["python", "-m", "pytest"],
        cwd=repo,
        capture_output=True,
        text=True,
        timeout=300
    )

    if result.returncode == 0:
        baseline_status = "PASSED"
    else:
        baseline_status = "FAILED"

    baseline = (
        f"Baseline test status: {baseline_status}\n"
        f"Exit code: {result.returncode}\n"
        f"{result.stdout[-1000:]}"
    )

except Exception as e:
    baseline = f"Tests could not run: {e}"

print(baseline)

test_after = "Not executed"

if version:
    new_version = "2.32.3"

    if new_version != version:
        print(f"Testing upgrade: {dependency}=={version} -> {dependency}=={new_version}")

        with open(requirements_path, "r", encoding="utf-8") as f:
            req_content = f.read()

        req_content = req_content.replace(
            f"{dependency}=={version}",
            f"{dependency}=={new_version}"
        )

        with open(requirements_path, "w", encoding="utf-8") as f:
            f.write(req_content)

        try:
            subprocess.run(
                ["python", "-m", "pip", "install", f"{dependency}=={new_version}"],
                cwd=repo,
                check=True,
                capture_output=True,
                text=True,
                timeout=300
            )

            after_result = subprocess.run(
                ["python", "-m", "pytest"],
                cwd=repo,
                capture_output=True,
                text=True,
                timeout=300
            )

            if after_result.returncode == 0:
                after_status = "PASSED"
            else:
                after_status = "FAILED"

            test_after = (
                f"Upgraded {dependency} from {version} to {new_version}.\n"
                f"Test status after upgrade: {after_status}\n"
                f"Exit code: {after_result.returncode}\n"
                f"{after_result.stdout[-1000:]}"
            )

        except Exception as e:
            test_after = f"Upgrade test could not run: {e}"

print(test_after)

print("Asking Gemma...")
ai = analyze(dependency, usage, baseline)
print(ai)

create_capsule(
    dependency=dependency,
    dependency_file=dependency_file,
    version=version,
    usage=usage,
    baseline=baseline + "\n\nManually verified ground truth:\n" + ground_truth,
    ai_text=ai,
    test_after=test_after
)