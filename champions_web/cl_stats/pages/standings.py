import reflex as rx
from cl_stats.states.standings_state import StandingsState
from cl_stats.components.standings_table import standings_table

def standings_page() -> rx.Component:
    return rx.box(
        rx.heading("Tabla de Posiciones"),
        rx.cond(
            StandingsState.is_loading,
            rx.text("Cargando..."),
            rx.cond(
                StandingsState.error_message != "",
                rx.text(StandingsState.error_message, color = "red"),
                standings_table(),
            ),
        ),
        on_mount=StandingsState.load_standings,
        padding="2em",
    )