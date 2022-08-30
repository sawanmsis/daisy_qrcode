from barcode import EAN13
from barcode.writer import ImageWriter

import uuid

def _random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4()) # Convert UUID format to a Python string.
    random = random.upper() # Make all characters uppercase.
    random = random.replace("-","") # Remove the UUID '-'.
    return random[0:string_length] # Return the random string.


def generate_barcode(number):
    '''
    Returns PNG barcode for 12 digit number

    Parameters:
    - number (str) : 12 digit number to create barcode for

    Return:
    - file png : Image Barcode 
    '''

    my_code = EAN13(number,writer=ImageWriter())
    my_code.save(_random_string(6))