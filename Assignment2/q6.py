"""Finally you are ready to put all the components together and solve the actual problem.  You have to write a
function predict_rest(sequence) that takes a sequence of integers of length at least 5, finds the pattern in the
sequence, and "predicts" the rest by returning a list of the next five integers in the sequence.

This question is somewhat open-ended; it is up to you what algorithm you implement. The patterns in the test cases
are easy enough that even a random search (i.e. generating random expressions until a match is found) is very likely
to solve all the test cases. This demonstrates that a good representation can significantly simplify a problem. If
you are interested in developing a more sophisticated solution, then you can look into implementing a proper
evolutionary algorithm with operators for mutation and crossover. See the lecture notes and the related links.

Further assumptions
All the sequences in the test cases have patterns that can be expressed as a function of x, y,
and i as described before. All the patterns (functions) can be constructed by combining three binary functions:
addition, subtraction, and multiplication. Using integers between -2 and 2 (inclusive) as constant leafs should be
enough to represent the patterns in the test cases. All the patterns (functions) can  be constructed by expression
trees not deeper than 3. Your algorithm must be able to solve all the problems given in the example test cases in
less than 2 seconds (collectively). Following the guidelines given in the assignment should naturally achieve this.

Notes
To make sure your function does not overfit (e.g. memorise) the given example sequences, there are some hidden
test cases (which are not more difficult than the example test cases). Consider using random.seed so that your
offline results match what will be generated on the server and you can replicate your results if needed. Make sure
the function does not modify its input. In its simplest form, this function can be implemented in less than 10 lines
of code. It would be interesting to go through the test cases yourself and see if you can find the patterns."""


from q4 import random_expression
from q5 import generate_rest
import copy


def predict_rest(sequence):
    temp_sequence = copy.copy(sequence)
    function_symbols = ['+', '-', '*']
    constant_leaves = list(range(-2, 3))
    variable_leaves = ['x', 'y', 'i']
    leaves = constant_leaves + variable_leaves
    expression_valid = False
    valid_expression = []
    while not expression_valid:
        test_sequence = temp_sequence[:3]
        expression = random_expression(function_symbols, leaves, 3)
        generated_result = generate_rest(test_sequence, expression, 5)
        test_sequence += generated_result
        expression_valid = True
        for index, _ in enumerate(temp_sequence):
            if temp_sequence[index] != test_sequence[index]:
                expression_valid = False
        if expression_valid:
            valid_expression.append(expression)
    return generate_rest(temp_sequence, valid_expression[0], 5)


def main():
    # Test 1
    print('--------------Test 1--------------')
    print('Result should equal [0, 1, 2, 3, 4, 5, 6, 7]')
    print('                    [8, 9, 10, 11, 12]')
    print('----------------------------------')
    sequence = [0, 1, 2, 3, 4, 5, 6, 7]
    the_rest = predict_rest(sequence)
    print(sequence)
    print(the_rest)

    # Test 2
    print('--------------Test 2--------------')
    print('Result should equal [16, 18, 20, 22, 24]')
    print('----------------------------------')
    sequence = [0, 2, 4, 6, 8, 10, 12, 14]
    print(predict_rest(sequence))

    # Test 3
    print('--------------Test 3--------------')
    print('Result should equal [19, 17, 15, 13, 11]')
    print('----------------------------------')
    sequence = [31, 29, 27, 25, 23, 21]
    print(predict_rest(sequence))

    # Test 4
    print('--------------Test 4--------------')
    print('Result should equal [64, 81, 100, 121, 144]')
    print('----------------------------------')
    sequence = [0, 1, 4, 9, 16, 25, 36, 49]
    print(predict_rest(sequence))

    # Test 5
    print('--------------Test 5--------------')
    print('Result should equal [51, 66, 83, 102, 123]')
    print('----------------------------------')
    sequence = [3, 2, 3, 6, 11, 18, 27, 38]
    print(predict_rest(sequence))

    # Test 6
    print('--------------Test 6--------------')
    print('Result should equal [21, 34, 55, 89, 144]')
    print('----------------------------------')
    sequence = [0, 1, 1, 2, 3, 5, 8, 13]
    print(predict_rest(sequence))

    # Test 7
    print('--------------Test 7--------------')
    print('Result should equal [5, -4, 29, -13, 854]')
    print('----------------------------------')
    sequence = [0, -1, 1, 0, 1, -1, 2, -1]
    print(predict_rest(sequence))

    # Test 8
    print('--------------Test 8--------------')
    print('Result should equal [-1055, 2547, -6149, 14845, -35839]')
    print('----------------------------------')
    sequence = [1, 3, -5, 13, -31, 75, -181, 437]
    print(predict_rest(sequence))


if __name__ == "__main__":
    main()
