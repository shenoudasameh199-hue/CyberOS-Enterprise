import platform, socket, os
from rich.console import Console
from rich.table import Table
console = Console()
def get_system_info():
    table = Table(title="💻 CyberOS Apex v5 System Core", header_style="bold red")
    table.add_column("Metric", style="green")
    table.add_column("Status", style="yellow")
    table.add_row("Operating System", f"{platform.system()} {platform.release()}")
    table.add_row("Architecture", platform.machine())
    table.add_row("Python Engine", platform.python_version())
    table.add_row("Hostname", socket.gethostname())
    console.print(table)
