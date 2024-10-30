import os
import re

def parse_tree_structure(tree_input):
    """Parse the tree structure input into a nested dictionary."""
    structure = {}
    current_path = [structure]  # Keeps track of the current level in the nested dictionary

    for line in tree_input.strip().splitlines():
        # Remove leading spaces and special symbols to calculate indent level
        stripped_line = re.sub(r"^[│├└─\s]*", "", line)
        indent_level = (len(line) - len(stripped_line)) // 4  # Assumes 4 spaces per indent

        # Determine if it's a directory or a file
        is_directory = stripped_line.endswith("/")
        item_name = stripped_line.rstrip("/")

        # Adjust current path based on indentation level
        current_path = current_path[:indent_level + 1]

        # Add to the structure based on whether it's a directory or file
        if is_directory:
            # Create a new dictionary for the directory and add it to the current level
            new_dir = {}
            current_path[-1][item_name] = new_dir
            current_path.append(new_dir)
        else:
            # It's a file, set as None since no further structure is needed
            current_path[-1][item_name] = None
    
    return structure

def create_structure(base_dir, structure, initial_content=""):
    """Recursively create directories and files from the parsed structure."""
    for name, sub_structure in structure.items():
        path = os.path.join(base_dir, name)
        if sub_structure is None:
            # Create file with optional initial content
            with open(path, 'w') as f:
                f.write(initial_content)
            print(f"Created file: {path}")
        else:
            # Create directory and recurse to create any nested items
            os.makedirs(path, exist_ok=True)
            print(f"Created directory: {path}")
            create_structure(path, sub_structure, initial_content)

def main():
    print("Enter the directory structure in tree format (end input with 'done' on a new line):")
    lines = []
    while True:
        line = input()
        if line.strip().lower() == "done":
            break
        lines.append(line)
    
    tree_input = "\n".join(lines)
    
    # Use the current working directory as the base directory
    base_directory = os.getcwd()
    
    # Parse the tree structure
    structure = parse_tree_structure(tree_input)
    print("Parsed structure:", structure)
    
    # Create the directory and file structure in the current directory
    create_structure(base_directory, structure, initial_content="Initial file content here")

if __name__ == "__main__":
    main()
