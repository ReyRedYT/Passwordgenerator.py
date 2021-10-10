length = 15

digits = '0123456789'
chars = 'abcdefghijklmnopqrstuvwxyz'
up = chars.upper()
special = '_-!?&#+*'

all = digits+chars+up+special
from random import choice
password = ''.join(
    choice(all) for i in range(length)
)
print(password)