"""Create a belief network with five random variables A, B, C, D, and E with the following properties:

A and C are independent of any other variable (and each other). D and E depend on each other unless B is given (
observed). Hints The first property is expressing absolute independence of A and C from any other variable. In other
words, no arc comes in or goes out of these nodes. The second property is expressing conditional independence. It
means D and E are independent of each other when B is given (observed). The second property is achieved by the right
topology (arrows/parents) and a set of different CPTS in D and E. [If the CPTs are the same, even though the topology
allows dependence, they remain independent.]"""


network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2
        }},

    'B': {
        'Parents': [],
        'CPT': {
            (): 0.2
        }},

    'C': {
        'Parents': [],
        'CPT': {
            (): 0.2
        }},

    'D': {
        'Parents': ['B'],
        'CPT': {
            (True,): 0.50,
            (False,): 0.25,
        }},

    'E': {
        'Parents': ['B'],
        'CPT': {
            (True,): 0.90,
            (False,): 0.05,
        }}
}


def main():
    # Test 1
    print('--------------Test 1--------------')
    print(sorted(network.keys()))


if __name__ == "__main__":
    main()
