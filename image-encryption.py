from PIL import Image
import numpy as np

def load_image(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    return img
def save_image(image, image_path):
    image.save(image_path)
def encrypt_image(image, key):
    pixel_data = np.array(image)
    encrypted_data = (pixel_data + key) % 256  
    encrypted_image = Image.fromarray(encrypted_data.astype(np.uint8))
    return encrypted_image
def decrypt_image(image, key):
    pixel_data = np.array(image)
    decrypted_data = (pixel_data - key) % 256 
    decrypted_image = Image.fromarray(decrypted_data.astype(np.uint8))
    return decrypted_image
image_path = "input_image.png" 
encrypted_image_path = "encrypted_image.png"
decrypted_image_path = "decrypted_image.png"
key = 50 
original_image = load_image(image_path)
encrypted_image = encrypt_image(original_image, key)
save_image(encrypted_image, encrypted_image_path)
decrypted_image = decrypt_image(encrypted_image, key)
save_image(decrypted_image, decrypted_image_path)

print("Encryption and decryption completed.")
