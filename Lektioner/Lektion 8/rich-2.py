from rich.console import Console
from rich.table import Table

console = Console()
table = Table(title="Elevernas Favoritfilmer")

table.add_column("Namn", style="cyan", no_wrap=True)
table.add_column("Film", style="magenta")
table.add_column("Ålder", justify="right", style="green")

table.add_row("Alice", "Interstellar", "25")
table.add_row("Bob", "Inception", "30")
table.add_row("Charlie", "The Matrix", "22")

console.print(table)
