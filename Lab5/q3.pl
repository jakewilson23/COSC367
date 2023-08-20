/*
Suppose we are given a knowledge base with facts about the translation of words between 
Language1 and Language2. The following is an example of translation of numbers between 
te reo Maori and English:

tran(tahi,one). 
tran(rua,two). 
tran(toru,three). 
tran(wha,four). 
tran(rima,five). 
tran(ono,six). 
tran(whitu,seven). 
tran(waru,eight). 
tran(iwa,nine).
Write a predicate listtran(?List1, ?List2) which translates a list of words in Language1 
to/from the corresponding list of words in Language2. For example, for the facts given 
above:

listtran([tahi,iwa,rua],X).
should give:
X = [one, nine, two].
Your program should also work in the other direction. For example, the query

listtran(X, [one, seven, six, two]).
should succeed with
X = [tahi, whitu, ono, rua].
Hint: to answer this question, first ask yourself “How do I translate two empty lists of 
words?”. That’s the base case. For non-empty lists, first translate the head of the list,
 then use recursion to translate the tail.

Important: do not include any tran facts for any specific language. These will provided in
 the test cases. Only include the necessary clauses to get listtran working.
*/

listtran([], []).
listtran([L1Head|L1Tail], [L2Head|L2Tail]) :- tran(L1Head, L2Head), listtran(L1Tail, L2Tail).