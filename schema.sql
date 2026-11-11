
CREATE DATABASE IF NOT EXISTS etl_example;

USE etl_example;

CREATE TABLE IF NOT EXISTS sample_data (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    city VARCHAR(100) NOT NULL
);

INSERT INTO sample_data (name, age, city) VALUES
('Dinesh', 22, 'Tirunelveli'),
('Arun', 35, 'Chennai'),
('Kumar', 42, 'Madurai'),
('Ravi', 28, 'Coimbatore'),
('Mani', 50, 'Thoothukudi'),
('Suresh', 31, 'Trichy');
