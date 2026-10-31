from data_pipeline.football_data_client import get_champions_league_matches
from data_pipeline.transform import transform_to_match
from data_pipeline.supabase_client import upsert_matches

def sync_matches() -> None:
    """
    Traer los datos y guardarlo en Supabase
    """
    raw_matches = get_champions_league_matches()
    
    matches = [
        transform_to_match(raw_matches)
        for raw_matches in raw_matches
    ]
    
    upsert_matches(matches)
    
    print(f"Se guardaron {len(matches)} partidos correctamente")

if __name__ == "__main__":
    sync_matches()