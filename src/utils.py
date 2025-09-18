# Utility functions (JSON read/write etc.)
import json  # Import the json module to work with JSON files

# This function reads all the data from a JSON file
def load_json(filename):
    # Open the file in read mode ('r')
    with open(filename, 'r') as file:
        # Load the contents of the file into a Python object (usually a dict or list)
        data = json.loads(file.read())

    # (Optional) Return the loaded data so it can be used outside the function
    return data


def write_json(filename):
