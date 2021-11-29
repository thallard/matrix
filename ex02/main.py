from Matrix import Matrix
from Vector import Vector


# Linear interpolation with interpolation scalar
def lerp(origin, target, interpolation):
    # Un
    if interpolation > 1 or interpolation < 0:
        return None

    # Floats and integers gestion
    if isinstance(origin, (int, float)) or isinstance(target, (int, float)):
        return ((target - origin) * interpolation) + origin

    # Vectors gestion
    if isinstance(origin, Vector) or isinstance(target, Vector):
        return 1
    return None


if __name__ == '__main__':
    print('\033[35mLinear interpolation with int or float\033[0m')
    print(lerp(0, 1, 12))
    print(lerp(0, 1, 0))
    print(lerp(0, 1, 1))
    print(lerp(0, 1, 0.5))
    print(lerp(21, 42, 0.3))

    print('\n\033[35mLinear interpolation with matrices and vectors\033[0m')
    v1 = Vector([2, 1])
    v2 = Vector([4, 2])
    print(lerp(v1.vector, v2.vector, 0.3))

    # println!("{}", lerp(Vector::from([2., 1.]), Vector::from(4., 2.), 0.3));
    # [2.6]
    # [1.3]
    # println!("{}", lerp(Matrix::from([[2., 1.], [3., 4.]]), Matrix::from([[20., 10.], [30., 40.]]), 0.5));
    # [11., 16.5]
    # [5.5, 22.]