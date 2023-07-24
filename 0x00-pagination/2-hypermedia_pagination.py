#!/usr/bin/env python3
"""Hypermedia pagination"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple of size two containing a start index and an end index"""
    return ((page - 1) * page_size, page * page_size)


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
        """Method get_page"""
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        total_records = len(self.dataset())
        offset, limit = index_range(page, page_size)
        if offset >= total_records:
            return []
        return self.dataset()[offset:limit]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Method get_hyper"""
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            'page_size': page_size if page < total_pages else 0,
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }


# test
# server = Server()

# print(server.get_hyper(1, 2))
# print("---")
# print(server.get_hyper(2, 2))
# print("---")
# print(server.get_hyper(100, 3))
# print("---")
# print(server.get_hyper(3000, 100))
