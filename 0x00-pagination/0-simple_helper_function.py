#!/usr/bin/env python3
"""
0-simple_helper_function.py
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Helper function to generate start and end index,
    for iterating and paginating a given data.

    :page - The page number to paginate and it's 1-index.
    :page_size - The number or size of each page.
    :rtype - A tuple of start and end index.
    """
    start_index = (page - 1) * page_size
    end_index = page_size + start_index
    return start_index, end_index
