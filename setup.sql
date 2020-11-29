CREATE TABLE IF NOT EXISTS
user(id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(120),
hobby VARCHAR(120),
sex VARCHAR(120)
);

INSERT INTO user(
    name,
    hobby,
    sex)
VALUES(
    "Duane",
    "Games",
    "Male"
);