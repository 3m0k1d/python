array_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


max_in_third_column = max(row[2] for row in array_2d)


max_in_second_row = max(array_2d[1])

print("Максимальное значение в третьем столбце:", max_in_third_column)
print("Максимальное значение во второй строке:", max_in_second_row)

def transform_array(original):
     new_array = [[1 if elem > 0 else 0 for elem in row] for row in original]
     return new_array

m, n = 3, 4
original_array = [
    [1, -2, 3, 4],
    [-5, 6, -7, 8],
    [9, -10, 11, 0]
]

new_array = transform_array(original_array)

print("Исходный массив:")
for row in original_array:
    print(row)

print("\nНовый массив:")
for row in new_array:
    print(row)

def is_magic_square(matrix):
    n = len(matrix)

    magic_sum = sum(matrix[0])

    for row in matrix:
        if sum(row) != magic_sum:
            return False

    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != magic_sum:
            return False

    if sum(matrix[i][i] for i in range(n)) != magic_sum:
        return False

    if sum(matrix[i][n - 1 - i] for i in range(n)) != magic_sum:
        return False

    return True


matrix = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

if is_magic_square(matrix):
    print("Это магический квадрат!")
else:
    print("Это не магический квадрат.")
