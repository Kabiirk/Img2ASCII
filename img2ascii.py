# Imports
from typing import Sized
import PIL.Image

# ASCII characters
ASCII = [ "@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "." ]
new_width = 100

# Resze image while maintaining aspect ratio
def resize_img(image, new_width=100):
    width, height = image.size
    print(width, height)
    ratio = height/width
    new_height = int(new_width * ratio)//1.75
    print(new_width, new_height)
    resized_img = image.resize((new_width, int(new_height)))
    return resized_img

# Convert each Pixel to Grayscale
def fifty_shades_of_grey(image):
    grayscale_img = image.convert("L")
    return grayscale_img

# Pixel to equivalent ASCII string
def pixel_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII[pixel//25] for pixel in pixels])
    return characters

# Read Image
path = input("Enter image Path : \n")

try:
    image = PIL.Image.open(path)
except:
    print(path, "Not a valid Pathname to any image.")

# Do Stuff
# image -> ASCII
new_image_data = pixel_to_ascii(fifty_shades_of_grey(resize_img(image)))

# Format
pixel_count = len(new_image_data)
ascii_img = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])

# Output
# Print on Terminal
# print(ascii_img)

# Output to a .txt File
with open(r"output\ascii_image.txt", "w") as f:
    f.write(ascii_img)

print("Output Written ! Check output\ascii_image.txt for result")
