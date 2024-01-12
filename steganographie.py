
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
        print('image to array' ,image_array[:32])
        return image_array

    def binary_array_to_image(self, binary_array:np.array) -> im.Image:
        reshaped_binary_array = binary_array.reshape(self.image_height, self.image_width).astype(np.uint8)
        pil_image = im.fromarray(reshaped_binary_array)
        return pil_image

    def text_binary_encode(self, message:str) -> str:
        binary_string = ''.join(format(ord(char), '08b') for char in message)
        print('binary string', binary_string[:32])
        return binary_string

    def image_extract_binary(self, image:np.array) -> str:
        print('extracting binary')
        extracted_bits = np.array([str(bit & 1) for bit in image])
        print('binary extraction complete')
        print('extracted binary',extracted_bits[:32])
        return extracted_bits

    def text_binary_decode(self, binary_encoded_message:str) -> str:
        print('decoding message of len', len(binary_encoded_message))
        chonks_as_list_of_list = [binary_encoded_message[i:i+8] for i in range(0, len(binary_encoded_message), 8)]
        print('len chonk as list of lists' ,len(chonks_as_list_of_list))
        chonks = [''.join(chonk_list) for chonk_list in chonks_as_list_of_list]
        ascii_string = ''.join([chr(int(chonk, 2)) for chonk in chonks])
        print('outputing chars of len', len(ascii_string))
        return ascii_string

    def image_encode(self, image:np.array, binary_encoded_message:str) -> np.array:
        print('encoding')
        encoded_image = np.array([pixel | 1 if int(message_bit, 2) and not(pixel & 1) else pixel & -2 for pixel, message_bit in zip_longest(image, binary_encoded_message, fillvalue='0')])
        print('encoding complete')
        print(encoded_image[:32])
        return encoded_image

    def encoding_process(self, message:str) -> None:
        print('Starting encoding')
        imported_image = self.image_importer(self.image_path)
        image_array = self.image_to_array(imported_image)
        binary_text = self.text_binary_encode(message)
        encoded_image = self.image_encode(image_array, binary_text)
        pil_encoded_image = self.binary_array_to_image(encoded_image)
        pil_encoded_image.save('steganography_images/' + self.new_image_path)
        self.export_counter += 1

    def decoding_process(self) -> str:
        print('starting decoding')
        imported_image = self.image_importer( 'steganography_images/' + self.new_image_path)
        image_array = self.image_to_array(imported_image)
        extracted_binary = self.image_extract_binary(image_array)
        message_long = self.text_binary_decode(extracted_binary)
        print(len(message_long))
        message = message_long
        print(message_long[:100])
        return message

print('starting execution')
stegano1 = Steganographie('steganography_images\salgado_amazone.png')
stegano1.encoding_process('schmilblick')
stegano1.decoding_process()