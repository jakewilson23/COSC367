import itertools


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


def main():
    atoms = {'q', 'p'}
    for i in interpretations(atoms):
        print(i)

    atoms = {'human', 'mortal', 'rational'}
    for i in interpretations(atoms):
        print(i)


if __name__ == "__main__":
    main()
