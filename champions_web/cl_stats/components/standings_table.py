import reflex as rx
from cl_stats.states.standings_state import StandingsState

def _position_border(index) -> rx.Var[str]:
    return rx.cond(
        index < 8,
        "4px solid #22c55e",
        rx.cond(
            index <24,
            "4px solid #eab308",
            "4px solid transparent",
        ),
    )

def _standings_row(standing: dict, index: int) -> rx.Component:
    """
    Tabla de posiciones
    """
    return rx.table.row(
        rx.table.cell(index + 1, width="1%", white_space="nowrap"),
        rx.table.cell(
            rx.hstack(
                rx.image(src=standing["team_crest"],
                         width="20px", height="20px"),
                rx.text(standing["team_name"]),
            )
        ),
        rx.table.cell(standing["played"], text_align="center", width="1%", white_space="nowrap"),
        rx.table.cell(standing["won"], text_align="center", width="1%", white_space="nowrap"),
        rx.table.cell(standing["drawn"], text_align="center", width="1%", white_space="nowrap"),
        rx.table.cell(standing["lost"], text_align="center", width="1%", white_space="nowrap"),
        rx.table.cell(standing["goals_for"], text_align="center", width="1%", white_space="nowrap"),
        rx.table.cell(standing["goals_against"], text_align="center", width="1%", white_space="nowrap"),
        rx.table.cell(standing["goal_difference"], text_align="center", width="1%", white_space="nowrap"),
        rx.table.cell(standing["points"], text_align="center", width="1%", white_space="nowrap"),
        style={"border_left": _position_border(index)},
    ),


def standings_table() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Pos", width="1%", white_space="nowrap"),
                rx.table.column_header_cell("Equipo"),
                rx.table.column_header_cell("PJ", text_align="center", width="1%", white_space="nowrap"),
                rx.table.column_header_cell("PG", text_align="center", width="1%", white_space="nowrap"),
                rx.table.column_header_cell("PE", text_align="center", width="1%", white_space="nowrap"),
                rx.table.column_header_cell("PP", text_align="center", width="1%", white_space="nowrap"),
                rx.table.column_header_cell("GF", text_align="center", width="1%", white_space="nowrap"),
                rx.table.column_header_cell("GC", text_align="center", width="1%", white_space="nowrap"),
                rx.table.column_header_cell("DF", text_align="center", width="1%", white_space="nowrap"),
                rx.table.column_header_cell("Puntos", text_align="center", width="1%", white_space="nowrap"),
            ),
        ),
        rx.table.body(
            rx.foreach(
                StandingsState.standings,
                lambda standing, index: _standings_row(standing, index),
            ),
        ),
    )
