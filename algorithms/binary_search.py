def binary_search(sorted_list, item):
    print(sorted_list)
    low = 0
    high = len(sorted_list) - 1
    if high >= low:
        mid = int((low + high) / 2)
        guess = sorted_list[mid]
        if item < guess:
            return binary_search(sorted_list[:mid], item)
        elif item > guess:
            return binary_search(sorted_list[mid + 1 :], item)
        else:
            return True
    else:
        return None
