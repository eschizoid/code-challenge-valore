from database_handler.database_handler import DatabaseHandler


class TestDatabaseHandler:

    def test_insert_words(self):
        database_handler = DatabaseHandler("127.0.0.1", "5432", "docker", "docker", "valore")
        cursor = database_handler.cursor
        cursor.execute("""SELECT count(*) FROM words""")
        assert cursor.fetchone()[0] > 0
        database_handler.connection.close()

    def test_insert_speeches(self):
        database_handler = DatabaseHandler("127.0.0.1", "5432", "docker", "docker", "valore")
        cursor = database_handler.cursor
        cursor.execute("""SELECT count(*) FROM speeches""")
        assert cursor.fetchone()[0] > 0
        database_handler.connection.close()
