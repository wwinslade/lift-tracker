import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env.local')
print(os.getenv('DJANGO_SECRET_KEY'))
print(os.getenv('DATABASE_URL'))