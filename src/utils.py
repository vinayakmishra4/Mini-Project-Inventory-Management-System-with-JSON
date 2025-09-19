import json
import os


# ---------------------------
# 🔍 Helper Validation Functions
# ---------------------------

def validate_filename(filename):
    """
    Ensures the filename ends with .json
    """
    if not filename.endswith('.json'):
        raise ValueError(f"Invalid file extension for '{filename}'. Only .json files are allowed.")


def validate_data_structure(data):
    """
    Checks if the data is of type dict or list.
    JSON root must be an object or array.
    """
    if not isinstance(data, (dict, list)):
        raise TypeError("Data must be a dictionary or list.")

# ---------------------------
# 📖 JSON Loading Function
# ---------------------------

def load_json(filename, required_keys=None):
    """
    Loads and validates JSON data from a file.

    Args:
        filename (str): Path to the JSON file.
        required_keys (list, optional): Keys that must exist in the JSON object.

    Returns:
        dict or list: Parsed JSON data.

    Raises:
        FileNotFoundError: If the file doesn't exist.
        json.JSONDecodeError: If the content is not valid JSON.
        ValueError: If validation fails (e.g., file extension, missing keys).
    """
    validate_filename(filename)  # Ensure it's a .json file

    if not os.path.exists(filename):
        raise FileNotFoundError(f"File not found: {filename}")

    # Open and read the file safely
    with open(filename, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)  # Parses the JSON content
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in file {filename}: {str(e)}", e.doc, e.pos)

    validate_data_structure(data)        # Ensure top-level data is dict or list

    return data


# ---------------------------
# ✏️ JSON Writing Function
# ---------------------------

def write_json(filename, data):
    """
    Validates and writes data to a JSON file.

    Args:
        filename (str): Output filename (must end in .json).
        data (dict or list): The data to write to the file.

    Raises:
        TypeError: If data is not a dictionary or list, or not serializable.
        OSError: If the file can't be written.
    """
    validate_filename(filename)         # Ensure it's a .json file
    validate_data_structure(data)       # Ensure data is dict or list

    try:
        with open(filename, 'w', encoding='utf-8') as file:
            # Write the data with pretty formatting
            json.dump(data, file, indent=4, ensure_ascii=False)
    except TypeError as e:
        raise TypeError(f"Data is not JSON serializable: {e}")
    except OSError as e:
        raise OSError(f"Could not write to file '{filename}': {e}")
