from unittest import TestCase
from unittest.mock import MagicMock, patch

from binaryimager import create_bw_image, create_image_from_config


class TestConfigration(TestCase):

    def test_with_config(self):
        config = {
            "filename": "a",
            "output_filename": "b",
            "thresholds": {
                "white": 1,
                "black": 254
            }
        }

        with patch("binaryimager.create_bw_image") as mock_create:
            mock_create.return_value = MagicMock()
            mock_create.return_value.save = MagicMock()

            with patch("PIL.Image.open") as mock_open:
                create_image_from_config(config)

                mock_open.assert_called_once()
                mock_create.assert_called_once()
                mock_create.return_value.save.assert_called_once()
