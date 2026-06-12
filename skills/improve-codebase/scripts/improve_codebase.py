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

def get_guideline_pool(language="python"):
    script_dir = Path(__file__).parent.absolute()
    assets_dir = script_dir.parent / "assets"

    pool = []

    # Language agnostic (common) guidelines
    common_dir = assets_dir / "guides" / "common"
    if common_dir.exists():
        pool.extend([str(p.relative_to(Path.cwd())) for p in common_dir.glob("*.md") if p.is_file()])

    # Language specific guidelines
    lang_dir = assets_dir / "guides" / language
    if lang_dir.exists():
        pool.extend([str(p.relative_to(Path.cwd())) for p in lang_dir.glob("*.md") if p.is_file()])

    return pool

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

    # 3. Get guideline pool and select a random one
    guideline_pool = get_guideline_pool(language="python")
    if not guideline_pool:
        print("No style guides found in the skill assets.")
        sys.exit(1)

    selected_guideline = random.choice(guideline_pool)

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
        style_guide_path=selected_guideline
    )

    # 5. Output diagnostics and prompt
    print(f"--- DIAGNOSTICS ---")
    print(f"Selected file: {rel_selected_file}")
    print(f"Selected style guide: {selected_guideline}")
    print(f"-------------------\n")
    print(prompt)

if __name__ == "__main__":
    main()
