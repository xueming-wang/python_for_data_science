

def count_in_list(lst: list, string: str) -> int:
    return len([x for x in lst if x == string])
