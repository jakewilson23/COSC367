"""Write a function knn_predict(input, examples, distance, combine, k) that takes an input and predicts the output by
combining the output of the k nearest neighbours. If after selecting k nearest neighbours, the distance to the
farthest selected neighbour and the distance to the nearest unselected neighbour are the same, more neighbours must
be selected until these two distances become different or all the examples are selected. The description of the
parameters of the function are as the following:

input: an input object whose output must be predicted. Do not make any assumption about the type of input other than
that it can be consumed by the distance function.

examples: a collection of pairs. In each pair the first element is
of type input and the second element is of type output.

distance: a function that takes two objects and returns a non-negative number that is the distance between the two
objects according to some metric. combine: a function that takes a set of outputs and combines them in order to
derive a new prediction (output).

k: a positive integer which is
the number of nearest neighbours to be selected. If there is a tie more neighbours will be selected (see the
description above).

Notes
You only need to provide a single function knn_predict and the related import statements.
You do not need to provide any distance or combine functions. These functions are defined in the test cases and are
passed to your function as arguments.
The majority_element function used in some test cases returns the smallest
element when there is a tie. For example majority_element('--++') returns '+' because it is the most common label (
like -) and in the character encoding system '+' comes before '-'."""


def knn_predict(input, examples, distance, combine, k):
    # work out the distances from the input to all neighbours in the examples
    distance_to_neighbours = []
    for neighbour in examples:
        distance_to_neighbours.append((distance(input, neighbour[0]), neighbour[1]))

    # sort neighbours by distance
    sorted_dist_neighbours = sorted(distance_to_neighbours)

    # Take the first k neighbours in the sorted list, these are the k closest neighbours
    # Also collect the remaining unselected neighbours
    k_closest_neighbour = sorted_dist_neighbours[:k]
    unselected_neighbours = sorted_dist_neighbours[k:]

    # If the distance of the furthest k_closest_neighbour is the same as the closest unselected,
    # remove the closest unselected and add it to the k_nearest_neighbours
    # Do this until either they are not the same distance or the unselected list is empty
    keep_checking = True
    while unselected_neighbours and keep_checking:
        keep_checking = False
        if k_closest_neighbour[-1][0] == unselected_neighbours[0][0]:
            k_closest_neighbour.append(unselected_neighbours[0])
            del unselected_neighbours[0]
            keep_checking = True

    # from the k_closest_neighbours take the values of the neighbour and put them into the combine
    # function to find the most common
    neighbour_values = []
    for neighbour in k_closest_neighbour:
        neighbour_values.append(neighbour[1])
    return combine(neighbour_values)


def main():
    from q1 import euclidean_distance, majority_element

    # Test 1
    print('--------------Test 1--------------')
    print('Result should equal:')
    print('k = 1, x prediction,0 -,1 -,2 -,3 -,4 +,5 +,6 +,7 +,8 +,9 +')
    print('k = 3, x prediction,0 -,1 -,2 -,3 -,4 -,5 +,6 +,7 +,8 +,9 +')
    print('k = 5, x prediction,0 +,1 +,2 +,3 +,4 +,5 +,6 +,7 +,8 +,9 +')
    print('----------------------------------')
    examples = [
        ([2], '-'),
        ([3], '-'),
        ([5], '+'),
        ([8], '+'),
        ([9], '+'),
    ]

    distance = euclidean_distance
    combine = majority_element

    for k in range(1, 6, 2):
        print("k =", k)
        print("x", "prediction")
        for x in range(0, 10):
            print(x, knn_predict([x], examples, distance, combine, k))
        print()

    # Test 2
    print('--------------Test 2--------------')
    print('Result should equal')
    print('k = 1, x prediction,0 5.00,1 5.00,2 -1.00,3 -1.00,4 1.00,5 1.00,6 2.50,7 4.00,8 6.00,9 8.00')
    print('k = 3, x prediction,0 1.67,1 1.67,2 1.67,3 1.67,4 2.25,5 1.33,6 4.33,7 4.33,8 4.33,9 4.33')
    print('k = 5, x prediction,0 3.40,1 3.40,2 3.40,3 3.40,4 3.40,5 3.40,6 3.40,7 3.40,8 3.40,9 3.40')
    print('----------------------------------')
    # using knn for predicting numeric values

    examples = [
        ([1], 5),
        ([2], -1),
        ([5], 1),
        ([7], 4),
        ([9], 8),
    ]

    def average(values):
        return sum(values) / len(values)

    distance = euclidean_distance
    combine = average

    for k in range(1, 6, 2):
        print("k =", k)
        print("x", "prediction")
        for x in range(0, 10):
            print("{} {:4.2f}".format(x, knn_predict([x], examples, distance, combine, k)))
        print()


if __name__ == "__main__":
    main()
