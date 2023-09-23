"""Write a function joint_prob(network, assignment) that takes a belief network and a complete assignment of all the
variables in the network, and returns the probability of the assignment. The data structure of the network is as
described above. The assignment is a dictionary where keys are the variable names and the values are either True or
False.

Note that no inference is required here. You only need to compute the product (multiplication) of the probability of
a variable given its parent(s), repeated over all the variables in the network."""


def joint_prob(network, assignment):
    p = 1
    for node in assignment:
        if not network[node]['Parents']:
            for value in network[node]['CPT']:
                node_value = network[node]['CPT'][value]
            if assignment[node]:
                p *= node_value
            else:
                p *= (1 - node_value)
        else:
            node_bool = False
            if assignment[node]:
                node_bool = True
            parent_bool_list = []
            for parent in network[node]['Parents']:
                if parent in assignment:
                    parent_bool_list.append(assignment[parent])
            for CPT in network[node]['CPT']:
                temp_CPT_list = list(CPT)
                if temp_CPT_list == parent_bool_list:
                    if node_bool:
                        p *= network[node]['CPT'][CPT]
                    else:
                        p *= (1 - network[node]['CPT'][CPT])
    return p


def main():
    # Test 1
    print('--------------Test 1--------------')
    network = {
        'A': {
            'Parents': [],
            'CPT': {
                (): 0.2
            }},
    }

    p = joint_prob(network, {'A': True})
    print("{:.5f}".format(p))

    # Test 2
    print('--------------Test 2--------------')
    network = {
        'A': {
            'Parents': [],
            'CPT': {
                (): 0.2
            }},
    }

    p = joint_prob(network, {'A': False})
    print("{:.5f}".format(p))

    # Test 3
    print('--------------Test 3--------------')
    network = {
        'A': {
            'Parents': [],
            'CPT': {
                (): 0.1
            }},

        'B': {
            'Parents': ['A'],
            'CPT': {
                (True,): 0.8,
                (False,): 0.7,
            }},
    }

    p = joint_prob(network, {'A': False, 'B': True})
    print("{:.5f}".format(p))

    # Test 4
    print('--------------Test 4--------------')
    network = {
        'A': {
            'Parents': [],
            'CPT': {
                (): 0.1
            }},

        'B': {
            'Parents': ['A'],
            'CPT': {
                (True,): 0.8,
                (False,): 0.7,
            }},
    }

    p = joint_prob(network, {'A': False, 'B': False})
    print("{:.5f}".format(p))
    p = joint_prob(network, {'A': False, 'B': True})
    print("{:.5f}".format(p))
    p = joint_prob(network, {'A': True, 'B': False})
    print("{:.5f}".format(p))
    p = joint_prob(network, {'A': True, 'B': True})
    print("{:.5f}".format(p))

    # Test 5
    print('--------------Test 5--------------')
    network = {
        'Burglary': {
            'Parents': [],
            'CPT': {
                (): 0.001
            }},

        'Earthquake': {
            'Parents': [],
            'CPT': {
                (): 0.002,
            }},
        'Alarm': {
            'Parents': ['Burglary', 'Earthquake'],
            'CPT': {
                (True, True): 0.95,
                (True, False): 0.94,
                (False, True): 0.29,
                (False, False): 0.001,
            }},

        'John': {
            'Parents': ['Alarm'],
            'CPT': {
                (True,): 0.9,
                (False,): 0.05,
            }},

        'Mary': {
            'Parents': ['Alarm'],
            'CPT': {
                (True,): 0.7,
                (False,): 0.01,
            }},
    }

    p = joint_prob(network, {'John': True, 'Mary': True,
                             'Alarm': True, 'Burglary': False,
                             'Earthquake': False})
    print("{:.8f}".format(p))


if __name__ == "__main__":
    main()
