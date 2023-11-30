% Facts about individuals with their name and date of birth
dob(john, date(1990, 5, 15)).
dob(susan, date(1985, 9, 20)).
dob(mike, date(1992, 3, 10)).
dob(lisa, date(1988, 12, 5)).
dob(emma, date(1995, 7, 25)).

% Query to find the date of birth given a name
find_dob(Name, DateOfBirth) :-
    dob(Name, DateOfBirth).

% Query to find individuals born in a specific year
born_in_year(Year, Person) :-
    dob(Person, date(Year, _, _)).
