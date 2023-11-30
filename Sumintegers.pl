sum(1, 1).
sum(N, Total) :-
    N > 1,
    Prev is N - 1,
    sum(Prev, PrevTotal),
    Total is PrevTotal + N.
