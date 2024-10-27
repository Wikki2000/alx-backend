#!/usr/bin/env python3
"""
0-simple_helper_function.py
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Helper function to generate start and end index,
    for iterating and paginating a given data.

    :page - The number of page to paginate and it's 1-index.
    :page_size - The number or size of each page.
    :rtype - A tuple of start and end index.
    """
    start_index = (page - 1) * page_size
    end_index = page_size + start_index
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Paginate a large dataset from csv file.

        :page - The number of page to paginate and it's 1-index.
        :page_size - The number or size of each page.

        :rtype - The paginated dataset.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        start_index, end_index = index_range(page, page_size)

        try:
            return self.dataset()[start_index: end_index]
        except IndexError:
            return []
