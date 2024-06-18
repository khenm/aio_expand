def list_creation_and_accessing():
    """Create list and access by index
    """
    # Q1: print the list
    list_data: list[int] = [x for x in range(1, 11)]
    # Q2: print the first 5 integers
    print(list_data[:5])
    # Q3: Print the elements that are not divisble by 2
    for i in range(len(list_data)):
        if list_data[i] % 2 != 0:
            print(list_data[i], end=" ")
    print()  # end line
    # Q4: Print the sum of all elements
    sum_element: int = 0
    for i in range(len(list_data)):
        sum_element = sum_element + list_data[i]
    print(sum_element)


def main():
    list_creation_and_accessing()


if __name__ == "__main__":
    main()
