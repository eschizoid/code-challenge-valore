from collections import Counter
from typing import ItemsView


class FileParser:

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read_file(self) -> ItemsView[str, int]:
        """Retrieves the number of appearances of each word"""
        file = open(self.file_path, "r+")
        wordcount = Counter(file.read().split())
        return wordcount.items()
