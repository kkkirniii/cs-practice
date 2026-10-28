def csv_to_records(text: str) -> list[dict]:
    if not text.strip():
        return []

    lines = text.strip().splitlines()
    headers = [header.strip() for header in lines[0].split(',')]
    records = []

    for line in lines[1:]:
        values = [value.strip() for value in line.split(',')]
        record = dict(zip(headers, values))
        records.append(record)

    return records

def parse_settings(lines: list[str]) -> dict:
    settings = {}
    current_list = None

    for line in lines:
        line = line.split('#', 1)[0].strip()

        if not line:
            continue

        if line.startswith('- ') and current_list is not None:
            current_list.append(line[2:].strip())
            continue

        if ':' not in line:
            continue

        key, value = line.split(':', 1)
        key = key.strip()
        value = value.strip()

        if not value:
            settings[key] = []
            current_list = settings[key]
        else:
            current_list = None

            if value.lower() in ('true', 'yes'):
                settings[key] = True
            elif value.lower() in ('false', 'no'):
                settings[key] = False
            else:
                try:
                    settings[key] = int(value)
                except ValueError:
                    try:
                        settings[key] = float(value.replace(',', '.'))
                    except ValueError:
                        settings[key] = value

    return settings

def merge_by_key(rows: list[dict], extra: dict, key: str = 'id') -> list[dict]:
    result = []

    for row in rows:
        merged = extra.get(str(row.get(key)), {}).copy()
        merged.update(row)
        result.append(merged)

    return result

import json

def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)