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
        map_str.strip()
        split_map_rows = map_str.splitlines()
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
                        head = (search_col, search_col, fuel)
                        action_string = "Teleport to ({row}, {col})".format(row=search_col, col=search_col)
                        yield Arc(tail, head, action_string, cost)

        if self.map_list[row][col] == 'F' and fuel < 9:     # The agent can use 'Fuel up' action
            cost = 15
            head = (row, col, 9)
            yield Arc(tail, head, "Fuel up", cost)


def main():

    # Test 1
    print("Test 1 Begins Here")

    map_str = """\
    +-------+
    |  9  XG|
    |X XXX P|
    | S  0FG|
    |XX P XX|
    +-------+
    """

    graph = RoutingGraph(map_str)

    print("Starting nodes:", sorted(graph.starting_nodes()))
    print("Outgoing arcs (available actions) at starting states:")
    for s in sorted(graph.starting_nodes()):
        print(s)
        for arc in graph.outgoing_arcs(s):
            print("  " + str(arc))

    node = (1, 1, 5)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print("  " + str(arc))

    node = (1, 7, 2)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print("  " + str(arc))

    node = (3, 7, 0)
    print("\nIs {} goal?".format(node), graph.is_goal(node))

    node = (3, 7, math.inf)
    print("\nIs {} goal?".format(node), graph.is_goal(node))

    node = (3, 6, 5)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print("  " + str(arc))

    node = (3, 6, 9)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print("  " + str(arc))

    node = (2, 7, 4)  # at a location with a portal
    print("\nOutgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print("  " + str(arc))

    # Test 2
    print("Test 2 Begins Here")

    map_str = """\
    +--+
    |GS|
    +--+
    """

    graph = RoutingGraph(map_str)

    print("Starting nodes:", sorted(graph.starting_nodes()))
    print("Outgoing arcs (available actions) at the start:")
    for start in graph.starting_nodes():
        for arc in graph.outgoing_arcs(start):
            print("  " + str(arc))

    node = (1, 1, 1)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print("  " + str(arc))

    # Test 3
    print("Test 3 Begins Here")

    map_str = """\
    +------+
    |S    S|
    |  GXXX|
    |S     |
    +------+
    """

    graph = RoutingGraph(map_str)
    print("Starting nodes:", sorted(graph.starting_nodes()))


if __name__ == "__main__":
    main()