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