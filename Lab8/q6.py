"""Consider the belief network given in the answer box with three random variables A, B, and C. The topology of the
network implies the following:

A influences B
A influences C
B and C are conditionally independent given A
Without modifying the topology of the network, change the CPTs such that B and C become independent (unconditionally).

Notes You can achieve this by making B independent of A or by making C independent of A. While you could do this by
simply removing one of the arcs (i.e. parents), here you are being asked to do this without changing the
topology/parents and by only changing the CPTs. The point of this exercise is to show that arcs allow dependence but
do not enforce it. We can have an arc from A to B and still have the CPTs in B in a way that makes it independent of
A. When hand-designing belief networks, there is no point in changing CPTs in order to make two variables
independent; instead you can (and should) modify the topology. When the topology of the network is hand-designed but
the CPTs are obtained by looking at data (machine learning), then the values obtained for CPTs may effectively make
two variables independent. For example in this network if A is a disease and B and C are some tests, when designing
the topology, you may consider A as influencing both B and C but after you use data to obtain the values in CPTs,
in turns out that B is independent of A (i.e. does not provide useful information)."""


network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
        }},
    'B': {
        'Parents': ['A'],
        'CPT': {
            (False,): 0.2,
            (True,): 0.2
        }},

    'C': {
        'Parents': ['A'],
        'CPT': {
            (False,): 0.4,
            (True,): 0.4
        }},
}


def main():
    # Test 1
    print('--------------Test 1--------------')
    print(sorted(network.keys()))


if __name__ == "__main__":
    main()
