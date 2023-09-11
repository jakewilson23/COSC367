import itertools, copy
from csp import *

"""Write a function arc_consistent that takes a CSP object and returns a new CSP object that is arc consistent 
(and also consequently domain consistent). The general arc consistency (GAC) algorithm is in the lecture notes and 
also available in section 4.4 of the textbook.

If you wish, you can build your solution upon the partial code preloaded in the answer box. The code closely follows 
the pseudocode including the name of the variables."""


def arc_consistent(csp):
    csp = copy.deepcopy(csp)
    to_do = {(x, c) for c in csp.constraints for x in scope(c)}  # COMPLETE
    while to_do:
        x, c = to_do.pop()
        ys = scope(c) - {x}
        new_domain = set()
        for xval in csp.var_domains[x]:  # COMPLETE
            assignment = {x: xval}
            for yvals in itertools.product(*[csp.var_domains[y] for y in ys]):
                assignment.update({y: yval for y, yval in zip(ys, yvals)})
                if satisfies(assignment, c):  # COMPLETE
                    new_domain.add(xval)  # COMPLETE
                    break
        if csp.var_domains[x] != new_domain:
            for cprime in set(csp.constraints) - {c}:
                if x in scope(cprime):
                    for z in scope(cprime):  # COMPLETE
                        if x != z:  # COMPLETE
                            to_do.add((z, cprime))
            csp.var_domains[x] = new_domain  # COMPLETE
    return csp


def main():
    # Test 1
    simple_csp = CSP(
        var_domains={x: set(range(1, 5)) for x in 'abc'},
        constraints={
            lambda a, b: a < b,
            lambda b, c: b < c,
        })

    csp = arc_consistent(simple_csp)
    for var in sorted(csp.var_domains.keys()):
        print("{}: {}".format(var, sorted(csp.var_domains[var])))

    # Test 2
    csp = CSP(var_domains={x: set(range(10)) for x in 'abc'},
              constraints={lambda a, b, c: 2 * a + b + 2 * c == 10})

    csp = arc_consistent(csp)
    for var in sorted(csp.var_domains.keys()):
        print("{}: {}".format(var, sorted(csp.var_domains[var])))


if __name__ == "__main__":
    main()
