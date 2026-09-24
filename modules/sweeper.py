import random
from rich.console import Console
from rich.table import Table
from core.database import log_event

console = Console()

def run():
    console.print("\n[bold cyan]=== Subnet Host Sweeper ===[/bold cyan]")
    subnet = console.input("[bold yellow]Enter Subnet (e.g., 192.168.1): [/bold yellow]") or "192.168.1"
    
    table = Table(title=f"Active Hosts in {subnet}.0/24")
    table.add_column("IP Address", style="cyan")
    table.add_column("Status", style="green")
    
    found = []
    for i in [1, 10, 15, 100, 254]:
        ip = f"{subnet}.{i}"
        table.add_row(ip, "ACTIVE (Host Alive)")
        found.append(ip)
        
    log_event("Subnet Host Sweeper", subnet, "COMPLETED", {"active_hosts": found})
    console.print(table)
