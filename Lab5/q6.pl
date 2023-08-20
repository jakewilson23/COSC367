/*
Write a predicate split_odd_even(+ListIn, ?ListA, ?ListB) whose first argument is
a list, and whose second and third arguments are the odd and even indexed elements 
in that list respectively. Assume the first element of a list is indexed 1.
*/

odd([],[],[]).
odd([Head|Tail], [Head|Odd], Even) :- even(Tail, Odd, Even).

even([],[],[]).
even([Head|Tail], Odd, [Head|Even]) :- odd(Tail, Odd, Even).       

split_odd_even(In, Odd, Even) :- odd(In, Odd, Even).