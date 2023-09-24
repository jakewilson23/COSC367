## Representation of expressions
Mathematical expressions can be seen as trees. For example the expression 4*y - 3 can be seen as the following tree.
```python
      -
     / \
    / 	\
   *     3
  / \
 /   \
4     y
```

We need an easy way of representing these trees in Python. A natural choice is to use nested lists where each list is a function application in prefix notation. For example the above tree can be represented as ['-', ['*', 4, 'y'], 3]

## Specification
We define an object to be an expression if it is either:
- a constant leaf: a Python integer (for example 3);
- a variable leaf: a Python string (for example 'y') from a pre-specified set of leaf symbols;
- a Python list such that:
  * the list has exactly 3 elements; and
  * the first element is a string (for example '*') from a pre-specified set of function symbols; and
  * the remaining two elements of the list are expressions themselves; these two serve as the arguments of the function.

Note that for simplicity we are assuming that all functions in these expressions are binary; that is, they take exactly two arguments.