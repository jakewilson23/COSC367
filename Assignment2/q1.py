"""Write a function of the form is_valid_expression(object, function_symbols, leaf_symbols) that takes an object as
its first argument and tests whether it is a valid expression according to our definition of expressions in this
assignment. The function must return True if the given object is valid expression, False otherwise.

The parameters of the function are:

object: any Python object function_symbols: a collection (list, set, ...) of strings that are allowed to be used in
function positions (internal nodes of the tree). leaf_symbols: a collection of strings that are allowed to be used as
variable leaves. Notes This function needs to be recursive. The base cases are for leaf nodes. This function can be
written in less than 10 lines of code. The built-in function type can be useful here."""


def is_valid_expression(object, function_symbols, leaf_symbols):
    is_valid = True
    if type(object) != list:  # object is a leaf
        if object not in leaf_symbols and type(object) != int:
            is_valid = False
    else:   # object is a list
        if object[0] in function_symbols and len(object) == 3:
            for item in range(1, len(object)):
                is_valid = is_valid_expression(object[item], function_symbols, leaf_symbols)
        else:
            is_valid = False
    return is_valid


def main():
    # Test 1
    print('--------------Test 1--------------')
    print('Result should equal True')
    print('----------------------------------')
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = 1

    print(is_valid_expression(expression, function_symbols, leaf_symbols))

    # Test 2
    print('--------------Test 2--------------')
    print('Result should equal True')
    print('----------------------------------')
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = 'y'

    print(is_valid_expression(
        expression, function_symbols, leaf_symbols))

    # Test 3
    print('--------------Test 3--------------')
    print('Result should equal False')
    print('----------------------------------')
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = 2.0

    print(is_valid_expression(
        expression, function_symbols, leaf_symbols))

    # Test 4
    print('--------------Test 4--------------')
    print('Result should equal True')
    print('----------------------------------')
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['f', 123, 'x']

    print(is_valid_expression(
        expression, function_symbols, leaf_symbols))

    # Test 5
    print('--------------Test 5--------------')
    print('Result should equal True')
    print('----------------------------------')
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['f', ['+', 0, -1], ['f', 1, 'x']]

    print(is_valid_expression(
        expression, function_symbols, leaf_symbols))

    # Test 6
    print('--------------Test 6--------------')
    print('Result should equal True')
    print('----------------------------------')
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['+', ['f', 1, 'x'], -1]

    print(is_valid_expression(
        expression, function_symbols, leaf_symbols))

    # Test 7
    print('--------------Test 7--------------')
    print('Result should equal True')
    print('----------------------------------')
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y', -1, 0, 1]
    expression = ['f', 0, ['f', 0, ['f', 0, ['f', 0, 'x']]]]

    print(is_valid_expression(
        expression, function_symbols, leaf_symbols))

    # Test 8
    print('--------------Test 8--------------')
    print('Result should equal False')
    print('----------------------------------')
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = 'f'

    print(is_valid_expression(
        expression, function_symbols, leaf_symbols))

    # Test 9
    print('--------------Test 9--------------')
    print('Result should equal False')
    print('----------------------------------')
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['f', 1, 0, -1]

    print(is_valid_expression(
        expression, function_symbols, leaf_symbols))

    # Test 10
    print('--------------Test 10--------------')
    print('Result should equal False')
    print('----------------------------------')
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['x', 0, 1]

    print(is_valid_expression(
        expression, function_symbols, leaf_symbols))

    # Test 11
    print('--------------Test 11--------------')
    print('Result should equal False')
    print('----------------------------------')
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['g', 0, 'y']

    print(is_valid_expression(
        expression, function_symbols, leaf_symbols))


if __name__ == "__main__":
    main()
