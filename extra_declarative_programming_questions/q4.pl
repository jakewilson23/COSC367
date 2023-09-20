%match(Left, Right) :- (Left = c , Right = g); (Left = g , Right = c).
%match(Left, Right) :- (Left = a , Right = t); (Left = t , Right = a).
%dna([], []).
%dna([LH|LTail], [RH|RTail]) :- match(LH, RH), dna(LTail, RTail).

pair(a, t).
pair(c, g).
match(L, R) :- pair(L, R); pair(R, L).
dna([], []).
dna([H1|T1], [H2|T2]) :- match(H1, H2), dna(T1, T2).

test_answer :- dna([a, t, c, g], X), writeln(X).
test_answer2 :- dna(X, [t, a, g, c]), writeln(X).