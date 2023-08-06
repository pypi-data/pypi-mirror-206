import numpy as np
import cv2
import requests
from io import BytesIO
from PIL import Image

def remove_blur(image_path_or_url, scale=1.0):
    """ Remove the blurness from the image using the Gausian Blur.
    Args:
        image_path_or_url (str): Path to the image or to url of it
        scale (float) : Scaling factor for kernel size (default =1.0).

        Returns:
            numpy.ndarray: The blurred image"""

    # Load the image from file or URL
    if image_path_or_url.startswith('https'):
        response = requests.get(image_path_or_url)
        img = np.array(Image.open(BytesIO(response.content)))
    else:
        img = cv2.imread(image_path_or_url)

    # Apply the Gaussian Blur
    kernel_size = int(2*round(scale) + 1)
    blurred = cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

    return blurred


def increase_resolution(image_path_or_url, factor=1.0):
    """Toggle with Increase or Decrease the Resolution of the image using the Lanczoz Interpolation.

    Args:
        image_path_or_url (str): Path to the image or to url of it
        factor : Scaling factor to increase or decrease image resolution (default=1.0)

    Returns:
        numpy.ndarray: The high resolution image

    """
    if image_path_or_url.startswith('https'):
        response = requests.get(image_path_or_url)
        img = np.array(Image.open(BytesIO(response.content)))

    else:
        img = cv2.imread(image_path_or_url)

    # Determine the output size

    width = int(img.shape[1] * factor)
    height = int(int.shape[0] * factor)

    # Resize image using the Lanczoz interpolation
    highres = cv2.cv2.resize(img, (width, height),interpolation=cv2.INTER_LANCZOS4)

    return highres


def remove_background(image_path_or_url):
    """ Remove background from the image using the remove.bg open API

    Args:
        image_path_or_url (str): Path to the image or to url of it


    Returns:
        numpy.ndarray : The foreground image with transparent background

    Raises:
        Valueerror : If the API key is missing or invalid

    """

    # Sepcify the remove.bg API key here
    api_key = 'Hb3roW3ufVpKF5JVVE9APuYF'

    if not api_key:
        raise ValueError("Please provide a valid api key")

    if image_path_or_url.startswith('https' or 'http'):
        response = requests.get(image_path_or_url)
        img = np.array(Image.open(BytesIO(response.content)))

    else:
        img = cv2.imread(image_path_or_url)

    # Prepare data for the API request

    headers = {'X-api-Key': api_key}
    data = {'size': 'auto'}

    # Send API request to remove.bg

    response = requests.post('https://api.remove.bg/v1.0/removebg', headers=headers,data=data, files={'image_file': img.tobytes()}, stream=True)

    # Check for errors in the API response

    if response.status_code != requests.codes.ok:
        raise ValueError('Error from remove.bg API: {}'.format(response.text))

    # Convert the response data to image format

    img = np.array(Image.open(BytesIO(response.content)))

    return img

def main():
    print("Please select an option:")
    print("1. Remove background from image")
    print("2. Remove blur from image")
    print("3. Increase resolution of image")

    choice = input("Enter your choice: ")

    if choice == '1':
        image_path_or_url = input("Enter path or URL of the input image: ")
        scale = float(input("Enter the scale for blur removal: "))
        img = remove_blur(image_path_or_url, scale)
        cv2.imshow('Blurred image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
       

    elif choice == '2':
        image_path_or_url = input("Enter path or URL of the input image: ")
        factor = float(input("Enter the factor for resolution increase: "))
        img = toggle_resolution(image_path_or_url, factor)
        cv2.imshow('High-resolution image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice == '3':
        image_path_or_url = input("Enter path or URL of the input image: ")
        img = remove_background(image_path_or_url)
        cv2.imshow('Foreground image with transparent background', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
       

    else:
        print("Invalid choice. Please enter a number from 1 to 3.")

if __name__ == 'main':
    main()

