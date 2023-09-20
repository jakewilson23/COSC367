eats(bob, Thing) :- hungry(bob), edible(Thing).
eats(alice, Thing) :- hungry(alice), edible(Thing), not(fast_food(Thing)). 

edible(fries).
edible(salad).
fast_food(fries).

hungry(bob).
hungry(alice).


test_answer :- eats(bob, fries),
               eats(bob, salad),
               eats(alice, salad),
               write('OK').

test_answer2 :- write('Wrong answer!').

