## Final notes
This assignment demonstrates the importance of representation in AI and Machine Learning. We devised a functional form to represent the underlying pattens of sequences of numbers. The functions themselves where represented as trees. This allowed us to define operations such as generation (and crossover and mutation) to perform an (evolutionary) search. Python and the natural way in which it handles references, allowed us to represent trees as nested lists with elements pointing to objects such as functions, integers, and other lists.

If you have managed to answer the last question correctly, then you should be able to solve many similar problems available on the web. As an example take a look at http://www.fibonicci.com/math/number-sequences-test/ (commercial website) and see how many of the problems in the "hard" category you can solve (first yourself, then your program). Your program should be able to solve quite a number of them with ease - specially if you have implemented an evolutionary search.

Some problems (number sequences) require richer search spaces. For some problems you may need to allow for deeper expression trees. For some, you may need a different function set. Some problems may need a more elaborate representation for functions (not just x, y, and i). One may consider performing a meta-search (on top of a normal search) to find the right settings for a problem. For some sequences, however, like the sequence of prime numbers, there is no right settings in the current model; you need a whole new way of thinking about sequences and introduce more sophisticated models/machines. Unsurprisingly, as we allow for more sophisticated models, the search space becomes bigger (often exponentially), and the expected time to find a solution increases.