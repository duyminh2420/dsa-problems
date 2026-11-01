with first_login as (
    select player_id, min(event_date) as first_date
    from activity
    group by player_id
)

select round(count(distinct a.player_id) * 1.0 / (select count(distinct player_id) from activity), 2) as fraction
from activity a
join first_login f 
    on a.player_id = f.player_id
    and a.event_date = f.first_date + interval '1 day';