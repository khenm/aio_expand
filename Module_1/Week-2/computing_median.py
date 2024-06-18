def computing_median_of_list():
    """Median: is the center data point of a data base
    """
    # Q1: create lst_data
    lst_data: list[int] = [x for x in range(1, 11)]
    print(lst_data)

    # Q2: find the median
    n: int = len(lst_data)
    median: int = 0
    if n % 2 != 0:
        median = lst_data[n // 2]
    else:
        median = (lst_data[n // 2 - 1] + lst_data[n // 2]) / 2
    print(f'Median: {median}')

    # Q3: filter all the odd numbers and reversed
    lst_odd_filter = [x for x in lst_data if x % 2 != 0]
    lst_odd_filter.sort(reverse=True)
    print(lst_odd_filter)


def main():
    computing_median_of_list()


if __name__ == "__main__":
    main()
