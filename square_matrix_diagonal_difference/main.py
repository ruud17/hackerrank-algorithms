def diagonal_difference(matrix):
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            primary_diagonal_sum += matrix[i][i]
            secondary_diagonal_sum += matrix[i][-i - 1]
            break

    abs_difference = abs(primary_diagonal_sum - secondary_diagonal_sum)

    return abs_difference
