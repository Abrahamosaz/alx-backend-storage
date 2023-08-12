-- script that creat a table user with the below fields
-- id, name, email, country
CREATE TABLE IF NOT EXISTS users(
id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
email VARCHAR(255) NOT NULL UNIQUE,
name VARCHAR(255),
country ENUM('US',  'CO', 'TI') DEFAULT 'US' NOT NULL
);