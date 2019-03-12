def process_elements(max_times, iterable):
    """
    Takes a collection (iterable) and processes as many elements as indicated by max_times
    :param max_times: maximum numbers of elements to process
    :param iterable: collection of elements
    :returns: Yields the processed element
    """
    internal_counter = 0
    for element in iterable:
        if internal_counter == max_times:
            return
        internal_counter += 1
        yield element * 3


items = [3, 5, 20, 1000000]
for item in process_elements(3, items):
    print(item)
