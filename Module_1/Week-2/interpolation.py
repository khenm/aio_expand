def nearest_neighbor_interpolate(lst_data: list[float]):
    """Nearest neighbor interpolation is a technique to estimate 
    the value of an unknown point baseed on the neighbors' value

    Args:
        lst_data (list[float]): data
    """
    # find None -- the position need to be determined
    size: int = len(lst_data)
    interpolated_data: list[int] = lst_data.copy()
    for i in range(size):
        if interpolated_data[i] == None:
            if i == 0:
                interpolated_data[i] = interpolated_data[i + 1]
            elif i == size - 1:
                interpolated_data[i] = interpolated_data[i - 1]
            else:
                interpolated_data[i] = min(
                    interpolated_data[i - 1], interpolated_data[i + 1])
    print(f'Nearest Neighbor Interpolation: {interpolated_data}')


def main():
    lst_data = [1, 1.1, None, 1.4, None, 1.5, None, 2.0]
    nearest_neighbor_interpolate(lst_data=lst_data)


if __name__ == '__main__':
    main()
