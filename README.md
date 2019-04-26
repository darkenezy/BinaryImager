# BinaryImager
Creates B/W pixel image from your picture

## Requirements
* python 3.6+
* pillow
`pip install pillow`

## Usage
### Config it
Configuring file `config.cfg` contains single string formatted like:
`<filename> <black border> <white border>  `

#### Examples:
`filename` test.jpg
`black border` - integer, 0 - 128, default 85
`white border` - integer, 128 - 255, default 170

### Run the service
`python3 main.py`