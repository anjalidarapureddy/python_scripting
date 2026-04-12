from dotenv import load_dotenv
#Loads environment variables from a .env file into your application

import os

load_dotenv()
print(os.getenv("DB_USER"))
