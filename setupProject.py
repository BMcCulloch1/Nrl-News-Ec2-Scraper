import os

# Define the directory structure
folders = [
    "scrapers",
    "utils",
    "data",
    "tests"
]

# Create subdirectories and __init__.py files
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    init_file = os.path.join(folder, "__init__.py")
    open(init_file, 'a').close()  # Create an empty __init__.py file

# Create main.py, requirements.txt, and README.md in the main directory
main_files = ["main.py", "requirements.txt", "README.md"]
for file in main_files:
    open(file, 'a').close()  # Create empty files
