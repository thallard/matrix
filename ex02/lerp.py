import sys

sys.path.append('../')

from Classes.Matrix import Matrix
from Classes.Vector import Vector


# Linear interpolation with interpolation scalar
def lerp(origin, target, interpolation):
    if interpolation > 1 or interpolation < 0:
        return None

    # Floats and integers gestion
    if isinstance(origin, (int, float)) or isinstance(target, (int, float)):
        return ((target - origin) * interpolation) + origin

    # Vectors gestion
    if isinstance(origin, Vector) and isinstance(target, Vector):
        return origin.lerp(target, interpolation)

    # Matrix gestion
    if isinstance(origin, Matrix) or isinstance(target, Matrix):
        return origin.lerp(target, interpolation)
    return None


if __name__ == '__main__':
    print('\033[35mLinear interpolation with int or float\033[0m')
    print(lerp(0, 1, 0))
    print(lerp(0, 1, 1))
    print(lerp(0, 42, 0.5))
    print(lerp(-42, 42, 0.5))

    print('\n\033[35mLinear interpolation with vectors\033[0m')
    v1 = Vector([2, 1])
    v2 = Vector([4, 2])
    print(lerp(v1, v2, 0.3))

    print('\n\033[35mLinear interpolation with matrices\033[0m')
    print(lerp(Matrix([[2, 1], [3, 4]]), Matrix([[20, 10], [30, 40]]), 0.5))
    print(lerp(Matrix([5, 10]), Matrix([5, 10]), 0.5))
