# Regex objects

import re

def get_phone(string):
    """

    Regular expression to get a phone number.

    To access matched text use the <obj name>.group() method.

    :param string: a string of text which may contain a phone number of format 555-555-5555
    :return: a string of format 555-555-5555
    """

    try:
        phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
        match_obj = phone_num_regex.search(string)
        num = match_obj.group()
        return num
    except AttributeError:
        return "Number in format 555-555-5555 not found."

# email address

# US home address

# US state abbreviation

