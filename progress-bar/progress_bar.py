#! /usr/local/bin/python
from rich.console import Console
from rich.progress import track
console = Console()
console.print("Starting the task...")
for point in track(range(100), description="Processing..."):
    pass
console.print(":sparkles: Task completed!", style="bold green")