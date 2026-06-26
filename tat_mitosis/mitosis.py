def mitosis(chunk, max_size=50000):
    if len(str(chunk)) > max_size:
        mid = max_size // 2
        return [chunk[:mid], chunk[mid:]]
    return [chunk]
