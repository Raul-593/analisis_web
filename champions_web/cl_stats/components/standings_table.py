import reflex as rx
from cl_stats.states.standings_state import StandingsState


def _standings_row(standing: dict, index: int) -> rx.Component:
    """
    Tabla de posiciones
    """
    return rx.table.row(
        rx.table.cell(index + 1),
        rx.table.cell(
            rx.hstack(
                rx.image(src=standing["team_crest"],
                         width="20px", height="20px"),
                rx.text(standing["team_name"]),
            )
        ),
        rx.table.cell(standing["played"]),
        rx.table.cell(standing["won"]),
        rx.table.cell(standing["drawn"]),
        rx.table.cell(standing["lost"]),
        rx.table.cell(standing["goals_for"]),
        rx.table.cell(standing["goals_against"]),
        rx.table.cell(standing["goal_difference"]),
        rx.table.cell(standing["points"]),

    )


def standings_table() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Pos"),
                rx.table.column_header_cell("Equipo"),
                rx.table.column_header_cell("PJ"),
                rx.table.column_header_cell("PG"),
                rx.table.column_header_cell("PE"),
                rx.table.column_header_cell("PP"),
                rx.table.column_header_cell("GF"),
                rx.table.column_header_cell("GC"),
                rx.table.column_header_cell("DF"),
                rx.table.column_header_cell("Puntos"),
            )
        ),
        rx.table.body(
            rx.foreach(
                StandingsState.standings,
                lambda standing, index: _standings_row(standing, index),
            )
        ),
    )
