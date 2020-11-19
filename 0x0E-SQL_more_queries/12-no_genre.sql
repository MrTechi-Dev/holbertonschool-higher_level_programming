-- Use left join
--  List no genre
SELECT tv.title, ge.genre_id
FROM tv_shows AS tv
LEFT JOIN tv_show_genres AS ge
ON ge.show_id = tv.id
WHERE ge.genre_id IS NULL ORDER BY tv.title, ge.genre_id ASC;

    © 2020 GitHub, Inc.
    Terms
    Privacy
    Security
    Status
    Help
    Contact GitHub
    Pricing
    API
