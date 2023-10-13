CREATE TABLE friends (
  id INTEGER,
  name TEXT,
  birthday DATE
);

INSERT INTO friends (id, name, birthday)
VALUES (1, 'Ororo Munroe', '1940-05-30');

INSERT INTO friends(id, name, birthday)
VALUES (2, 'Cieran', '2003-08-18');

INSERT INTO friends(id, name, birthday)
VALUES (3, 'Annie', '2002-09-17');

UPDATE friends
SET name = 'Storm'
WHERE id = 1;

ALTER TABLE friends
ADD COLUMN email TEXT;

UPDATE friends
SET email = 'storm@codecademy.com'
where id = 1;

UPDATE friends
SET email = 'cieran@codecademy.com'
where id = 2;

UPDATE friends
SET email = 'annie@codecademy.com'
where id = 3;

delete from friends
where id = 1;

SELECT * FROM friends;