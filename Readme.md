
# Dynamic Directory and File Creator

This project is a Python script that dynamically creates directory and file structures based on a tree-like input format. Users can define a nested directory and file structure using a text-based format, which the script then parses and creates in the current working directory.

## Features

- **Tree Structure Parsing**: Parses text input that represents a file and directory structure.
- **Automatic Directory Creation**: Creates nested directories and files as specified in the input.
- **Initial Content for Files**: Optional initial content can be added to files upon creation.
- **Direct Execution**: After entering the directory structure and typing `done`, the script immediately builds the structure in the current directory.

## Usage

1. **Run the Script**: Execute the script in a Python environment.
2. **Input Tree Structure**: Enter the directory and file structure in a tree format.
   - Use `├──` for files and folders within a directory.
   - Use `│` to indicate continuation lines for readability.
   - Type `done` on a new line to finish input.
3. **Verify Creation**: Check the current directory to see the newly created folder and file structure.

### Example Input

```plaintext
project/
├── src/
│   ├── main.py
│   ├── utils/
│   │   ├── helper.py
│   │   └── config.py
├── tests/
│   ├── test_main.py
│   └── utils/
│       └── test_helper.py
└── README.md
```

### Expected Output

In the current working directory, a `project` folder will be created with the nested structure shown in the input.

## Code Overview

### `parse_tree_structure(tree_input)`
Parses the user-provided tree input into a nested dictionary that represents the file structure.

### `create_structure(base_dir, structure, initial_content="")`
Recursively creates directories and files based on the parsed structure dictionary. Files can include optional initial content.

### `main()`
Prompts the user for tree-structured input, parses it, and calls `create_structure` to build the directory and file structure.

## Requirements

- Python 3.x

## Running the Script

```bash
python directory_creator.py
```

### Sample Output

The script will print each created file and directory path to confirm successful creation:

```plaintext
Created directory: project/src/
Created file: project/src/main.py
Created directory: project/src/utils/
Created file: project/src/utils/helper.py
...
```

## Notes

- The script assumes a 4-space indentation for each nested level.
- The script executes immediately after typing `done`, with no additional prompts.

## License

This project is licensed under the MIT License.
