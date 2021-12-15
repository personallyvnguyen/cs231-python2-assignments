# iterators.py
#
# A231 Python 2 Spring 2021
# Credit: Nguyen, Van (C02699930)
# Practice w/Iterators


# 1
'''
An iterable is an object that can be iterated over.
An iterator is an object that has a next() method.
Iterables can be iterated over by creating an iterator.
'''


# 2
test_str = 'abcdefg'.__iter__()

try:
    while True:
        print(test_str.__next__())
except StopIteration:
    pass


# 3
def group_n(iterable: any, len: int) -> list[list]:
    '''
    Returns a list of lists of size len composed of the given iterables
    elements.
    '''
    group = []
    sub_group = []

    for idx, item in enumerate(iter(iterable), 1):
        sub_group.append(item)

        if idx % len == 0:
            group.append(sub_group)
            sub_group = []

    return group


# 4
class fib_range:
    'Generates values of fibonacci values from indices start to end'
    def __init__(self, start: int, end: int) -> None:
        self.start, self.end = start, end

    def __iter__(self):
        self.prev = 1
        self.next = 1
        self.curIdx = 1

        while self.curIdx != self.start:
            self.prev, self.next = self.next, self.prev + self.next
            self.curIdx += 1

        return self

    def __next__(self):
        if self.curIdx > self.end:
            raise StopIteration
        elif self.curIdx >= self.start:
            answer = self.prev
            self.prev, self.next = self.next, self.prev + self.next
            self.curIdx += 1
            return answer

