/*
Find customers who have never made an order.
Output the first name of the customer.

customers
id:int
first_name:varchar
last_name:varchar
city:varchar
address:varchar
phone_number:varchar

orders
id:int
cust_id:int
order_date:datetime
order_details:varchar
total_order_cost:int
*/

select first_name
from customers
where id not in (select cust_id from orders);