import os
import json
from datetime import datetime

def generate_html_report(module_name, target, results):
    os.makedirs("reports", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/report_{timestamp}.html"
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CyberOS Security Report - {module_name}</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0f172a; color: #f8fafc; padding: 20px; }}
        .card {{ background-color: #1e293b; border-radius: 8px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); margin-bottom: 20px; }}
        h1 {{ color: #38bdf8; border-bottom: 2px solid #334155; padding-bottom: 10px; }}
        .status {{ color: #22c55e; font-weight: bold; }}
        pre {{ background-color: #020617; padding: 15px; border-radius: 5px; color: #a855f7; overflow-x: auto; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>🛡️ CyberOS v8 Security Audit Report</h1>
        <p><strong>Module:</strong> {module_name}</p>
        <p><strong>Target:</strong> {target}</p>
        <p><strong>Timestamp:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        <p><strong>Status:</strong> <span class="status">COMPLETED</span></p>
    </div>
    <div class="card">
        <h2>Scan Results & Analytics</h2>
        <pre>{json.dumps(results, indent=4)}</pre>
    </div>
</body>
</html>"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    return filename
