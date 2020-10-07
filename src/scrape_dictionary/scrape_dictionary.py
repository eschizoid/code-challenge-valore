from typing import List

import requests
from bs4 import BeautifulSoup
from multiprocessing.pool import ThreadPool

DICTIONARY_COM_URL = 'https://www.dictionary.com/browse/'


class DictionaryScrapper:

    @staticmethod
    def get_html(words: List) -> List:
        """Retrieves a list of words with their respective speeches coming from dictionary.com"""
        content = []
        for word in words:
            results = BeautifulSoup(requests.get(DICTIONARY_COM_URL + word[1]).content, "html.parser")
            speeches = results.find_all(class_="luna-pos")
            cleanse_speeches = [speech.text.replace(",", "") for speech in speeches]
            speech = (word[0], ",".join(list(dict.fromkeys(cleanse_speeches))))
            content.append(speech)
        return content
