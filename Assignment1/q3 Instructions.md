## The print_map procedure

Write a procedure print_map(map_graph, frontier, solution) that takes three parameters: an 
instance of RoutingGraph, an instance of AStarFrontier which has just been used to run a 
graph search on the given graph, and the result of the search, and then prints a map such 
that:

- the position of the walls, obstacles, agents, and the goal points are all unchanged and 
they are marked by the same set of characters as in the original map string;

- those free spaces (space characters) that have been expanded during the search are marked 
with a '.' (a period character); and

- those free spaces (spaces characters) that are part of the solution (best path to the goal)
are marked with '*' (an asterisk character).

### Further assumptions and requirements

1. The frontier object that is passed to print_map is your own implementation of AStarFrontier. 
You should use this object to see which nodes have been expanded.

2. The solution parameter is either a sequence of Arc objects that make up a path from a starting 
node to a goal node, or is None.

3. For this question, the graph class must have a proper heuristic function named 
estimated_cost_to_goal. You have to design the most dominant (highest value) function that 
can be computed very efficiently. See the signature of the method in the Graph class in 
search.py.

4. In this question, we are only concerned with agents of type S—agents that have infinite amount 
of fuel and do not require to fuel up.

5. The test cases do not include any fuel-based agents, fuel stations, or portals. Do not consider 
anything fuel-related or portal-related when devising the heuristic function.

6. Only the first solution returned by the generic search procedure (if there is one) is used to test 
your procedure.

7. In addition to print_map, your solution must include the code for RoutingGraph and AStarFrontier.

### Notes

1. A node is said to have been expanded if a path leading to that node is removed and returned by the 
frontier. If the returned node has neighbours, the corresponding extended paths are added to
the frontier.

2. This question puts your code for the graph and A* frontier into real test. Previous 
questions did not test the heuristic function and as long as the frontier class could provide
the functionality of the LCFS, it would pass the test cases. In this question, however, 
your code needs to produce the correct A* behaviour. Therefore, even if your code has passed
previous tests, you may still need to modify it in order to meet the required spec in this
question.

3. Note that you only need to consider movement actions when designing the heuristic function 
and that all movement actions have the same cost (as defined in the first question).

4. If your algorithm expands more nodes than the expected output, you might be using a 
heuristic that is not good enough; you need to find a better heuristic. Refer to the 
specification of the heuristic function stated above.

5. If for any reason you decide to answer this question before Question 2, please remember 
that in Question 2 the heuristic function is required to always return zero

6. The generic graph search algorithm returns None when no solution if found.

7. It is recommended (but not required) that your answer for print_map is shorter than 20 
lines of code. If your code is much longer, you might be doing something wrong.