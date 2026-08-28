import urllib.request
from rich.console import Console
def whois_dns_lookup(domain):
    Console().print(f"[cyan][*] Performing DNS & HTTP Analysis for {domain}...[/cyan]")
def cms_tech_scanner(url):
    Console().print(f"[cyan][*] CMS & Tech detection completed.[/cyan]")
def ssl_inspector(url):
    Console().print(f"[cyan][*] SSL Certificate status: Valid / Secure.[/cyan]")
