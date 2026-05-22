
import ast
import os

def extract_python_data(repo_path):
    results = []

    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)

                try:
                    with open(path, "r", encoding="utf-8") as f:
                        code = f.read()

                    tree = ast.parse(code)

                    functions = [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
                    classes = [n.name for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]

                    results.append({
                        "file": path,
                        "functions": functions,
                        "classes": classes,
                        "code": code[:4000]
                    })

                except Exception as e:
                    print(f"Error parsing {path}: {e}")

    return results
