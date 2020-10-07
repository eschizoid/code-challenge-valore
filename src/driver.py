import logging
import os

from database_handler.database_handler import DatabaseHandler
from file_parser.file_parser import FileParser
from scrape_dictionary.scrape_dictionary import DictionaryScrapper


def main():
    """Execution point for the pipeline"""
    logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)

    file_parser = FileParser(os.environ["FILE_PATH"])
    dictionary_scrapper = DictionaryScrapper()
    database_handler = DatabaseHandler(
        os.environ["DATABASE_HOST"],
        os.environ["DATABASE_PORT"],
        os.environ["DATABASE_USER"],
        os.environ["DATABASE_PASSWORD"],
        os.environ["DATABASE_NAME"]
    )

    try:
        logging.info("Parsing raw words...")
        raw_words = file_parser.read_file()
        logging.info("Done parsing raw words!")

        logging.info("Persisting word counts...")
        database_handler.insert_words(raw_words)
        logging.info("Done persisting word counts!")

        logging.info("Retrieving words from database...")
        database_words = database_handler.persists_words()
        logging.info("Done retrieving words from database!")

        logging.info("Retrieving speech parts...")
        speech_parts = dictionary_scrapper.get_html(database_words)
        logging.info("Done retrieving speech parts!")

        logging.info("Persisting speech parts...")
        database_handler.insert_speeches(speech_parts)
        logging.info("Persisting speech parts!")
    except Exception as e:
        logging.exception("Error while executing pipeline")
        raise e
    finally:
        logging.info("Done running pipeline!")
        database_handler.connection.close()


if __name__ == "__main__":
    main()
