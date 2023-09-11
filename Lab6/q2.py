from csp import CSP

"""Make the following CSP arc consistent by modifying the code (if necessary) and pasting the result in the answer box.

from csp import CSP

crossword_puzzle = CSP(
    var_domains={
        # read across:
        'across1': set("ant big bus car has".split()),
        'across3': set("book buys hold lane year".split()),
        'across4': set("ant big bus car has".split()),
        # read down:
        'down1': set("book buys hold lane year".split()),
        'down2': set("ginger search symbol syntax".split()),
        },
    constraints={
        lambda across1, down1: across1[0] == down1[0],
        lambda down1, across3: down1[2] == across3[0],
        lambda across1, down2: across1[2] == down2[0],
        lambda down2, across3: down2[2] == across3[2],
        lambda down2, across4: down2[4] == across4[0],
        })
Notes:

This CSP instance is for a crossword puzzle (visualised here). In the instance presented above, the domains contain 
only words that have the same length as the corresponding field in the puzzle. Another approach would be to have all 
the given words in all the domains and provide additional length constraints for variables 
(e.g. lambda across1: len(across1) == 3).
Start by copying the above program into your editor. Modify the domains and then paste in the result. Remember to 
include the import statement in your answer.
The expression set("ant big bus car has".split()) is equivalent to {"ant", "big", "bus", "car", "has"}. However, it 
emphasises the fact that we can use any expression that evaluates to a set of values and that these values need not 
be hard-coded. For example we could use an expression to fetch the words from a file, database, web, or other sources.
 In your answer, you are free to use any expression you wish as long as it evaluates to the correct set of values."""

crossword_puzzle = CSP(
    var_domains={
        # read across:
        'across1': set("bus has".split()),
        'across3': set("lane year".split()),
        'across4': set("ant car".split()),
        # read down:
        'down1': set("buys hold".split()),
        'down2': set("search syntax".split()),
    },
    constraints={
        lambda across1, down1: across1[0] == down1[0],
        lambda down1, across3: down1[2] == across3[0],
        lambda across1, down2: across1[2] == down2[0],
        lambda down2, across3: down2[2] == across3[2],
        lambda down2, across4: down2[4] == across4[0],
    })

print(sorted(crossword_puzzle.var_domains['across1']))
