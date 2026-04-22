#!/usr/bin/env python3
"""Module for index_range helper function."""


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
