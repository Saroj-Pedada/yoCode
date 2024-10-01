from PIL import Image

# Define your color map for 3-bit sequences
color_map = {
    '000': (0, 0, 0),       # Black
    '001': (0, 0, 255),     # Blue
    '010': (0, 255, 0),     # Green
    '011': (255, 0, 0),     # Red
    '100': (255, 255, 0),   # Yellow
    '101': (0, 255, 255),   # Cyan
    '110': (255, 0, 255),   # Magenta
    '111': (255, 255, 255)  # White
}

# Convert text to binary string
def text_to_binary(text):
    binary = ''.join(format(ord(c), '08b') for c in text)
    return binary

# Generate the custom code image
def generate_code(data, image_path='custom_code.png'):
    # Convert text to binary
    binary_data = text_to_binary(data)
    # Group binary data into 3-bit chunks
    chunks = [binary_data[i:i+3] for i in range(0, len(binary_data), 3)]
    
    # Create an image (width = number of chunks, height = 1 row)
    img = Image.new('RGB', (len(chunks), 1), 'white')
    pixels = img.load()

    # Assign colors based on 3-bit chunks
    for i, chunk in enumerate(chunks):
        # Ensure chunk is exactly 3 bits long
        if len(chunk) < 3:
            chunk = chunk.ljust(3, '0')  # Pad with 0s if needed
        color = color_map.get(chunk, (255, 255, 255))  # Default to white if not found
        pixels[i, 0] = color

    # Save the image
    img.save(image_path)
    print(f"Custom code saved as {image_path}")

# Example usage
generate_code("hello world")
