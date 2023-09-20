postorder(leaf(X), [X]).
postorder(tree(Root, Left, Right), Traversal) :-
    postorder(Left, LeftTraversal),
    postorder(Right, RightTraversal),
    append(LeftTraversal, RightTraversal, LeftRightTraversal),
    append(LeftRightTraversal, [Root], Traversal).

test_answer :- postorder(tree(a, leaf(b), leaf(c)), T), writeln(T).
test_answer2 :- postorder(tree(a, tree(b, leaf(c), leaf(d)), leaf(e)), T), writeln(T).
