import unittest
import os
from PIL import Image
from imagefx.main import remove_background, remove_blur, increase_resolution


class TestImageFX(unittest.TestCase):
    def setUp(self):
        # Load test image
        self.image_path = os.path.join(os.path.dirname(__file__), 'test_image.jpg')
        self.image = Image.open(self.image_path)

    def tearDown(self):
        # Remove temporary output files
        for filename in ['background_removed.jpg', 'blur_removed.jpg', 'resized.jpg']:
            if os.path.exists(filename):
                os.remove(filename)

    def test_remove_background(self):
        # Test with default parameters
        remove_background(self.image_path)
        self.assertTrue(os.path.exists('background_removed.jpg'))
        
        # Test with different threshold
        remove_background(self.image_path, threshold=100)
        self.assertTrue(os.path.exists('background_removed.jpg'))

    def test_remove_blur(self):
        # Test with default parameters
        remove_blur(self.image_path)
        self.assertTrue(os.path.exists('blur_removed.jpg'))
        
        # Test with different scale
        remove_blur(self.image_path, scale=10)
        self.assertTrue(os.path.exists('blur_removed.jpg'))

    def test_increase_resolution(self):
        # Test with default parameters
        increase_resolution(self.image_path, 2)
        self.assertTrue(os.path.exists('resized.jpg'))
        resized_image = Image.open('resized.jpg')
        self.assertEqual(resized_image.size, (self.image.size[0]*2, self.image.size[1]*2))
        
        # Test with different scale
        increase_resolution(self.image_path, 0.5)
        self.assertTrue(os.path.exists('resized.jpg'))
        resized_image = Image.open('resized.jpg')
        self.assertEqual(resized_image.size, (self.image.size[0]//2, self.image.size[1]//2))


if __name__ == '__main__':
    unittest.main()
