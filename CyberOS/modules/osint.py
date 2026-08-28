import requests
from rich.console import Console
from core.database import log_action

def username_recon(username):
    console = Console()
    console.print(f"[cyan][*] Searching digital footprint for username: {username}...[/cyan]")
    platforms = {
        "GitHub": f"https://github.com/{username}",
        "Twitter/X": f"https://twitter.com/{username}",
        "Instagram": f"https://instagram.com/{username}",
        "Telegram": f"https://t.me/{username}"
    }
    for name, url in platforms.items():
        try:
            res = requests.get(url, timeout=4, headers={"User-Agent": "CyberOS-OSINT"})
            if res.status_code == 200:
                console.print(f" [bold green]✔ Found on {name}: {url}[/bold green]")
            else:
                console.print(f" [dim]✖ Not found on {name}[/dim]")
        except:
            console.print(f" [yellow]! Connection timeout for {name}[/yellow]")
    log_action("OSINT-Recon", username, "COMPLETED")
