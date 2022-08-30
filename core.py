from barcode import EAN13
from barcode.writer import ImageWriter
from utils import random_string


def generate_barcode(number):
    '''
    Returns PNG barcode for 12 digit number

    Parameters:
    - number (str) : 12 digit number to create barcode for

    Return:
    - file png : Image Barcode 
    '''

    barcode = EAN13(number,writer=ImageWriter())
    file_name = random_string(6)
    barcode.save(file_name)

    return open(f"{file_name}.png")