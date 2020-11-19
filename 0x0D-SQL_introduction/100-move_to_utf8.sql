-- Turns database hbtn_0c_0 to utf8
-- converts hbtn_0c_0 to utf8
USE hbtn_0c;
ALTER DATABASE hbtn_0c CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
