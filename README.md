 💡𝙋𝙝𝙮𝙨𝙞𝙘𝙖𝙡 𝙀𝙭𝙥𝙡𝙖𝙣𝙖𝙩𝙞𝙤𝙣💡

To create a hologram, we need an object and a light source. Sunlight is unsuitable due to its various wavelengths, which are only effective for photography. In holography, we require laser light, which emits a single wavelength, travels in a specific direction, and is coherent.

•The laser light🔦 is split into two beams using lenses.One, called 
•the object beam O(x,y)=exp(jδ(x,y)), bounces off the object and then reaches the holographic plate, carrying the object's information. In our case, this beam is unknown and not needed for the encryption process, so we focus on the reference beam.

•The other beam, the reference beam, travels directly to the holographic plate. The intersection of these two beams creates the interference pattern, which is the 3D model.
In our case, we will generate a reference wave. As an electromagnetic wave, it is represented in complex terms: 
R(x,y) = R0exp(2jπfy) 

💡𝘿𝙞𝙜𝙞𝙩𝙖𝙡 𝙃𝙤𝙡𝙤𝙜𝙧𝙖𝙥𝙝𝙮💡

Returning to our code, we will use the holography concept to hide image information, such as amplitude, phase, and frequency, extracted using the FFT. This will encrypt the image.

✨The code begins by importing necessary libraries:

𝘯𝘶𝘮𝘱𝘺 for numerical operations,
cv2 for image processing,
matplotlib.pyplot for displaying images,
scipy.fft for Fourier Transform functions.

✨Generating the Reference Wave Function

•The key role of the reference wave is to modify the phase of the image's frequency components during modulation. The random phase values in the reference wave ensure that the encrypted hologram is secure and impossible to decrypt without the correct key.

•The function's output is a complex Numpy array with the same shape as our image. The reference wave elements have a constant magnitude of 1 and a random phase.

 •We use np.random.seed(key) to ensure reproducibility. The same key will generate the same random values, resulting in the same reference wave for multiple encryptions.
 
•np.random.rand(*image_shape) generates random values representing the phase values of the reference wave array. However, they are not truly random due to the random.seed function. With the same key, the function will generate the same random values for decryption.

✨Fast Fourier Transform (FFT)

The output of the FFT function is a complex Numpy array with the same shape as the image. It encodes critical image information, such as amplitude, phase, and spatial frequency components.
The amplitude represents the strength of these frequency components, and the phase encodes their spatial relationships.

✨The Digital Hologram

•Multiplying the FFT and the reference wave performs "modulation" of two complex values. This operation combines the frequency information of the image with the phase and frequency characteristics of the reference wave, resulting in another complex Numpy array, the hologram.
hologram = image_fft * reference_wave
 
•Since the reference wave has a magnitude of 1, the magnitude information of the original image's frequency components is preserved.

 • The hologram's phase is the sum of both the image_fft phase and the reference wave phase. This step hides the phase information of the original image's frequency within the reference wave phase, making it impossible to infer the image without knowing the reference wave.

✨Decryption

• To recover the original data (amplitude, phase, and frequency), we divide the hologram by the reference wave (the same key as encryption) , undoing the phase modulation. This restores the original FFT of the image.
Original_fft =hologram / refrence_wave

 •Performing an inverse FFT then converts the image from the frequency domain back to the spatial domain, reconstructing the decrypted image.

