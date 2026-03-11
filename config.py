import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_config():
    """
    Get configuration from environment variables.

    Returns:
        dict: Configuration dictionary.
    """
    return {
        "notes_dir": os.getenv("NOTES_DIR"),
        "db_url": os.getenv("DB_URL")
    }