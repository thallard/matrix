import sys

sys.path.append('../')

from Classes.Matrix import Matrix

if __name__ == '__main__':
    print('\033[35mInverse on matrices (subject)\033[0m')
    # m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    # print(m1.inverse())
    #
    # m1 = Matrix([[2, 0, 0], [0, 2, 0], [0, 0, 2]])
    # print(m1.inverse())
    #
    # m1 = Matrix([[8, 5, -2], [4, 7, 20], [7, 6, 1]])
    # print(m1.inverse())

    m1 = Matrix([[1, 2, 1], [4, 0, -1], [-1, 2, 2]])
    m1.inverse().print()

    print('\033[35mInverse on matrices (correction)\033[0m')
    # m1 = Matrix([[1, 0], [0, 1]])
    # print(m1.inverse())
