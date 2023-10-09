"""Write a function learn_perceptron_parameters(weights, bias, training_examples, learning_rate, max_epochs) that
adjusts the weights and bias by iterating through the training data and applying the perceptron learning rule. The
function must return a pair (2-tuple) where the first element is the vector (list) of adjusted weights and second
argument is the adjusted bias.

The parameters of the function are:

weights: an array (list) of initial weights of length n

bias: a scalar number which is the initial bias

training_examples: a list of training examples where each example is a pair. The first element of the pair is a
vector (tuple) of length n. The second element of the pair is an integer which is either 0 or 1 representing the
negative or positive class correspondingly.

learning_rate: a positive number representing eta in the learning
equations of perceptron.

max_epochs: the maximum number of times the learner is allowed to iterate through all the
training examples."""


def learn_perceptron_parameters(weights, bias, training_examples, learning_rate, max_epochs):
    working_weights = weights
    working_bias = bias
    example_iterator = 0
    needed_updating = True
    while needed_updating and example_iterator < max_epochs:
        needed_updating = False
        for weight, target in training_examples:
            y = working_bias + (working_weights[0] * weight[0]) + (working_weights[1] * weight[1])
            if y >= 0:
                y = 1
            else:
                y = 0
            if y != target:
                working_weights[0] = working_weights[0] + learning_rate * weight[0] * (target - y)
                working_weights[1] = working_weights[1] + learning_rate * weight[1] * (target - y)
                working_bias = working_bias + learning_rate * (target - y)
                needed_updating = True
        example_iterator += 1
    return working_weights, working_bias


def main():
    from q3 import construct_perceptron
    # Test 1
    print('--------------Test 1--------------')
    print('Result should equal:')
    print('Weights: [1.0, 0.5]')
    print('Bias: -1.5')
    print('')
    print('0')
    print('0')
    print('0')
    print('1')
    print('1')
    print('0')
    print('1')
    print('----------------------------------')
    weights = [2, -4]
    bias = 0
    learning_rate = 0.5
    examples = [
        ((0, 0), 0),
        ((0, 1), 0),
        ((1, 0), 0),
        ((1, 1), 1),
    ]
    max_epochs = 50

    weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
    print(f"Weights: {weights}")
    print(f"Bias: {bias}\n")

    perceptron = construct_perceptron(weights, bias)

    print(perceptron((0, 0)))
    print(perceptron((0, 1)))
    print(perceptron((1, 0)))
    print(perceptron((1, 1)))
    print(perceptron((2, 2)))
    print(perceptron((-3, -3)))
    print(perceptron((3, -1)))

    # Test 2
    print('--------------Test 2--------------')
    print('Result should equal:')
    print('Weights: [-0.5, -0.5]')
    print('Bias: 0.0')
    print('----------------------------------')
    weights = [2, -4]
    bias = 0
    learning_rate = 0.5
    examples = [
        ((0, 0), 0),
        ((0, 1), 1),
        ((1, 0), 1),
        ((1, 1), 0),
    ]
    max_epochs = 50

    weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
    print(f"Weights: {weights}")
    print(f"Bias: {bias}\n")


if __name__ == "__main__":
    main()
