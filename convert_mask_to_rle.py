from label_studio_converter import brush
import json
import cv2
import os
import argparse

# Create the parser
parser = argparse.ArgumentParser(description="Process some paths.")


# Add the arguments
parser.add_argument("--images_path", type=str, required=True, help="The path to the images.")
parser.add_argument("--masks_path", type=str, required=True, help="The path to the masks.")
parser.add_argument("--new_masks_path", type=str, required=True, help="The path to the new masks.")
parser.add_argument("--class_name", type=str, required=True, help="The class name.")
parser.add_argument("--json_name", type=str, required=True, help="The name of the JSON file.")

# Parse the arguments
args = parser.parse_args()

# Assign the arguments to variables
images_path = args.images_path
masks_path = args.masks_path
new_masks_path = args.new_masks_path
class_name = args.class_name
json_name = args.json_name


def convert_mask_to_img_size(mask_path, new_mask_path, img_path):
    mask = cv2.imread(mask_path, cv2.IMREAD_UNCHANGED)
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    # -> Convert the mask.png files to the real size of the image
    mask = cv2.resize(
        mask, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_NEAREST)
    # -> Multiply the mask * 255
    mask = mask * 255
    # -> Store the new masks in a new directory
    os.makedirs(os.path.dirname(new_mask_path), exist_ok=True)
    cv2.imwrite(new_mask_path, mask)


def convert_mask_to_rle(image_path, mask_path, class_name):
    # -> Convert the mask to RLE format
    annotation = brush.image2annotation(mask_path, class_name, "tag", "image")

    task = {
        "data": {"image": image_path},
        "annotations": [annotation]
    }
    return task


def create_json_file(task, json_path):
    # -> Create the json file
    with open(json_path, 'w') as f:
        json.dump(task, f)


def convert_path(path):
    # Get the home directory of the current user
    home_dir = os.path.expanduser("~")
    # Remove the home directory prefix
    path = path.replace(home_dir, "")

    # Add the prefix "\/data\/local-files\/?d="
    path = "/data/local-files/?d=" + path
    return path


def main():

    annotated_images = []
    images = sorted(os.listdir(images_path))
    masks = sorted(os.listdir(masks_path))

    for image, mask in zip(images, masks):

        # -> Convert the mask.png files to the real size of the image multiplied by 255 and store them in a new directory
        convert_mask_to_img_size(os.path.join(masks_path, mask), os.path.join(
            new_masks_path, mask), os.path.join(images_path, image))

        # -> Convert the path to the right format
        path = convert_path(os.path.join(images_path))
        img_name_path = path + "/" + image

        # -> Store the RLE format in a json file
        task = convert_mask_to_rle(img_name_path, os.path.join(
            new_masks_path, mask), class_name)
        # -> Create a list of all the objects (images) with their annotations
        annotated_images.append(task)

    create_json_file(annotated_images, json_name)


if __name__ == "__main__":
    main()