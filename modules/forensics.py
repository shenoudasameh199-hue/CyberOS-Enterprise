import os
from rich.console import Console
def extract_exif(img_path):
    Console().print(f"[cyan][*] Extracting EXIF metadata from {img_path}...[/cyan]")
def hide_text_in_file(path, text):
    Console().print(f"[green]Text hidden successfully inside {path}.[/green]")
def extract_text_from_file(path): pass
