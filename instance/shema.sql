DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS users;

CREATE TABLE book (
  id SERIAL,
  user_id INTEGER NOT NULL,
  title TEXT NOT NULL,
  auther TEXT,
  publisher TEXT,
  PRIMARY KEY (id)
);

CREATE TABLE users (
  id SERIAL,
  username TEXT UNIQUE NOT NULL,
  salt varchar(32),
  password TEXT NOT NULL,
  PRIMARY KEY (id)
);