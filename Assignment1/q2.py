import heapq
import math
import re
from search import *


class RoutingGraph(Graph):
    def __init__(self, map_str):
        self.agents, self.goals, self.map_list = self.process_map_str(map_str)

    def process_map_str(self, map_str):
        agent_list = []
        goal_list = []
        map_list = []
        strip_map_str = map_str.strip()
        split_map_rows = strip_map_str.splitlines()
        for row, row_contents in enumerate(split_map_rows):
            temp_row = []
            strip_row_contents = row_contents.strip()
            for col, char in enumerate(strip_row_contents):
                if char == 'G':
                    goal_list.append((row, col))
                elif char == 'S':
                    agent_list.append((row, col, math.inf))
                elif re.match("([0-9])", char):
                    agent_list.append((row, col, int(char)))
                temp_row.append(char)
            map_list.append(temp_row)
        return agent_list, goal_list, map_list

    def estimated_cost_to_goal(self, node):
        return 0

    def starting_nodes(self):
        return self.agents

    def is_goal(self, node):
        row, col, fuel = node
        return (row, col) in self.goals

    def outgoing_arcs(self, tail):
        moves = [('N', -1, 0), ('E', 0, 1), ('S', 1, 0), ('W', 0, -1)]
        row, col, fuel = tail

        if fuel > 0:    # there are available actions to be made by the agent
            for direction, row_move, col_move in moves:
                new_pos_char = self.map_list[row + row_move][col + col_move]
                if new_pos_char not in ['X', '+', '-', '|']:    # check new position is not an obstacle or map edge
                    cost = 5
                    head = (row + row_move, col + col_move, fuel - 1)
                    yield Arc(tail, head, direction, cost)
        if self.map_list[row][col] == 'P':  # The agent can use "Teleport to (row, col)" action
            for search_row, row_contents in enumerate(self.map_list):
                for search_col, char in enumerate(row_contents):
                    if char == 'P' and search_row != row and search_col != col:
                        cost = 10
                        head = (search_row, search_col, fuel)
                        action_string = "Teleport to ({row}, {col})".format(row=search_row, col=search_col)
                        yield Arc(tail, head, action_string, cost)

        if self.map_list[row][col] == 'F' and fuel < 9:     # The agent can use 'Fuel up' action
            cost = 15
            head = (row, col, 9)
            yield Arc(tail, head, "Fuel up", cost)


class AStarFrontier(Frontier):
    """Implements a frontier container appropriate for Least Cost First Search."""

    def __init__(self, map_graph):
        """The constructor takes no argument. It initialises the
        container to an empty Priority Queue. It also initialises
        a counter for entry count of items added to the queue"""
        self.container = []
        heapq.heapify(self.container)
        self.entry_count = 0
        self.map_graph = map_graph
        self.considered = []

    def add(self, path):
        if (path[-1][0], path[-1][1]) not in self.considered:
            cost = 0
            estimated_cost = self.map_graph.estimated_cost_to_goal(path[-1])
            for arc in path:
                cost += arc[3]
            combined_cost = cost + estimated_cost
            heapq.heappush(self.container, [combined_cost, self.entry_count, path])
            self.entry_count += 1
            self.considered.append((path[-1][0], path[-1][1]))

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

    # Test 1
    print("Test 1 Begins Here")

    map_str = """\
    +-------+
    |   G   |
    |       |
    |   S   |
    +-------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    # Test 2
    print("Test 2 Begins Here")

    map_str = """\
    +-------+
    |  GG   |
    |S    G |
    |  S    |
    +-------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    # Test 3
    print("Test 3 Begins Here")

    map_str = """\
    +-------+
    |     XG|
    |X XXX  |
    | S     |
    +-------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    # Test 4
    print("Test 4 Begins Here")

    map_str = """\
    +-------+
    |  F  X |
    |X XXXXG|
    | 3     |
    +-------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    # Test 5
    print("Test 5 Begins Here")

    map_str = """\
    +--+
    |GS|
    +--+
    """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    # Test 6
    print("Test 6 Begins Here")

    map_str = """\
    +---+
    |GF2|
    +---+
    """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    # Test 7
    print("Test 7 Begins Here")

    map_str = """\
    +----+
    | S  |
    | SX |
    |GX G|
    +----+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    # Test 8
    print("Test 8 Begins Here")

    map_str = """\
    +---------+
    |         |
    |    G    |
    |         |
    +---------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    # Test 9
    print("Test 9 Begins Here")

    map_str = """\
    +------------+
    |    P       |
    | 7          |
    |XXXX        |
    |P F X  G    |
    +------------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    # Test 10
    print("Test 10 Begins Here")

    map_str = """\
    +----------+
    |    X     |
    | S  X  G  |
    |    X     |
    +----------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)


if __name__ == "__main__":
    main()