import sys

sys.path.append('../')

from Classes.Matrix import Matrix

if __name__ == '__main__':
    v1 = Matrix([[8, 5, -2, 4, 28],
                 [4, 2.5, 20, 4, -4],
                 [8, 5, 1, 4, 17]])

    print("{}", v1.row_echelon())
    # // [1.0, 0.625, 0.0, 0.0, -12.1666667]
    # // [0.0, 0.0, 1.0, 0.0, -3.6666667]
    # // [0.0, 0.0, 0.0, 1.0, 29.5]