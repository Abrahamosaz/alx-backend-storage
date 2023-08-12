-- sql script that create a new table users
-- fields id, name, email
CREATE TABLE IF NOT EXISTS users(
id INT NOT NULL AUTO_INCREMENT,
email VARCHAR(255) NOT NULL UNIQUE,
name VARCHAR(255),
primary key(id)
);