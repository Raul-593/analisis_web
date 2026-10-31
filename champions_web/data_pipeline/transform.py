from cl_stats.models.match import Match

def transform_to_match(data: dict) -> Match:
    # Guarda el diccionario anidado de home y away team
    home_team = data["homeTeam"]
    away_team = data["awayTeam"]
    
    # Guarda el diccionario anidado del resultado del partido
    score = data.get("score", {})
    full_time = score.get("fullTime", {})
    
    start_date = data["season"]["startDate"]
    
    match_data = {
        "id": data["id"],
        "utc_date": data["utcDate"],
        "status": data["status"],
        "matchday": data.get("matchday"),
        "stage": data.get("stage"),
        "group_name": data.get("group"),
        # Extraemos solo el año [:4]
        "season": start_date[:4],
        
        # Obtenemos los datos del home team
        "home_team_id": home_team["id"],
        "home_team_name": home_team["name"],
        "home_team_short_name": home_team.get("shortName"),
        "home_team_tla": home_team.get("tla"),
        "home_team_crest": home_team.get("crest"),
        
        # Obtenemos los datos del away team
        "away_team_id": away_team["id"],
        "away_team_name": away_team["name"],
        "away_team_short_name": away_team.get("shortName"),
        "away_team_tla": away_team.get("tla"),
        "away_team_crest": away_team.get("crest"),
        
        # Goles del partido
        "home_score": full_time.get("home"),
        "away_score": full_time.get("away"),
        
        "last_updated": data.get("lastUpdated")
    }
    return Match.model_validate(match_data)