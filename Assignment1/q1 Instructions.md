## Writing the RoutingGraph class

In the first step of the assignment you have to write a subclass of Graph for a routing 
problem in an environment. The map of the environment is given in the form of a multi-line 
string of characters. The following shows an example map. 

```python
map_str = """\
+--------+
|  G    G|
|  XXX   |
|  S X   |
|    X 2 |
+--------+
"""
```

### Map description

- The map is always rectangular. We refer to positions in the map by a pair of numbers 
(row, col) which correspond to the row and column number of the position. Row numbers 
start from 0 for the first (topmost) line, 1 for the second line, and so on. The column 
numbers start from 0 for the first (leftmost) position (character) in the line, 1 for 
the second position, and so on.

- The environment is always surrounded by walls which are represented with characters '+' 
or '-' or '|'. For example the position (0,0) is always a '+' (i.e. wall) and so are all 
other three corners of the map. The first and last rows and the first and last columns 
are always '-' and '|' respectively (except for the corners). 
- The obstacles are marked by 'X'.

- There may be zero or more agents on the map. The location of agents are marked by 'S' or 
digits 0 to 9

  - Agents indicated by S are solar and do not need fueling. We assume they have unlimited 
  energy capacity (and/or it's always sunny).
  
  - Agents indicated by digits have fuel tanks. The capacity of the tank is 9. The digit 
  used to indicate the agent shows how much fuel is initially available in the tank.
  
- There may be zero or more call points (customers) on the map. The location of call points
(potential destinations) are marked by 'G'. To simplify textual representation, we 
assume that an agent is never initially at a call point.

- An agent can move in four directions, N, E, S, W, as long as it has fuel and there is no 
obstacle or wall in the way. This means that agents can also go to cells where other 
agents are present. The agent loses one unit of fuel for each move. The order of actions 
is clockwise starting from N. For example, if from a position all four directional moves 
are possible, then the first arc in the sequence of arcs returned by outgoing_arcs is for 
going north, then east, and so on. All single directional moves take 5 units of time. This 
is what we regard as the cost of the action (since the objective of the problem is to 
minimise the service time).

- The symbol F indicates a fuel station. If an agent is in a cell marked as F and its current
fuel amount is less than 9 it can take the action of "Fuel up" which fills the tank to its 
maximum capacity of 9. In the sequence of arcs, the "Fuel up" action (if available) should 
appear after any other directional actions. The action costs 15 units of time (regardless 
of how much fuel is obtained).

- The symbol P indicates a portal. There can be zero or more portals on a map. If an agent 
is in a cell marked as P, in addition to the usual movements, it has the option of 
teleporting to any other location on the map marked as P. In the sequence of arcs, the 
teleport action (if available) should appear after any other directional action. The 
action does not consume any fuel but costs 10 units of time (regardless of the 
destination). The action must be labeled as "Teleport to (row, col)" where row and col 
are the row and column indices of the destination portal. If multiple outgoing arcs of 
this type are available, they should appear in the ascending order of the row number 
and the column number of the target portals (i.e. arcs leading to portals on lower row 
numbers should come first and for portals on the same row, arcs leading to portals on 
lower column numbers should come first).

### Task

Write a class RoutingGraph which is initialised by the map string and represents the map 
in the form of a graph by implementing the required methods in the Graph class. Represent 
the state of the agent by a tuple of the form (row, column, fuel)

### Notes

1. It is recommended that you write your class as a subclass of Graph.

2. The test cases do not test the method estimated_cost_to_goal in this question. You have the option of not 
implementing it for this question.

3. Try to avoid using indices to refer to elements of a tuple. For example instead of using 
position[0] and position[1], use readable names. For example use row, col = position 
instead.

4. You may find math.inf useful.

5. If you copy a multi-line string from the examples given in the questions into a function 
in your code, some leading spaces will be introduced. Use the method strip to get rid of 
these leading/trailing spaces. Also be mindful of the difference between the following 
two strings:

    ```python
    str1 = """This string splits into one line.
    """
    def main():
        str2 = """This string splits into TWO lines.
    """
    ```

6. It is recommended (but not required) that your answer for RoutingGraph is shorter than 
70 lines of code. If your code is much longer, you might be doing something wrong.

7. Avoid repetitive code. If you wish you can use the following list when implementing 
outgoing_arcs. You have to decipher it yourself.

    ```python
    [('N' , -1, 0),
     ('E' ,  0, 1),
     ('S' ,  1, 0),
     ('W' ,  0, -1),]
    ```

8. In a more realistic scenario, teleportation corresponds to using a different mode of 
transportation using a different network (e.g. using a train or a ferry)
