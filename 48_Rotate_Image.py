# Rotate_Image
def rotate(matrix):
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate(matrix)
print(matrix)



Transpose matrix
matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
where i is looping from 0 to len of matrix and j is i + 1 to len of matrix

Then reverse each row
matrix[i] = matrix[i][::-1]