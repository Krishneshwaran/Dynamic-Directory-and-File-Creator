import os

def parse_tree_structure(tree_input):
    """Parse the tree structure input into a nested dictionary."""
    structure = {}
    current_path = [structure]
    
    for line in tree_input.strip().splitlines():
        # Remove leading spaces and determine level based on indentation
        stripped_line = line.lstrip()
        indent_level = (len(line) - len(stripped_line)) // 4  # Assumes 4 spaces per indent
        
        # Extract directory or file name
        is_directory = stripped_line.endswith("/")
        item_name = stripped_line.rstrip("/")
        
        # Adjust current path level to match indent level
        current_path = current_path[:indent_level + 1]
        
        # Add new entry based on whether it's a directory or file
        if is_directory:
            new_dir = {}
            current_path[-1][item_name] = new_dir
            current_path.append(new_dir)
        else:
            current_path[-1][item_name] = None
    
    return structure

def create_structure(base_dir, structure, initial_content=""):
    """Recursively create directories and files from the nested structure."""
    for name, sub_structure in structure.items():
        path = os.path.join(base_dir, name)
        if sub_structure is None:
            # It's a file, create it with optional initial content
            with open(path, 'w') as f:
                f.write(initial_content)
            print(f"Created file: {path}")
        else:
            # It's a directory, create it and recurse
            os.makedirs(path, exist_ok=True)
            print(f"Created directory: {path}")
            create_structure(path, sub_structure, initial_content)

def main():
    # Input: Tree structure as string
    tree_input = """
    src/
        styles/
            App.css
            CenterPanel.css
            LeftPanel.css
            RightPanel.css
        components/
            App.js
            MainComponent.js
            CenterPanel/
                CenterPanel.js
            LeftPanel/
                LeftPanel.js
            RightPanel/
                RightPanel.js
        index.js
    """
    
    base_directory = input("Enter base directory path: ")
    
    # Parse the tree structure
    structure = parse_tree_structure(tree_input)
    print("Parsed structure:", structure)
    
    # Create the directory and file structure
    create_structure(base_directory, structure, initial_content="Initial file content here")

if __name__ == "__main__":
    main()
