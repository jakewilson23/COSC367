is_binary(X) :- X = 0; X = 1.
is_binary_list([Head | Tail]) :- is_binary(Head), (Tail = []; is_binary_list(Tail)).
binary_number([0, b | Tail]) :- is_binary_list(Tail).

test_answer :- binary_number([0, b, 1, 0, 1]), writeln('OK').

test_answer2 :- binary_number([0, b, 0, 1, 2]), writeln('Wrong!'), halt.
test_answer2 :- writeln('OK').