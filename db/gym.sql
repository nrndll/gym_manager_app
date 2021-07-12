DROP TABLE bookings;
DROP TABLE activities;
DROP TABLE members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    premium BOOLEAN
);

CREATE TABLE activities (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255),
    capacity INT,
    premium BOOLEAN,
    date VARCHAR(255),
    time VARCHAR(255)
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    activity_id INT REFERENCES activities(id) ON DELETE CASCADE
);