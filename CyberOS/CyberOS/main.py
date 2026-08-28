import os
import sys
import time
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.progress import track

from core.database import init_db
from modules.system import get_system_info
from modules.network import ip_lookup, port_scanner
from modules.osint import username_recon
from modules.vuln import assess_risk
from modules.password import generate_password
from modules.qr import generate_terminal_qr

init_db()
console = Console(record=True)

def show_splash():
    console.clear()
    banner = r"""
   ██████╗██╗   ██╗██████╗ ███████╗██████╗  ██████╗ ███████╗
  ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔════╝
  ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝██║   ██║███████╗
  ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗██║   ██║╚════██║
  ╚██████╗   ██║   ██████╔╝███████╗██║  ██║╚██████╔╝███████║
   ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
                 [ ELITE FRAMEWORK v6.0 ]
    """
    console.print(f"[bold red]{banner}[/bold red]")
    console.print("[bold yellow]⚡ INITIALIZING CYBEROS ELITE CORE MODULES...[/bold yellow]\n")
    for _ in track(range(10), description="[bold green]Loading Framework Components...[/bold green]"):
        time.sleep(0.02)
    console.clear()

def display_dashboard():
    status_text = (
        f"[bold green]STATUS:[/bold green] ONLINE  |  "
        f"[bold cyan]DATABASE:[/bold cyan] SQLITE ACTIVE  |  "
        f"[bold red]EDITION:[/bold red] ELITE v6.0"
    )
    console.print(Panel(status_text, title="[bold white]🛡️ CyberOS Elite Operations Center[/bold white]", border_style="bright_red", expand=True))

def display_menu():
    table = Table(show_header=True, header_style="bold magenta", border_style="bright_red", expand=True)
    table.add_column("ID", style="bold cyan", justify="center", width=6)
    table.add_column("Elite Security Module", style="bold green")
    table.add_column("Description & Capabilities", style="dim white")

    table.add_row("1", "System Intelligence", "Monitor hardware, OS metrics, and device resources")
    table.add_row("2", "Advanced Port Scanner", "Fast multi-threaded TCP port scanning & IP resolution")
    table.add_row("3", "OSINT Digital Footprint", "Reconnaissance for usernames across online platforms")
    table.add_row("4", "AI Vulnerability Assessment", "Evaluate target risk levels and perimeter security")
    table.add_row("5", "Cyber Password Generator", "Generate high-entropy cryptographic passkeys")
    table.add_row("6", "Terminal QR Tools", "Generate instantaneous QR codes in terminal output")
    table.add_row("7", "Session HTML Reports", "Export complete active session logs to HTML")
    table.add_row("0", "Exit Framework", "Safely close session and exit CyberOS Elite")

    console.print(table)

def main():
    show_splash()
    while True:
        console.clear()
        display_dashboard()
        display_menu()

        choice = Prompt.ask("\n[bold red]CyberOS Elite[/bold red] > [bold yellow]Select Command Option[/bold yellow]", choices=[str(i) for i in range(8)])

        if choice == "1":
            console.clear()
            get_system_info()
            Prompt.ask("\n[bold cyan]Press Enter to return to main menu...[/bold cyan]")
        elif choice == "2":
            console.clear()
            target = Prompt.ask("Enter target IP address or domain name")
            port_scanner(target, 1, 100)
            Prompt.ask("\n[bold cyan]Press Enter to return to main menu...[/bold cyan]")
        elif choice == "3":
            console.clear()
            username = Prompt.ask("Enter target username for OSINT reconnaissance")
            username_recon(username)
            Prompt.ask("\n[bold cyan]Press Enter to return to main menu...[/bold cyan]")
        elif choice == "4":
            console.clear()
            target = Prompt.ask("Enter target for AI vulnerability assessment")
            assess_risk(target)
            Prompt.ask("\n[bold cyan]Press Enter to return to main menu...[/bold cyan]")
        elif choice == "5":
            console.clear()
            pwd = generate_password(24)
            console.print(f"\n[bold green]🔑 Generated Cryptographic Password:[/bold green] [bold yellow]{pwd}[/bold yellow]")
            Prompt.ask("\n[bold cyan]Press Enter to return to main menu...[/bold cyan]")
        elif choice == "6":
            console.clear()
            data = Prompt.ask("Enter text or URL to encode into QR")
            generate_terminal_qr(data)
            Prompt.ask("\n[bold cyan]Press Enter to return to main menu...[/bold cyan]")
        elif choice == "7":
            console.clear()
            os.makedirs("reports", exist_ok=True)
            rep_path = f"reports/cyberos_elite_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
            console.save_html(rep_path)
            console.print(f"[bold green]📄 Elite Session Report successfully exported to: {rep_path}[/bold green]")
            Prompt.ask("\n[bold cyan]Press Enter to return to main menu...[/bold cyan]")
        elif choice == "0":
            console.print("\n[bold red][-] Shutting down CyberOS Elite Framework. Stay secure![/bold red]")
            sys.exit(0)

if __name__ == "__main__":
    main()
