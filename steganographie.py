
from PIL import Image as im
import typing
import numpy as np

# So we're doing this in OOP, I need to import a file, convert it to a binary array. 
# Then if I am encoding I'll need to encode the message in binary and then LSB1 it into the binary array
# and save the  resulting image in a lossless format.
# If I am decoding I read the LSB1 in the binary array and then convert the message back to text and display it

class Steganographie:

    def __init__(self, image_path:str):
        self.image_path = image_path
    
    def image_importer(self, image_path:str) -> im.Image:
        imported_image = im.open(image_path)
        return imported_image

    def image_to_binary_array(self, image:im.Image) -> np.array:
        binary_image_array = np.array(image)
        return binary_image_array

    def binary_array_to_image(self, binary_array: np.array) -> im.Image:
        pil_image = im.Image.frombytes(binary_array)
        return pil_image

    def text_binary_encode(self, message:str) -> str:
        binary_string = ''.join(format(ord(i), '08b') for i in message)
        return binary_string

    def image_decode(self) -> str:
        pass

    def text_binary_decode(self, binary_encoded_message:str) -> str:
        binary_chunks = [binary_encoded_message[i:i+8] for i in range(0, len(binary_encoded_message), 8)]
        #Shit that list comprehension is beautiful, still a bit too one-liner'ish for me but I'm getting there
        integers = [int(chunk, 2) for chunk in binary_chunks]
        return integers

    def image_encode(self, image:np.array, binary_encoded_message:str) -> np.array:
        temp_list = []