import os
import sys


def rename_items(directory):
    """
    Recursively renames files and folders within a directory (excluding hidden items).

    Args:
        directory (str): Path to the directory to be processed.
    """

    for item in os.listdir(directory):
        # Skip hidden items (like .git)
        if item.startswith("."):
            continue

        # Construct the full path to the item
        item_path = os.path.join(directory, item)

        # Check if the item is a directory
        if os.path.isdir(item_path):
            # Create the new lowercase, space-free name
            new_name = item.lower().replace(" ", "_").replace("-", "")
            # Construct the full path for the renamed directory
            new_path = os.path.join(directory, new_name)
            # Perform the directory renaming
            os.rename(item_path, new_path)
            print(f"Renamed directory '{item}' to '{new_name}'")

            # Recursively process the subdirectory
            rename_items(new_path)
        else:  # If the item is a file
            # Create the new lowercase, space-free name
            new_name = item.lower().replace(" ", "_").replace("-", "")
            # Construct the full path for the renamed file
            new_path = os.path.join(directory, new_name)
            # Perform the file renaming
            os.rename(item_path, new_path)
            print(f"Renamed file '{item}' to '{new_name}'")


def main():
    """
    Handles command-line arguments and initiates the renaming process.
    """

    if len(sys.argv) != 2:
        print("Usage: python rename_items.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    rename_items(directory)


if __name__ == "__main__":
    main()
