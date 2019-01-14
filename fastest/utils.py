def count_truthy(items):
    counter = 0
    for item in items:
        if item is not None:
            counter += 1
    return counter
