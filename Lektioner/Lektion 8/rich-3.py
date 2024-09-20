from rich.progress import track
import time

for step in track(range(10), description="Laddar..."):
    time.sleep(0.3)
