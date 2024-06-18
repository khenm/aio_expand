def list_crud():
    """Executing basic functions:
    adding, removing, changing elements
    """
    # Q1: create a list lst_data containing
    # even number from 1 to 12
    lst_data: list[int] = [x for x in range(1, 13) if x % 2 == 0]
    print(lst_data)

    # Q2: remove every element that is divisible by 3
    data_q2 = lst_data.copy()
    i: int = 0
    while i < len(data_q2):
        if (data_q2[i] % 3 == 0):
            data_q2.pop(i)
        else:
            i = i + 1
    print(data_q2)
    
    # Q3: add an element to the end from 1 to 3 
    # add at the position 3 a list from 6 to 8
    data_q3 = data_q2.copy()
    data_q3.extend([1, 2, 3])
    insert_index: int = 3
    for i in [6, 7, 8]:
        data_q3.insert(insert_index, i)
        insert_index += 1
    print(data_q3)
    
    # Q4:
    data_q4 = data_q3.copy()
    for i in range(len(data_q4)):
        if data_q4[i] % 2 == 0 or data_q4[i] % 5 == 0:
            data_q4[i] = 0
    print(data_q4)


def main():
    list_crud()


if __name__ == "__main__":
    main()
