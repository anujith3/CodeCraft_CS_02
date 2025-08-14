import cv2
import numpy as np

def encrypt_image(image_path, key, output_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return

    # Create a key array of the same shape as the image
    key_array = np.full(img.shape, key, dtype=np.uint8)

    # Encrypt using XOR
    encrypted_img = cv2.bitwise_xor(img, key_array)
    cv2.imwrite(output_path, encrypted_img)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(encrypted_path, key, output_path):
    enc_img = cv2.imread(encrypted_path)
    if enc_img is None:
        print("Error: Encrypted image not found!")
        return

    # Create the same key array
    key_array = np.full(enc_img.shape, key, dtype=np.uint8)

    # Decrypt using XOR (XOR again with the same key)
    decrypted_img = cv2.bitwise_xor(enc_img, key_array)
    cv2.imwrite(output_path, decrypted_img)
    print(f"Decrypted image saved as {output_path}")

# Usage example
if __name__ == '__main__':
    key = 123  # Integer from 0 to 255
    encrypt_image('input_image.jpg', key, 'encrypted_image.png')
    decrypt_image('encrypted_image.png', key, 'decrypted_image.png')
