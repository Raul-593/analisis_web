import reflex as rx
from cl_stats.services.standings_calculator import get_current_standings

class StandingsState(rx.State):
    standings: list[dict] = []
    is_loading: bool = True
    error_message: str = ""
    
    def load_standings(self):
        self.is_loading = True
        self.error_message = ""
        
        try:
            self.standings = get_current_standings()
        except Exception as e:
            self.error_message = str(e)
        finally:
            self.is_loading = False
