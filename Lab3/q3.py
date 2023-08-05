import itertools


def atoms(formula):
    """Takes a formula in the form of a lambda expression and returns a set of
    atoms used in the formula. The atoms are parameter names represented as
    strings.
    """

    return {atom for atom in formula.__code__.co_varnames}


def value(formula, interpretation):
    """Takes a formula in the form of a lambda expression and an interpretation
    in the form of a dictionary, and evaluates the formula with the given
    interpretation and returns the result. The interpretation may contain
    more atoms than needed for the single formula.
    """
    arguments = {atom: interpretation[atom] for atom in atoms(formula)}
    return formula(**arguments)


def interpretations(atoms):
    """Takes a non-empty set of atoms and returns the list of all possible interpretations for the given atoms. Each
    interpretation is a dictionary where the keys are all the atoms and each value is either True or False. The
    output list must be ordered such that for every two interpretations that are only different in the value of one
    atom, the one with value of False comes before the other one"""
    atom_list = sorted(list(atoms))
    result = []
    binary_list = list(itertools.product([0, 1], repeat=len(atoms)))
    for dict_count, item in enumerate(binary_list):
        temp_dict = {}
        for atom_count, atom in enumerate(item):
            if atom == 0:
                temp_dict[atom_list[atom_count]] = False
            else:
                temp_dict[atom_list[atom_count]] = True
        result.append(temp_dict)
    return result


def models(knowledge_base):
    """Write a function models(knowledge_base) that takes a knowledge base in the form of a non-empty set of logical
    formulas and returns a (possibly empty) list of interpretations that are the models of the knowledge base. Each
    logical formula is represented as a lambda expression that evaluates to a boolean value. The parameters of the
    lambda expression are the atoms used in the formula. For example lambda a, b: a and b is a compound proposition
    that involves atoms a and b and the formula is the logical conjunction of the two. The keys of the dictionaries
    and the output list must follow the same order established in the previous question (interpretations)."""
    models_results = []
    all_atoms_set = set([])
    for formula in knowledge_base:
        all_atoms_set = all_atoms_set | atoms(formula)
    inters = interpretations(all_atoms_set)
    for inter in inters:
        formula_list = []
        for formula in knowledge_base:
            formula_list.append(value(formula, inter))
        if all(formula_list):
            models_results.append(inter)
    return models_results


def main():
    knowledge_base = {
        lambda a, b: a and not b,
        lambda c: c
    }

    print(models(knowledge_base))

    knowledge_base = {
        lambda a, b: a and not b,
        lambda c, d: c or d
    }

    for interpretation in models(knowledge_base):
        print(interpretation)


if __name__ == "__main__":
    main()
