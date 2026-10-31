import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.football-data.org/v4"
API_KEY = os.getenv("FOOTBALL_DATA_API_KEY")

def get_champions_league_matches() -> list[dict]:
    """ 
    Llamada a los partidos de la Champions League
    Returns: la lista de partidos
    """
    url = f"{BASE_URL}/competitions/CL/matches"
    headers = { "X-Auth-Token": API_KEY }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    return response.json()["matches"]
