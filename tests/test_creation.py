from unittest import TestCase
from unittest.mock import MagicMock, patch

from PIL import Image

from binaryimager import create_bw_image, create_image_from_config


class TestCreation(TestCase):
    B = (0, 0, 0)
    W = (255, 255, 255)
    G = (127, 127, 127)

    FAKE_IMAGE = {
        (0, 0): B, (1, 0): B, (2, 0): B, (3, 0): B, (4, 0): B,
        (0, 1): B, (1, 1): B, (2, 1): B, (3, 1): B, (4, 1): B,
        (0, 2): G, (1, 2): G, (2, 2): G, (3, 2): G, (4, 2): G,
        (0, 3): W, (1, 3): W, (2, 3): W, (3, 3): W, (4, 3): W,
        (0, 4): W, (1, 4): W, (2, 4): W, (3, 4): W, (4, 4): W,
    }

    FAKE_IMAGE_EXPECTED = {
        (0, 0): B, (1, 0): B, (2, 0): B, (3, 0): B, (4, 0): B,
        (0, 1): B, (1, 1): B, (2, 1): B, (3, 1): B, (4, 1): B,
        (0, 2): W, (1, 2): B, (2, 2): W, (3, 2): B, (4, 2): W,
        (0, 3): W, (1, 3): W, (2, 3): W, (3, 3): W, (4, 3): W,
        (0, 4): W, (1, 4): W, (2, 4): W, (3, 4): W, (4, 4): W,
    }

    def test_creation(self):
        image = MagicMock(width=5, height=5)
        pixels = MagicMock()

        image.copy.return_value = image  # no copy now
        image.load.return_value = pixels
        image.resize = MagicMock(return_value=image)

        pixels.__getitem__ = MagicMock(
            wraps=lambda p: self.FAKE_IMAGE[p[0], p[1]]
        )

        pixels.__setitem__ = MagicMock()

        create_bw_image(image, 254, 1)

        image.copy.assert_called_once()
        image.load.assert_called_once()
        pixels.__setitem__.assert_called()
        pixels.__getitem__.assert_called()

        for args, _ in pixels.__setitem__.call_args_list:
            x, y = args[0]

            self.assertEqual(self.FAKE_IMAGE_EXPECTED[x, y], args[1])

        image.resize.assert_any_call((1, 1))
        image.resize.assert_any_call((5, 5), Image.NEAREST)
