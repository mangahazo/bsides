CREATE TABLE websites (
  id TEXT PRIMARY KEY,
  content TEXT,
  user_id TEXT
);

CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  username TEXT,
  password TEXT
);

INSERT INTO users (username, password) VALUES ('admin', 'localpassword');