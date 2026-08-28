import platform, socket, os
from rich.console import Console
from rich.table import Table
console = Console()

def get_system_info():
    table = Table(title="[bold red]CyberOS Elite - System Intelligence[/bold red]", header_style="bold cyan", border_style="bright_red")
    table.add_column("System Metric", style="green")
    table.add_column("Value / Status", style="yellow")
    table.add_row("Operating System", f"{platform.system()} {platform.release()}")
    table.add_row("Architecture", platform.machine())
    table.add_row("Python Version", platform.python_version())
    table.add_row("Hostname", socket.gethostname())
    table.add_row("Working Directory", os.getcwd())
    console.print(table)
