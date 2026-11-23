CREATE TABLE Book (
  id INTEGER PRIMARY KEY,
  reference_name TEXT NOT NULL,
  title TEXT NOT NULL,
  author TEXT NOT NULL,
  year INTEGER NOT NULL,
  publisher TEXT NOT NULL
);

CREATE TABLE Article (
  id INTEGER PRIMARY KEY,
  reference_name TEXT NOT NULL,
  title TEXT NOT NULL,
  author TEXT NOT NULL,
  year INTEGER NOT NULL,
  journal TEXT NOT NULL,
  pages TEXT NOT NULL
);

CREATE TABLE Inproceedings (
  id INTEGER PRIMARY KEY,
  reference_name TEXT NOT NULL,
  title TEXT NOT NULL,
  author TEXT NOT NULL,
  year INTEGER NOT NULL,
  series TEXT NOT NULL,
  pages TEXT NOT NULL
);

