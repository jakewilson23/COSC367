max(X,Y,X) :- X >= Y.
max(X,Y,Y) :- Y >= X.

max([X], X).   
max([Head|Tail],Max) :-
    Tail = [_|_], 
    max(Tail, TailMax),
    max(Head, TailMax, Max).  

test_answer :- max([1, 2, 3, 4, 5], M), writeln(M).
test_answer2 :- max([], M), writeln("Max of an empty list is undefined!").