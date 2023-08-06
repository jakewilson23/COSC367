## Introduction

In this assignment you apply the search techniques you have learnt in the course to a 
routing problem. The problem involves a number of mobile agents 
(think of self-driving taxis) scattered across a flat rectangular grid environment. 
There are also a number of call points (think of customers) waiting to be served. 
The objective is to, if possible, navigate an agent to a call point that is time-wise 
the closest.

The following points apply to all the questions in this super quiz:


1. In each instance of this problem we want to navigate one agent to one call point 
    (not all agent and not all call points, only the closest pair).
2. In all the questions you can assume that the search module (the file search.py) is 
available on the quiz server. This means that you can safely import the search module (in 
addition to all the standard Python modules) in your program. Do not repeat the code of 
search module in your answers.
3. Your solution must contain all the import statements that it requires, even for the
search module.
4. You can have your entire program for all the three questions in one file and every 
time you want to submit your answer you can simply paste the content of the entire 
file in the answer box. Just make sure that you don't have any function calls in 
the global section of your file that may interfere with auto-grading (e.g. do not 
print anything). You can put all of your own test cases and calls to the print 
function in a main function and then have a statement like the following at the 
global level:
    ```python
    if __name__ == "__main__":
        main()
    ```
    This way, the main function will not be run when your code is imported on the 
server and therefore it will not interfere with the output of the test cases.
5. Answer the questions in order. The answer to some questions require your answer to 
earlier questions (to use or to build on).
6. For each question, the test cases test some aspects of the provided answer. It is 
computationally infeasible to exhaustively test all possible scenarios. Your answer to a 
question may pass all of our test cases (and receive full mark) but lack some 
functionality that is needed later or even have an undetected bug. As with all programming 
tasks, it is your responsibility to read the specs carefully, and write, test, and debug 
your program.





