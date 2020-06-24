
# Inverts 3x3 matrix
def inv3x3(m):
    det = m[0][0] * (m[1][1] * m[2][2] - m[2][1] * m[1][2]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])

    invdet = 1 / det

    minv = [[0 for x in range(columns)] for y in range(rows)] # Inverse of matrix m
    minv[0][0] = (m[1][1] * m[2][2] - m[2][1] * m[1][2]) * invdet
    minv[0][1] = (m[0][2] * m[2][1] - m[0][1] * m[2][2]) * invdet
    minv[0][2] = (m[0][1] * m[1][2] - m[0][2] * m[1][1]) * invdet
    minv[1][0] = (m[1][2] * m[2][0] - m[1][0] * m[2][2]) * invdet
    minv[1][1] = (m[0][0] * m[2][2] - m[0][2] * m[2][0]) * invdet
    minv[1][2] = (m[1][0] * m[0][2] - m[0][0] * m[1][2]) * invdet
    minv[2][0] = (m[1][0] * m[2][1] - m[2][0] * m[1][1]) * invdet
    minv[2][1] = (m[2][0] * m[0][1] - m[0][0] * m[2][1]) * invdet
    minv[2][2] = (m[0][0] * m[1][1] - m[1][0] * m[0][1]) * invdet
    return minv

def sum_matrices(A, B):
    rows = len(A)
    columns = len(A[0])
    C = [[A[y][x] + B[y][x] for x in range(columns)] for y in range(rows)]
    return C

def multiply_matrix_by_number(A, number):
    rows = len(A)
    columns = len(A[0])
    return [[A[j][i] * number for i in range(columns)] for j in range(rows)]

def subtract_matrix(A):
    return multiply_matrix_by_number(A, -1)

# Two matrices multiplication
def matrixmult (A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
      print("Nie można pomnozyc macierzy")
      return

    C = [[0 for row in range(cols_B)] for col in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C

# Euklides norm
def vector_norm(V):
    rows_V = len(V)
    doubles_sum = 0
    for row in range(rows_V):
        doubles_sum += r[row][0]**2
    return doubles_sum**(1/2.0)

columns, rows = 3, 3
A = [[4, -1, 0], [-1, 4, -1], [0, -1, 4]]
b = [[2], [6], [2]]
L = [[0 for x in range(columns)] for y in range(rows)]
D = [[0 for x in range(columns)] for y in range(rows)]
U = [[0 for x in range(columns)] for y in range(rows)]



for i in range(rows):
    for j in range(columns):
        if i == j:
            D[i][j] = A[i][j]
        elif i < j:
            U[i][j] = A[i][j]
        else:
            L[i][j] = A[i][j]

############################
####### Jacobi Method ######
############################

# N = D^-1
N = inv3x3(D)
# przemnozenie macierzy razy (-1)
minus_N = subtract_matrix(N)

# x_0 - zero approximation (zerowe przybliżenie)
x_k = [[0], [0], [0]]

M = matrixmult(minus_N, sum_matrices(L, U))

for i in range(5):
    x_prev = x_k
    x_k = sum_matrices(matrixmult(M, x_prev), matrixmult(N, b))

print('Przybliżenie rozwiązania [[x], [y], [z]] otrzymane w piątej iteracji dla metody Jacobiego wynosi: {}'.format(x_k))

# Residual vector (wektor residualny) r = b - Ax
r = sum_matrices(b, subtract_matrix(matrixmult(A, x_k)))
# r vector euklides norm (norma euklidesowa wektora r)
print('\nNorma wektora residualnego dla piątej iteracji x_5 = {}'.format(vector_norm(r)))

# ||x_5-v|| vector norm where v is equations set exact solution
# Norma wektora ||x_5-v||, gdzie v to rozwiązanie dokładne układu
v = [[1], [2], [1]]
r = sum_matrices(x_k, subtract_matrix(v))
print('Norma wektora ||x_5-v||, gdzie v to rozwiązanie dokładne układu = {}'.format(vector_norm(r)))


###########################
######## SOR Method #######
###########################

omega = 1.1
G = matrixmult(
    inv3x3(sum_matrices(
        D, multiply_matrix_by_number(L, omega))),sum_matrices(multiply_matrix_by_number(D, 1 - omega), subtract_matrix(multiply_matrix_by_number(U, omega)))
    )
omega_omega = matrixmult(multiply_matrix_by_number(inv3x3(sum_matrices(D, multiply_matrix_by_number(L, omega))), omega), b)

x_k = [[0], [0], [0]]
# Iterations
for i in range(5):
    x_prev = x_k
    x_k = sum_matrices(matrixmult(G, x_prev), omega_omega)

print('\n\nPrzybliżenie rozwiązania [[x], [y], [z]] otrzymane w piątej iteracji dla metody SOR wynosi: {}'.format(x_k))

# Residual vector (wektor residualny) r = b - Ax
r1 = sum_matrices(b, subtract_matrix(matrixmult(A, x_k)))
# r vector euklides norm
print('\nNorma wektora residualnego dla piątej iteracji x_5 = {}'.format(vector_norm(r1)))

# ||x_5-v|| vector norm where v is equations set exact solution
r2 = sum_matrices(x_k, subtract_matrix(v))
print('Norma wektora ||x_5-v||, gdzie v to rozwiązanie dokładne układu = {}'.format(vector_norm(r2)))