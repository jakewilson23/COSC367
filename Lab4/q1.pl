/*
Define a set of relations in the form of Prolog rules about people according to the following statements.

A person eats something if the person likes that thing. Use the predicate eats/2 where the first argument is 
a person and the second argument is a thing, and the predicate likes/2 where the first argument is a person 
and the second is a thing. For example if the fact likes(bob, chocolate) is in the knowledge base then the 
query eats(bob, chocolate) must always succeed (be true), even if the fact is not explicitly in the knowledge 
base.
A person eats something if the person is hungry and the thing is edible. Use predicates hungry/1 and edible/1.
Please note that you do not need to provide any facts. Only write two rules (two lines).
*/

eats(Person, Thing) :- likes(Person, Thing).
eats(Person, Thing) :- hungry(Person), edible(Thing).