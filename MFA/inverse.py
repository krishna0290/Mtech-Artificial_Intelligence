# Input matrix
A = [
    [9.066964285714286, -10.076785714285716, -0.726785714285714],
    [-10.076785714285716, 159.125, 123.05357142857143],
    [-0.726785714285714, 123.05357142857143, 684.6964285714286]
]

def determinant3(A):
    return (A[0][0]*(A[1][1]*A[2][2] - A[1][2]*A[2][1])
          - A[0][1]*(A[1][0]*A[2][2] - A[1][2]*A[2][0])
          + A[0][2]*(A[1][0]*A[2][1] - A[1][1]*A[2][0]))

def cofactor(A, row, col):
    # build the 2x2 minor by removing 'row' and 'col'
    minor = []
    for i in range(3):
        if i == row:
            continue
        r = []
        for j in range(3):
            if j == col:
                continue
            r.append(A[i][j])
        minor.append(r)
    minor_det = minor[0][0]*minor[1][1] - minor[0][1]*minor[1][0]
    sign = (-1) ** (row + col)
    return sign * minor_det

def inverse3(A):
    det = determinant3(A)
    if det == 0:
        raise ValueError("Matrix is singular, inverse does not exist")

    # cofactor matrix
    C = [[cofactor(A, i, j) for j in range(3)] for i in range(3)]

    # adjugate = transpose of cofactor matrix
    adj = [[C[j][i] for j in range(3)] for i in range(3)]

    # inverse = adjugate / determinant
    inv = [[adj[i][j] / det for j in range(3)] for i in range(3)]
    return inv

def print_matrix(M, label):
    print(label)
    for row in M:
        print(["{:.6f}".format(x) for x in row])
    print()

det = determinant3(A)
print(f"Determinant: {det:.6f}\n")

A_inv = inverse3(A)
print_matrix(A_inv, "Inverse of A:")

# # ---- verification: A * A_inv should be identity ----
# def mat_mult(X, Y):
#     result = [[0]*3 for _ in range(3)]
#     for i in range(3):
#         for j in range(3):
#             result[i][j] = sum(X[i][k]*Y[k][j] for k in range(3))
#     return result

# check = mat_mult(A, A_inv)
# print_matrix(check, "A * A_inv (should be ~identity):")