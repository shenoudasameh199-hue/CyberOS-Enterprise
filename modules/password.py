import random
import string
from rich.console import Console
from rich.panel import Panel
from core.database import log_event

console = Console()

def run():
    console.print("\n[bold cyan]=== Cyber Password Generator ===[/bold cyan]")
    length = int(console.input("[bold yellow]Enter Password Length (Default 16): [/bold yellow]") or 16)
    
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    passkey = "".join(random.choice(chars) for _ in range(length))
    
    log_event("Password Generator", "Local System", "SUCCESS", {"entropy": "High"})
    console.print(Panel(f"[bold green]Generated Passkey:[/bold green]\n[bold yellow]{passkey}[/bold yellow]", title="Cryptographic Passkey"))
