SELECT title
FROM movies
WHERE year = "2008"
SELECT birth
FROM people
WHERE name = "Emma Stone"
SELECT title
FROM movies
WHERE year >= 2018
ORDER BY title ASC
SELECT COUNT(movie_id)
FROM ratings
WHERE rating = 10.0
SELECT title,
    year
FROM movies
WHERE title LIKE "%Harry Potter%"
ORDER BY year ASC
SELECT AVG(rating)
FROM ratings
WHERE movie_id IN (
        SELECT id
        FROM movies
        WHERE year = "2012"
    )
SELECT title,
    ratings.rating
FROM movies
    JOIN ratings ON movies.id = ratings.movie_id
WHERE year = "2010"
ORDER BY ratings.rating DESC,
    movies.title ASC;
SELECT name
FROM people
WHERE people.id IN (
        SELECT stars.person_id
        FROM movies
            JOIN stars ON movies.id = stars.movie_id
        WHERE title = "Toy Story"
    )
SELECT name
FROM people
WHERE people.id IN (
        SELECT stars.person_id
        FROM movies
            JOIN stars ON movies.id = stars.movie_id
        WHERE year = "2004"
    )
ORDER BY people.birth ASC;
SELECT name
FROM people
    JOIN directors ON people.id = directors.person_id
WHERE people.id IN (
        SELECT person_id
        FROM directors
            JOIN movies ON movies.id = directors.movie_id
        WHERE directors.movie_id IN (
                SELECT id
                FROM movies
                    JOIN ratings ON movies.id = ratings.movie_id
                WHERE ratings.movie_id IN (
                        SELECT movie_id
                        FROM ratings
                        WHERE rating >= 9.0
                    )
            )
    )
SELECT title
FROM ratings
    JOIN movies ON movies.id = ratings.movie_id
WHERE movies.title IN (
        SELECT title
        FROM movies
            JOIN stars ON stars.movie_id = movies.id
        WHERE stars.person_id IN (
                SELECT person_id
                FROM stars
                    JOIN people ON people.id = stars.person_id
                WHERE stars.person_id = (
                        SELECT id
                        FROM people
                        WHERE name = "Chadwick Boseman"
                    )
            )
    )
ORDER BY rating DESC
LIMIT 5;
SELECT title
FROM movies
    JOIN stars ON stars.movie_id = movies.id
WHERE stars.person_id IN (
        SELECT person_id
        FROM stars
            JOIN people ON stars.person_id = people.id
        WHERE stars.person_id IN (
                SELECT id
                FROM people
                WHERE name = 'Johnny Depp'
            )
    )
INTERSECT
SELECT title
FROM movies
    JOIN stars ON stars.movie_id = movies.id
WHERE stars.person_id IN (
        SELECT person_id
        FROM stars
            JOIN people ON stars.person_id = people.id
        WHERE stars.person_id IN (
                SELECT id
                FROM people
                WHERE name = 'Helena Bonham Carter'
            )
    )
SELECT DISTINCT name
FROM movies
    JOIN stars ON movies.id = stars.movie_id
    JOIN people ON stars.person_id = people.id
WHERE movies.id IN (
        SELECT movie_id
        FROM stars
        WHERE person_id IN(
                SELECT id
                FROM people
                WHERE name = "Kevin Bacon"
                    AND birth = 1958
            )
    )
    AND people.id NOT IN (
        SELECT id
        FROM people
        WHERE name = "Kevin Bacon"
            AND birth = 1958
    );