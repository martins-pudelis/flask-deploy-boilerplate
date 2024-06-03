from os import environ
from dotenv import load_dotenv


load_dotenv('.env')

SAMPLE_CONST = environ.get('SAMPLE_CONST', None)
