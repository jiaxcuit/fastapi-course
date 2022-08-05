--select * from votes;


-- select 
-- posts.title as post_title, 
-- posts.content as post_content, 
-- users.email as user_email
-- from posts join users on posts.owner_id = users.id;

-- select users.id, count(posts.id) as user_post_count 
-- from posts right join users
-- on posts.owner_id = users.id group by users.id;

select posts.*, COUNT(votes.post_id) as votes 
from posts left join votes 
on posts.id = votes.post_id
group by posts.id;