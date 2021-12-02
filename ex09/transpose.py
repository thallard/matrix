import sys

sys.path.append('../')

from Classes.Matrix import Matrix

if __name__ == '__main__':
    v1 = Matrix([[2, 3], [4, 5]])
    print('', v1.matrix, '\n', v1.transpose())

    print('\n')

    v1 = Matrix([[2, 3], [2, 3]])
    print('', v1.matrix, '\n', v1.transpose())
