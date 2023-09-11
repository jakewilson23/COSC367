"""Provide an instance of CSP class named cryptic_puzzle that represents the following cryptarithmetic problem:

    two
  + two
  ------
   four

  The objective is to find what digit each letter can represent. Each letter is associated to
  exactly one digit and each digit is associated to up to one letter. The letters on the left (t and f) cannot be
  zero (if they were they wouldn't be there). This problem is depicted in the lecture notes (as an additional example)

Important: Your solution must also contain the solution to two earlier questions: the functions generate_and_test and
arc_consistent.

Notes

If you wish, you can use the code template provided in the answer box. Use lower case letters for variable names. The
domains of t, w, o, f, u, and r must be the set of integers from 0 to 9 (inclusive). Enforce the requirements of the
problem by adding appropriate constraints. The arc consistency algorithm will automatically trim the domains. You
need to define some auxiliary variables to take care of the carry overs. In the template provided, these are called
c1 and c2. The CSP object must contain a number of constraints describing the given problem. One of the constraints,
should require that the variable t, w, o, f, u, r must have different values. One way of implementing this is to use
a set. For example, consider what the expression len({a, b}) evaluates to if a and b have the same value. All the
constraints in this problem can be added as a number of lambda expression (one line each). A lambda expression
evaluates to a function object without a name (an anonymous function). If you think for some of the constraints you
need to write more code, you can define a named function outside and then include the name of the function in the set
of constraints. The answer must include all the required import statements. Notice that we first make an
arc-consistent version of the network (using the function you provide) and then solve the instance using
generate-and-test. Without making the network arc-consistent, the generate-and-test algorithm takes a long time (
about 30 seconds on a mid-range desktop computer) to find all the solutions. which is not allowed on the server.
However, once the network is made arc-consistent, all the solutions can be found in a few seconds."""

import itertools, copy
from csp import scope, satisfies, CSP


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

def generate_and_test(csp):
    names, domains = zip(*csp.var_domains.items())
    for values in itertools.product(*domains):
        assignment = {x: v for x, v in zip(names, values)}
        if all(satisfies(assignment, constraint) for constraint in csp.constraints):
            yield assignment


domains = {x: set(range(10)) for x in "twofur"}
domains.update({'c1': {0, 1}, 'c2': {0, 1}})  # domains of the carry overs

cryptic_puzzle = CSP(
    var_domains=domains,
    constraints={
        lambda t, w, o, f, u, r: len({t, w, o, f, u, r}) == len([t, w, o, f, u, r]),
        lambda o, r, c1: o + o == r + 10 * c1,  # one of the constraints
        lambda w, u, c1, c2: c1 + w + w == u + 10 * c2,
        lambda t, o, f, c2: c2 + t + t == (f * 10) + o,
        lambda f: f == 1,
        lambda t: t * 2 >= 10
        # add more constraints
    })


def main():
    # Test 1
    print(set("twofur") <= set(cryptic_puzzle.var_domains.keys()))
    print(all(len(cryptic_puzzle.var_domains[var]) == 10 for var in "twofur"))

    # Test 2
    new_csp = arc_consistent(cryptic_puzzle)
    print(sorted(new_csp.var_domains['r']))

    # Test 3
    new_csp = arc_consistent(cryptic_puzzle)
    print(sorted(new_csp.var_domains['w']))

    # Test 4
    new_csp = arc_consistent(cryptic_puzzle)
    solutions = []
    for solution in generate_and_test(new_csp):
        solutions.append(sorted((x, v) for x, v in solution.items()
                                if x in "twofur"))
    print(len(solutions))
    solutions.sort()
    print(solutions[0])
    print(solutions[5])


if __name__ == "__main__":
    main()
