"""Write a function depth(expression) that takes an expression (that follows our definition of expression) and
returns the depth of the expression tree. The depth of a tree is the depth of its deepest leaf.

Notes
This is a recursive function and can be written in 5 lines of code (or even fewer).
The depth of an expression that is just a single leaf (e.g. the expression 2 or y) is zero.
Converting the expression into a string and analysing the string to compute the depth is not a good idea."""


def depth(expression):
    if type(expression) != list:    # expression is a leaf
        return 0
    else:                           # expression is a list
        depth_value, nested_depth_value = 1, 0
        for index in range(1, len(expression)):
            nested_depth_value = max(depth(expression[index]), nested_depth_value)
    return depth_value + nested_depth_value


def main():
    # Test 1
    print('--------------Test 1--------------')
    print('Result should equal 0')
    print('----------------------------------')
    expression = 12
    print(depth(expression))

    # Test 2
    print('--------------Test 2--------------')
    print('Result should equal 0')
    print('----------------------------------')
    expression = 'weight'
    print(depth(expression))

    # Test 3
    print('--------------Test 3--------------')
    print('Result should equal 1')
    print('----------------------------------')
    expression = ['add', 12, 'x']
    print(depth(expression))

    # Test 4
    print('--------------Test 4--------------')
    print('Result should equal 2')
    print('----------------------------------')
    expression = ['add', ['add', 22, 'y'], 'x']
    print(depth(expression))

    # Test 5
    print('--------------Test 5--------------')
    print('Result should equal 2')
    print('----------------------------------')
    expression = ['+', ['*', 2, 'i'], ['*', -3, 'x']]
    print(depth(expression))

    # Test 6
    print('--------------Test 6--------------')
    print('Result should equal 3')
    print('----------------------------------')
    expression = ['add', ['add', ['add', 22, 'y'], 'y'], ['add', 22, 'y']]
    print(depth(expression))


if __name__ == "__main__":
    main()
