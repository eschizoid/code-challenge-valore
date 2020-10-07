DROP TABLE IF EXISTS words;
DROP TABLE IF EXISTS definitions;

CREATE TABLE IF NOT EXISTS words
(
    word_id    SERIAL PRIMARY KEY,
    word       VARCHAR(255) NOT NULL,
    word_count INT          NOT NULL
);

CREATE TABLE IF NOT EXISTS speeches
(
    speech_id    SERIAL PRIMARY KEY,
    word_id      INTEGER REFERENCES words (word_id),
    speech_parts VARCHAR(255) NOT NULL
);
