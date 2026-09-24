import sys
import time
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt

from core.database import get_logs
from modules import network, osint, password, qr, system, vuln, fuzzer, sweeper, ai_eval

console = Console()

def display_menu():
    console.clear()
    header_text = (
        "[bold cyan]      ██████╗██╗   ██╗██████╗ ███████╗██╗  ██╗███████╗[/bold cyan]\n"
        "[bold cyan]     ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██║  ██║██╔════╝[/bold cyan]\n"
        "[bold green]     ██║      ╚████╔╝ ██████╔╝█████╗  ███████║███████╗[/bold green]\n"
        "[bold green]     ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██║╚════██║[/bold green]\n"
        "[bold white]     ╚██████╗   ██║   ██████╔╝███████╗██║  ██║███████║[/bold white]\n"
        "[bold yellow]      ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝ v9 Enterprise Matrix[/bold yellow]\n"
        "[bold magenta]           DevSecOps Automation Suite | Built by Shenouda[/bold magenta]"
    )
    console.print(Panel(header_text, expand=True, border_style="cyan"))

    table = Table(title="[bold white]⚡ CYBEROS V9 MATRIX MODULES ⚡[/bold white]", show_header=True, header_style="bold magenta")
    table.add_column("ID", style="cyan", justify="center", width=4)
    table.add_column("Module Name", style="bold green", width=28)
    table.add_column("Capabilities", style="white")

    table.add_row("1", "Network Tools", "Basic network utilities and analysis")
    table.add_row("2", "Security Tools", "Port scanning & vulnerability tools")
    table.add_row("3", "Subnet Host Sweeper", "Discover active devices on local subnet")
    table.add_row("4", "OSINT Digital Footprint", "Reconnaissance for usernames across platforms")
    table.add_row("5", "AI Matrix Radar Engine", "Live async scanning & CVSS risk prediction")
    table.add_row("6", "Web Directory Fuzzer", "Scan URLs for hidden paths & admin panels")
    table.add_row("7", "Cyber Password Generator", "Generate high-entropy passkeys")
    table.add_row("8", "Terminal QR Tools", "Generate QR codes in terminal")
    table.add_row("9", "Audit Logs Viewer", "Inspect historical security scans from SQLite")
    table.add_row("0", "Exit Framework", "Safely exit CyberOS Engine")

    console.print(table)

def show_audit_logs():
    console.clear()
    console.print("[bold cyan]=== Historical Audit Logs (SQLite DB) ===[/bold cyan]\n")
    logs = get_logs(15)
    
    table = Table(show_header=True, header_style="bold yellow")
    table.add_column("ID", style="cyan")
    table.add_column("Timestamp", style="white")
    table.add_column("Module", style="green")
    table.add_column("Target", style="magenta")
    table.add_column("Status", style="bold blue")

    for row in logs:
        table.add_row(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]))

    console.print(table)

def main():
    while True:
        display_menu()
        choice = Prompt.ask("\n[bold yellow]CyberOS Shell > Select Module[/bold yellow]", default="5")

        if choice == "1":
            network.run()
        elif choice == "2":
            vuln.run()
        elif choice == "3":
            sweeper.run()
        elif choice == "4":
            osint.run()
        elif choice == "5":
            ai_eval.run()
        elif choice == "6":
            fuzzer.run()
        elif choice == "7":
            password.run()
        elif choice == "8":
            qr.run()
        elif choice == "9":
            show_audit_logs()
        elif choice == "0":
            console.print("[bold red]Deactivating CyberOS Engine... System Shutdown.[/bold red]")
            sys.exit(0)
        else:
            console.print("[bold red]Invalid selection![/bold red]")
            time.sleep(1)

        input("\n[dim]Press Enter to return to CyberOS Matrix Command Center...[/dim]")

if __name__ == "__main__":
    main()
