/*
Write a predicate remove(+X, +ListIn, ?ListOut) that succeeds if ListOut 
can be obtained by removing all instances of X from ListIn. Note that the
 first two arguments will always be bound (given as input).
*/

remove(_, [], []).
remove(X, [Head|Tail], ListOut) :- X = Head, remove(X, Tail, ListOut).
remove(X, [Head|Tail], ListOut) :- X \= Head, remove(X, Tail, Out), append([Head], Out, ListOut).
