def linear_search_first_none(lst_data: list[float]) -> int:
    """Find the None value from the list

    Args:
        lst_data (list[float]): list of integers

    Returns:
        int: if None is in the list, return the position
    """
    n: int = len(lst_data)
    for i in range(n):
        if lst_data[i] == None:
            return i


def linear_search_all_none(lst_data: list[float]) -> list[int]:
    """Find all the position of None from the list

    Args:
        lst_data (list[float]): data

    Returns:
        list[int]: list of all None index
    """
    none_index_list: list[int] = []
    n: int = len(lst_data)
    for i in range(n):
        if lst_data[i] == None:
            none_index_list.append(i)
    return none_index_list


def main():
    lst_data = [1, 1.1, None, 1.4, None, 1.5, None, 2.0]
    print(
        f'Position first None: {linear_search_first_none(lst_data=lst_data)}')
    print(
        f'List of all None positions: {linear_search_all_none(lst_data=lst_data)}')


if __name__ == '__main__':
    main()
