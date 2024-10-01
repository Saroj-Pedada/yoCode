import cv2
import numpy as np

# Define the reverse color map to decode colors back to 3-bit binary values
reverse_color_map = {
    (0, 0, 0): '000',        # Black
    (0, 0, 255): '001',      # Blue
    (0, 255, 0): '010',      # Green
    (255, 0, 0): '011',      # Red
    (255, 255, 0): '100',    # Yellow
    (0, 255, 255): '101',    # Cyan
    (255, 0, 255): '110',    # Magenta
    (255, 255, 255): '111'   # White
}

# Function to convert binary to text
def binary_to_text(binary_data):
    chars = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    text = ''.join([chr(int(char, 2)) for char in chars])
    return text

# Function to decode an image with custom color codes
def scan_code(image_path):
    # Read the image
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    binary_data = ''

    # Loop through each pixel in the row (assuming 1 row of data)
    for x in range(width):
        # Get pixel color
        b, g, r = image[0, x]  # OpenCV uses BGR format, not RGB
        color = (r, g, b)  # Convert to RGB format

        # Find corresponding 3-bit binary value from the color map
        binary_value = reverse_color_map.get(color, '000')  # Default to '000' if color not found
        binary_data += binary_value

    # Convert the binary data back to text
    decoded_text = binary_to_text(binary_data)
    return decoded_text

# Example usage to scan the generated image
decoded_text = scan_code('custom_code.png')
print(f"Deciphered text: {decoded_text}")
