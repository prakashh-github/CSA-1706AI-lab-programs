% Facts about planets
planet(mercury, rocky, small, closest_to_sun).
planet(venus, rocky, medium, second_closest_to_sun).
planet(earth, rocky, medium, third_closest_to_sun).
planet(mars, rocky, small, fourth_closest_to_sun).
planet(jupiter, gas_giant, large, fifth_closest_to_sun).
planet(saturn, gas_giant, large, sixth_closest_to_sun).
planet(uranus, ice_giant, medium, seventh_closest_to_sun).
planet(neptune, ice_giant, medium, eighth_closest_to_sun).

% Rules for categorizing planets


all_rocky(Planet) :-
findall(Planet, planet(Planet, rocky, _, _), Planet ).

all_gasgiant(Planet) :-
findall(Planet, planet(Planet, gas_giant, _, _), Planet ).

all_icegiant(Planet) :-
findall(Planet, planet(Planet, ice_giant, _, _), Planet ).

all_closesun(Planet) :-
findall(Planet, planet(Planet, _, _, closest_to_sun), Planet ).
