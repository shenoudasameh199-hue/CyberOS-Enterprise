import socket
from concurrent.futures import ThreadPoolExecutor
from rich.console import Console
from core.database import log_action
console = Console()

def ip_lookup(target):
    try:
        ip = socket.gethostbyname(target)
        console.print(f"[bold green][+] Resolved Target IP: {ip}[/bold green]")
        log_action("Network-IPLookup", target, "SUCCESS")
        return ip
    except socket.gaierror:
        console.print(f"[bold red][-] Error: Could not resolve hostname {target}[/bold red]")
        log_action("Network-IPLookup", target, "FAILED")
        return None

def port_scanner(target, start_port=1, end_port=100):
    ip = ip_lookup(target)
    if not ip: return
    console.print(f"[bold cyan][*] Scanning ports ({start_port}-{end_port}) on {ip}...[/bold cyan]\n")
    
    open_ports = 0
    def scan(p):
        nonlocal open_ports
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.3)
            if s.connect_ex((ip, p)) == 0:
                try: serv = socket.getservbyport(p, 'tcp')
                except: serv = "unknown"
                console.print(f" [bold green]✔ Port {p:<5} | Service: {serv:<10} | STATUS: OPEN[/bold green]")
        except: pass

    with ThreadPoolExecutor(max_workers=60) as ex:
        ex.map(scan, range(start_port, end_port + 1))
    
    console.print(f"\n[bold green][+] Port scanning completed successfully.[/bold green]")
    log_action("PortScanner", target, "COMPLETED")
