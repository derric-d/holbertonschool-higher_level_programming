-- create db to use, give user and pswd as provided
-- grant select (read of crud) of db to user
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
USE hbtn_0d_2;
DROP USER IF EXISTS user_0d_2@localhost;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
