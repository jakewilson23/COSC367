"""Write a function nb_classify(prior, likelihood, input_vector) that takes the learnt prior and likelihood
probabilities and classifies an (unseen) input vector. The input vector will be a tuple of 12 integers (each 0 or 1)
corresponding to attributes X1 to X12. The function should return a pair (tuple) where the first element is either
"Spam" or "Not Spam" and the second element is the certainty. The certainty is the (posterior) probability of spam
when the instance is classified as spam, or the probability of 'not-spam' otherwise. If spam and 'not spam' are
equally likely (i.e. p=0.5) then choose 'not spam'.

This is a very simple function to implement as it only wraps the posterior function developed earlier.

Supply the following functions you developed earlier: learn_prior and learn_likelihood. Also include import
statements and any other function that you may be using (e.g. posterior)."""

import csv


def nb_classify(prior, likelihood, input_vector):
    certainty = posterior(prior, likelihood, input_vector)
    if certainty > (1 - certainty):
        return ("Spam", certainty)
    else:
        return ("Not Spam", (1 - certainty))


def posterior(prior, likelihood, observation):
    true_prior = prior
    false_prior = 1 - prior
    for i in range(len(observation)):
        if observation[i]:
            true_prior *= likelihood[i][True]
            false_prior *= likelihood[i][False]
        else:
            true_prior *= 1 - likelihood[i][True]
            false_prior *= 1 - likelihood[i][False]
    return true_prior / (true_prior + false_prior)


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
    print('Prediction: Not Spam, Certainty: 0.99351')
    print('Prediction: Spam, Certainty: 0.57441')
    print('Prediction: Spam, Certainty: 0.59337')
    print('Prediction: Spam, Certainty: 0.83465')
    print('Prediction: Not Spam, Certainty: 0.99140')
    print('----------------------------------')
    prior = learn_prior("spam-labelled.csv")
    likelihood = learn_likelihood("spam-labelled.csv")

    input_vectors = [
        (1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0),
        (0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1),
        (1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1),
        (1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1),
        (0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0),
    ]

    predictions = [nb_classify(prior, likelihood, vector)
                   for vector in input_vectors]

    for label, certainty in predictions:
        print("Prediction: {}, Certainty: {:.5f}"
              .format(label, certainty))

    # Test 2
    print('--------------Test 2--------------')
    print('Result should equal')
    print('Prediction: Not Spam, Certainty: 0.99213')
    print('Prediction: Spam, Certainty: 0.57759')
    print('Prediction: Spam, Certainty: 0.59073')
    print('Prediction: Spam, Certainty: 0.83059')
    print('Prediction: Not Spam, Certainty: 0.98989')
    print('----------------------------------')
    prior = learn_prior("spam-labelled.csv", pseudo_count=1)
    likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)

    input_vectors = [
        (1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0),
        (0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1),
        (1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1),
        (1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1),
        (0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0),
    ]

    predictions = [nb_classify(prior, likelihood, vector)
                   for vector in input_vectors]

    for label, certainty in predictions:
        print("Prediction: {}, Certainty: {:.5f}"
              .format(label, certainty))


if __name__ == "__main__":
    main()
