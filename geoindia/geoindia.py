"""Main module."""
import random
import string
import ipyleaflet

class Map(ipyleaflet.Map):

    def __init__(self, center, zoom, **kwargs):

        if "scroll_wheel_zoom" not in kwargs:
            kwargs["scroll_wheel_zoom"]  =True
        super().__init__(center=center, zoom=zoom, **kwargs)

    def add_search_control(self, position='topleft' ,**kwargs):


        if "url" not in kwargs:
            kwargs['url'] = "https://nominatim.openstreetmap.org/search?format=json&q={s}"
            
        search_control = ipyleaflet.SearchControl(position=position, **kwargs)
        self.add_control(search_control)

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