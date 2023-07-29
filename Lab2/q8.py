"""
In this question, you have to write a graph class for an agent that can be at certain locations on a 2D plane. The
graph class is called LocationGraph. An object of this class is initialised with a dictionary called location and a
non-negative number called radius. The keys of the dictionary are of type string and are the nodes of the graph. The
value of each key is a pair of numbers that designates a location for that node.

From a node, there will be an outgoing arc to every other node in the graph that is within the given radius. The
action field of the arc must of the form "A->B" where A and B are placeholders for the tail node and the head node of
the arc respectively. The cost of the arc is the straight-line distance between the tail node and the head node. The
outgoing arcs of a node must be in the alphabetical order of the head nodes.

Notes

The search module is available here: search.py. On a 2D plane, two points are within a radius r of each other if (and
only if) the euclidean distance between the two points is less than or equal to r. While from a scalability
perspective, it makes sense to use an efficient data structure for querying points on a plane or to cache the edges
explicitly, for this exercise, simply iterate through the location dictionary every time the outgoing arcs of a node
need to be computed. Remember to include all the import statements in the solution (or just paste your entire file if
it does not produce unwanted output when it is imported by another module).
"""

from search import Arc, Graph
from math import dist


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


def main():
    graph = LocationGraph(
        location={'SW': (-2, -2),
                  'NW': (-2, 2),
                  'NE': (2, 2),
                  'SE': (2, -2)},
        radius=5,
        starting_nodes=['NE'],
        goal_nodes={'SW'}
    )

    for arc in graph.outgoing_arcs('NE'):
        print(arc)

    print()

    for arc in graph.outgoing_arcs('NW'):
        print(arc)

    print()

    for arc in graph.outgoing_arcs('SW'):
        print(arc)

    print()

    for arc in graph.outgoing_arcs('SE'):
        print(arc)


if __name__ == "__main__":
    main()
