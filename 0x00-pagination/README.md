# Pagination

## Description
Pagination is a way to divide content into separate pages. It is commonly used in web applications that display lots of content in a single page. Pagination allows users to view a specific section of the website, without having to scroll through the entire page. This project contains tasks on how to paginate datasets.

## Tasks
### 0. Simple helper function
Write a function named ```index_range``` that takes two integer arguments ```page``` and ```page_size```.
The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.
Page numbers are 1-indexed, i.e. the first page is page 1.

### 1. Simple pagination
Copy ```index_range``` function and the ```Server``` class from ```0-simple_helper_function.py``` into ```1-simple_pagination.py```.
Implement a ```get_page``` method with the following prototype:

* ```def get_page(self) -> List[List[str]]:```
* Use ```assert``` to verify that both ```page``` and ```page_size``` are integers greater than 0.
* Use ```index_range``` to find the correct indexes to paginate the dataset correctly and return the appropriate page of the dataset (i.e. the correct list of rows).
* If the input arguments are out of range for the dataset, an empty list should be returned.

### 2. Hypermedia pagination
Replicate code from the previous task.
Implement a ```get_hyper``` method that takes the same arguments (and defaults) as ```get_page``` and returns a dictionary containing the following key-value pairs:

* ```page_size```: the length of the returned dataset page
* ```page```: the current page number
* ```data```: the dataset page (equivalent to return from previous task)
* ```next_page```: number of the next page, ```None``` if no next page
* ```prev_page```: number of the previous page, ```None``` if no previous page
* ```total_pages```: the total number of pages in the dataset as an integer

### 3. Deletion-resilient hypermedia pagination
The goal here is that if between two queries, certain rows are removed from the dataset, the user does not miss items from dataset when changing page.
Start with the code below:

``` python
#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


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
            pass
```

Implement a ```get_hyper_index``` method with two integer arguments: ```index``` with a ```None``` default value and ```page_size``` with default value of ```10```.
The method should return a dictionary with the following key-value pairs:

* ```index```: the current start index of the return page. That is the index of the first item in the current page. For example if requesting page 3 with ```page_size``` 20, and no data was removed from the dataset, the current index should be 60.
* ```next_index```: the next index to query with. That should be the index of the first item after the last item on the current page.
* ```page_size```: the current page size
* ```data```: the actual page of the dataset

#### Requirements/Behaviour:
* Use ```assert``` to verify that ```index``` is in a valid range.
* if the user queries index 0, ```page_size``` 10, they will get rows indexed 0 to 9 included.
* if they request the next index, 10, with ```page_size``` 10, but rows 3, 6 and 7 were deleted, they user should still receive rows indexed 10 to 19 included.

## License
MIT. See [LICENSE](./LICENSE) for more details.