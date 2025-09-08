from logger import logging

def add(a, b):
    logging.debug(f"Adding {a} and {b}")
    return a + b


# logging.debug(f"call")
add('5', '3')