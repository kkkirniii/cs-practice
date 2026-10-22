def parse_event(line):
    parts = line.split(' ', 2)
    if len(parts) != 3:
        raise ValueError
    for i in range(3):
        if parts[i] == '':
            raise ValueError
    if parts[1] not in ['DEBUG', 'INFO', 'WARNING', 'ERROR']:
        raise ValueError
    return {'time': parts[0],'level': parts[1],'message': parts[2]}
