from pathlib import Path

def get_cats_info(path: str) -> list:
    """
    Reads a file containing cat information and returns a list of dictionaries.

    Each line in the file must be in the format: id,name,age
    Example:
        60b90c1c13067a15887e1ae1,Tayson,3

    Args:
        path (str): The path to the file containing cat data.

    Returns:
        list: A list of dictionaries, each representing a cat with keys 'id', 'name', and 'age'  (all as strings).
    """
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat_id, cat_name, cat_age = parts 
                    cat_info = {"id": cat_id, "name": cat_name, "age": cat_age}
                    cats.append(cat_info)
                else:
                    print(f"Warning: Skipping malformed line: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File not found at '{path}'")

    return cats

# Construct the absolute path to the file
current_dir = Path(__file__).parent
file_path = current_dir / "cats.txt"

# Get cats information
cats_info = get_cats_info(str(file_path))
print(cats_info)