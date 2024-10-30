import os
import json

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            # Create a folder and recurse
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            # Create a file with specified content
            with open(path, 'w') as file:
                file.write(content)

# Main function to open and parse the .myext file
def setup_from_myext(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    base_directory = os.path.dirname(file_path)
    create_structure(base_directory, data["structure"])

# Path to your .myext file
setup_from_myext("first.rurox")
