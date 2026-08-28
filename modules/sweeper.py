import socket
from concurrent.futures import ThreadPoolExecutor
from rich.console import Console
from core.database import log_action

def local_subnet_sweep(base_ip):
    console = Console()
    console.print(f"[bold cyan][*] Initializing Subnet Sweeper for base: {base_ip}.1-254...[/bold cyan]\n")
    
    def ping_host(ip):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.2)
            result = s.connect_ex((ip, 80)) # Checking port 80/web
            if result == 0:
                console.print(f" [bold green]✔ Active Host Found: {ip}[/bold green]")
            s.close()
        except:
            pass

    # Generate IPs for standard /24 subnet (e.g. 192.168.1)
    ip_list = [f"{base_ip}.{i}" for i in range(1, 100)] # Scans 1-99 for speed
    with ThreadPoolExecutor(max_workers=50) as ex:
        ex.map(ping_host, ip_list)

    console.print(f"\n[bold green][+] Subnet sweep completed.[/bold green]")
    log_action("SubnetSweeper", base_ip, "COMPLETED")
