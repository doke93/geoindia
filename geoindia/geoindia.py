"""Main module."""
import random
import string

def generate_random_string(length):
    characters = string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation
    rnd = random.SystemRandom()
    return ''.join(rnd.choice(characters) for i in range(length))

def generate_lucky_number(length=1):
    result_str = ''.join(random.choice(string.digits) for i in range(length))
    return result_str