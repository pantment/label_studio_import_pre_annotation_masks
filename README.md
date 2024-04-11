# Create JSON file for pre-annotation masks for Label-Studio

This script is used to convert mask images to the real size of the corresponding images, multiply the mask by 255, and store the new masks in a new directory. It also converts the mask to RLE (Run-Length Encoding) format and stores the RLE format in a JSON file.

## Requirements

- Python 3
- OpenCV
- label-studio

You can install the required Python packages using pip:

```bash
pip install opencv-python label-studio-converter
```

## Usage
You can run the script using the following command:
```bash
python script.py --images_path <images_path> --masks_path <masks_path> --new_masks_path <new_masks_path> --class_name <class_name> --json_name <json_name>
```
## File Format Requirements

To ensure compatibility and optimal processing, adhere to the following file format requirements:

- **Images:** Must be in `.jpg` format.
- **Masks:** Should be in `.png` format.

It's essential that the images and masks are named correspondingly to ensure they are correctly paired during processing.

## Configuring Local Storage in Label Studio

Before importing the generated JSON file, you must configure Label Studio to connect to your local storage. This setup enables Label Studio to access the images and masks for annotation.

### Steps for Configuration

1. Navigate to the Label Studio documentation on local storage setup: [Local Storage Configuration Guide](https://labelstud.io/guide/storage#Local-storage).
2. Follow the instructions to configure your local storage connection. This typically involves setting up paths to your image and mask directories within Label Studio.

## Importing JSON File into Label Studio

After configuring local storage and generating the JSON file with your annotations:

1. Open your Label Studio project.
2. Navigate to the **Data Import** section.
3. Select the option to import tasks from a JSON file.
4. Upload the generated JSON file containing your mask annotations.

This process will import your pre-annotated masks into Label Studio, ready for further annotation or review.

## Additional Notes

- Ensure that the local storage configuration is completed before importing the JSON file to avoid any discrepancies or issues with accessing the images and masks.
- The JSON file should match the format expected by Label Studio, as detailed in the documentation.
