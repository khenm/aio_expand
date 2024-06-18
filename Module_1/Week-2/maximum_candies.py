def add_candies(extra_candies: int, candies_list: list[int]) -> list[bool]:
    """If the person get extra candies and have the most condies, 
    return true

    Args:
        extra_candies (int): the add candies
        candies_list (list[int]): candies of each person

    Returns:
        list[bool]: condition met of each person
    """
    checklist: list[bool] = []
    max_candies: int = max(candies_list)
    for x in candies_list:
        if x + 3 >= max_candies:
            checklist.append(True)
        else:
            checklist.append(False)
    return checklist


def main():
    candies = [2, 3, 5, 1, 3]
    extra = 3
    print(add_candies(extra_candies=extra, candies_list=candies))


if __name__ == "__main__":
    main()
