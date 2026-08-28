import urllib.request
import os
from rich.console import Console
from core.database import log_action

def web_dir_busting(target_url):
    console = Console()
    if not target_url.startswith("http"):
        target_url = "https://" + target_url
    
    wordlist_file = "wordlist.txt"
    if not os.path.exists(wordlist_file):
        default_paths = ["admin", "login", "dashboard", "api", "uploads", "config.json", ".env", "robots.txt", "sitemap.xml", "backup.zip", "panel", "root"]
        with open(wordlist_file, "w") as f:
            f.write("\n".join(default_paths))
    
    with open(wordlist_file, "r") as f:
        paths = [line.strip() for line in f if line.strip()]

    console.log(f"[cyan][*] Fuzzing {target_url} using {len(paths)} payloads...[/cyan]\n")
    
    for path in paths:
        url = f"{target_url.rstrip('/')}/{path}"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "CyberOS-Enterprise-Fuzzer"})
            with urllib.request.urlopen(req, timeout=3) as res:
                console.print(f" [bold green]✔ FOUND ({res.getcode()}): {url}[/bold green]")
        except urllib.error.HTTPError as e:
            if e.code == 403:
                console.print(f" [yellow]! FORBIDDEN (403): {url}[/yellow]")
        except:
            pass
            
    console.log(f"\n[bold green][+] Web directory fuzzing completed.[/bold green]")
    log_action("WebFuzzer", target_url, "COMPLETED")
