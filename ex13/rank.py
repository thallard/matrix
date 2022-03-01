import sys

sys.path.append('../')

from Classes.Matrix import Matrix

if __name__ == '__main__':
    print('\033[35mRank on matrices (subject)\033[0m')
    m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    m1.print(False)
    print('Rank :', m1.rank(), '\n')

    m1 = Matrix([[1, 2, 0, 0], [2, 4, 0, 0], [-1, 2, 1, 1]])
    m1.print(False)
    print('Rank :', m1.rank(), '\n')

    m1 = Matrix([[8, 5, -2], [4, 7, 20], [7, 6, 1], [21, 18, 7]])
    m1.print(False)
    print('Rank :', m1.rank(), '\n')

    print('\033[35mRank on matrices (correction)\033[0m')
    m1 = Matrix([[0, 0], [0, 0]])
    m1.print(False)
    print('Rank :', m1.rank(), '\n')

    m1 = Matrix([[1, 0], [0, 1]])
    m1.print(False)
    print('Rank :', m1.rank(), '\n')

    m1 = Matrix([[2, 0], [0, 2]])
    m1.print(False)
    print('Rank :', m1.rank(), '\n')

    m1 = Matrix([[1, 1], [1, 1]])
    m1.print(False)
    print('Rank :', m1.rank(), '\n')

    m1 = Matrix([[0, 1], [1, 0]])
    m1.print(False)
    print('Rank :', m1.rank(), '\n')

    m1 = Matrix([[1, 2], [3, 4]])
    m1.print(False)
    print('Rank :', m1.rank(), '\n')

    m1 = Matrix([[-7, 5], [4, 6]])
    m1.print(False)
    print('Rank :', m1.rank(), '\n')

    m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    m1.print(False)
    print('Rank :', m1.rank(), '\n')

