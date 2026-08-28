import socket
from rich.console import Console
def subdomain_enum(domain):
    console = Console()
    console.print(f"[cyan][*] Checking common subdomains for {domain}...[/cyan]")
    common = ["www", "mail", "ftp", "test", "admin", "api", "shop"]
    for sub in common:
        sub_domain = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(sub_domain)
            console.print(f" [green]✔ Found: {sub_domain} ({ip})[/green]")
        except: pass
def dir_buster(url): pass
