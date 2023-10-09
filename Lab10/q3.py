"""A perceptron is a function that takes a vector (list of numbers) of size n and returns 0 or 1 according to the
definition of perceptron.

Write a function construct_perceptron(weights, bias) where weights is a vector (list of numbers) of of length n and
bias is a scalar number and returns the corresponding perceptron function."""


def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given paramers."""

    def perceptron(input):
        # Complete (a line or two)
        value_sum = bias
        for i in range(len(input)):
            value_sum += (weights[i] * input[i])
        return 1 if value_sum >= 0 else 0

        # Note: we are masking the built-in input function but that is
        # fine since this only happens in the scope of this function and the
        # built-in input is not needed here.
        return  # what the perceptron should return

    return perceptron  # this line is fine


def main():
    # Test 1
    print('--------------Test 1--------------')
    print('Result should equal:')
    print('0, 1, 1, 1')
    print('----------------------------------')
    weights = [2, -4]
    bias = 0
    perceptron = construct_perceptron(weights, bias)

    print(perceptron([1, 1]))
    print(perceptron([2, 1]))
    print(perceptron([3, 1]))
    print(perceptron([-1, -1]))


if __name__ == "__main__":
    main()
