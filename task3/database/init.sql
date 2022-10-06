CREATE DATABASE IF NOT EXISTS test;

CREATE USER IF NOT EXISTS 'guest'@'%' IDENTIFIED BY 'guestguest';
GRANT ALL ON test.* TO 'guest'@'%';
FLUSH PRIVILEGES;

USE test;
CREATE TABLE IF NOT EXISTS users (
    id INT(10) NOT NULL AUTO_INCREMENT,
    login VARCHAR(20) NOT NULL UNIQUE,
    password VARCHAR(80) NOT NULL,
    `group` VARCHAR(10),
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS items (
    id INT(10) NOT NULL AUTO_INCREMENT,
    name VARCHAR(60) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id)
);

INSERT IGNORE INTO users
SET id = 1,
login = 'admin',
password = '$2y$10$zg8.a61TAaVe.IbijfV/9OcCK2mqWruVU9ZPDCt3LaV0kyfjIgj4K',
`group` = 'admin';

INSERT INTO items (name, price)
VALUES
    ('Дверь входная', 17490),
    ('Светильник светодиодный', 749),
    ('Шпаклевка полимерная', 632),
    ('Мембрана звукоизоляционная', 1719);