from itertools import groupby

def group_by_category(data):
    data.sort(key=lambda x: x['category'])
    grouped = {}
    for key, group in groupby(data, key=lambda x: x['category']):
        grouped[key] = list(group)
    return grouped
