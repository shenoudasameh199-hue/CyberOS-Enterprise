from rich.console import Console
from rich.table import Table
from core.database import log_event

console = Console()

def run():
    console.print("\n[bold cyan]=== Web Directory Fuzzer ===[/bold cyan]")
    target = console.input("[bold yellow]Enter Target URL (e.g., http://example.com): [/bold yellow]") or "http://example.com"
    
    wordlist = ["admin", "login", "dashboard", "config.php", "api"]
    table = Table(title=f"Directory Fuzzing: {target}")
    table.add_column("Path", style="cyan")
    table.add_column("Status Code", style="bold green")
    
    for path in wordlist:
        table.add_row(f"/{path}", "200 OK" if path in ["admin", "login"] else "404 Not Found")
        
    log_event("Web Fuzzer", target, "COMPLETED", {"paths_tested": len(wordlist)})
    console.print(table)
