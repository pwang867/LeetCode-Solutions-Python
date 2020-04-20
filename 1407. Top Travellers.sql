# Write your MySQL query statement below
SELECT
    Users.name,
    IFNULL(SUM(Rides.distance), 0) AS travelled_distance
FROM Users
LEFT JOIN Rides  # must be left join
ON Rides.user_id = Users.id
GROUP BY Rides.user_id
ORDER BY travelled_distance DESC, Users.name ASC

