## Introduction
Finding patterns in sequences of numbers is considered an intellectually-challenging problem.
These problems are commonly used in "IQ" tests. For example given the sequence 
3, 2, 3, 6, 11, 18, the question asks for the next number in the sequence.

Being challenging for humans, they are also considered good benchmarks for AI algorithms. 
Finding patterns in sequences is in fact a special case of the more-general problem of 
modelling and predicting time series with a wide range of applications from weather forecast
to finding trends in markets.

The objective of this quiz is to use ideas from tree-representation of expressions, CSPs, 
optimisation, and population-based and evolutionary search techniques to create a program 
that given a sequence of integers, it can 'predicts' the rest of the sequence.

This super-quiz has multiple questions. Many of the questions ask for writing functions 
that can later be used in other parts and in the final predicting program.

## Introduction to the representation and the search strategy
Consider the very simple sequence of numbers 1, 2, 3, 4, 5, 6. What is the most obvious 
pattern in this sequence and what is the next number? It is fair to say that the next number 
is 7 and that the most obvious (simplest) pattern is that the numbers are increasing one at
a time. [There is a philosophical problem (known as generalisation fallacy) in this argument
but we put that aside in this quiz.]

So how can we represent patterns? A good answer would be by functions. For example if a(i) 
denotes the number at position i in the sequence where i starts from zero, then one function
(pattern) that matches the above sequence is a(i) = a(i-1) + 1 which is a recursive function.
The sequence can also be explained by function a(i) = i + 1. Therefore in order to 
automatically recognise a pattern in a sequence, the program must perform a search over the
space of possible functions to find one that matches the given sequence. So what is a good 
representation for functions? When functions are mathematical expressions, the prefix 
notation provides a very useful and robust representation. For example the above pattern 
can be represented by the expression (+ i 1).

Because of the complexity of the neighbourhood in the space of expressions, CSP or greedy 
local search algorithms are not applicable. A good choice is using evolutionary algorithms 
where each individual is an expression tree (prefix notation). In this assignment you will 
implement a tree-based (prefix notation) representation for expressions. This representation
is powerful enough that will allow you to use a simple random search to solve many instances 
the problem of recognising patterns in sequence of numbers. You are welcome (but not 
required) to extend the search part of the assignment to a complete evolutionary algorithm.

## Technical Notes
Although it might be possible to skip some of the questions, it is recommended that you 
answer the questions in order. Some question specs are referred to in later questions.
Similar to the previous quizzes, in order to avoid accidental break of dependency or 
forgetting import statements, you can have all of your functions in one file and every time
just copy and paste the entire file in the answer box. However you have to make sure that 
the code in the body of your program (module) does not interfere with the output and tests 
(e.g. it does not print stuff etc.)