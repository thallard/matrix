import sys

sys.path.append('../')

from Classes.Vector import Vector


# Cosine function using eucledian norm
def angle_cos(vector1, vector2):
    return round((vector1.dot(vector2)) / (vector1.norm() * vector2.norm()), 4)


if __name__ == '__main__':
    v1 = Vector([1, 0])
    v2 = Vector([1, 0])
    print(angle_cos(v1, v2))

    v1 = Vector([1, 0])
    v2 = Vector([0, 1])
    print(angle_cos(v1, v2))

    v1 = Vector([-1, 1])
    v2 = Vector([1, -1])
    print(angle_cos(v1, v2))

    v1 = Vector([2, 1])
    v2 = Vector([4, 2])
    print(angle_cos(v1, v2))

    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    print(angle_cos(v1, v2))
