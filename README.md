# Image Encryption and Decryption using XOR in Python

This Python script demonstrates how to **encrypt** and **decrypt** images using the **XOR bitwise operation**. It uses the `OpenCV` and `NumPy` libraries to load, manipulate, and save images. The encryption and decryption process is symmetric, meaning the same key is used for both operations.

## How It Works

- **Encryption**: The image is XOR'd with a key to generate an encrypted version.
- **Decryption**: The encrypted image is XOR'd again with the same key to recover the original image.
- The key used for XOR can be any integer between 0 and 255.

### Key Features:
- Encrypts and decrypts images using a reversible XOR operation.
- Supports color (BGR) images.
- Simple to understand and easy to modify.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy

You can install the required dependencies using pip:

```bash
pip install opencv-python numpy
