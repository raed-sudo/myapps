from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

import os

password = os.getenv('PASSWORD')

print(password)

