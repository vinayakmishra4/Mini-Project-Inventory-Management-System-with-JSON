# Manage category operations
import json
import os
import utils as ut

CATEGORY_FILE = 'categories.json'
DATA=os.path.join(ut.get_data_directory(), CATEGORY_FILE)

# Load categories from the JSON file

def get_all_categories():