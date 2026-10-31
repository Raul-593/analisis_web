import os
from dotenv import load_dotenv
from supabase import create_client, Client
from cl_stats.models.match import Match

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def upsert_matches(matches: list[Match])-> None:
    if not matches:
        return
    
    matches_data = [
        match.model_dump(mode="json")
        for match in matches
    ]
    
    response = supabase.table("matches").upsert(matches_data).execute()
    
    if getattr(response, "error", None):
        raise RuntimeError(
            f"Error al guardar los partidos: {response.error}"
        )