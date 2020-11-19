-- Consult database
-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv.title, ge.genre_id
FROM tv_shows AS tv
JOIN tv_show_genres AS ge
ON ge.show_id = tv.id ORDER BY tv.title, ge.genre_id ASC;
