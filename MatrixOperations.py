import numpy as np

def getStringNumber(matrix):
    return len(matrix)

def getColumnNumber(matrix):
    try:
        return len(matrix[0])
    except Exception:
        print('ERROR: empty matrix')

# def bubble_max_row(m, col):
#     max_element = m[col][col]
#     max_row = col
#     for i in range(col + 1, len(m)):
#         if abs(m[i][col]) > abs(max_element):
#             max_element = m[i][col]
#             max_row = i
#     if max_row != col:
#         m[col], m[max_row] = m[max_row], m[col]
#     print('max_row', max_row)

def find_max_row(m,col):
    max_elem = m[col][col]
    max_row = col
    if max_elem == 1:
        print('max_row', max_row)
        return
    for i in range(col+1, len(m)):
        if m[i][col] > max_elem:
            max_elem = m[i][col]
            max_row = i
            break
    if max_row != col:
        m[col], m[max_row] = m[max_row], m[col]
    print('max_row', max_row)


# def solve_gauss(m):
#     n = len(m)
#     # forward trace
#     for k in range(n - 1):
#         bubble_max_row(m, k)
#         for i in range(k + 1, n):
#             div = m[i][k] / m[k][k]
#             m[i][-1] -= div * m[k][-1]
#             for p in range(k, n):
#                 m[i][p] -= div * m[k][p]


def gaussChange(self):
    max_str = getStringNumber(self.Hmatrix)
    print('max_str:', max_str)
    max_col = getColumnNumber(self.Hmatrix)
    print('max_col:', max_col)

    for k in range(max_str - 1):
        # bubble_max_row(self.Hmatrix, k)
        find_max_row(self.Hmatrix, k)
        for l in range(k + 1, max_str):
                for p in range(k, max_col):
                    self.Hmatrix[l][p] = (self.Hmatrix[l][p] + self.Hmatrix[k][p]) % 2

def make_generator_matrix(H):
    """
    Create code generator matrix using given check matrix. The function must raise DegenerateMatrixError exception,
    if given check matrix is degenerate

    :param H: check matrix of size (m,n), np.array
    :return G: generator matrix of size (n,k), np.array
    :return ind: indices for systematic coding, i.e. G[ind,:] is unity matrix
    """
    H = np.copy(H)
    m, n = H.shape
    k = n - m
    in_ind = np.zeros(n, dtype=bool)
    nfixed = 0
    for j in range(n):
        flag = False
        for i in range(nfixed, m):
            if H[i, j] == 1:
                if i != nfixed:
                    H[[i, nfixed]] = H[[nfixed, i]]
                flag = True
                break
        if flag:
            w = H[:, [j]]
            w[nfixed] = 0
            H = (H + H[nfixed] * w) % 2
            nfixed += 1
            in_ind[j] = True
    if nfixed < m:
        #raise DegenerateMatrixError
        print('ERROR')
    G = np.zeros((n, k), dtype=H.dtype)
    G[~in_ind] = np.eye(k, dtype=H.dtype)
    G[in_ind] = H[:, ~in_ind]
    ind = np.where(~in_ind)[0]
    print('G:', G)
    print('ind:', ind)
    return G, ind