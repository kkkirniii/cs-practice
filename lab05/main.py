from pathlib import Path

from logstats import count_levels, top_errors, format_report

BASE_DIR = Path(__file__).resolve().parent

filename = input().strip()
log_path = BASE_DIR / filename

with open(log_path, encoding='utf-8') as log:
    counts = count_levels(log)

with open(log_path, encoding='utf-8') as log:
    errors = top_errors(log, 3)

total = sum(counts.values())
error_count = counts.get('ERROR', 0)
broken_count = counts.get('BROKEN', 0)

print(total)
print(error_count)
print(broken_count)

report = format_report(counts, errors)

report_path = BASE_DIR / 'report.txt'
with open(report_path, 'w', encoding='utf-8') as file:
    file.write(report)