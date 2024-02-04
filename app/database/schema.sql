DROP TABLE IF EXISTS elements;

CREATE TABLE elements(
  id TEXT unique PRIMARY KEY,
  generatedCode TEXT NOT NULL
);
