import re

def extract_digits(val):
    val = re.findall(r'\d+$', val)
    return ''.join(val)
