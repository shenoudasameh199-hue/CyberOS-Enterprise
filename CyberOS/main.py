import os
import sys
import json
import time
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.progress import track

from core.database import init_db
from modules.system import get_system_info
from modules.network import ip_lookup, port_scanner
from modules.osint import username_recon
from modules.vuln import assess_risk
from modules.password import generate_password
from modules.qr import generate_terminal_qr

init_db()
console = Console(record=True)

def show_splash():
    console.clear()
    banner = r"""
   ██████╗██╗   ██╗██████╗ ███████╗██████╗  ██████╗ ███████╗
  ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔════╝
  ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝██║   ██║███████╗
  ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗██║   ██║╚════██║
  ╚██████╗   ██║   ██████╔╝███████╗██║  ██║╚██████╔╝███████║
   ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
                     [ APEX EDITION v5.0 ]
    """
    console.print(f"[bold red]{banner}[/bold red]")
    console.print("[bold yellow]⚡ LOADING APEX INTELLIGENCE CORE & DATABASES...[/bold yellow]\n")
    for _ in track(range(10), description="[bold green]Booting v5 Modules...[/bold green]"):
        time.sleep(0.02)
    console.clear()

def display_dashboard():
    status_text = (
        f"[bold green]CORE:[/bold green] ONLINE  |  "
        f"[bold cyan]DB ENGINE:[/bold cyan] SQLITE (ACTIVE)  |  "
        f"[bold red]EDITION:[/bold red] APEX v5.0"
    )
    console.print(Panel(status_text, title="[bold white]🛡️ CyberOS v5 Command Center[/bold white]", border_style="bright_red", expand=True))

def display_menu():
    table = Table(show_header=True, header_style="bold magenta", border_style="bright_red", expand=True)
    table.add_column("ID", style="bold cyan", justify="center", width=6)
    table.add_column("الوحدة / v5 Module", style="bold green")
    table.add_column("الوصف / Description", style="dim white")

    table.add_row("1", "💻 معلومات واستكشاف النظام", "فحص موارد الجهاز والبيئة الحية")
    table.add_row("2", "🌐 محرك الشبكة والمنافذ المتقدم", "فحص IP و Port Scanner متعدد المسارات")
    table.add_row("3", "🕵️ استخبارات المستخدمين (OSINT)", "البحث عن الأثر الرقمي للمستخدمين عبر المنصات")
    table.add_row("4", "⚠️ تقييم الثغرات السريع (Vulnerability AI)", "تقدير المخاطر الأمنية للهدف")
    table.add_row("5", "🔑 توليد كلمات السر السيبرانية", "إنشاء مفاتيح مرور معقدة للغاية")
    table.add_row("6", "📱 مولد رموز QR السريعة", "توليد الرموز داخل الطرفية مباشرة")
    table.add_row("7", "📂 مركز التقارير وجلسات العمل", "حفظ وتصدير تقارير HTML تفاعلية")
    table.add_row("0", "❌ خروج (Exit)", "إنهاء الجلسة وإغلاق النظام بأمان")

    console.print(table)

def main():
    show_splash()
    while True:
        console.clear()
        display_dashboard()
        display_menu()

        choice = Prompt.ask("\n[bold red]CyberOS v5[/bold red] > [bold yellow]اختر أمر التشغيل[/bold yellow]", choices=[str(i) for i in range(8)])

        if choice == "1":
            console.clear()
            get_system_info()
            Prompt.ask("\nاضغط Enter للمتابعة...")
        elif choice == "2":
            console.clear()
            t = Prompt.ask("أدخل الهدف للفحص (IP أو Domain)")
            port_scanner(t, 1, 100)
            Prompt.ask("\nاضغط Enter للمتابعة...")
        elif choice == "3":
            console.clear()
            u = Prompt.ask("أدخل اسم المستخدم (Username) للبحث عنه")
            username_recon(u)
            Prompt.ask("\nاضغط Enter للمتابعة...")
        elif choice == "4":
            console.clear()
            t = Prompt.ask("أدخل الهدف لتقييم الثغرات")
            assess_risk(t)
            Prompt.ask("\nاضغط Enter للمتابعة...")
        elif choice == "5":
            console.clear()
            pwd = generate_password(20)
            console.print(f"\n[bold green]🔑 كلمة السر السيبرانية المنشأة:[/bold green] [bold yellow]{pwd}[/bold yellow]")
            Prompt.ask("\nاضغط Enter للمتابعة...")
        elif choice == "6":
            console.clear()
            data = Prompt.ask("أدخل النص أو الرابط للتحويل")
            generate_terminal_qr(data)
            Prompt.ask("\nاضغط Enter للمتابعة...")
        elif choice == "7":
            console.clear()
            os.makedirs("reports", exist_ok=True)
            rep_file = "reports/cyberos_v5_report.html"
            console.save_html(rep_file)
            console.print(f"[bold green]📄 تم حفظ تقرير الجلسة بنجاح في: {rep_file}[/bold green]")
            Prompt.ask("\nاضغط Enter للمتابعة...")
        elif choice == "0":
            console.print("\n[bold red][-] إغلاق جلسة CyberOS v5 Apex. إلى اللقاء![/bold red]")
            sys.exit(0)

if __name__ == "__main__":
    main()
