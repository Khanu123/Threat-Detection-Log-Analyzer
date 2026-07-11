# Threat Detection Log Analyzer

A Python blue-team project that analyzes authentication logs and identifies suspicious login behavior such as brute-force attempts and repeated failed logins.

## Overview

This project demonstrates defensive security engineering: parsing logs, identifying patterns, classifying severity, and producing analyst-friendly output. It is designed as a portfolio project for cybersecurity, SOC analyst, and junior detection-engineering roles.

## Features

- Parses sample authentication logs.
- Detects repeated failed login attempts.
- Identifies suspicious source IP addresses.
- Tracks targeted usernames.
- Classifies alert severity.
- Generates readable security reports.
- Uses Rich for improved terminal output.

## Example Finding

```text
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
  analyzer.py
  requirements.txt
  sample_logs/
  reports/
  screenshots/
```

## Skills Demonstrated

- Python log parsing
- Detection logic
- Alert severity classification
- Security reporting
- SOC-style investigation thinking

## Roadmap

- Add JSON and HTML report export.
- Add MITRE ATT&CK mapping.
- Add unit tests for detection rules.
- Support Windows Event Logs and web access logs.
- Add alert deduplication and time-window correlation.

## Responsible Use

This project is intended for defensive cybersecurity learning and authorized log analysis only.

## Employer Review

| Area | Evidence |
| --- | --- |
| Role relevance | SOC Analyst / Blue Team / Detection Engineering |
| Main security lesson | Repeated authentication failures can be grouped, scored, and reported for analyst review |
| Defensive value | Shows log parsing, severity classification, sample logs, and analyst-friendly output |
| Safe scope | Uses provided sample logs and defensive detection logic only |

## Professional Upgrade Path

- Add time-window correlation so alerts are based on realistic event timing.
- Add MITRE ATT&CK references for brute-force and valid-account activity.
- Add unit tests for each detection rule.
- Export findings to Markdown, JSON, and CSV.
- Add false-positive notes for shared workstations, service accounts, and misconfigured clients.

## Interview Talking Points

- How raw logs become SOC alerts.
- Why repeated failures alone are not always malicious.
- What evidence should be collected before escalation.
- How this project relates to the newer Splunk and Sentinel labs.
