#!/usr/bin/env python3
"""Module for simple pagination."""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of start and end indexes for the given pagination params.

    Args:
        page: 1-indexed page number.
        page_size: number of items per page.

    Returns:
        A tuple (start_index, end_index).
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of the dataset.

        Args:
            page: 1-indexed page number (default 1).
            page_size: number of items per page (default 10).

        Returns:
            List of rows for the requested page, or [] if out of range.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        if start >= len(dataset):
            return []

        return dataset[start:end]
