def print_(mat_):
    for row in range(len(mat_)):
        print(mat_[row])
        
def rotate_2d_matrix(mat_):
    n = len(mat_) # y
    m = len(mat_[0]) # x

    res = [[0] * m for _ in range(n)]

    for j in range(n):
        for i in range(m):
            # row -> col
            # col -> row 과정에서 뒤집힌 위치로 가야함 n 4 일 때  2 -> 1, 3 -> 0, 1 -> 2, 0 -> 3
            res[i][n - j - 1] = mat_[j][i]

    # print_(res)
    return res

if __name__ == "__main__":
    '''
    [[0,0,0],
     [1,0,0],
     [0,1,1],]
    ->
    [[0,1,0],
     [1,0,0],
     [1,0,0],]
    '''
    mat = [[0,0,0],
           [1,0,0],
           [0,1,1],]
    rotate_2d_matrix([[0, 0, 0], [1, 0, 0], [0, 1, 1]])

    