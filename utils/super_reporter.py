import json
import os
from datetime import datetime

def build_cyberpunk_report(target, scan_data, ai_insights):
    os.makedirs("reports", exist_ok=True)
    filename = f"reports/cyberos_v9_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CyberOS Matrix Audit - {target}</title>
    <style>
        :root {{ --bg: #030712; --card: #0b1329; --primary: #06b6d4; --danger: #ef4444; --text: #f3f4f6; }}
        body {{ background: var(--bg); color: var(--text); font-family: 'Courier New', monospace; padding: 20px; }}
        .container {{ max-width: 1000px; margin: 0 auto; }}
        .header {{ border: 1px solid var(--primary); padding: 20px; background: var(--card); border-radius: 8px; box-shadow: 0 0 15px rgba(6, 182, 212, 0.2); }}
        h1 {{ color: var(--primary); margin: 0; font-size: 24px; text-transform: uppercase; }}
        .badge {{ background: var(--danger); color: white; padding: 4px 8px; border-radius: 4px; font-weight: bold; }}
        .grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 20px; }}
        .card {{ background: var(--card); border: 1px solid #1e293b; padding: 15px; border-radius: 8px; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
        th, td {{ border: 1px solid #1e293b; padding: 8px; text-align: left; }}
        th {{ background: #0f172a; color: var(--primary); }}
        pre {{ background: #020617; padding: 10px; color: #a7f3d0; border-radius: 4px; overflow-x: auto; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🛡️ CyberOS Enterprise Matrix Report</h1>
            <p>TARGET: <strong>{target}</strong> | TIMESTAMP: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p>SECURITY THREAT STATUS: <span class="badge">{ai_insights.get('risk_level', 'CRITICAL')}</span></p>
        </div>
        <div class="grid">
            <div class="card">
                <h3>🔍 Discovered Network Surface</h3>
                <table>
                    <tr><th>Port/Service</th><th>State</th><th>Threat Info</th></tr>
                    {"".join([f"<tr><td>{r['port']}/{r['service']}</td><td style='color:#22c55e'>{r['status']}</td><td>{r['threat']}</td></tr>" for r in scan_data])}
                </table>
            </div>
            <div class="card">
                <h3>🤖 AI Threat Vector Analysis</h3>
                <p><strong>Estimated CVSS Score:</strong> {ai_insights.get('cvss', '8.9')}</p>
                <p><strong>Predicted Vector:</strong> {ai_insights.get('vector', 'Perimeter Attack')}</p>
                <h4>Remediation Steps:</h4>
                <pre>{json.dumps(ai_insights.get('remediation', []), indent=2)}</pre>
            </div>
        </div>
    </div>
</body>
</html>"""
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
        
    return filename
