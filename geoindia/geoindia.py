"""Main module."""
import random
import string

def generate_random_string(length=10):
    """Generate a randowm string of a given length

    Args:
        length (int, optional): The length of the string to generate. Default to 10

    Returns:
        str: The generated string
    """    

    characters = string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation
    rnd = random.SystemRandom()
    return ''.join(rnd.choice(characters) for i in range(length))

def generate_lucky_number(length=1):
    """Generate a randowm number of a given length

    Args:
        length (int, optional): The length of the string to generate. Default to 1.

    Returns:
        str: The generated number string
    """
    result_str = ''.join(random.choice(string.digits) for i in range(length))
    return result_str