#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return deletion-resilient pagination metadata and data.

        Ensures that rows deleted between two queries are not skipped.

        Args:
            index: start index of the page (default None).
            page_size: number of items per page (default 10).

        Returns:
            Dictionary with keys: index, next_index, page_size, data.
        """
        indexed_dataset = self.indexed_dataset()
        assert index is not None and 0 <= index < len(indexed_dataset)

        data = []
        current_index = index
        dataset_size = len(self.dataset())

        while len(data) < page_size and current_index < dataset_size:
            if current_index in indexed_dataset:
                data.append(indexed_dataset[current_index])
            current_index += 1

        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': current_index,
        }
