/*
Here are six Italian words:

astante , astoria , baratto , cobalto , pistola , statale .

They have to be assigned to rows and columns (crossword puzzle fashion) in the 
following grid:



The following knowledge base represents a lexicon containing these words:

word(astante, a,s,t,a,n,t,e).
word(astoria, a,s,t,o,r,i,a).
word(baratto, b,a,r,a,t,t,o).
word(cobalto, c,o,b,a,l,t,o).
word(pistola, p,i,s,t,o,l,a).
word(statale, s,t,a,t,a,l,e).
Write a predicate solution/6 in the form of solution(V1,V2,V3,H1,H2,H3) that tells 
us how to fill in the grid.

Notes
In this question, the same word can appear in different rows or columns. [As an additional
 exercise for yourself, think what rule needs to be added in order to have each word used 
only once.]
The rules you provide will be used with different sets of six-letter words.
Prolog has some facilities that make it possible to solve this sort of problems in simpler
 ways but at this stage we have to solve it in a somewhat tedious way (you need some copy 
    and paste).
*/

word(astante, a,s,t,a,n,t,e).
word(astoria, a,s,t,o,r,i,a).
word(baratto, b,a,r,a,t,t,o).
word(cobalto, c,o,b,a,l,t,o).
word(pistola, p,i,s,t,o,l,a).
word(statale, s,t,a,t,a,l,e).

solution(V1,V2,V3,H1,H2,H3) :- word(V1, _, A, _, D, _, G, _), word(V2, _, B, _, E, _, H, _), 
                                word(V3, _, C, _, F, _, I, _), word(H1, _, A, _, B, _, C, _), 
                                word(H2, _, D, _, E, _, F, _), word(H3, _, G, _, H, _, I, _).
                            