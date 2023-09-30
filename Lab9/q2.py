"""Write a function posterior(prior, likelihood, observation) that returns the posterior probability of the class
variable being true, given the observation; that is, it returns p(Class=true|observation). The argument observation
is a tuple of n Booleans such that observation[i] is the observed value (True or False) for the input feature X[i].
The arguments prior and likelihood are as described above.

Notes

Example 9.36 in the textbook is relevant. The model used in the test cases is according to this network. You can
download and explore the model in the belief network applet."""


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


def main():
    # Test 1
    print('--------------Test 1--------------')
    print('Result should equal')
    print('P(C=False|observation) is approximately 0.00248')
    print('P(C=True |observation) is approximately 0.99752')
    print('----------------------------------')
    prior = 0.05
    likelihood = ((0.001, 0.3), (0.05, 0.9), (0.7, 0.99))

    observation = (True, True, True)

    class_posterior_true = posterior(prior, likelihood, observation)
    print("P(C=False|observation) is approximately {:.5f}"
          .format(1 - class_posterior_true))
    print("P(C=True |observation) is approximately {:.5f}"
          .format(class_posterior_true))

    # Test 2
    print('--------------Test 2--------------')
    print('Result should equal')
    print('P(C=False|observation) is approximately 0.29845')
    print('P(C=True |observation) is approximately 0.70155')
    print('----------------------------------')
    prior = 0.05
    likelihood = ((0.001, 0.3), (0.05, 0.9), (0.7, 0.99))

    observation = (True, False, True)

    class_posterior_true = posterior(prior, likelihood, observation)
    print("P(C=False|observation) is approximately {:.5f}"
          .format(1 - class_posterior_true))
    print("P(C=True |observation) is approximately {:.5f}"
          .format(class_posterior_true))

    # Test 3
    print('--------------Test 3--------------')
    print('Result should equal')
    print('P(C=False|observation) is approximately 0.99454')
    print('P(C=True |observation) is approximately 0.00546')
    print('----------------------------------')
    prior = 0.05
    likelihood = ((0.001, 0.3), (0.05, 0.9), (0.7, 0.99))

    observation = (False, False, True)

    class_posterior_true = posterior(prior, likelihood, observation)
    print("P(C=False|observation) is approximately {:.5f}"
          .format(1 - class_posterior_true))
    print("P(C=True |observation) is approximately {:.5f}"
          .format(class_posterior_true))

    # Test 4
    print('--------------Test 4--------------')
    print('Result should equal')
    print('P(C=False|observation) is approximately 0.99987')
    print('P(C=True |observation) is approximately 0.00013')
    print('----------------------------------')
    prior = 0.05
    likelihood = ((0.001, 0.3), (0.05, 0.9), (0.7, 0.99))

    observation = (False, False, False)

    class_posterior_true = posterior(prior, likelihood, observation)
    print("P(C=False|observation) is approximately {:.5f}"
          .format(1 - class_posterior_true))
    print("P(C=True |observation) is approximately {:.5f}"
          .format(class_posterior_true))


if __name__ == "__main__":
    main()
