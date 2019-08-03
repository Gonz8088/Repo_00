# Regex objects

import re

def get_phone(string):
    """

    Regular expression to get a phone number.

    :param string: a string of text which may contain a phone number of format 555-555-5555
    :return: a string of format 555-555-5555
    """

    try:
        phone_num_regex = re.compile(r'(\d\d\d-)?(\d\d\d-\d\d\d\d)')
        match_obj = phone_num_regex.search(string)
        num = match_obj.group()
        return num
    except AttributeError:
        return "Number in format 555-555-5555 not found."

# email address
def get_email(string):
    """

    Regular expression to get an email address.

    https://stackoverflow.com/questions/201323/how-to-validate-an-email-address-using-a-regular-expression/201378#201378

    :param string:
    :return: an email address string.
    """
    try:
        email_add_regex = re.compile(r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])")
        match_obj = email_add_regex.search(string)
        email = match_obj.group()
        return email
    except AttributeError:
        return "Email not found."

# US home address

# US state abbreviation

