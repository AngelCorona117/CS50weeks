-- Keep a log of any SQL queries you execute as you solve the mystery.
--SELECT * FROM crime_scene_reports LIMIT 10;
--SELECT * FROM crime_scene_reports WHERE day="28" AND month="7"
--SELECT * FROM interviews WHERE month="7" AND day="28";
--SELECT * FROM atm_transactions WHERE month=7 AND day=28 AND atm_location="Leggett Street"
-- SELECT * FROM flights WHERE month=7 AND day="29";
--SELECT destination_airport_id FROM flights WHERE id=36;
--SELECT * FROM airports JOIN flights ON flights.destination_airport_id=airports.id WHERE flights.destination_airport_id=(SELECT destination_airport_id FROM flights WHERE id=36);
--SELECT * FROM phone_calls WHERE month=7 AND day=28 AND duration <60;
--SELECT name that has a licence plate in the scene and made a call with lees that 60 seconds
-- at that hour and made a flight on july 29
autos a la hora del robo que salieron
select license_plate
FROM bakery_security_logs
WHERE month = 7
    AND day = 28
    AND hour = 10
    and activity = "exit";
SELECT name
FROM people
WHERE license_plate IN (
        select license_plate
        FROM bakery_security_logs
        WHERE month = 7
            AND day = 28
            AND hour = 10
            and activity = "exit"
    ) OWNERS of cars that left the bakery at 10 am
SELECT name
FROM people
WHERE license_plate IN (
        select license_plate
        FROM bakery_security_logs
        WHERE month = 7
            AND day = 28
            AND hour = 10
            and activity = "exit"
    );
DURATION LESS THAN 60
SELECT *
FROM phone_calls
WHERE month = 7
    AND day = 28
    AND duration < 60;
SELECT receiver
FROM phone_calls
WHERE month = 7
    AND day = 28
    AND duration < 60;
SELECT name
FROM people
WHERE license_plate IN (
        select license_plate
        FROM bakery_security_logs
        WHERE month = 7
            AND day = 28
            AND hour = 10
            and activity = "exit"
    )
    AND phone_number IN (
        SELECT receiver
        FROM phone_calls
        WHERE month = 7
            AND day = 28
            AND duration < 60
    ) PHONE OF THE RECEIVER OF THE CALL (aka the thief)
SELECT name
FROM people
WHERE phone_number IN (
        SELECT receiver
        FROM phone_calls
        WHERE month = 7
            AND day = 28
            AND duration < 60
    );
SUSPECTS OF BOTH BEING AT THE BAKERY AT 10 AM
AND MAKING A CALL FOR LESS THAN 60 SECONDS SOSPECHOSOS ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
SELECT name
FROM people
WHERE license_plate IN (
        select license_plate
        FROM bakery_security_logs
        WHERE month = 7
            AND day = 28
            AND hour = 10
            and activity = "exit"
    )
INTERSECT
SELECT name
FROM people
WHERE phone_number IN (
        SELECT caller
        FROM phone_calls
        WHERE month = 7
            AND day = 28
            AND duration < 60
    );
! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
SELECT *
FROM people
WHERE license_plate IN (
        select license_plate
        FROM bakery_security_logs
        WHERE month = 7
            AND day = 28
            AND hour = 10
            and activity = "exit"
    )
INTERSECT
SELECT *
FROM people
WHERE phone_number IN (
        SELECT caller
        FROM phone_calls
        WHERE month = 7
            AND day = 28
            AND duration < 60
    );
CHECA SI HIZO UNA RANSACCION ANTES DEL ROBO
SELECT account_number
FROM atm_transactions
WHERE month = 7
    AND day = 28
    AND atm_location = "Leggett Street"
SELECT person_id
FROM bank_accounts
WHERE account_number IN (
        SELECT account_number
        FROM atm_transactions
        WHERE month = 7
            AND day = 28
            AND atm_location = "Leggett Street"
    )
SELECT *
FROM people
WHERE id IN (
        SELECT person_id
        FROM bank_accounts
        WHERE account_number IN (
                SELECT account_number
                FROM atm_transactions
                WHERE month = 7
                    AND day = 28
                    AND atm_location = "Leggett Street"
            )
    );
PERSONAS QUE HICIERON UNA TRANSACCION ANTES DEL ROBO
SELECT *
FROM people
WHERE id IN (
        SELECT person_id
        FROM bank_accounts
        WHERE account_number IN (
                SELECT account_number
                FROM atm_transactions
                WHERE month = 7
                    AND day = 28
                    AND atm_location = "Leggett Street"
            )
    );
COMPARALO CON LOS SOSPECHOSOS ACTUALES
SELECT name
FROM people
WHERE license_plate IN (
        select license_plate
        FROM bakery_security_logs
        WHERE month = 7
            AND day = 28
            AND hour = 10
            and activity = "exit"
    )
INTERSECT
SELECT name
FROM people
WHERE phone_number IN (
        SELECT caller
        FROM phone_calls
        WHERE month = 7
            AND day = 28
            AND duration < 60
    )
INTERSECT
SELECT name
FROM people
WHERE id IN (
        SELECT person_id
        FROM bank_accounts
        WHERE account_number IN (
                SELECT account_number
                FROM atm_transactions
                WHERE month = 7
                    AND day = 28
                    AND atm_location = "Leggett Street"
            )
    );
NUVEOS SOSPECHOSOS ! ! ! !
SELECT name
FROM people
WHERE license_plate IN (
        select license_plate
        FROM bakery_security_logs
        WHERE month = 7
            AND day = 28
            AND hour = 10
            and activity = "exit"
    )
INTERSECT
SELECT name
FROM people
WHERE phone_number IN (
        SELECT caller
        FROM phone_calls
        WHERE month = 7
            AND day = 28
            AND duration < 60
    )
INTERSECT
SELECT name
FROM people
WHERE id IN (
        SELECT person_id
        FROM bank_accounts
        WHERE account_number IN (
                SELECT account_number
                FROM atm_transactions
                WHERE month = 7
                    AND day = 28
                    AND atm_location = "Leggett Street"
            )
    );
NUEVOS SOSPECHOSOS ! ! ! ! ! ! CHECA SUS VUELOS EL QUE HAYA VOLADO EN LA MAÑANA DEL 29 LO HIZO:
SELECT *
FROM people
WHERE license_plate IN (
        select license_plate
        FROM bakery_security_logs
        WHERE month = 7
            AND day = 28
            AND hour = 10
            and activity = "exit"
    )
INTERSECT
SELECT *
FROM people
WHERE phone_number IN (
        SELECT caller
        FROM phone_calls
        WHERE month = 7
            AND day = 28
            AND duration < 60
    )
INTERSECT
SELECT *
FROM people
WHERE id IN (
        SELECT person_id
        FROM bank_accounts
        WHERE account_number IN (
                SELECT account_number
                FROM atm_transactions
                WHERE month = 7
                    AND day = 28
                    AND atm_location = "Leggett Street"
            )
    );
SELECT *
FROM passengers
WHERE passport_number IN (
        SELECT passport_number
        FROM people
        WHERE license_plate IN (
                select license_plate
                FROM bakery_security_logs
                WHERE month = 7
                    AND day = 28
                    AND hour = 10
                    and activity = "exit"
            )
        INTERSECT
        SELECT passport_number
        FROM people
        WHERE phone_number IN (
                SELECT caller
                FROM phone_calls
                WHERE month = 7
                    AND day = 28
                    AND duration < 60
            )
        INTERSECT
        SELECT passport_number
        FROM people
        WHERE id IN (
                SELECT person_id
                FROM bank_accounts
                WHERE account_number IN (
                        SELECT account_number
                        FROM atm_transactions
                        WHERE month = 7
                            AND day = 28
                            AND atm_location = "Leggett Street"
                    )
            )
    );
RECUERDA QUE EL VUELO NUMERO 36 ERA EL PRIMER VUELO AL DIA SIGUIENTE
SELECT *
FROM passengers
WHERE passport_number IN (
        SELECT passport_number
        FROM people
        WHERE license_plate IN (
                select license_plate
                FROM bakery_security_logs
                WHERE month = 7
                    AND day = 28
                    AND hour = 10
                    and activity = "exit"
            )
        INTERSECT
        SELECT passport_number
        FROM people
        WHERE phone_number IN (
                SELECT caller
                FROM phone_calls
                WHERE month = 7
                    AND day = 28
                    AND duration < 60
            )
        INTERSECT
        SELECT passport_number
        FROM people
        WHERE id IN (
                SELECT person_id
                FROM bank_accounts
                WHERE account_number IN (
                        SELECT account_number
                        FROM atm_transactions
                        WHERE month = 7
                            AND day = 28
                            AND atm_location = "Leggett Street"
                    )
            )
    );
suspects
SELECT *
FROM people
WHERE passport_number = 3592750733;
= DIANA HIJA DE PUTA
SELECT *
FROM people
WHERE passport_number = 1988161715;
= MALDITA TAYLOR CULEA WHO CALLED WHO
SELECT *
FROM phone_calls
WHERE month = 7
    AND day = 28
    AND duration < 60;
SELECT name
FROM people
WHERE phone_number = "(676) 555-6554";
WHAT A PLOTTWIST IT WASNT DIANA,
NEITHER TAYLOR BUT BRUCE HOW COULD YOUUUUUUU you were my gallo