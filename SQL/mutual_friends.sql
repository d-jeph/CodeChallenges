// You are analyzing a social network dataset at Google. 
// Your task is to find mutual friends between two users, Karl and Hans. 
// There is only one user named Karl and one named Hans in the dataset.

SELECT
  users.user_id,
  users.first_name,
  users.surname,
  Sum(IF(users.user_id = friend_links_1.friend_id, 1, 0)) As mutual
FROM
  users inner join
    (friend_links INNER JOIN friend_links friend_links_1
     ON friend_links.friend_id = friend_links_1.user_id)
  ON friend_links.user_id=1 AND users.user_id<>1
WHERE
  users.surname LIKE '%bloggs%'
GROUP BY
  users.user_id, users.first_name, users.surname
HAVING
  Sum(IF(users.user_id = friend_links.friend_id, 1, 0))=0