CREATE DATABASE solar_system;

CREATE TABLE planets (
    
    name VARCHAR(50),
    surface_area BIGINT,
    moons INT,
    distance_from_sun BIGINT,
    namesake TEXT
);

INSERT INTO planets (
    name,
    surface_area,
    moons, 
    distance_from_sun,
    namesake
    )
    VALUES ('Jupiter',23710000000,79,483300000,'King of the Roman gods, aka Zeus.'),
    ('Mars',55910000,2,141000000,'Roman god of war, aka Ares.'),
    ('Venus',67400000,0,177700000,'Roman goddess of love, aka Aphrodite.'),
    ('Earth',57510000,1,93123021,'A variation on the word ''ground'' in several languages'),
    ('Neptune',2941000000,14,2793000000,'Roman god of the sea aka, Poseidon.'),
    ('Saturn',16490000000,62,890900000,'Jupiter''s'' father and titan aka, Chronos.'),
    ('Uranus',3171000000,27,1784000000,'Greek personificatino of the sky or heavens, aka Caelus.'),
    ('Mercury',28880000,0,35980000,'Roman god of travellers, aka Hermes.');

DELETE FROM planets WHERE name = 'Jupiter' 
-- # How many planets are there?
SELECT COUNT (*) FROM planets
-- What are the names of all the planets and the number of their moons that have a distance from the -- sun greater than 500,000,000 miles?
SELECT name , moons FROM planets WHERE distance_from_sun > 500000000;
-- What is the ID of the record with the 62 moons?
INSERT INTO planets (id)
VALUES (PRIMARY KEY GENERATED ALWAYS AS IDENTITY);
