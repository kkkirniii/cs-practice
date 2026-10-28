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