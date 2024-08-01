import json

ENCRYPT_JSON_STRING = '''
{
    "A": "T",
    "B": "H",
    "C": "E",
    "D": "Q",
    "E": "U",
    "F": "I",
    "G": "C",
    "H": "K",
    "I": "B",
    "J": "R",
    "K": "O",
    "L": "W",
    "M": "N",
    "N": "F",
    "O": "X",
    "P": "J",
    "Q": "M",
    "R": "P",
    "S": "S",
    "T": "V",
    "U": "A",
    "V": "L",
    "W": "Z",
    "X": "Y",
    "Y": "D",
    "Z": "G"
}
'''

# TODO: Help Alice load the JSON string into a dictionary
ENCRYPTION_DICT = {}


def encrypt(plaintext):
    """
    Takes in plaintext as an input and returns 'ciphertext': the result 
    of substituting each letter in the plaintext by its corresponding 
    encrypted character in ENCRYPTION_DICT. 

    The plaintext comprises entirely of uppercase letters and non-alphabetic 
    characters like punctuation. Non-alphabetic characters needn't be encrypted, 
    but rather should appear in the plaintext in their original form. 

    >>> encrypt("HEY, HOW'S IT GOING?")
    "KUD, KXZ'S BV CXBFC?"
    >>> encrypt("I LOVE CS 106A!")
    'B WXLU ES 106T!'
    >>> encrypt("UNICORNS ARE THE MOST BEAUTIFUL ANIMALS IN EXISTENCE")
    'AFBEXPFS TPU VKU NXSV HUTAVBIAW TFBNTWS BF UYBSVUFEU'
    """
    pass


def decrypt(ciphertext):
    """
    Uses ENCRYPTION_DICT to decrypt each of the alphabetic characters of
    ciphertext.

    >>> decrypt("KUD, KXZ'S BV CXBFC?")
    "HEY, HOW'S IT GOING?"
    >>> decrypt('B WXLU ES 106T!')
    'I LOVE CS 106A!'
    >>> decrypt('AFBEXPFS TPU VKU NXSV HUTAVBIAW TFBNTWS BF UYBSVUFEU')
    'UNICORNS ARE THE MOST BEAUTIFUL ANIMALS IN EXISTENCE'
    """
    pass


def create_encryption_dict(filename):
    """
    Creates an encryption dictionary from the provided filename.

    >>> create_encryption_dict('encryption_file')
    {'A': 'T', 'B': 'H', 'C': 'E', 'D': 'Q', 'E': 'U', 'F': 'I', 'G': 'C', 'H': 'K'}
    """
    pass
