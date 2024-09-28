🔍 Holography is a technique that records the light scattered from an object and reconstructs it as a three-dimensional image.
In digital holography, we use mathematical methods like fft to encode and decode these images, capturing intricate details that traditional imaging techniques can’t.
We can find holography in VR , Medical Imaging and Engineering Applications etc .. 

💡 FFT (Fast Fourier Transform) is a mathematical algorithm that converts spatial data into frequency data, and vice versa (ifft) .
It allows us to manipulate images in the frequency domain, making it possible to perform complex operations like encryption, filtering, and image reconstruction.

🔐 How the code works :

✨The code begins by importing necessary libraries:
numpy for numerical operations,
cv2 for image processing,
matplotlib.pyplot for displaying images,
scipy.fft for Fourier Transform functions.

✨the reference wave contains random values and will be used to create the hologram. 
The exp function generates the complex exponential, where (j) represents the imaginary unit.

✨The hologram is created by multiplying the Fourier-transformed image with the reference wave. 
This step encodes the amplitude and phase information of the image, producing a new complex representation.

✨The Inverse Fourier Transform is applied to the hologram to bring it back to the spatial domain.
The magnitude of the resulting complex values is calculated to get the intensity of the hologram, which represents the light intensity at each pixel.

✨Decryption: Using the same reference wave, reverse the process to retrieve the original image from the hologram, ensuring a secure encryption-decryption cycle.
