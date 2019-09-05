def sum_list(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            small = sum_list(item)
            total += small
        else:
            total += item
    return total

if __name__ == "__main__":

    lst = [1, 2, [3, [4]], 5]
    print(sum_list(lst))
