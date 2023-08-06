def count_in_list(lst : list, to_find : str) -> int:
    """
    count_in_list(list, str) -> int

    count the number of occurence of a string in a list
    """
    return len([elem for elem in lst if elem == to_find])