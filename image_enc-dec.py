import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.fft import fft2, ifft2

# Function to generate a reference wave based on a user-defined key
def generate_reference_wave(image_shape, key):
    np.random.seed(key)  # Use the key for reproducibility
    return np.exp(2j * np.pi * np.random.rand(*image_shape))

def encrypt_image(image, key):
    # Generate a reference wave using the key
    reference_wave = generate_reference_wave(image.shape, key)

    # Perform Fourier Transform on the original image
    image_fft = fft2(image, axes=(0, 1))  # Apply FFT along height and width for RGB

    # Create a hologram by multiplying fft with the reference wave
    hologram = image_fft * reference_wave

    return hologram, reference_wave

def decrypt_image(hologram, key):
    # Regenerate the reference wave using the same key
    reference_wave = generate_reference_wave(hologram.shape, key)

    # Reconstruct the image by dividing by the reference wave
    reconstructed_fft = hologram / reference_wave

    # Perform the inverse Fourier Transform to get the decrypted image
    decrypted_image = ifft2(reconstructed_fft, axes=(0, 1))

    return np.real(decrypted_image)


choice = input("Enter 'E' for Encryption or 'D' for Decryption: ").strip().lower()

if choice == 'e':
        # Load the image
        image_path = input("Enter the path of the image to encrypt: ")
        image = cv2.imread(image_path)  # Load as color (BGR)

        

        # Convert BGR to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Get user-defined key
        key = int(input("Enter a key for encryption (an integer value): "))

        # Encrypt the image
        hologram, _ = encrypt_image(image, key)

        # Calculate the magnitude for visualization
        hologram_magnitude = np.abs(hologram)

        # Normalize hologram for display (scaling to 0-255)
        hologram_display = np.clip(hologram_magnitude, 0, 255).astype(np.uint8)

        # Display the hologram (encrypted image)
        plt.imshow(hologram_display)
        plt.title("Encrypted Image (Hologram)")
        plt.axis('off')
        plt.show()

        # Save the hologram as a numpy array to preserve complex data
        hologram_file_path = input("Enter the path to save the hologram (e.g., 'hologram.npy'): ")
        np.save(hologram_file_path, hologram)
        print(f"Hologram saved as: {hologram_file_path}")

elif choice == 'd':
        # Load the saved hologram
        hologram_file_path = input("Enter the path of the hologram to decrypt: ")
        
        loaded_hologram = np.load(hologram_file_path)

        # Get user-defined key
        key = int(input("Enter the key for decryption (the same integer value): "))

        # Decrypt the image
        decrypted_image = decrypt_image(loaded_hologram, key)

        # Normalize the decrypted image to 0-255 and convert to uint8
        decrypted_image_normalized = np.clip(decrypted_image, 0, 255).astype(np.uint8)

        # Save and display the decrypted image
        plt.imshow(decrypted_image_normalized)
        plt.title("Decrypted Image")
        plt.axis('off')
        plt.show()

        # Save the decrypted image in RGB format
        cv2.imwrite('decrypted_image.jpg', cv2.cvtColor(decrypted_image_normalized, cv2.COLOR_RGB2BGR))
        print("Decrypted image saved as 'decrypted_image.jpg'.")

else:
        print("Invalid choice. Please enter 'E' for Encryption or 'D' for Decryption.")


