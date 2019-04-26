# BinaryImager

Creates B/W pixel image from your picture with dithering.

## Installation

- Install `python` version 3.6 or newer.
- Install requirements from `requirements.txt` -> `pip install-r requirements.txt`

## Usage

### Configuration

Set your settings in file `config.json`. Configuration file structure:

```json
{
  "filename": "example.png",
  "output_filename": "example.out.png",
  "thresholds": {
    "white": 170,
    "black": 85
  }
}

```

Place your target file's name in place of `"example.png"`, threshold values
for white and black in corresponding fields inside of `"thresholds"` key.

Recommended values:

- `"thresholds"."white"` -> 85
- `"thresholds"."black"` -> 170

### Run

Run script from terminal with `python main.py`.
