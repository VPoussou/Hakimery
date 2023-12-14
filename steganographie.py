
from PIL import Image as im
import typing
import numpy as np
from itertools import zip_longest

# So we're doing this in OOP, I need to import a file, convert it to a binary array. 
# Then if I am encoding I'll need to encode the message in binary and then LSB1 it into the binary array
# and save the  resulting image in a lossless format.
# If I am decoding I read the LSB1 in the binary array and then convert the message back to text and display it

class Steganographie:

    def __init__(self, image_path:str):
        self.image_path = image_path
        self.export_counter = 1
        self.image_width = None
        self.image_height = None
        self.new_image_path = 'new_im' + str(self.export_counter) + '.png'
    
    def image_importer(self, image_path:str) -> im.Image:
        imported_image = im.open(image_path).convert('L')
        self.image_width = imported_image.width
        self.image_height = imported_image.height
        return imported_image

    def image_to_array(self, image:im.Image) -> np.array:
        image_array = np.array(image).flatten()
        return image_array

    def binary_array_to_image(self, binary_array:np.array) -> im.Image:
        reshaped_binary_array = binary_array.reshape(self.image_height, self.image_width).astype(np.uint8)
        pil_image = im.fromarray(reshaped_binary_array)
        return pil_image

    def text_binary_encode(self, message:str) -> str:
        binary_string = ''.join(format(ord(i), '08b') for i in message)
        return binary_string

    def image_extract_binary(self, image:np.array) -> str:
           
        pass

    def text_binary_decode(self, binary_encoded_message:str) -> str:
        binary_chunks = [binary_encoded_message[i:i+8] for i in range(0, len(binary_encoded_message), 8)]
        #Shit that list comprehension is beautiful, still a bit too one-liner'ish for me but I'm getting there
        #It's just a beautiful way to chunk out any type of iterable really.
        integers = [int(chunk, 2) for chunk in binary_chunks]
        ascii_string = ''.join(chr(i) for i in integers)
        return ascii_string

    def image_encode(self, image:np.array, binary_encoded_message:str) -> np.array:
        encoded_image = np.array([pixel + 1 if (message_bit and not(pixel & 1)) else pixel & -2 for pixel, message_bit in zip_longest(image, binary_encoded_message, fillvalue=0)])
        return encoded_image

    def encoding_process(self, message:str) -> None:
        imported_image = self.image_importer(self.image_path)
        image_array = self.image_to_array(imported_image)
        binary_text = self.text_binary_encode(message)
        encoded_image = self.image_encode(image_array, binary_text)
        pil_encoded_image = self.binary_array_to_image(encoded_image)
        pil_encoded_image.save('steganography_images/' + self.new_image_path)
        self.export_counter += 1
        pass

    def decoding_process(self) -> str:
        imported_image = self.image_importer(self.image_path)
        image_array = self.image_to_array(imported_image)
        extracted_binary = self.image_extract_binary(image_array)
        message = self.text_binary_decode(extracted_binary)
        print(message)
        return message
    
stegano1 = Steganographie('steganography_images\salgado_amazone.png')
stegano1.encoding_process('schmilblick')
stegano1.decoding_process()