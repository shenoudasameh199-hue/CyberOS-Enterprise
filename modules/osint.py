import requests
from rich.console import Console
from rich.table import Table
from core.database import log_event

console = Console()

def run():
    console.print("\n[bold cyan]=== OSINT Username Footprint Scanner ===[/bold cyan]")
    username = console.input("[bold yellow]Enter Target Username: [/bold yellow]")
    if not username:
        return
        
    platforms = {
        "GitHub": f"https://github.com/{username}",
        "Twitter/X": f"https://x.com/{username}",
        "Instagram": f"https://instagram.com/{username}"
    }
    
    table = Table(title=f"OSINT Footprint for '{username}'")
    table.add_column("Platform", style="magenta")
    table.add_column("Profile URL", style="cyan")
    
    for platform, url in platforms.items():
        table.add_row(platform, url)
        
    log_event("OSINT Footprint", username, "COMPLETED", platforms)
    console.print(table)
