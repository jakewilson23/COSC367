"""Consider a medical test for a certain disease that is very rare, striking only 1 in 100,000 people. Suppose the
probability of testing positive if the person has the disease is 99%, as is the probability of testing negative when
the person does not have the disease.

Express these facts in the form of a (causal) belief network. Use variable names 'Disease' and 'Test'. Assign the
network to the variable network.

Important: Supply the query function and all the functions and modules it depends on (e.g. joint_prob) from the
previous questions.

Comment: After solving the problem, you may find the value of P(having disease| positive test), which is essentially
the precision of the test, counter-intuitive; one may expect this value to be much higher. Observe that the
probability of returning positive regardless of the disease is about 1%, which is quite high compared to how rare the
disease is. A good test for this rare disease must have a much higher specificity, which is the probability of
returning negative when the person does not have the disease. You can explore this by changing the values in the CPTs
(more specifically, making the value corresponding to Disease being False in the CPT of Test smaller)."""


from q2 import *

network = {
    'Disease': {
        'Parents': [],
        'CPT': {
            (): 0.00001
        }},

    'Test': {
        'Parents': ['Disease'],
        'CPT': {
            (True,): 0.99,
            (False,): 0.01,
        }},
}


def main():
    # Test 1
    print('--------------Test 1--------------')
    answer = query(network, 'Disease', {'Test': True})
    print("The probability of having the disease\n"
          "if the test comes back positive: {:.8f}"
          .format(answer[True]))

    # Test 2
    print('--------------Test 2--------------')
    answer = query(network, 'Disease', {'Test': False})
    print("The probability of having the disease\n"
          "if the test comes back negative: {:.8f}"
          .format(answer[True]))


if __name__ == "__main__":
    main()
