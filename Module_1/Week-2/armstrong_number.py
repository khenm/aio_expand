# Armstrong function return bool
def armstrong(number: int) -> bool:
    """An Armstrong number is a positive integer
    which equals to the sum of each cube of digit

    Args:
        number (int): integer to be checked

    Returns:
        bool: if a number is an armstrong number
    """
    sum_integer: int = 0
    temp: int = number
    while temp > 0:
        sum_integer = sum_integer + (temp % 10) ** 3
        temp = temp // 10
    return sum_integer == number


def main():
    test_case_1 = [130, 270, 153, 407, 177, 371, 1000, 1634, 370]
    results = []
    for x in test_case_1:
        if armstrong(x):
            results.append(x)
    print(results)


if __name__ == "__main__":
    main()
