import collections

from search import *


class BFSFrontier(Frontier):
    """Implements a frontier container appropriate for breadth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty queue."""
        self.container = collections.deque()

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self

    def __next__(self):
        if len(self.container) > 0:
            top_of_queue = self.container.popleft()
            return top_of_queue
        else:
            raise StopIteration  # don't change this one


def main():
    flights = ExplicitGraph(nodes=['Christchurch', 'Auckland',
                                   'Wellington', 'Gold Coast'],
                            edge_list=[('Christchurch', 'Gold Coast'),
                                       ('Christchurch', 'Auckland'),
                                       ('Christchurch', 'Wellington'),
                                       ('Wellington', 'Gold Coast'),
                                       ('Wellington', 'Auckland'),
                                       ('Auckland', 'Gold Coast')],
                            starting_nodes=['Christchurch'],
                            goal_nodes={'Gold Coast'})

    my_itinerary = next(generic_search(flights, BFSFrontier()), None)
    print_actions(my_itinerary)

if __name__ == "__main__":
    main()
