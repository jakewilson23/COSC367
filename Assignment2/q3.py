"""Write a function evaluate(expression, bindings) that takes an expression and a dictionary of bindings and returns
an integer that is the value of the expression. The parameters of the function are:

expression: an expression according to our definition of expressions; bindings: a dictionary where all the keys are
strings and are either a function symbol or a variable leaf. A function symbol is mapped to a function that takes two
arguments. A leaf symbol is mapped to an integer. Note: this function is recursive and can be written in less than 10
lines of code."""


def evaluate(expression, bindings):
    if type(expression) != list:  # expression is a leaf
        if type(expression) is str:
            return bindings[expression]
        return expression
    else:                         # expression is a list
        function_symbol = bindings[expression[0]]
        value_one = evaluate(expression[1], bindings)
        value_two = evaluate(expression[2], bindings)
    return function_symbol(value_one, value_two)


def main():
    # Test 1
    print('--------------Test 1--------------')
    print('Result should equal 12')
    print('----------------------------------')
    bindings = {}
    expression = 12
    print(evaluate(expression, bindings))

    # Test 2
    print('--------------Test 2--------------')
    print('Result should equal 10')
    print('----------------------------------')
    bindings = {'x': 5, 'y': 10, 'time': 15}
    expression = 'y'
    print(evaluate(expression, bindings))

    # Test 3
    print('--------------Test 3--------------')
    print('Result should equal 17')
    print('----------------------------------')
    bindings = {'x': 5, 'y': 10, 'time': 15, 'add': lambda x, y: x + y}
    expression = ['add', 12, 'x']
    print(evaluate(expression, bindings))

    # Test 4
    print('--------------Test 4--------------')
    print('Result should equal 37')
    print('----------------------------------')
    import operator

    bindings = dict(x=5, y=10, blah=15, add=operator.add)
    expression = ['add', ['add', 22, 'y'], 'x']
    print(evaluate(expression, bindings))

    # Test 4
    print('--------------Test 5--------------')
    print('Result should equal 64')
    print('----------------------------------')
    import operator

    bindings = dict(x=5, y=10, blah=15, add=operator.add)
    expression = ['add', ['add', 22, 'y'], ['add', 22, 'y']]
    print(evaluate(expression, bindings))


if __name__ == "__main__":
    main()
