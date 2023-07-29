"""
Write a class LCFSFrontier such that when an instance of this class along with a graph object is passed to
generic_search, lowest-cost-first search (LCFS) is performed. Your answer must also include the code for
LocationGraph class since it is used in some test cases.

Notes The search module is available here: search.py. We require priority queues to be stable. We recommend you use
heapq from the standard Python library. Read the documentation and pay attention to the "implementation notes" to see
how you can make it stable. It is recommended that you write LCFSFrontier as a subclass of Frontier class (instead of
writing it from scratch). Although the Frontier class does not provide any functionality to reuse, subclassing makes
it easier to check whether the new class implements all the methods required by the abstract base class.
"""

from search import *
from math import dist
import heapq


class LocationGraph(Graph):
    def __init__(self, location, radius, starting_nodes, goal_nodes):
        self.location = location
        self.radius = radius
        self._starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes

    def starting_nodes(self):
        return self._starting_nodes

    def is_goal(self, node):
        return node in self.goal_nodes

    def outgoing_arcs(self, tail):
        arcs = []
        for head in self.location:
            if head != tail:
                cost = dist(self.location[tail], self.location[head])
                if cost <= self.radius:
                    arcs.append(Arc(tail=tail, head=head, action=tail + '->' + head, cost=cost))
        return sorted(arcs)

class LCFSFrontier(Frontier):
    """Implements a frontier container appropriate for Least Cost First Search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty Priority Queue. It also initialises
        a counter for entry count of items added to the queue"""
        self.container = []
        heapq.heapify(self.container)
        self.entry_count = 0

    def add(self, path):
        cost = 0
        for arc in path:
            cost += arc[3]
        heapq.heappush(self.container, [cost, self.entry_count, path])
        self.entry_count += 1

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self

    def __next__(self):
        if len(self.container) > 0:
            cost, entry, path = heapq.heappop(self.container)
            return path
        else:
            raise StopIteration  # don't change this one

def main():
    frontier = LCFSFrontier()
    frontier.add((Arc(None, None, None, 17),))
    frontier.add((Arc(None, None, None, 11), Arc(None, None, None, 4)))
    frontier.add((Arc(None, None, None, 7), Arc(None, None, None, 8)))

    for path in frontier:
        print(path)

    graph = LocationGraph(
        location={'A': (25, 7),
                  'B': (1, 7),
                  'C': (13, 2),
                  'D': (37, 2)},
        radius=15,
        starting_nodes=['B'],
        goal_nodes={'D'}
    )

    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)

    graph = ExplicitGraph(nodes=set('ABCD'),
                          edge_list=[('A', 'D', 7), ('A', 'B', 2),
                                     ('B', 'C', 3), ('C', 'D', 1)],
                          starting_nodes=['A'],
                          goal_nodes={'D'})

    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)

if __name__ == "__main__":
    main()
