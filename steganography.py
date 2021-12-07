"""Encode and decode images with hidden messages."""

from PIL import Image, ImageDraw

def decode_image(path_to_png):
    """Decodes an image and returns the hidden message."""

    # Open the image using PIL:
    encoded_image = Image.open(path_to_png)

    # Separate the red channel from the rest of the image:
    red_channel = encoded_image.split()[0]

    # Create a new PIL image with the same size as the encoded image:
    decoded_image = Image.new("RGB", encoded_image.size)
    # pixels = decoded_image.load()
    x_size, y_size = encoded_image.size

    # Decode implementation:
    for x in range(x_size):
        for y in range(y_size):
            pixel_bin = bin(red_channel.getpixel((x, y)))
            if pixel_bin[-1] == "1":
                decoded_image.putpixel((x, y), (255, 255, 255))

    # DO NOT MODIFY. Save the decoded image to disk:
    decoded_image.save("img/decoded_image.png")

def encode_image(path_to_png, text_to_write):
    """Encodes an image and returns the hidden message."""

    image_to_encode = Image.open(path_to_png)
    x_size, y_size = image_to_encode.size

    secret_message = write_text((x_size, y_size), text_to_write)

    for x in range(x_size):
        for y in range(y_size):
            if secret_message.getpixel((x, y)) == (255, 255, 255):
                original_pixel = list(image_to_encode.getpixel((x, y)))
                red_channel_bin = bin(original_pixel[0])
                red_channel_encoded = int(red_channel_bin[2:-1] + '1', 2)
                encoded_pixel = (red_channel_encoded, original_pixel[1], original_pixel[2])
                image_to_encode.putpixel((x, y), encoded_pixel)
            else:
                original_pixel = list(image_to_encode.getpixel((x, y)))
                red_channel_bin = bin(original_pixel[0])
                red_channel_encoded = int(red_channel_bin[2:-1] + '0', 2)
                encoded_pixel = (red_channel_encoded, original_pixel[1], original_pixel[2])
                image_to_encode.putpixel((x, y), encoded_pixel)

    image_to_encode.save("img/encoded_image.png")

def write_text(img_size, text_to_write):
    """
    Returns an image of specified size with specified text written on it.
    Image has black background and white text.
    """

    secret_message = Image.new("RGB", img_size)
    draw = ImageDraw.Draw(secret_message)
    draw.text((10, 10), text_to_write, fill=(255, 255, 255))
    return secret_message

if __name__ == "__main__":
    encode_image("img/img_clean.png", "Curious George is a very cute monkey :)")
    decode_image("img/encoded_image.png")
