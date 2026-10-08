def parse_record(line: str):
    words = line.split(';')

    if len(words)!=3:
        raise ValueError('Негодная строка. Должно быть ровно 3 разделителя.')
    if not(words[0]) or not(words[2]):
        raise ValueError('Негодная строка. Поля города или даты пустые.')
    try:
        temp = float(words[1])
    except ValueError:
        raise ValueError('Негодная строка. Температура должна быть числом.')
    dict = {
        'city': words[0],
        'temperature': temp,
        'date': words[2],
    }
    return dict

def read_valid(lines: list[str]):
    l = []
    for line in lines:
        if not(line.strip()):
            continue
        try:
            l.append(parse_record(line))
        except ValueError:
            pass
    return l
