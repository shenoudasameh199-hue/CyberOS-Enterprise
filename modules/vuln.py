import socket
from rich.console import Console
from rich.table import Table
from core.database import log_event

console = Console()

def run():
    console.print("\n[bold cyan]=== Security Port Scanner ===[/bold cyan]")
    target = console.input("[bold yellow]Enter Target IP/Domain: [/bold yellow]") or "127.0.0.1"
    
    ports = [21, 22, 80, 443, 8080]
    results = []
    
    table = Table(title=f"Port Scan Results for {target}")
    table.add_column("Port", style="cyan")
    table.add_column("Status", style="bold")
    
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        res = s.connect_ex((target, port))
        status = "OPEN" if res == 0 else "CLOSED"
        color = "green" if status == "OPEN" else "red"
        table.add_row(str(port), f"[{color}]{status}[/{color}]")
        results.append({"port": port, "status": status})
        s.close()
        
    log_event("Security Tools", target, "COMPLETED", results)
    console.print(table)
