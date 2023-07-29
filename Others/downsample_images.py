import os
from PIL import Image

main_folder = "assets/img/thumbnails"

top_level_dir = os.listdir(f"{main_folder}")

# Repeat 3 times
for i in range(3):
    # Go through each folder in "assets/img/thumbnails"
    for dir in top_level_dir:
        sub_dir = os.listdir(f"{main_folder}/{dir}")

        try:
            # Go through any more sub-folders
            for dirs in sub_dir:
                files = os.listdir(f"{main_folder}/{dir}/{dirs}")

                # Go through each file in that folder
                for file in files:
                    # Open the image
                    img = Image.open(f"{main_folder}/{dir}/{dirs}/{file}")

                    # If the image height is more than 500px, downsample it
                    if img.size[1] > 500:
                        # Downsample the image by a factor of 2
                        img = img.resize((int(img.size[0]/2), int(img.size[1]/2)))

                        # Remove the alpha channel
                        img = img.convert("RGB")

                        # Save the image to the same place with the same filename
                        img.save(f"{main_folder}/{dir}/{dirs}/{file}", format="JPEG")
        except NotADirectoryError:
            # If there are no more sub-folders, go through each file in that folder
            for file in sub_dir:
                # Open the image
                img = Image.open(f"{main_folder}/{dir}/{file}")

                # If the image height is more than 500px, downsample it
                if img.size[1] > 500:
                    # Downsample the image by a factor of 2
                    img = img.resize((int(img.size[0]/2), int(img.size[1]/2)))

                    # Remove the alpha channel
                    img = img.convert("RGB")

                    # Save the image to the same place with the same filename
                    img.save(f"{main_folder}/{dir}/{file}", format="JPEG")

print("\nCompleted downsampling images 3 times.\n")
