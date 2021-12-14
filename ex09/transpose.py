import sys

sys.path.append('../')

from Classes.Matrix import Matrix

if __name__ == '__main__':
    print('\033[35mTranspose matrices (subject)\033[0m')
    m1 = Matrix([[2, 3], [4, 5]])
    print('', m1.matrix, '\n', m1.transpose(), '\n')


    m1 = Matrix([[2, 3], [2, 3]])
    print('', m1.matrix, '\n', m1.transpose())

    print('\033[35mTranspose matrices (correction)\033[0m')
    m1 = Matrix([[0, 0], [0, 0]])
    m1.print(False)
    m1.transpose()
    m1.print()

    m1 = Matrix([[1, 0], [0, 1]])
    m1.print(False)
    m1.transpose()
    m1.print()

    m1 = Matrix([[1, 2], [3, 4]])
    m1.print(False)
    m1.transpose()
    m1.print()

    m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    m1.print(False)
    m1.transpose()
    m1.print()

    m1 = Matrix([[1, 2], [3, 4], [5, 6]])
    m1.print(False)
    m1.transpose()
    m1.print()

