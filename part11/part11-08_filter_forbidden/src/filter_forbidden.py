# WRITE YOUR SOLUTION HERE:
def filter_forbidden(string: str, forbidden: str):
    new_string = "".join([character for character in string if character not in forbidden])
    return new_string