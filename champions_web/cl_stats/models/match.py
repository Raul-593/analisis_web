from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Match(BaseModel):
    #* Match information
    id: int
    utc_date: datetime
    status: str
    matchday: Optional[int] = None
    stage: Optional[str] = None
    group_name: Optional[str] = None
    season: str
    
    #* Home team information
    home_team_id: int
    home_team_name: str
    home_team_short_name: Optional[str] = None
    home_team_tla: Optional[str] = None
    home_team_crest: Optional[str] = None

    #* Away team information
    away_team_id: int
    away_team_name: str
    away_team_short_name: Optional[str] = None
    away_team_tla: Optional[str] = None
    away_team_crest: Optional[str] = None
    
    #* Goals
    home_score: Optional[int] = None
    away_score: Optional[int] = None
    
    last_updated: Optional[datetime] = None