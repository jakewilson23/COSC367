"""Write a function accuracy(classifier, inputs, expected_outputs) that passes each input in the sequence of inputs
to the given classifier function (e.g. a perceptron) and compares the predictions with the expected outputs. The
function must return the accuracy of the classifier on the given data. Accuracy must be a number between 0 and 1 (
inclusive).

Note: an important application of a metric such as accuracy is to see how a classifier (e.g. a spam filter) performs
on unseen data. In this case, the inputs must be some data that it has not seen during training but has been labeled
by humans."""


def accuracy(classifier, inputs, expected_outputs):
    num_correct = 0
    for i in range(len(inputs)):
        if classifier(inputs[i]) == expected_outputs[i]:
            num_correct += 1
    return num_correct / len(inputs)


def main():
    from q3 import construct_perceptron
    # Test 1
    print('--------------Test 1--------------')
    print('Result should equal:')
    print('0.75')
    print('----------------------------------')
    perceptron = construct_perceptron([-1, 3], 2)
    inputs = [[1, -1], [2, 1], [3, 1], [-1, -1]]
    targets = [0, 1, 1, 0]

    print(accuracy(perceptron, inputs, targets))


if __name__ == "__main__":
    main()
