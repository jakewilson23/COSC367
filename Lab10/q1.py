"""The k-Nearest Neighbours (kNN) algorithm depends on two functions that must be passed to the algorithm:

distance: this is a function that takes two objects and returns a non-negative number that is the distance between
the objects according to some metric. This function is used to identify the neighbours of an object. combine: this is
a function that takes a set of outputs and combines them in order to derive a new prediction. In this question you
have to write two concrete examples of these functions. Write the following functions:

euclidean_distance(v1, v2) where v1 and v2 are two numeric vectors (non-empty sequences) with the same number of
elements. The function must return the Euclidean distance between the points represented by v1 and v2.
majority_element(labels) where labels is a non-empty collection of class labels. The function must return a label
that has the highest frequency (most common). [if there is a tie it doesn't matter which majority is returned.] This
is an example of a combine function."""


from math import sqrt


def euclidean_distance(v1, v2):
    distance_squared = 0
    for i in range(len(v1)):
        distance_squared += (v2[i] - v1[i]) ** 2
    return sqrt(distance_squared)


def majority_element(labels):
    num_count = {}
    for num in labels:
        if num not in num_count.keys():
            num_count[num] = 1
        else:
            num_count[num] += 1
    most_occurrences = None
    for key in num_count:
        if most_occurrences is None:
            most_occurrences = key
        elif num_count[key] > num_count[most_occurrences]:
            most_occurrences = key
    return most_occurrences


def main():
    # Test 1
    print('--------------Test 1--------------')
    print('Result should equal:')
    print('9.25526876973327')
    print('----------------------------------')
    print(euclidean_distance([0, 3, 1, -3, 4.5], [-2.1, 1, 8, 1, 1]))

    # Test 2
    print('--------------Test 2--------------')
    print('Result should equal')
    print('0')
    print('True')
    print('----------------------------------')
    print(majority_element([0, 0, 0, 0, 0, 1, 1, 1]))
    print(majority_element("ababc") in "ab")


if __name__ == "__main__":
    main()
