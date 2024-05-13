import json
import os

# Path to the JSON file containing the ID to image name mappings
JSON_FILE_PATH = 'path/id_to_image_name_mapping.json'

# Directory containing the images to be renamed
IMAGE_DIR = 'img_mask_dir'

# Load the mapping from the JSON file
with open(JSON_FILE_PATH, 'r') as file:
    id_to_image_name = json.load(file)

# Function to extract ID from filename
def extract_id(filename):
    parts = filename.split('-')
    if parts[0] == 'task':
        return int(parts[1])
    return None

# Iterate over each file in the directory
for filename in os.listdir(IMAGE_DIR):
    if filename.endswith('.png'):  # Check if it's a PNG file
        image_id = extract_id(filename)
        if image_id and str(image_id) in id_to_image_name:
            new_filename = f"{id_to_image_name[str(image_id)]}.png"
            old_file_path = os.path.join(IMAGE_DIR, filename)
            new_file_path = os.path.join(IMAGE_DIR, new_filename)
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed {filename} to {new_filename}")
        else:
            print(f"No mapping found for {filename}")
