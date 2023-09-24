## Evaluation of expressions
All expressions in this assignment evaluate to integers. These are the rules of evaluation:

- A constant leaf (an integer) evaluates to itself.
- A variable leaf (a string) is looked up in a dictionary of bindings which maps leaf symbols (strings) to integers.
- For a list, the following steps are taken:
  * The value of the function symbol is looked up in a dictionary of bindings. The function symbol are mapped to a binary function that takes two integers as its arguments and returns an integer.
  * The two remaining elements are evaluated.
  * The function is applied to the value of the two arguments. The returned value is the value of the list.