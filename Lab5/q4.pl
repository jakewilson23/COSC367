/*
Write a predicate twice(?In, ?Out) whose left argument is a list, and whose right
 argument is a list consisting of every element in the left list repeated twice. 
 For example, the query

twice([a,4,buggle],X).
gives
X = [a,a,4,4,buggle,buggle].
and the query
twice(X, [1, 1, 2, 2]).
gives
X = [1,2].
and the query
twice(X, [a, a, b, b, c]).
fails.
Hint: to answer this question, first ask yourself “What should happen when the first
 argument is the empty list?”. That’s the base case. For non-empty lists, think about
  what you should do with the head, and use recursion to handle the tail.
*/

twice([], []).
twice([X|Tail1], [X,X|Tail2]) :- twice(Tail1, Tail2).