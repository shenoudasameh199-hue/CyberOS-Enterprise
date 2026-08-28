import qrcode
from rich.console import Console
def generate_terminal_qr(data):
    qr = qrcode.QRCode()
    qr.add_data(data)
    qr.print_ascii(invert=True)
