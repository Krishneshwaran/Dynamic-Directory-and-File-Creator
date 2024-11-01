import os
import re
from rich.console import Console
from rich.prompt import Prompt
from rich.tree import Tree

# Initialize the console for rich output
console = Console()

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

def display_structure(structure, parent_tree=None):
    """Recursively display the structure as a tree."""
    if parent_tree is None:
        parent_tree = Tree("Parsed Structure")

    for name, sub_structure in structure.items():
        if sub_structure is None:
            parent_tree.add(f"[file]{name}[/file]")
        else:
            dir_tree = parent_tree.add(f"[bold cyan]{name}/[/bold cyan]")
            display_structure(sub_structure, dir_tree)

    return parent_tree

def create_structure(base_dir, structure, initial_content=""):
    """Recursively create directories and files from the parsed structure."""
    for name, sub_structure in structure.items():
        path = os.path.join(base_dir, name)
        if sub_structure is None:
            # Check if the file already exists
            if os.path.exists(path):
                console.print(f"File already exists, skipping: {path}", style="yellow")
            else:
                # Create file with optional initial content
                with open(path, 'w') as f:
                    f.write(initial_content)
                console.print(f"Created file: {path}", style="green")
        else:
            # Create directory and recurse to create any nested items
            os.makedirs(path, exist_ok=True)
            console.print(f"Created directory: {path}", style="cyan")
            create_structure(path, sub_structure, initial_content)

def main():
    console.print("Enter the directory structure in tree format (type 'done' to finish):", style="bold blue")
    lines = []
    while True:
        line = Prompt.ask("Enter line")
        if line.strip().lower() == "done":
            break
        lines.append(line)
    
    tree_input = "\n".join(lines)
    
    # Use the current working directory as the base directory
    base_directory = os.getcwd()
    
    # Parse the tree structure
    structure = parse_tree_structure(tree_input)
    console.print("Parsed structure:", style="bold green")
    
    # Display the structure as a tree for confirmation
    console.print(display_structure(structure))

    # Create the directory and file structure in the current directory
    create_structure(base_directory, structure, initial_content="Made by Krish")

if __name__ == "__main__":
    main()
