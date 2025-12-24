import os

PROJECT_STRUCTURE = [
    # App (Flask UI)
    "app/__init__.py",
    "app/routes.py",
    "app/templates/index.html",
    "app/static/style.css",

    # Source code
    "src/config/config.py",
    "src/data/load_data.py",
    "src/data/preprocess.py",
    "src/features/vectorizer.py",
    "src/models/recommender.py",

    # Data folders (no data files)
    "data/raw/.gitkeep",
    "data/processed/.gitkeep",

    # Model artifacts
    "models/.gitkeep",

    # Root files
    "app.py",
    "requirements.txt",
    "README.md",
    ".gitignore",
]

def create_project_structure():
    for path in PROJECT_STRUCTURE:
        directory = os.path.dirname(path)

        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                pass

    print("✅ Project structure created successfully.")

if __name__ == "__main__":
    create_project_structure()
