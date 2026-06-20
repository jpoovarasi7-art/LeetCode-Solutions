# Write your MySQL query statement below
SELECT C.name AS Customers FROM Customers C LEFT JOIN Orders o ON o.customerId = c.id WHERE o.id IS NULL;