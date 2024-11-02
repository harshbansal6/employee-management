import os
from configparser import ConfigParser
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'

# Check if the .env file exists
if not env_path.exists():
    print(".env file does not exist")

load_dotenv(dotenv_path=str(env_path))
env = os.getenv('environment')  # DEV for Development/Testing, 'STAG' for Staging and 'PROD' for Production
config = ConfigParser()
config.read('config.ini')
