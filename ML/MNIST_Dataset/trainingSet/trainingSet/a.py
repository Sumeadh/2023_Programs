import os

# Loop over all directories in the current directory
for dirpath, dirnames, filenames in os.walk('.'):
    # Check if directory contains images
    if any(filename.endswith('.jpg') or filename.endswith('.png') for filename in filenames):
        # Sort images by name
        images = sorted([filename for filename in filenames if filename.endswith('.jpg') or filename.endswith('.png')])
        # Keep only the first 250 images
        images_to_remove = images[250:]
        # Remove the extra images
        for image in images_to_remove:
            os.remove(os.path.join(dirpath, image))
