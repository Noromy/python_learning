import random
import string

def random_string(length=str):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))