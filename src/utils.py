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


# the function writes all the data to a JSON file
def write_json(filename, data):
    # Open the file in write mode ('w')
    with open(filename, 'w') as file:
        # Convert the Python object (data) to a JSON string and write it to the file 
        file.write(json.dumps(data, indent=4))  # indent=4 for pretty-printing



