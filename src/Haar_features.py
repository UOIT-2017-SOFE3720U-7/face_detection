from math import floor

# 2 rectangles
#   Horizontal
#       Black above white boxes
#       White above black boxes
#   Vertical
#       Black right to white boxes
#       White right to black boxes

# 3 rectangles:
#   Horizontal:
#       Black rectangle in the middle
#       White rectangle in the middle
#   Vertical:
#       Black rectangle in the middle
#       White rectangle in the middle

# 4 rectangles:
#   Black upper left, bottom right
#   White upper right, bottom left


def two_horizontal_rectangles(window_size):
    classifiers = []
    for sign in [1,-1]:
        for width in range(1, window_size+1):
            for hight in range(2, window_size+1,2):
                row = 0
                while (hight + row <= window_size):
                    column = 0
                    while (width + column <= window_size):
                        A = [row-1, column-1]
                        B = [A[0], A[1]+ width]
                        C = [A[0]+ int(hight/2), A[1]]
                        D = [C[0], B[1]]
                        E = [A[0]+ hight, A[1]]
                        F = [E[0], B[1]]
                        area = (abs(A[1]-B[1])) * (abs(A[0]-C[0]))
                        classifiers.append([sign,[A[0],A[1]],[B[0],B[1]],[C[0],C[1]],[D[0],D[1]],[E[0],E[1]],[F[0],F[1]],area])
                        column += 1
                    row += 1
    return classifiers

def two_vertical_rectangles(window_size):
    classifiers = []
    for sign in [1,-1]:
        for width in range(2, window_size+1,2):
            for hight in range(1, window_size+1):
                row = 0
                while (hight + row <= window_size):
                    column = 0
                    while (width + column <= window_size):
                        A = [row-1, column-1]
                        B = [A[0]+ hight, A[1]]
                        C = [A[0], A[1] + int(width/2)]
                        D = [B[0], C[1]]
                        E = [A[0],A[1] + width]
                        F = [B[0], E[1]]
                        area = (abs(A[1] - C[1])) * (abs(A[0] - B[0]))
                        classifiers.append([sign,[A[0],A[1]],[B[0],B[1]],[C[0],C[1]],[D[0],D[1]],[E[0],E[1]],[F[0],F[1]],area])
                        column += 1
                    row += 1
    return classifiers

def three_horizontal_rectangles(window_size):
    classifiers = []
    for sign in [1, -1]:
        for width in range(1, window_size + 1):
            for hight in range(3, window_size + 1, 3):
                row = 0
                while (hight + row <= window_size):
                    column = 0
                    while (width + column <= window_size):
                        A = [row - 1, column - 1]
                        B = [A[0], A[1] + width]
                        C = [A[0] + int(hight / 3), A[1]]
                        D = [C[0], B[1]]
                        E = [A[0] + int(hight*2/3), A[1]]
                        F = [E[0], B[1]]
                        G = [A[0] + hight, A[1]]
                        H = [G[0], B[1]]
                        area = (abs(A[1]-B[1])) * (abs(A[0]-C[0]))
                        classifiers.append(
                            [sign, [A[0], A[1]], [B[0], B[1]], [C[0], C[1]], [D[0], D[1]], [E[0], E[1]], [F[0], F[1]],[G[0], G[1]], [H[0], H[1]],area])
                        column += 1
                    row += 1
    return classifiers

def three_Vertical_rectangles(window_size):
    classifiers = []
    for sign in [1, -1]:
        for width in range(3, window_size + 1, 3):
            for hight in range(1, window_size + 1):
                row = 0
                while (hight + row <= window_size):
                    column = 0
                    while (width + column <= window_size):
                        A = [row - 1, column - 1]
                        B = [A[0] + hight, A[1]]
                        C = [A[0], A[1] + int(width / 3)]
                        D = [B[0], C[1]]
                        E = [A[0], A[1] + int(width*2/3)]
                        F = [B[0], E[1]]
                        G = [A[0], A[1] + width]
                        H = [B[0], G[1]]
                        area = (abs(A[1] - C[1])) * (abs(A[0] - B[0]))
                        classifiers.append(
                            [sign, [A[0], A[1]], [B[0], B[1]], [C[0], C[1]], [D[0], D[1]], [E[0], E[1]], [F[0], F[1]],[G[0], G[1]], [H[0], H[1]], area])
                        column += 1
                    row += 1
    return classifiers

def four_squares(window_size):
    classifiers = []
    for sign in [1, -1]:
        for size in range(2, window_size + 1, 2):
                row = 0
                while (size + row <= window_size):
                    column = 0
                    while (size + column <= window_size):
                        A = [row - 1, column - 1]
                        B = [A[0], A[1] + int(size/2)]
                        C = [A[0], A[1] + size]
                        D = [A[0] + int(size/2), A[1]]
                        E = [D[0], B[1]]
                        F = [D[0], C[1]]
                        G = [A[0] + size, A[1]]
                        H = [G[0], B[1]]
                        I = [G[0], C[1]]
                        area = (abs(A[1]-B[1]))*2
                        classifiers.append(
                            [sign, [A[0], A[1]], [B[0], B[1]], [C[0], C[1]], [D[0], D[1]], [E[0], E[1]], [F[0], F[1]],[G[0], G[1]], [H[0], H[1]], [I[0], I[1]],area])
                        column += 1
                    row += 1
    return classifiers

def all_features(window_size):
    classifiers = two_horizontal_rectangles(window_size)
    classifiers.extend(two_vertical_rectangles(window_size))
    classifiers.extend(three_horizontal_rectangles(window_size))
    classifiers.extend(three_Vertical_rectangles(window_size))
    classifiers.extend(four_squares(window_size))
    return classifiers

def two_rectangles(window_size):
    classifiers = two_horizontal_rectangles(window_size)
    classifiers.extend(two_vertical_rectangles(window_size))
    return classifiers

def three_rectangles(window_size):
    classifiers = three_horizontal_rectangles(window_size)
    classifiers.extend(three_Vertical_rectangles(window_size))
    return classifiers


