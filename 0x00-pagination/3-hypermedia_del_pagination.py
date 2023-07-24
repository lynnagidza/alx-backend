#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Method get_hyper_index"""
        assert type(index) == int and type(page_size) == int
        assert 0 <= index < len(self.indexed_dataset())
        dataset = self.indexed_dataset()
        data = []
        next_index = index + page_size
        for i in range(index, next_index):
            if dataset.get(i):
                data.append(dataset[i])
            else:
                next_index += 1
        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        }


# test
# server = Server()

# server.indexed_dataset()

# try:
#     server.get_hyper_index(300000, 100)
# except AssertionError:
#     print("AssertionError raised when out of range")

# index = 3
# page_size = 2

# print("Nb items: {}".format(len(server._Server__indexed_dataset)))

# # 1- request first index
# res = server.get_hyper_index(index, page_size)
# print(res)

# # 2- request next index
# print(server.get_hyper_index(res.get('next_index'), page_size))

# # 3- remove the first index
# del server._Server__indexed_dataset[res.get('index')]
# print("Nb items: {}".format(len(server._Server__indexed_dataset)))

# # 4- request again the initial index -> the first data retreives is not the
# # same as the first request
# print(server.get_hyper_index(index, page_size))

# # 5- request again initial next index -> same data page as the request 2-
# print(server.get_hyper_index(res.get('next_index'), page_size))
