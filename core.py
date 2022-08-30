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

    my_code = EAN13(number,writer=ImageWriter())
    my_code.save(random_string(6))