/*

Write a query that'll identify returning active users. 
A returning active user is a user that has made a second purchase within 7 days of any other of their purchases. 
Output a list of user_ids of these returning active users.

Table
id:int
user_id:int
item:varchar
created_at:datetime
revenue:int
*/

select distinct a.user_id
--,a.created_at as first_purchase  ,b.created_at as return_purchase
from amazon_transactions as a
join amazon_transactions as b
on a.user_id=b.user_id
where (b.created_at >= a.created_at and b.created_at <= a.created_at + INTERVAL '7 day')
and a.id != b.id
order by a.user_id 
;