from Vector import Vector


# Apply vector values with a scalar
def linear_combination(vectors, scalars):
    modified_vectors = []

    # Check size input
    for i in range(len(vectors)):
        if len(vectors[i]) != len(vectors[0]) or len(scalars) != len(vectors):
            return None

    # Linear combination
    for i in range(len(vectors[0])):
        value = 0
        for j in range(len(scalars)):
            value += vectors[j][i] * scalars[j]
        modified_vectors.append(value)
    return modified_vectors


if __name__ == '__main__':
    vector1 = Vector([1, 2, 3])
    vector2 = Vector([0, 10, -100])

    vectors = [vector1.vector, vector2.vector]
    print(linear_combination(vectors, [10, -2]))

    e1 = Vector([1, 0, 0])
    e2 = Vector([0, 1, 0])
    e3 = Vector([0, 0, 1])

    vectors = [e1.vector, e2.vector, e3.vector]
    print(linear_combination(vectors, [10, -2, 0.5]))
