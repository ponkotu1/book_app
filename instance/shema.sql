DROP TABLE  book;
DROP TABLE IF EXISTS users;

CREATE TABLE book (
  id SERIAL,
  ISBN INTEGER NOT NULL,
  title varchar(64) NOT NULL,
  auther varchar(64),
  publisher varchar(64),
  PRIMARY KEY (id)
);

CREATE TABLE users (
  id SERIAL,
  name TEXT UNIQUE NOT NULL,
  hashed_password varchar(64),
  salt varchar(32) NOT NULL,
  PRIMARY KEY (id)
);