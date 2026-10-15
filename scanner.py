import os
import re

def find_dependency_files(repo_path):
    possible = ["requirements.txt", "pyproject.toml", "setup.py"]
    found = []

    for name in possible:
        path = os.path.join(repo_path, name)
        if os.path.exists(path):
            found.append(path)

    return found

def find_imports(repo_path, dependency):
    usage = []

    for root, dirs, files in os.walk(repo_path):
        if ".git" in root or "venv" in root:
            continue

        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                try:
                    content = open(path, "r", encoding="utf-8", errors="ignore").read()
                except:
                    continue

                if re.search(rf"\b(import {dependency}|from {dependency})\b", content):
                    usage.append(os.path.relpath(path, repo_path))

    return usage