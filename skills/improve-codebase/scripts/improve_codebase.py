# /// script
# dependencies = [
#   "jinja2",
# ]
# ///

import os
import random
import sys
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

EXCLUDED_DIRS = {
    ".git",
    "node_modules",
    "venv",
    ".venv",
    "target",
    "dist",
    ".cache",
    "__pycache__",
    ".tox",
    "build",
}

def find_python_files(root_dir):
    python_files = []
    for root, dirs, files in os.walk(root_dir):
        # Filter out excluded directories
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]

        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files

def find_style_guides(root_dir, language="python"):
    # Search for coding-guidelines/{language} directory
    guidelines_dir = None
    for root, dirs, _ in os.walk(root_dir):
        # Filter out excluded directories to speed up search
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]

        target_path = os.path.join(root, "coding-guidelines", language)
        if os.path.isdir(target_path):
            guidelines_dir = target_path
            break

    if guidelines_dir:
        guides = [str(p.relative_to(Path.cwd())) for p in Path(guidelines_dir).glob("*") if p.is_file()]
        if guides:
            return guides

    # Fallback to internal guide
    script_dir = Path(__file__).parent.absolute()
    fallback_guide = script_dir.parent / "assets" / "guides" / language / "pep8.md"
    if fallback_guide.exists():
        return [str(fallback_guide.relative_to(Path.cwd()))]

    return []

def main():
    root_dir = os.getcwd()

    # 1. Find all Python files
    python_files = find_python_files(root_dir)
    if not python_files:
        print("No Python files found in the project.")
        sys.exit(1)

    # 2. Select a random file
    selected_file = random.choice(python_files)
    rel_selected_file = os.path.relpath(selected_file, root_dir)

    # 3. Find style guides
    style_guides = find_style_guides(root_dir)

    if not style_guides:
        print("No style guides found (including fallback).")
        sys.exit(1)

    # 4. Render the prompt template
    script_dir = Path(__file__).parent.absolute()
    template_dir = script_dir.parent / "assets" / "templates"

    env = Environment(loader=FileSystemLoader(str(template_dir)))
    try:
        template = env.get_template("prompt_template.j2")
    except Exception as e:
        print(f"Error loading template: {e}")
        sys.exit(1)

    prompt = template.render(
        file_path=rel_selected_file,
        style_guide_paths=style_guides
    )

    # 5. Output diagnostics and prompt
    print(f"--- DIAGNOSTICS ---")
    print(f"Selected file: {rel_selected_file}")
    print(f"Style guide(s) used: {', '.join(style_guides)}")
    print(f"-------------------\n")
    print(prompt)

if __name__ == "__main__":
    main()
