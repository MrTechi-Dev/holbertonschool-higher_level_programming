-- Use left join
--  lists all shows contained in the database hbtn_0d_tvshows.
SELECT tv.title, ge.genre_id
FROM tv_shows AS tv
LEFT JOIN tv_show_genres AS ge
ON ge.show_id = tv.id ORDER BY tv.title, ge.genre_id ASC;
