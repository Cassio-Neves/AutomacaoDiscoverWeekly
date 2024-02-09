import os
from dotenv import load_dotenv

load_dotenv()

secret_infos = {
    "client_id": os.getenv("SPOTIPY_CLIENT_ID"),
    "client_secret": os.getenv("SPOTIPY_CLIENT_SECRET"),
    "redirect_uri": os.getenv("SPOTIPY_REDIRECT_URI")
}