import computing_median


def computing_mean():
    """Compute the mean value of the list
    """
    lst_data: list[int] = [x for x in range(1, 11)]
    print(lst_data)
    # get the mean value for all even and odd data
    even_mean: int = 0
    odd_mean: int = 0
    for x in lst_data:
        if x % 2 == 0:
            even_mean = even_mean + x
        else:
            odd_mean = odd_mean + x
    even_mean //= (len(lst_data) // 2)
    odd_mean //= (len(lst_data) // 2)
    print(f'Odd mean: {odd_mean} -- Even mean: {even_mean}')
    # median
    computing_median.computing_median_of_list()
    print(f'Mean is {(odd_mean + even_mean) / 2}')


def main():
    computing_mean()


if __name__ == '__main__':
    main()
