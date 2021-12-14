import sys

sys.path.append('../')

from Classes.Matrix import Matrix

if __name__ == '__main__':
    print('\033[35mReduced row echelon form matrices (subject)\033[0m')
    m1 = Matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])
    m1.print(False)
    m1.row_echelon()
    m1.print()

    m1 = Matrix([[1., 2.], [3., 4.]])
    m1.print(False)
    m1.row_echelon()
    m1.print()

    m1 = Matrix([[1., 2.], [2., 4.]])
    m1.print(False)
    m1.row_echelon()
    m1.print()

    m1 = Matrix([[8., 5., -2., 4., 28.], [4., 2.5, 20., 4., -4.], [8., 5., 1., 4., 17.]])
    m1.print(False)
    m1.row_echelon()
    m1.print()

    print('\033[35mReduced row echelon form matrices (correction)\033[0m')
    m1 = Matrix([[0., 0.], [0., 0.]])
    m1.print(False)
    m1.row_echelon()
    m1.print()

    m1 = Matrix([[1., 0.], [0., 1.]])
    m1.print(False)
    m1.row_echelon()
    m1.print()

    m1 = Matrix([[4., 2.], [2., 1.]])
    m1.print(False)
    m1.row_echelon()
    m1.print()

    m1 = Matrix([[-7., 2.], [4., 8.]])
    m1.print(False)
    m1.row_echelon()
    m1.print()

    m1 = Matrix([[1., 2.], [4., 8.]])
    m1.print(False)
    m1.row_echelon()
    m1.print(False)
