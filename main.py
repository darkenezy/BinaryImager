"""
Main module with function for creating B/W verison of image with usage of
dithering.
"""

import json

from PIL import Image


def create_bw_image(image, white_thresholds, black_thresholds):
    """
    Create copy of the image with only black and white colors. Every pixel
    with average color brightness lower than `white_thresholds` will turn
    white, while every pixel with average color brightness higher than
    `black_thresholds` will tunr black. Other pixels will decide color
    depending on their position.

    :param image: image to create copy of
    :param white_thresholds: threshold for turning white
    :param black_thresholds: threshold for turning black

    :returns: resulting image
    """

    bw_image = image.copy()

    pixels = bw_image.load()

    for i in range(bw_image.width):
        for j in range(bw_image.height):
            val = sum(pixels[i, j]) / 3

            if val < black_thresholds:
                pixels[i, j] = (0, 0, 0)

            elif val > white_thresholds:
                pixels[i, j] = (255, 255, 255)

            else:
                if (i+j)%2:
                    pixels[i, j] = (0, 0, 0)
                else:
                    pixels[i, j] = (255, 255, 255)

    orig_width = bw_image.width
    orig_height = bw_image.height

    bw_image = bw_image.resize((bw_image.width // 5, bw_image.height // 5))
    bw_image = bw_image.resize((orig_width, orig_height), Image.NEAREST)

    return bw_image


def create_image_from_config(config):
    """
    Create copy of the image with only black and white colors using
    passed configuration object and save it to specified file.
    For details about creation see :func:`.create_bw_image`.

    :param config: configuration object
    """

    image = Image.open(config["filename"])

    bw_image = create_bw_image(
        image,
        white_thresholds=config["thresholds"]["white"],
        black_thresholds=config["thresholds"]["black"],
    )

    bw_image.save(config["output_filename"])


if __name__ == "__main__":
    with open("config.json") as fp:
        CONFIG = json.load(fp)

    create_image_from_config(CONFIG)
