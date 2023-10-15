## Introduction
This quiz starts with a number questions that use explicit game trees. Towards the end of the quiz you will see an example that requires implicit game trees. Explicit trees are useful for education purposes. However, in practice, game trees are usually very big and would take a lot of memory (and time) if they were to be stored in the memory. It is also inefficient to first generate a tree and then search it. The search and generation can be done at the same time. The search and generation are done according to the rules of the game without using much memory (linear in branching factor and the average number of moves to the end of the game). The time however still grows exponentialy with respect to the depth of the tree.
## Representation of explicit game trees
An explicit game tree is a tree that is already constructed and resides in the memory (as opposed to being constructed on the fly). We use the following recursive representation for explicit game trees. A game tree is either

- a number which represents the utility (payoff) of a terminal (end-game) state; or
- a list of one or more game trees.
## Examples
The root of the following game tree has three children. The first child is a leaf node with a utility of 1. The second child has two children (leaf nodes with utilities 2 and 3). The third child of the root has a single child which has a single child (a leaf node with a utility of 4).

``` Python
game_tree = [1, [2, 3], [[4]]]
```
The following trees are all different. The first one is game tree that is a single leaf node. The second one has a root with one child which is terminal. The third one has a root which has one child which has one terminal child.

``` Python
game_tree1 = 7
game_tree2 = [7]
game_tree3 =[[7]]
```