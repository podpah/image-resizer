import os
import argparse
from PIL import Image, ImageOps

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", type=str, required=True, help="Path to the folder with images")
parser.add_argument("-f", "--force", action="store_true", help="Override original images")
args = parser.parse_args()
override_images = args.force

input_folder = args.path
output_folder = input_folder


def resize_image_with_padding(image_path, override):
    image = Image.open(image_path)
    width, height = image.size

    target_width = height * (43 / 18)  # Adjust this for the ratio you want
    padding = int((target_width - width) / 2)
    new_image = Image.new("RGB", (int(target_width), height), "white")
    new_image.paste(image, (padding, 0))

    output_folder, image_filename = os.path.split(image_path)
    name, extension = os.path.splitext(image_filename)
    output_filename = name + " edit" + extension

    if override:
        output_path = image_path
        print(f"Image resized and overridden: {os.path.basename(image_path)}")
    else:
        output_path = os.path.join(output_folder, output_filename)
        print(f"Image resized and saved: {os.path.basename(output_path)}")

    new_image.save(output_path, "JPEG")


def process_images_in_folder(input_folder, override):
    for filename in os.listdir(input_folder):
        if not os.path.isfile(os.path.join(input_folder, filename)):
            continue

        if "." not in filename:
            continue

        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            input_path = os.path.join(input_folder, filename)

            name, extension = os.path.splitext(filename)
            if override:
                output_filename = filename
            else:
                output_filename = f"{name} edit{extension}"
                while output_filename in os.listdir(input_folder):
                    output_filename = f"{name} edit{output_filename}"

            image_path = os.path.join(output_folder, output_filename)

            resize_image_with_padding(input_path, override)


process_images_in_folder(input_folder, override_images)


