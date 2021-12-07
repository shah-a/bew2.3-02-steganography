"""Encode and decode images with hidden messages."""

from PIL import Image

def decode_image(path_to_png):
    """Decodes an image and returns the hidden message."""

    # Open the image using PIL:
    encoded_image = Image.open(path_to_png)

    # Separate the red channel from the rest of the image:
    red_channel = encoded_image.split()[0]

    # Create a new PIL image with the same size as the encoded image:
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
    x_size, y_size = encoded_image.size

    # TODO: Using the variables declared above, replace `print(red_channel)` with a complete implementation:
    print(red_channel)  # Start coding here!

    # DO NOT MODIFY. Save the decoded image to disk:
    decoded_image.save("decoded_image.png")

def encode_image(path_to_png):
    """Encodes an image and returns the hidden message."""
    pass

def write_text(text_to_write):
    """TODO: Add docstring and complete implementation."""
    pass

if __name__ == "__main__":
    decode_image("encoded_sample.png")
