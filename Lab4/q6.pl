/*
Do you know these wooden Russian dolls (Matryoshka dolls) where the smaller ones are contained
in bigger ones?
In this question, you have to write a knowledge base that describes the nestedness in the above 
drawing. You have to:

First, write a number of facts using the predicate directlyIn/2 where directlyIn(X,Y) means that
 X is directly in Y. For example, irina is directly in natasha but irina is not directly in olga (thus do not write any fact about the latter).
Then, define a recursive predicate contains/2 , that tells us which doll (directly or indirectly)
 contains which other doll. For example, the query contains(katarina,natasha) should succeed 
 (be true), while contains(olga, katarina) should fail.
Notes
You have to write contains as two rules (or one rule with a disjunction in its body).
Note the spelling of katarina and other names.
In some test cases you may see the symbol "\+" which means negation (not). The goal \+ some_term
 succeeds if some_term fails (cannot be proved).
*/

directlyIn(irina, natasha).
directlyIn(natasha, olga).
directlyIn(olga, katarina).

contains(Doll_outside, Doll_inside) :- directlyIn(Doll_inside, Doll_outside).
contains(Doll_outside, Doll_inside) :- directlyIn(X, Doll_outside), contains(X, Doll_inside).
