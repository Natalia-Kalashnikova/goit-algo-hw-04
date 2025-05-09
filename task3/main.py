import sys
from pathlib import Path
from colorama import init, Fore

# Initialize colorama for cross-platform colored output
init(autoreset=True)

def print_directory_tree(path: Path, prefix: str = ""):
    """
    Recursively prints the directory structure of a given path with colored output.

    Args:
        path (Path): The root directory path to start traversing from.
        prefix (str): The visual prefix for tree branches (used internally during recursion).

    Output:
        Prints each file and subdirectory in a structured tree format with colors:
        - Blue for directories
        - Green for files
        - Red for errors or permission issues
    """
    try:
        # Sort items: directories first, then files; both alphabetically
        items = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
    except PermissionError:
        print(Fore.RED + prefix + "⛔ Permission Denied")
        return

    for index, item in enumerate(items):
        connector = "┣ " if index < len(items) - 1 else "┗ "
        if item.is_dir():
            print(Fore.BLUE + prefix + connector + f"📂 {item.name}")
            # Recursively print subdirectory contents with updated prefix
            print_directory_tree(item, prefix + ("┃   " if index < len(items) - 1 else "    "))
        else:
            print(Fore.GREEN + prefix + connector + f"📜 {item.name}")

def main():
    """
    Main entry point of the script.

    Expects a single command-line argument: the path to a directory.
    Verifies the path, and calls the tree printing function.
    """
    if len(sys.argv) != 2:
        print(Fore.RED + "❌ Please provide a directory path as a command-line argument.")
        print("Usage: python hw03.py /path/to/directory")
        sys.exit(1)

    directory = Path(sys.argv[1])

    if not directory.exists():
        print(Fore.RED + f"❌ The path '{directory}' does not exist.")
        sys.exit(1)
    if not directory.is_dir():
        print(Fore.RED + f"❌ The path '{directory}' is not a directory.")
        sys.exit(1)

    print(Fore.CYAN + f"\nDirectory structure: {directory}\n")
    print_directory_tree(directory)

if __name__ == "__main__":
    main()

