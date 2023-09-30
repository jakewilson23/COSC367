"""Write a function learn_prior(file_name, pseudo_count=0) that takes the file name of the training set and an
optional pseudo-count parameter and returns a real number that is the prior probability of spam being true. The
parameter pseudo_count is a non-negative integer and it will be the same for all the attributes and all the values.

Notes

Pseudo-counts are described in the lecture notes and section 7.2.3 of the textbook.
Although you see high values of pseudo-count in some test cases, in practice small values are mostly used. """

import csv


def learn_prior(file_name, pseudo_count=0):
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]
    num_spam = 0
    for email in training_examples:
        if email[-1] == '1':
            num_spam += 1
    return (num_spam + pseudo_count) / ((len(training_examples) - 1) + 2 * pseudo_count)


def main():
    # Test 1
    print('--------------Test 1--------------')
    print('Result should equal')
    print('Prior probability of spam is 0.25500.')
    print('----------------------------------')
    prior = learn_prior("spam-labelled.csv")
    print("Prior probability of spam is {:.5f}.".format(prior))

    # Test 2
    print('--------------Test 2--------------')
    print('Result should equal')
    print('Prior probability of not spam is 0.74500.')
    print('----------------------------------')
    prior = learn_prior("spam-labelled.csv")
    print("Prior probability of not spam is {:.5f}.".format(1 - prior))

    # Test 3
    print('--------------Test 3--------------')
    print('Result should equal')
    print('0.25743')
    print('----------------------------------')
    prior = learn_prior("spam-labelled.csv", pseudo_count=1)
    print(format(prior, ".5f"))

    # Test 4
    print('--------------Test 4--------------')
    print('Result should equal')
    print('0.25980')
    print('----------------------------------')
    prior = learn_prior("spam-labelled.csv", pseudo_count=2)
    print(format(prior, ".5f"))

    # Test 5
    print('--------------Test 5--------------')
    print('Result should equal')
    print('0.27727')
    print('----------------------------------')
    prior = learn_prior("spam-labelled.csv", pseudo_count=10)
    print(format(prior, ".5f"))

    # Test 6
    print('--------------Test 6--------------')
    print('Result should equal')
    print('0.37750')
    print('----------------------------------')
    prior = learn_prior("spam-labelled.csv", pseudo_count=100)
    print(format(prior, ".5f"))

    # Test 7
    print('--------------Test 7--------------')
    print('Result should equal')
    print('0.47773')
    print('----------------------------------')
    prior = learn_prior("spam-labelled.csv", pseudo_count=1000)
    print(format(prior, ".5f"))


if __name__ == "__main__":
    main()
