from cl_stats.models.match import Match
from cl_stats.models.standing import TeamStanding

def _get_or_create( standings: dict[int, TeamStanding], team_id:int, team_name: str, team_crest: str | None) -> TeamStanding:
    """
    Devuelve la posicion existente de un equipo o crea una nueva
    """
    if team_id not in standings:
        standings[team_id] = TeamStanding(
            team_id=team_id,
            team_name=team_name,
            team_crest=team_crest,
            played=0,
            won=0,
            drawn=0,
            lost=0,
            goals_for=0,
            goals_against=0,
            points=0,
        )
    return standings[team_id]

def calculate_standings(matches: list[Match]) -> list[TeamStanding]:
    """
    Recibe la lista de partidos y devuelve la tabla de posiciones
    """
    
    standings: dict[int, TeamStanding] = {}
    
    finished_matches = [
        match
        for match in matches
        if (
            match.status == "FINISHED"
        )
    ]
    
    for match in finished_matches:
        # Informacion de los Equipos
        home_standing = _get_or_create(
            standings=standings,
            team_id=match.home_team_id,
            team_name=match.home_team_name,
            team_crest=match.home_team_crest
        )
        away_standing = _get_or_create(
            standings=standings,
            team_id=match.away_team_id,
            team_name=match.away_team_name,
            team_crest=match.away_team_crest
        )
        
        # Partido Jugado
        home_standing.played += 1
        away_standing.played += 1
        
        # Goles del partido
        home_standing.goals_for += match.home_score
        home_standing.goals_against += match.away_score
        
        away_standing.goals_for += match.away_score
        away_standing.goals_against += match.home_score
        
        # Resultado y Puntos
        if match.home_score > match.away_score:
            home_standing.won += 1
            home_standing.points += 3
            away_standing.lost += 1
        
        elif match.away_score > match.home_score:
            away_standing.won += 1
            away_standing.points += 3
            home_standing.lost += 1
        
        else:
            home_standing.drawn += 1
            home_standing.points += 1
            
            away_standing.drawn += 1
            away_standing.points += 1

    result = list(standings.values())
    
    result = sorted(
        result,
        key= lambda s: (
            s.points,
            s.goal_difference,
            s.goals_for,            
        ),
        reverse= True,
    )

    return result