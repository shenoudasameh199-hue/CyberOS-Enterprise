import os
from rich.console import Console
def show_tree(path="."):
    Console().print(f"[cyan]📁 Files in {path}:[/cyan]")
    for root, dirs, files in os.walk(path):
        if root.count(os.sep) - path.count(os.sep) > 1: continue
        Console().print(f" [bold yellow]{root}[/bold yellow]")
        for f in files[:10]: Console().print(f"   ├── {f}")
        break

def get_dir_size(path): pass
def search_files(name): pass
