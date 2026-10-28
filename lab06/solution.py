def count_by_extension(paths: list[str]) -> dict[str, int]:
    counts = {}

    for path in paths:
        filename = path.split('/')[-1]
        extension = filename.rsplit('.', 1)[-1].lower() if '.' in filename else ''
        counts[extension] = counts.get(extension, 0) + 1

    return counts


def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ''

    return min(paths, key=lambda path: (-path.count('/'), path))

def human_size(n_bytes: int) -> str:
    units = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
    size = n_bytes
    unit_index = 0

    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1

    if unit_index == 0:
        return f'{size} {units[unit_index]}'

    return f'{size:.1f} {units[unit_index]}'