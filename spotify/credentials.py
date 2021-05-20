import os 
from dotenv import load_dotenv
load_dotenv()

CLIENT_ID = os.environ.get('CLIENT_ID', 'Some_random_default_key')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET', 'Some_random_default_key')
REDIRECT_URI = os.environ.get('REDIRECT_URI', 'Some_random_default_key')
