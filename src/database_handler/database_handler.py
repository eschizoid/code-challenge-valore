from typing import ItemsView, List

import psycopg2
import psycopg2.extras


class DatabaseHandler:

    def __init__(self, database_host, database_port, database_user, database_password, database_name) -> None:
        connection = psycopg2.connect(host=database_host,
                                      port=database_port,
                                      user=database_user,
                                      password=database_password,
                                      database=database_name)
        self.connection = connection
        self.cursor = connection.cursor()

    def insert_words(self, words: ItemsView) -> None:
        """Persists words and number of appearances"""
        self.cursor.executemany("""INSERT INTO words(word, word_count) VALUES (%s, %s);""", words)
        self.connection.commit()

    def persists_words(self) -> List:
        """Retrieves all words"""
        self.cursor.execute("""SELECT word_id, word FROM words LIMIT 100;""")
        return self.cursor.fetchall()

    def insert_speeches(self, speeches: List) -> None:
        """Persists words with their respective speech parts"""
        self.cursor.executemany("""INSERT INTO speeches(word_id, speech_parts) VALUES (%s, %s);""", speeches)
        self.connection.commit()
