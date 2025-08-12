#!/usr/bin/env python3
"""
Pixel Manipulation Image Encryption Tool
----------------------------------------
Author: Rif (Internship Task)
Description:
    A simple image encryption and decryption tool that uses pixel
    manipulation. Each pixel's RGB values are transformed with a 
    key-based mathematical operation to produce an encrypted image.
    The same process (in reverse) is used for decryption.
"""

from PIL import Image
import os

def encrypt_image(input_path: str, output_path: str, key: int) -> None:
    """
    Encrypts an image by modifying pixel values.

    Args:
        input_path (str): Path to the original image.
        output_path (str): Path to save the encrypted image.
        key (int): The encryption key (integer).
    """
    img = Image.open(input_path)
    pixels = img.load()

    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]
            # Apply simple key-based transformation
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            pixels[x, y] = (r, g, b)

    img.save(output_path)
    print(f"✅ Image encrypted and saved as: {output_path}")


def decrypt_image(input_path: str, output_path: str, key: int) -> None:
    """
    Decrypts an encrypted image by reversing pixel value changes.

    Args:
        input_path (str): Path to the encrypted image.
        output_path (str): Path to save the decrypted image.
        key (int): The same encryption key used earlier.
    """
    img = Image.open(input_path)
    pixels = img.load()

    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]
            # Reverse transformation
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            pixels[x, y] = (r, g, b)

    img.save(output_path)
    print(f"✅ Image decrypted and saved as: {output_path}")


def get_valid_int(prompt: str) -> int:
    """Prompt user for a valid integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Please enter a valid integer.")


def main():
    print("=== Image Encryption Tool ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? 
").strip().lower()

    if choice not in ('e', 'd'):
        print("❌ Invalid choice. Please choose 'E' or 'D'.")
        return

    input_path = input("Enter input image path: ").strip()
    if not os.path.exists(input_path):
        print("❌ File not found.")
        return

    output_path = input("Enter output image path: ").strip()
    key = get_valid_int("Enter encryption/decryption key (integer): ")

    if choice == 'e':
        encrypt_image(input_path, output_path, key)
    else:
        decrypt_image(input_path, output_path, key)


if __name__ == "__main__":
    main()

