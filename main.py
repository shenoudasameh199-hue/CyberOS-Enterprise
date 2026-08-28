import os
import sys
import json
import time
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.progress import track

from core.database import init_db, show_audit_logs
from modules.system import get_system_info
from modules.network import ip_lookup, port_scanner
from modules.osint import username_recon
from modules.vuln import assess_risk
from modules.password import generate_password
from modules.qr import generate_terminal_qr
from modules.fuzzer import web_dir_busting
from modules.sweeper import local_subnet_sweep

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
             [ ENTERPRISE OPERATIONS v8.0 ]
    """
    console.print(f"[bold red]{banner}[/bold red]")
    console.print("[bold yellow]⚡ BOOTING ENTERPRISE THREAT & AUTOMATION ENGINES...[/bold yellow]\n")
    for _ in track(range(10), description="[bold green]Loading v8.0 Framework...[/bold green]"):
        time.sleep(0.02)
    console.clear()

def display_dashboard():
    status_text = (
        f"[bold green]STATUS:[/bold green] ONLINE  |  "
        f"[bold cyan]SEC-OPS:[/bold cyan] ACTIVE  |  "
        f"[bold red]EDITION:[/bold red] v8.0 ENTERPRISE"
    )
    console.print(Panel(status_text, title="[bold white]🛡️ CyberOS v8 Command Center[/bold white]", border_style="bright_red", expand=True))

def display_menu():
    table = Table(show_header=True, header_style="bold magenta", border_style="bright_red", expand=True)
    table.add_column("ID", style="bold cyan", justify="center", width=6)
    table.add_column("v8 Enterprise Module", style="bold green")
    table.add_column("Description & Capabilities", style="dim white")

    table.add_row("1", "System Intelligence", "Monitor hardware, OS metrics, and device resources")
    table.add_row("2", "Advanced Port Scanner", "Fast multi-threaded TCP port scanning & IP resolution")
    table.add_row("3", "Subnet Host Sweeper", "Discover active devices & hosts on local network ranges")
    table.add_row("4", "OSINT Digital Footprint", "Reconnaissance for usernames across online platforms")
    table.add_row("5", "AI Vulnerability Assessment", "Evaluate target risk levels and perimeter security")
    table.add_row("6", "Web Directory Fuzzer", "Scan target URLs for hidden paths, admin panels, & configs")
    table.add_row("7", "Cyber Password Generator", "Generate high-entropy cryptographic passkeys")
    table.add_row("8", "Terminal QR Tools", "Generate instantaneous QR codes in terminal output")
    table.add_row("9", "Audit Logs Viewer", "Inspect historical security scans stored in SQLite DB")
    table.add_row("10", "Export Enterprise Reports", "Save session logs as HTML & JSON intelligence reports")
    table.add_row("0", "Exit Framework", "Safely close session and exit CyberOS v8")

    console.print(table)

def main():
    show_splash()
    while True:
        console.clear()
        display_dashboard()
        display_menu()

        choice = Prompt.ask("\n[bold red]CyberOS v8[/bold red] > [bold yellow]Select Command Option[/bold yellow]", choices=[str(i) for i in range(11)])

        if choice == "1":
            console.clear()
            get_system_info()
            Prompt.ask("\n[bold cyan]Press Enter to return...[/bold cyan]")
        elif choice == "2":
            console.clear()
            target = Prompt.ask("Enter target IP address or domain name")
            port_scanner(target, 1, 100)
            Prompt.ask("\n[bold cyan]Press Enter to return...[/bold cyan]")
        elif choice == "3":
            console.clear()
            subnet = Prompt.ask("Enter local network base prefix (e.g., 192.168.1)")
            local_subnet_sweep(subnet)
            Prompt.ask("\n[bold cyan]Press Enter to return...[/bold cyan]")
        elif choice == "4":
            console.clear()
            username = Prompt.ask("Enter target username for OSINT reconnaissance")
            username_recon(username)
            Prompt.ask("\n[bold cyan]Press Enter to return...[/bold cyan]")
        elif choice == "5":
            console.clear()
            target = Prompt.ask("Enter target for AI vulnerability assessment")
            assess_risk(target)
            Prompt.ask("\n[bold cyan]Press Enter to return...[/bold cyan]")
        elif choice == "6":
            console.clear()
            url = Prompt.ask("Enter target web URL (e.g. example.com)")
            web_dir_busting(url)
            Prompt.ask("\n[bold cyan]Press Enter to return...[/bold cyan]")
        elif choice == "7":
            console.clear()
            pwd = generate_password(24)
            console.print(f"\n[bold green]🔑 Generated Cryptographic Password:[/bold green] [bold yellow]{pwd}[/bold yellow]")
            Prompt.ask("\n[bold cyan]Press Enter to return...[/bold cyan]")
        elif choice == "8":
            console.clear()
            data = Prompt.ask("Enter text or URL to encode into QR")
            generate_terminal_qr(data)
            Prompt.ask("\n[bold cyan]Press Enter to return...[/bold cyan]")
        elif choice == "9":
            console.clear()
            show_audit_logs()
            Prompt.ask("\n[bold cyan]Press Enter to return...[/bold cyan]")
        elif choice == "10":
            console.clear()
            os.makedirs("reports", exist_ok=True)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            html_path = f"reports/cyberos_v8_{timestamp}.html"
            json_path = f"reports/cyberos_v8_{timestamp}.json"
            
            console.save_html(html_path)
            
            # Export basic json metadata
            meta = {"version": "8.0", "timestamp": timestamp, "status": "SECURE_OPERATION"}
            with open(json_path, "w") as jf:
                json.dump(meta, jf, indent=4)
                
            console.print(f"[bold green]📄 Enterprise Reports Exported Successfully:[/bold green]")
            console.print(f" - HTML: {html_path}")
            console.print(f" - JSON: {json_path}")
            Prompt.ask("\n[bold cyan]Press Enter to return...[/bold cyan]")
        elif choice == "0":
            console.print("\n[bold red][-] Shutting down CyberOS v8 Enterprise. Stay secure![/bold red]")
            sys.exit(0)

if __name__ == "__main__":
    main()
