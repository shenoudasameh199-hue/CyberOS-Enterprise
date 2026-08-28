import socket
from concurrent.futures import ThreadPoolExecutor
from rich.console import Console
from core.database import log_action
console = Console()

def ip_lookup(target):
    try:
        ip = socket.gethostbyname(target)
        console.print(f"[bold green][+] Resolved IP for {target}: {ip}[/bold green]")
        log_action("Network-IPLookup", target, "SUCCESS")
        return ip
    except socket.gaierror:
        console.print(f"[bold red][-] Error: Could not resolve {target}[/bold red]")
        log_action("Network-IPLookup", target, "FAILED")
        return None

def port_scanner(target, start_port=1, end_port=100):
    ip = ip_lookup(target)
    if not ip: return
    console.print(f"[bold cyan][*] Running v5 Multi-Threaded Port Scanner on {ip}...[/bold cyan]")
    
    def scan(p):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.4)
            if s.connect_ex((ip, p)) == 0:
                try: serv = socket.getservbyport(p, 'tcp')
                except: serv = "unknown"
                console.print(f" [bold green]✔ Port {p} ({serv}) -> OPEN[/bold green]")
            s.close()
        except: pass

    with ThreadPoolExecutor(max_workers=60) as ex:
        ex.map(scan, range(start_port, end_port + 1))
    log_action("PortScanner", target, "COMPLETED")
