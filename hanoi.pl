% Predicate to solve Towers of Hanoi problem
hanoi(N) :-
    move(N, left, middle, right).

% Base case: Move 1 disk from A to C
move(1, A, _, C) :-
    write('Move disk from '), write(A), write(' to '), write(C), nl.

% Recursive case: Move N disks from A to C using B as auxiliary
move(N, A, B, C) :-
    N > 1,
    M is N - 1,
    move(M, A, C, B),  % Move N-1 disks from A to B using C
    move(1, A, _, C),  % Move the largest disk from A to C
    move(M, B, A, C).  % Move N-1 disks from B to C using A
