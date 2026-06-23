import re
from collections import Counter
from pathlib import Path
from rich.console import Console
from rich.table import Table

console = Console()

LOG_FILE = Path("sample_logs/auth.log")
REPORT_FILE = Path("reports/report.txt")

failed_attempts = []

pattern = re.compile(
    r"Failed password for (?:invalid user )?(\w+) from ([\d.]+)"
)

with open(LOG_FILE, "r") as file:
    logs = file.readlines()

for line in logs:
    match = pattern.search(line)

    if match:
        username, ip = match.groups()

        failed_attempts.append(
            {
                "username": username,
                "ip": ip
            }
        )

ip_counter = Counter(
    attempt["ip"]
    for attempt in failed_attempts
)

user_counter = Counter(
    attempt["username"]
    for attempt in failed_attempts
)

console.print("\n[bold cyan]Threat Detection Log Analyzer[/bold cyan]\n")

ip_table = Table(title="Failed Login Attempts by IP")

ip_table.add_column("IP Address")
ip_table.add_column("Attempts")

for ip, count in ip_counter.items():
    ip_table.add_row(ip, str(count))

console.print(ip_table)

user_table = Table(title="Targeted Usernames")

user_table.add_column("Username")
user_table.add_column("Attempts")

for user, count in user_counter.items():
    user_table.add_row(user, str(count))

console.print(user_table)

alerts = []

for ip, count in ip_counter.items():

    if count >= 5:
        severity = "HIGH"

    elif count >= 3:
        severity = "MEDIUM"

    else:
        severity = "LOW"

    if count >= 3:

        alert = (
            f"[{severity}] Possible brute-force attack from "
            f"{ip} ({count} failed logins)"
        )

        alerts.append(alert)

console.print("\n[bold red]Threat Alerts[/bold red]\n")

for alert in alerts:
    console.print(alert)

with open(REPORT_FILE, "w") as report:

    report.write("Threat Detection Report\n")
    report.write("======================\n\n")

    for alert in alerts:
        report.write(alert + "\n")

console.print(
    f"\n[green]Report saved to {REPORT_FILE}[/green]"
)