import argparse
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

if result.returncode == 0:
    print("Baseline tests passed.")
else:
    print("Baseline tests failed, but continuing with AI analysis.")
    
print("Dependency files found:")
print(find_dependency_files(repo))

print("Finding imports...")
usage = find_imports(repo, dependency)
print(usage)

print("Running baseline tests...")
try:
    result = subprocess.run(
        ["python", "-m", "pytest"],
        cwd=repo,
        capture_output=True,
        text=True,
        timeout=300
    )
    baseline = result.stdout[-500:]
except Exception as e:
    baseline = f"Tests could not run: {e}"

print(baseline)

print("Asking Gemma...")
ai = analyze(dependency, usage, baseline)
print(ai)

create_capsule(
    dependency=dependency,
    dependency_file=None,
    version=None,
    usage=usage,
    baseline=baseline,
    ai_text=ai,
    test_after=None
)