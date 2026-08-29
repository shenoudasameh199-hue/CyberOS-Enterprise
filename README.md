# 🛡️ CyberOS v8 Command Center (Enterprise Edition)

![DevSecOps Pipeline](https://github.com/shenoudasameh199-hue/CyberOS-Enterprise/actions/workflows/main.yml/badge.svg)
![Release](https://img.shields.io/github/v/release/shenoudasameh199-hue/CyberOS-Enterprise?color=red)
![License](https://img.shields.io/github/license/shenoudasameh199-hue/CyberOS-Enterprise)

**CyberOS v8** هي منصة متكاملة للأمن السيبراني، فحص الشبكات، التحليل الجنائي، وتقييم الثغرات بالذكاء الاصطناعي، مصممة خصيصاً لبيئات **Termux** و **Linux**.

---

## 🛠️ v8 Enterprise Modules

| ID | Module Name | Description & Capabilities |
| :-: | :--- | :--- |
| **1** | **System Intelligence** | Monitor hardware, OS metrics, and device resources. |
| **2** | **Advanced Port Scanner** | Fast multi-threaded TCP port scanning & IP resolution. |
| **3** | **Subnet Host Sweeper** | Discover active devices & hosts on local network ranges. |
| **4** | **OSINT Digital Footprint** | Reconnaissance for usernames across online platforms. |
| **5** | **AI Vulnerability Assessment** | Evaluate target risk levels and perimeter security. |
| **6** | **Web Directory Fuzzer** | Scan target URLs for hidden paths, admin panels, & configs. |
| **7** | **Cyber Password Generator** | Generate high-entropy cryptographic passkeys. |
| **8** | **Terminal QR Tools** | Generate instantaneous QR codes in terminal output. |
| **9** | **Audit Logs Viewer** | Inspect historical security scans stored in SQLite DB. |
| **10** | **Export Enterprise Reports** | Save session logs as HTML & JSON intelligence reports. |

---

## ⚙️ DevSecOps & Security Pipeline

تعتمد المنصة على خط أتمتة أمني يعمل في الخلفية عبر **GitHub Actions**:
* **Bandit (SAST):** الفحص التلقائي للكود البرمجي لموديلات v8.
* **Checkov (IaC Scan):** تدقيق ملفات البنية التحتية لحاوية العمل.
* **Automated Tagging:** توليد إصدرا ت أوتوماتيكية تعتمد النمط (`v8.0.x`).

---

## 🚀 Quick Start (Termux / Linux)

```bash
# Clone repository
git clone [https://github.com/shenoudasameh199-hue/CyberOS-Enterprise.git](https://github.com/shenoudasameh199-hue/CyberOS-Enterprise.git)
cd CyberOS-Enterprise

# Install dependencies
pip install -r requirements.txt

# Run Command Center
python main.py
