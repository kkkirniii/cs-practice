def parse_event(line):
    parts = line.split(' ', 2)
    if len(parts) != 3:
        raise ValueError
    for i in range(3):
        if parts[i].strip() == '':
            raise ValueError
    if parts[1] not in ['DEBUG', 'INFO', 'WARNING', 'ERROR']:
        raise ValueError
    return {'time': parts[0],'level': parts[1],'message': parts[2]}

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
