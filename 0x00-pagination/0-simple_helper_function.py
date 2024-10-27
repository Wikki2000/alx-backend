#!/usr/bin/env python3
"""
0-simple_helper_function.py
"""


def index_range(page: int, page_size: int) ->tuple:
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
