from pydantic import BaseModel

class TeamStanding(BaseModel):
    team_id: int
    team_name: str
    team_crest: str | None = None
    
    played: int = 0
    won: int = 0
    drawn: int = 0
    lost: int = 0
    
    goals_for: int = 0
    goals_against: int = 0
    
    points: int = 0
    
    @property
    def goal_difference(self) -> int:
        return self.goals_for - self.goals_against