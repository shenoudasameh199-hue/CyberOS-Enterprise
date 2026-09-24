import asyncio
import random
import time
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

console = Console()

class CyberOSMatrixEngine:
    def __init__(self, target):
        self.target = target
        self.results = []

    def generate_radar_table(self, current_port, status, threat_level):
        table = Table(title=f"[bold green]⚡ CyberOS Matrix Stream :: Target [{self.target}][/bold green]", show_header=True)
        table.add_column("Port/Service", style="cyan", justify="center")
        table.add_column("State", style="bold white", justify="center")
        table.add_column("Protocol", style="magenta")
        table.add_column("Threat Vectors", style="yellow")
        
        for res in self.results:
            color = "green" if res['status'] == "OPEN" else "red"
            table.add_row(f"{res['port']}/{res['service']}", f"[{color}]{res['status']}[/{color}]", res['proto'], res['threat'])
            
        if current_port:
            table.add_row(f"[bold yellow]{current_port}/SCANNING[/bold yellow]", "[blue]TESTING[/blue]", "TCP", f"[dim]{threat_level}[/dim]")
            
        return table

    async def execute_advanced_radar(self):
        ports_to_scan = [
            (21, "FTP", "High (Anonymous Auth)"),
            (22, "SSH", "Medium (Brute-Force Risk)"),
            (80, "HTTP", "Low (Web Interface)"),
            (443, "HTTPS", "Low (TLS Encrypted)"),
            (445, "SMB", "CRITICAL (EternalBlue/Ransomware)"),
            (3389, "RDP", "HIGH (Remote Exploitation)")
        ]
        
        with Live(self.generate_radar_table(None, None, None), refresh_per_second=12) as live:
            for port, service, threat in ports_to_scan:
                await asyncio.sleep(0.4)
                status = "OPEN" if random.choice([True, False]) else "CLOSED"
                if status == "OPEN":
                    self.results.append({
                        "port": port,
                        "service": service,
                        "status": status,
                        "proto": "TCP",
                        "threat": threat
                    })
                live.update(self.generate_radar_table(port, status, threat))
                
        return self.results
