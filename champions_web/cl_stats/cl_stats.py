import reflex as rx
from cl_stats.pages.standings import standings_page


app = rx.App()
app.add_page(standings_page, route="/", title="Champions League")