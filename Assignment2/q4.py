"""Write a function random_expression(function_symbols, leaves, max_depth) that randomly generates an expression. The
function takes the following arguments:

function_symbols: a list of function symbols (strings) leaves: a list of constant and variable leaves (integers and
strings) max_depth: a non-negative integer that specifies the maximum depth allowed for the generated expression. The
function will be called 10,000 times to generate these many expressions. Then the following tests are performed on
the generated expressions:

All the generated expressions must be valid expressions constructed from the given function symbols and leaves. Out
of the 10,000 generated expressions, at least 1000 must be syntactically distinct. The semantic of expressions is
disregarded when testing for distinctness. For example ['+', 1, 2] and ['+', 2, 1] will be regarded as different
expressions. Out of the 10,000 generated expressions, at least 100 must be of depth 0, at least 100 of depth 1, ...,
and at least 100 must be of depth max_depth (which is set to 4 in the test cases). Notes This function is recursive.
I suggest an implementation along these lines: Toss a coin. If it's a head (or if some other condition that you have
to determine is satisfied) return a leaf node, otherwise return a random expression tree (a 3-element list). If the
latter, you also need to randomly generate its two arguments. Consider using functions provided in the random module.
You can implement this function in about 15 lines of code In order to be able to replicate your results (for example
for debugging purposes), consider using random.seed(some_integer) which will cause the generators to always produce
the same sequence of random numbers and as a result your program will always produce the same output. It is
recommended that you test your code locally. You should consider developing your own test code that checks the stated
requirements."""

from q1 import is_valid_expression as _is_valid_expression
from q2 import depth
from random import randint, choice


def random_expression(function_symbols, leaves, max_depth):
    leaf_or_tree = randint(0, 1)
    if leaf_or_tree == 0:  # Generate a Leaf Node
        return choice(leaves)
    else:  # Generate a Random Expression tree in the form of a list
        random_function = choice(function_symbols)
        if max_depth != 1:  # not at max depth
            random_expression_one = random_expression(function_symbols, leaves, max_depth - 1)
            random_expression_two = random_expression(function_symbols, leaves, max_depth - 1)
        else:
            random_expression_one = choice(leaves)
            random_expression_two = choice(leaves)
        tree_node = [random_function, random_expression_one, random_expression_two]
        return tree_node


def main():
    # Test 1
    print('--------------Test 1--------------')
    print('Result should equal OK')
    print('----------------------------------')
    # All the generated expressions must be valid

    function_symbols = ['f', 'g', 'h']
    constant_leaves = list(range(-2, 3))
    variable_leaves = ['x', 'y', 'i']
    leaves = constant_leaves + variable_leaves
    max_depth = 4

    for _ in range(10000):
        expression = random_expression(function_symbols, leaves, max_depth)
        if not _is_valid_expression(expression, function_symbols, leaves):
            print("The following expression is not valid:\n", expression)
            break
    else:
        print("OK")

    '''function_symbols = ['f', 'g', 'h']
    constant_leaves = list(range(-2, 3))
    variable_leaves = ['x', 'y', 'i']
    leaves = constant_leaves + variable_leaves
    max_depth = 4
    for _ in range(20):
        test = random_expression(function_symbols, leaves, max_depth)
        print('Random Expression: ', test)
        print('Depth: ', depth(test))'''


if __name__ == "__main__":
    main()
