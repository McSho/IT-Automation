
from PIL import Image
import os

# Input and output directories
input_dir = os.getcwd()  # Use the current working directory or inut working directory
output_dir = "C:\\Users\\Manojlo\\Desktop\\fix_slike"  # Output directory name

# Ensure the output directory exists (create it if it doesn't)
os.makedirs(output_dir, exist_ok=True)

# Iterate through each file in the input directory, for different img types change extensions
for filename in os.listdir(input_dir):
    if filename.endswith(".png") or filename.endswith(".webp"):
        # Open the TIFF image
        with Image.open(os.path.join(input_dir, filename)) as img:
            # Convert the image to RGB mode to remove alpha channel
            img = img.convert("RGB")
                      
            # Rotate the image 90 degrees clockwise or not
            img = img.rotate(-90, expand=True)
            
            # Resize the image from 192x192 to 128x128, or any size
            img = img.resize((128, 128))
            
            # Convert and save the image in .jpeg format to the output directory
            output_filename = os.path.splitext(filename)[0] + ".jpeg"
            output_path = os.path.join(output_dir, output_filename)
            img.save(output_path, "JPEG")
            print(f"Processed: {filename} => {output_path}")
