import socket
from rich.console import Console
from rich.panel import Panel
from core.database import log_event

console = Console()

def run():
    console.print("\n[bold cyan]=== Network Diagnostic & IP Lookup ===[/bold cyan]")
    target = console.input("[bold yellow]Enter Domain or Hostname (e.g., google.com): [/bold yellow]")
    if not target:
        target = "google.com"
        
    try:
        ip = socket.gethostbyname(target)
        log_event("Network Tools", target, "SUCCESS", {"ip": ip})
        console.print(Panel(f"[bold green]Host:[/bold green] {target}\n[bold cyan]Resolved IP:[/bold cyan] {ip}", title="Network Lookup Result"))
    except Exception as e:
        log_event("Network Tools", target, "FAILED", {"error": str(e)})
        console.print(f"[bold red]Error resolving host: {e}[/bold red]")
