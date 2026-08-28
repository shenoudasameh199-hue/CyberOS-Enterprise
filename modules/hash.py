import hashlib
from rich.console import Console
def hash_string(text):
    h = hashlib.sha256(text.encode()).hexdigest()
    Console().print(f"[green]SHA-256: {h}[/green]")
def hash_file(path): pass
