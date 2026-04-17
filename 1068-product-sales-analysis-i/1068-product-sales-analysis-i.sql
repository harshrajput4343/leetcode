# Write your MySQL query statement below
select d.product_name , s.year  , s.price
from sales s
join product d
on s.product_id = d.product_id 