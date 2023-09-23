"""Consider two medical tests, A and B, for a virus. Test A is 95% effective at recognising the virus when the virus
is present, but has a 10% false positive rate (indicating that the virus is present, when it is not). Test B is 90%
effective at recognizing the virus, but has a 5% false positive rate. The two tests use independent methods of
identifying the virus. The virus is carried by 1% of all people.

Express these facts in the form of a (causal) belief network. Use variable names 'A',  'B', and 'Virus'. Assign the
network to the variable network.

Important: Supply the query function and all the functions and modules it depends on (e.g. joint_prob) from the
previous questions."""


from q2 import *

network = {
    'Virus': {
        'Parents': [],
        'CPT': {
            (): 0.01
        }},

    'A': {
        'Parents': ['Virus'],
        'CPT': {
            (True,): 0.95,
            (False,): 0.10,
        }},

    'B': {
        'Parents': ['Virus'],
        'CPT': {
            (True,): 0.90,
            (False,): 0.05,
        }}
}


def main():
    # Test 1
    print('--------------Test 1--------------')
    answer = query(network, 'Virus', {'A': True})
    print("The probability of carrying the virus\n"
          "if test A is positive: {:.5f}"
          .format(answer[True]))

    # Test 2
    print('--------------Test 2--------------')
    answer = query(network, 'Virus', {'B': True})
    print("The probability of carrying the virus\n"
          "if test B is positive: {:.5f}"
          .format(answer[True]))


if __name__ == "__main__":
    main()
