import re


def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 2 Aug 2021

    """
    ATOM = r"[a-z][a-zA-Z\d_]*"
    HEAD = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")


def forward_deduce(kb_string):
    """Write a function forward_deduce that takes the string of a knowledge base containing propositional definite
    clauses and returns a (complete) set of atoms (strings) that can be derived (to be true) from the knowledge base."""
    derive_set = []
    kb_clause_list = list(clauses(kb_string))
    change_made = True
    while change_made:
        change_made = False
        for clause in kb_clause_list:
            if not clause[1]:       # clause has no body eg [('b', [])] b has no body
                derive_set.append(clause[0])
                kb_clause_list.remove(clause)
                change_made = True
            else:                   # clause has one or more bodies
                all_atoms_derive = True
                for atom in clause[1]:  # check if each body is in the derive list/set
                    if atom not in derive_set:
                        all_atoms_derive = False
                if all_atoms_derive:    # if all bodys are in derive set, then append atom to derive set
                    derive_set.append(clause[0])
                    kb_clause_list.remove(clause)
                    change_made = True
    return set(derive_set)



def main():
    kb = """
    a :- b.
    b.
    """

    print(", ".join(sorted(forward_deduce(kb))))

    kb = """
    good_programmer :- correct_code.
    correct_code :- good_programmer.
    """

    print(", ".join(sorted(forward_deduce(kb))))

    kb = """
    a :- b, c.
    b :- d, e.
    b :- g, e.
    c :- e.
    d.
    e.
    f :- a,
         g.
    """

    print(", ".join(sorted(forward_deduce(kb))))

if __name__ == "__main__":
    main()
