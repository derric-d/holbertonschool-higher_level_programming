-- convert db, table 'first_table' and field 'name' in table to utf8
use hbtn_0c_0;
alter table first_table
MODIFY name VARCHAR(256) CHARACTER SET utf8mb4;
alter table first_table
convert to character set utf8mb4 collate utf8mb4_unicode_ci;
alter database hbtn_0c_0
character set utf8mb4 collate utf8mb4_unicode_ci;
