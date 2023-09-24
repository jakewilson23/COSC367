"""Write a function generate_rest(initial_sequence, expression, length) that takes an initial sequence of numbers,
an expression, and a specified length, and returns a list of integers with the specified length that is the
continuation of the initial list according to the given expression. The parameters are:

initial_sequence: an initial sequence (list) of integer numbers that has at least two numbers; expression: an
expression constructed from function symbols '+', '-', and '*' which correspond to the three binary arithmetic
functions, and the leaf nodes are integers and 'x', 'y', and 'i' where the intended meaning of these three symbols is
described above; length: a non-negative integer that specifies the length of the returned list. Hint: The values must
be generated in order, from left to right. For the first value, the expression must be evaluated with 'i' set to the
length of the initial sequence (because this would be the index of the first number in the generated sequence) and
'x' and 'y' set to the last two elements of the initial sequence. As new values are generated, the values of i, x,
and y are updated. Recall that values of variable leaves are set via a dictionary of bindings.

Note: It is recommended that you use your implementation of the evaluate function. This would allow you to implement
this function in about 11 lines of code."""


from q3 import evaluate


def generate_rest(initial_sequence, expression, length):
    temp_sequence = initial_sequence
    x, y, i = len(temp_sequence) - 2, len(temp_sequence) - 1, len(temp_sequence)
    result = []
    for num in range(length):
        bindings = {'x': temp_sequence[x], 'y': temp_sequence[y], 'i': i, '+': lambda a, b: a + b,
                    '-': lambda a, b: a - b, '*': lambda a, b: a * b}
        answer = evaluate(expression, bindings)
        result.append(answer)
        temp_sequence.append(answer)
        x, y, i = x + 1, y + 1, i + 1
    return result

def main():
    # Test 1
    print('--------------Test 1--------------')
    print('Result should equal [3, 4, 5, 6, 7]')
    print('----------------------------------')
    initial_sequence = [0, 1, 2]
    expression = 'i'
    length_to_generate = 5
    print(generate_rest(initial_sequence,
                        expression,
                        length_to_generate))

    # Test 2
    print('--------------Test 2--------------')
    print('Result should equal [3, 4, 5, 6]')
    print('----------------------------------')
    # no particular pattern, just an example expression
    initial_sequence = [-1, 1, 367]
    expression = 'i'
    length_to_generate = 4
    print(generate_rest(initial_sequence,
                        expression,
                        length_to_generate))

    # Test 3
    print('--------------Test 3--------------')
    print('Result should equal [12, 14, 16, 18, 20]')
    print('----------------------------------')
    initial_sequence = [4, 6, 8, 10]
    expression = ['*', ['+', 'i', 2], 2]
    length_to_generate = 5
    print(generate_rest(initial_sequence,
                        expression,
                        length_to_generate))

    # Test 4
    print('--------------Test 4--------------')
    print('Result should equal [12, 14, 16, 18, 20]')
    print('----------------------------------')
    initial_sequence = [4, 6, 8, 10]
    expression = ['+', 2, 'y']
    length_to_generate = 5
    print(generate_rest(initial_sequence,
                        expression,
                        length_to_generate))

    # Test 5
    print('--------------Test 5--------------')
    print('Result should equal [0, 1, 0, 1, 0, 1]')
    print('----------------------------------')
    initial_sequence = [0, 1]
    expression = 'x'
    length_to_generate = 6
    print(generate_rest(initial_sequence,
                        expression,
                        length_to_generate))

    # Test 6
    print('--------------Test 6--------------')
    print('Result should equal [1, 2, 3, 5, 8]')
    print('----------------------------------')
    # Fibonacci sequence
    initial_sequence = [0, 1]
    expression = ['+', 'x', 'y']
    length_to_generate = 5
    print(generate_rest(initial_sequence,
                        expression,
                        length_to_generate))

    # Test 7
    print('--------------Test 7--------------')
    print('Result should equal [367, 367, 367, 367, 367]')
    print('----------------------------------')
    initial_sequence = [367, 367, 367]
    expression = 'y'
    length_to_generate = 5
    print(generate_rest(initial_sequence,
                        expression,
                        length_to_generate))

    # Test 8
    print('--------------Test 8--------------')
    print('Result should equal [-1, -1, -1, -1, -1]')
    print('----------------------------------')
    # no pattern, just a demo
    initial_sequence = [0, 1, 2]
    expression = -1
    length_to_generate = 5
    print(generate_rest(initial_sequence,
                        expression,
                        length_to_generate))

    # Test 9
    print('--------------Test 9--------------')
    print('Result should equal []')
    print('----------------------------------')
    initial_sequence = [0, 1, 2]
    expression = 'i'
    length_to_generate = 0
    print(generate_rest(initial_sequence,
                        expression,
                        length_to_generate))


if __name__ == "__main__":
    main()
