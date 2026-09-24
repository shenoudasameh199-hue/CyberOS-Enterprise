import qrcode
from rich.console import Console
from core.database import log_event

console = Console()

def run():
    console.print("\n[bold cyan]=== Terminal QR Generator ===[/bold cyan]")
    data = console.input("[bold yellow]Enter Text or URL to convert to QR: [/bold yellow]") or "https://github.com"
    
    qr = qrcode.QRCode()
    qr.add_data(data)
    qr.make(fit=True)
    
    console.print("\n[bold green]Generated QR Code:[/bold green]\n")
    qr.print_ascii(invert=True)
    
    log_event("Terminal QR", data, "SUCCESS", None)
