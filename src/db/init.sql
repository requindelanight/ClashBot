DROP DATABASE IF EXISTS clash_of_clan;
CREATE DATABASE clash_of_clan;

CREATE USER 'clash_admin'@'localhost' IDENTIFIED BY 'votremotdepasse';
GRANT ALL PRIVILEGES ON clash_of_clan.* TO 'clash_admin'@'localhost';

USE clash_of_clan;

DROP TABLE IF EXISTS user;
CREATE TABLE user (id BIGINT NOT NULL, tag VARCHAR(20) NOT NULL, PRIMARY KEY(id));

