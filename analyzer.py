import re
from collections import Counter
from pathlib import Path

from rich.console import Console
from rich.table import Table


console = Console()
LOG_FILE = Path("sample_logs/auth.log")
REPORT_FILE = Path("reports/report.txt")
FAILED_LOGIN_PATTERN = re.compile(
    r"Failed password for (?:invalid user )?([\w.-]+) from ([\d.]+)"
)


def parse_failed_logins(lines):
    attempts = []
    for line in lines:
        match = FAILED_LOGIN_PATTERN.search(line)
        if match:
            username, ip = match.groups()
            attempts.append({"username": username, "ip": ip})
    return attempts


def severity_for_count(count):
    if count >= 5:
        return "HIGH"
    if count >= 3:
        return "MEDIUM"
    return "LOW"


def build_alerts(failed_attempts, threshold=3):
    ip_counter = Counter(attempt["ip"] for attempt in failed_attempts)
    alerts = []
    for ip, count in ip_counter.items():
        if count >= threshold:
            severity = severity_for_count(count)
            alerts.append(
                f"[{severity}] Possible brute-force attack from "
                f"{ip} ({count} failed logins)"
            )
    return alerts


def render_counter_table(title, first_column, counter):
    table = Table(title=title)
    table.add_column(first_column)
    table.add_column("Attempts")
    for item, count in counter.items():
        table.add_row(item, str(count))
    return table


def write_report(report_file, alerts):
    report_file.parent.mkdir(parents=True, exist_ok=True)
    with open(report_file, "w", encoding="utf-8") as report:
        report.write("Threat Detection Report\n")
        report.write("======================\n\n")
        for alert in alerts:
            report.write(alert + "\n")


def analyze_log_file(log_file=LOG_FILE, report_file=REPORT_FILE):
    with open(log_file, "r", encoding="utf-8") as file:
        failed_attempts = parse_failed_logins(file.readlines())

    ip_counter = Counter(attempt["ip"] for attempt in failed_attempts)
    user_counter = Counter(attempt["username"] for attempt in failed_attempts)
    alerts = build_alerts(failed_attempts)
    write_report(report_file, alerts)
    return ip_counter, user_counter, alerts


def main():
    ip_counter, user_counter, alerts = analyze_log_file()
    console.print("\n[bold cyan]Threat Detection Log Analyzer[/bold cyan]\n")
    console.print(render_counter_table("Failed Login Attempts by IP", "IP Address", ip_counter))
    console.print(render_counter_table("Targeted Usernames", "Username", user_counter))
    console.print("\n[bold red]Threat Alerts[/bold red]\n")
    for alert in alerts:
        console.print(alert)
    console.print(f"\n[green]Report saved to {REPORT_FILE}[/green]")


if __name__ == "__main__":
    main()
