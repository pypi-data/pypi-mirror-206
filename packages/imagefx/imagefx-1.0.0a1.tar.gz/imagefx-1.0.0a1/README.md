# Imagefx

Imagefx is a Python library for performing various image processing operations on input images. With imagefx, you can easily remove the background from an image, remove blur from an image, and increase the resolution of an image. 

## Installation

You can install imagefx using pip:

```pip install imagefx```

## Usage

You can use imagefx from the command line or by importing it into your own Python scripts.

### Command Line

To use imagefx from the command line, use the following syntax:

```imagefx <operation> <image> [--scale <scale>] [--factor <factor>]```

`<operation>` can be one of the following:

- `remove_bg`: Remove the background from an image.
- `remove_blur`: Remove blur from an image.
- `toggle_resolution`: Increase the resolution of an image.

`<image>` can be either the path or URL of the input image.

`--scale` is a parameter for the `remove_blur` operation that controls the scale for blur removal. It defaults to 2.0.

`--factor` is a parameter for the `toggle_resolution` operation that controls the factor for resolution increase. It defaults to 2.0.

### Python Script

To use ImageFX in your own Python scripts, you can import it like this:

```python
import imagefx

# Call the functions as needed

Here are the available functions:

remove_background(image)

# Removes the background from the input image and returns the foreground image with a transparent background.

import imagefx
img = imagefx.remove_background('path/to/image.jpg')

remove_blur(image, scale)

# Removes blur from the input image and returns the resulting image.

import imagefx

img = imagefx.remove_blur('path/to/image.jpg', scale=2.0)

toggle_resolution(image, factor)

# Increases the resolution of the input image and returns the resulting image.

import imagefx

img = imagefx.increase_resolution('path/to/image.jpg', factor=2.0)

```

## Contributing


If you have any suggestions or find any bugs, please create an issue on the GitHub repository.

If you'd like to contribute to the project, feel free to submit a pull request!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

