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

def average_by_city(records: list[dict]):
    total = {}
    count = {}
    for record in records:
        temp = record['temperature']
        city = record['city']
        total[city] = total.get(city, 0) + temp
        count[city] = count.get(city, 0) + 1
    averages = {}
    for city in total:
        averages[city] = round(total[city] / count[city], 1)
    return averages

def warmest_city(records:list[dict]):
    average = average_by_city(records)
    mx = -float('inf')
    name = ''
    for city in average:
        if average[city] > mx:
            mx = average[city]
            name = city
        elif average[city] == mx:
            if city < name:
                name = city
    return name
