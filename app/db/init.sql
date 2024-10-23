CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(255) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL
);

INSERT INTO users (username, password) VALUES
('mercadobitcoin@gmail.com', 'mercadobitcoin2024')
ON CONFLICT (username) DO NOTHING;
