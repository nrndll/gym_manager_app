DROP TABLE bookings;
DROP TABLE lessons;
DROP TABLE members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    second_name VARCHAR(255),
    premium BOOLEAN
);

CREATE TABLE lessons (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255),
    capacity INT(255),
    premium BOOLEAN
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    lesson_id INT REFERENCES lessons(id) ON DELETE CASCADE
);