/*
Binary trees are trees where all internal nodes have exactly two children. The mirror of a binary 
tree is obtained by exchange all the left and right children. For example the following two trees 
are the mirror of each other:

     .                   . 
    / \	                / \
   1   .               .   1
      / \             / \ 
     2   3           3   2
The smallest binary trees consist of only one leaf node. We will represent leaf nodes as leaf(Label)
 . For instance, leaf(1) and leaf(3) are leaf nodes, and therefore small binary trees. Given two 
 binary trees B1 and B2 we combine them into one binary tree by tree(B1,B2).So, from the leaves 
 leaf(2) and leaf(3) we can build the binary tree tree(leaf(2),leaf(3)) . And from the binary trees
  leaf(1) and tree(leaf(2),leaf(3)) we can build the binary tree tree(leaf(1), tree(leaf(2), leaf(3))).

Define a predicate mirror/2 that succeeds when the two arguments are binary trees and are the mirror 
of each other.
*/

/*mirror(tree(B1, B2), tree(B3, B4)) :- mirror(B2, B3), mirror(B1, B4).
mirror(leaf(Label1), leaf(Label2)).*/

mirror(A, B) :- A = tree(T3, T4), B = tree(T1, T2),  mirror(T2, T3), mirror(T1, T4);
                A = leaf(B1), B = leaf(B2), B1 = B2.
