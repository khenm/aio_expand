def matrix_summation(matrix_1: list[list[int]], matrix_2: list[list[int]]):
    """Add 2 matrices

    Args:
        matrix_1 (list[list[int]]): _description_
        matrix_2 (list[list[int]]): _description_
    """
    matrix_result: list[list[int]] = []
    rows: int = len(matrix_1)
    cols: int = len(matrix_1[0])
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append((matrix_1[i][j] + matrix_2[i][j]))
        matrix_result.append(row)
    print(f'Sum = {matrix_result}')


def matrix_subtraction(matrix_1: list[list[int]], matrix_2: list[list[int]]):
    """Subtract 2 matrices

    Args:
        matrix_1 (list[list[int]]): _description_
        matrix_2 (list[list[int]]): _description_
    """
    matrix_result: list[list[int]] = []
    rows: int = len(matrix_1)
    cols: int = len(matrix_1[0])
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append((matrix_1[i][j] - matrix_2[i][j]))
        matrix_result.append(row)
    print(f'Sum = {matrix_result}')


def dot_product(matrix_1: list[list[int]], matrix_2: list[list[int]]):
    """Dot product

    Args:
        matrix_1 (list[list[int]]): _description_
        matrix_2 (list[list[int]]): _description_
    """
    matrix_result: list[list[int]] = []
    matrix1_rows: int = len(matrix_1)
    matrix1_cols: int = len(matrix_1[0])
    matrix2_rows: int = len(matrix_2)
    matrix2_cols: int = len(matrix_2[0])

    # check condition of dot product
    if matrix1_cols != matrix2_rows:
        print('Cannot do dot product.')
        return

    for i in range(matrix1_rows):
        row = []
        for j in range(matrix2_cols):
            dot: int = 0
            for k in range(matrix1_cols):
                dot += matrix_1[i][k] * matrix_2[k][j]
            row.append(dot)
        matrix_result.append(row)

    print(f'Dot product: {matrix_result}')


def main():
    matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_2 = [[2, 4, 6], [1, 3, 5], [1, 0, 1]]
    matrix_summation(matrix_1=matrix_1, matrix_2=matrix_2)
    matrix_subtraction(matrix_1=matrix_1, matrix_2=matrix_2)
    dot_product(matrix_1=matrix_1, matrix_2=matrix_2)


if __name__ == '__main__':
    main()
