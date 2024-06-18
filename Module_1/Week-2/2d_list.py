def twod_list(lst_data: list[list]):
    size: int = 3
    lst_sub_data = [lst_data[i:i + size:2] for i in range(0, len(lst_data), 3)]
    print(lst_sub_data)


def main():
    lst_data = list(range(1, 10))
    twod_list(lst_data=lst_data)


if __name__ == '__main__':
    main()
