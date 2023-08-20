/*
Write a predicate preorder(+Tree, Traversal) that determines the preorder traversal
 of a given binary tree. Each tree/subtree is either a leaf or of the form 
 tree(root, left_subtree, right_subtree). A preorder traversal records the current 
 node, then the left branch, then the right branch.
*/

preorder(leaf(X), Traversal) :- append([X], [], Traversal).
preorder(tree(Root, Left, Right), Traversal) :- append([Root], CombinedTrav, Traversal), 
                                                append(LeftTrav, RightTrav, CombinedTrav), 
                                                preorder(Left, LeftTrav),
                                                preorder(Right, RightTrav).