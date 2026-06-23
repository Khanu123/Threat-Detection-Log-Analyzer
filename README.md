# Threat Detection Log Analyzer

A Python-based cybersecurity tool that analyzes authentication logs and detects suspicious activity such as brute-force attacks and repeated failed login attempts.

## Features

- Detects failed login attempts
- Identifies suspicious IP addresses
- Tracks targeted usernames
- Classifies threat severity
- Generates security reports
- Terminal dashboard using Rich

## Example Output

```text
[MEDIUM] Possible brute-force attack from 192.168.1.50 (3 failed logins)

[MEDIUM] Possible brute-force attack from 203.0.113.10 (4 failed logins)
```

## Installation

```bash
git clone https://github.com/Khanu123/Threat-Detection-Log-Analyzer.git

cd Threat-Detection-Log-Analyzer

pip install -r requirements.txt
```

## Usage

```bash
python analyzer.py
```

## Project Structure

```text
Threat-Detection-Log-Analyzer/
├── analyzer.py
├── README.md
├── requirements.txt
├── sample_logs/
├── reports/
└── screenshots/
```

## Disclaimer

This project is intended for educational and defensive cybersecurity purposes only.
