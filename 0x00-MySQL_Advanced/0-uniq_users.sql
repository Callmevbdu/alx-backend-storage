-- This SQL script creates a table named 'users' if it doesn't already exist.

CREATE TABLE IF NOT EXISTS users (
    -- 'id' is an integer that auto-increments.
    id INT AUTO_INCREMENT PRIMARY KEY,
    
    -- 'email' is a string of up to 255 characters.
    email VARCHAR(255) NOT NULL UNIQUE,
    
    -- 'name' is a string of up to 255 characters.
    name VARCHAR(255)
);
