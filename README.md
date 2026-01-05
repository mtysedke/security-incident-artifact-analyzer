# **Security Incident Artifact Analyzer**

A lightweight DFIR tool for analyzing common incident artifacts such as registry keys, browser history, Sysmon logs, and network traces to support rapid triage and investigation.

---

## Overview

Security Incident Artifact Analyzer is a modular and extensible tool designed to help analysts quickly extract, parse, and interpret digital evidence during incident response.  
It focuses on **speed**, **clarity**, and **practical use cases** commonly encountered in real-world investigations.

---

## Features

- **Registry Analysis**  
  Extracts Run keys, MRU lists, USB artifacts, and persistence indicators.

- **Browser History Parsing**  
  Supports Chrome/Edge/Firefox history, downloads, and session data.

- **Sysmon Log Processing**  
  Identifies suspicious process creation, network events, and file modifications.

- **Network Artifact Inspection**  
  Parses active connections, suspicious IPs, and basic enrichment.

- **Report Generation**  
  Outputs results in JSON or Markdown for easy sharing and documentation.

---

## Project Structure

```
security-ıncident-artifact-analyzer/
 ├─ parsers/
 │   ├─ registry_parser.py
 │   ├─ browser_history.py
 │   ├─ sysmon_parser.py
 │   └─ network_parser.py
 ├─ core/
 │   ├─ analyzer.py
 │   └─ report.py
 ├─ README.md
 ├─ LICENSE
 └─ requirements.txt
```

---

## Getting Started

### **1. Clone the repository**
```bash
git clone https://github.com/secwexen/security-ıncident-artifact-analyzer
cd security-ıncident-artifact-analyzer
```

### **2. Install dependencies**
```bash
pip install -r requirements.txt
```

### **3. Run the analyzer**
```bash
python analyzer.py --input path/to/artifacts/
```

---

## Use Cases

- Rapid triage during security incidents  
- SOC/DFIR investigations  
- Malware analysis support  
- Threat hunting  
- Training and lab environments  

---

## License

Apache-2.0 License
