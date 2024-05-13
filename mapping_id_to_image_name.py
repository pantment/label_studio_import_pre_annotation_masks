import json


JSON_FILE = 'file.json'
# Load the original JSON data
with open(JSON_FILE, 'r') as file:
    data = json.load(file)

# Dictionary to store ID and image name mappings
id_to_image_name = {}

# Extract ID and image name
for item in data:
    image_path = item['image']
    image_id = item['id']
    # Extract the image name from the path
    image_name = image_path.split('/')[-1].split('.')[0]  # This splits off the file extension as well

    # Map ID to image name
    id_to_image_name[image_id] = image_name

# Save the mapping to a new JSON file
with open('id_to_image_name_mapping.json', 'w') as outfile:
    json.dump(id_to_image_name, outfile, indent=4)

print("Mapping saved to id_to_image_name_mapping.json")
