def parse_event(line: str) -> dict:
    parts = line.strip().split(maxsplit=2)
    if len(parts) != 3:
        raise ValueError
    time, level, message = parts
    if level not in {'DEBUG', 'INFO', 'WARNING', 'ERROR'}:
        raise ValueError
    if not message:
        raise ValueError
    return {
        'time': time,
        'level': level,
        'message': message,
    }

def count_levels(lines):
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            counts['BROKEN'] = counts.get('BROKEN', 0) + 1
            continue
        level = event['level']
        counts[level] = counts.get(level, 0) + 1
    return counts

from collections import Counter

def top_errors(lines, n: int):
    errors = Counter()

    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event['level'] == 'ERROR':
            errors[event['message']] += 1
    return [
        [message, count]
        for message, count in sorted(
            errors.items(),
            key=lambda item: (-item[1], item[0])
        )[:n]
    ]

def format_report(counts: dict, errors: list[list]):
    report = ['Отчёт по журналу', '']
    for level in sorted(counts):
        report.append(f'{level}: {counts[level]}')
    report.extend(['', 'Частые ошибки:'])
    for message, count in errors:
        report.append(f'- {message} — {count}')
    return '\n'.join(report) + '\n'