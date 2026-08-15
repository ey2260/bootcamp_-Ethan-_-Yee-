import os
from dotenv import load_dotenv
from pathlib import Path

def load_env():
    """Loads environment variables from the .env file."""
    load_dotenv()
    print(".env loaded (if present)")

def get_key(name, default=None):
    """Retrieves an environment variable key."""
    return os.getenv(name, default)

laod_env()