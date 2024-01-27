DROP TABLE IF EXISTS elements;

CREATE TABLE elements(
  id TEXT unique PRIMARY KEY,
  generatedCode TEXT UNIQUE NOT NULL
);

INSERT INTO elements (id, generatedCode) values ("550e8400-e29b-41d4-a716-446655440000","test")