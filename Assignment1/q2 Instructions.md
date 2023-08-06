## Writing the AStarFrontier class

Write a class AStarFrontier for performing A* search on graphs. An instance of AStarFrontier 
together with an instance of RoutingGraph that you wrote in the previous question will be 
passed to the generic search procedure in order to find the lowest cost (i.e. shortest time) 
solution (if one exists) from one of the agents to the goal node.

In this question, modify the method estimated_cost_to_goal in the RoutingGraph class so that 
it always returns 0 (zero) for any given node. In the next question, we will ask you to 
implement a proper heuristic.

### Notes:

1. Your solution must contain the definitions of both AStarFrontier and RoutingGraph classes.

2. Unlike other frontier objects, the AStarFrontier objects are initialised with an instance 
of a graph. This is because AStarFrontier needs to access the estimated_cost_to_goal method 
of the graph object.

3. Remember that in this course priority queues must be stable. See priority queue 
implementation notes in heapq documentation for a suggestion on how this can be achieved.

4. The algorithm must halt on all valid maps even when there is no solution.

5. It is recommended that before you submit your solution, you test it against the given 
test cases and some new examples (maps) designed by yourself with different positioning of 
agents and building blocks. You should think whether or not the frontier requires pruning 
and implement it accordingly.

6. Note the distinction between time and fuel consumption. We are interested in a solution 
with the shortest time.

7. The requirement of having a zero heuristic implies that the generic graph search algorithm
will behave as an LCFS (lowest-cost-first search). In the next question, we will more 
thoroughly test your A* frontier and graph class.

8. When there is no solution, the generic graph search automatically returns None instead of 
a path which causes the print_actions procedure to print "There is no solution." This happens
when the frontier becomes empty and no solution has been reached.

9. It is recommended (but not required) that your answer for AStarFrontier in 40 lines of code 
or shorter. If your code is much longer, you might be doing something wrong.