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

