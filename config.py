import configparser
import random
import string

config = configparser.ConfigParser()
gen = string.ascii_letters + string.digits + string.ascii_uppercase
key = ''.join(random.choice(gen) for i in range(12))

SECRET_KEY = key
DEBUG = True