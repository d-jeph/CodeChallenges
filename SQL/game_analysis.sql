-- Game Play Analysis 

create table activity (

 player_id     int     ,
 device_id     int     ,
 event_date    date    ,
 games_played  int
 );

 insert into activity values (1,2,'2016-03-01',5 ),(1,2,'2016-03-02',6 ),(2,3,'2017-06-25',1 )
 ,(3,1,'2016-03-02',0 ),(3,4,'2018-07-03',5 );

-- q1: Write an SQL query that reports the first login date for each player
 select player_id, min(event_date) as first_login_date from activity group by 1 order by 1;

-- q2: Write a SQL query that reports the device that is first logged in for each player
SELECT player_id, device_id
FROM 
(SELECT player_id, device_id, row_number() over(partition by player_id order by event_date asc) as rn
FROM activity) a
WHERE rn = 1;

-- q3: Write an SQL query that reports for each player and date, how many games played so far by the player. 
-- That is, the total number of games played by the player until that date.
SELECT player_id, event_date,
    sum(games_played) over(partition by player_id order by event_date asc) as games_played
FROM activity;

-- q4: Write an SQL query that reports the fraction of players that logged in again 
-- on the day after the day they first logged in, rounded to 2 decimal places
SELECT ROUND(AVG(b.event_date IS NOT NULL), 2) AS fraction
FROM
    (
        SELECT player_id, MIN(event_date) AS event_date
        FROM Activity
        GROUP BY 1
    ) AS a
    LEFT JOIN Activity AS b
        ON a.player_id = b.player_id AND DATEDIFF(a.event_date, b.event_date) = -1;