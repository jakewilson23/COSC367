"""Write a function learn_likelihood(file_name, pseudo_count=0) that takes the file name of a training set (for the
spam detection problem) and an optional pseudo-count parameter and returns a sequence of pairs of likelihood
probabilities. As described in the representation of likelihood, the length of the returned sequence (list or tuple)
must be 12. Each element in the sequence is a pair (tuple) of real numbers such that likelihood[i][False] is P(X[
i]=true|Spam=false) and likelihood[i][True] is P(X[i]=true|Spam=true )."""

import csv


def learn_likelihood(file_name, pseudo_count=0):
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]
    result = []
    for i in range(12):
        result.append([pseudo_count, pseudo_count])
    spam_count = 0
    for email in training_examples[1:]:
        spam = int(email[-1])
        for i in range(12):
            result[i][spam] += int(email[i])
        spam_count += spam
    for i in range(len(result)):
        result[i][False] /= ((len(training_examples) - 1) - spam_count + 2 * pseudo_count)
        result[i][True] /= (spam_count + 2 * pseudo_count)
    return result


def main():
    # Test 1
    print('--------------Test 1--------------')
    print('Result should equal')
    print('12')
    print('[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]')
    print('----------------------------------')

    likelihood = learn_likelihood("spam-labelled.csv")
    print(len(likelihood))
    print([len(item) for item in likelihood])

    # Test 2
    print('--------------Test 2--------------')
    print('Result should equal')
    print('P(X1=True | Spam = False) = 0.35570')
    print('P(X1=False | Spam = False) = 0.64430')
    print('P(X1=True | Spam = True ) = 0.66667')
    print('P(X1=False | Spam = True ) = 0.33333')
    print('----------------------------------')

    likelihood = learn_likelihood("spam-labelled.csv")
    print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
    print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
    print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
    print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))

    # Test 3
    print('--------------Test 3--------------')
    print('Result should equal')
    print("With Laplacian smoothing:")
    print('P(X1=True | Spam=False) = 0.35762')
    print('P(X1=False| Spam=False) = 0.64238')
    print('P(X1=True | Spam=True ) = 0.66038')
    print('P(X1=False| Spam=True ) = 0.33962')
    print('----------------------------------')

    likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)
    print("With Laplacian smoothing:")
    print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
    print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
    print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
    print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))


if __name__ == "__main__":
    main()
