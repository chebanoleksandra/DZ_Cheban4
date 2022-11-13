class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration
        return self.i


def generator(count):
    i = 0
    for i in count:
        yield i
    return i

count = Counter(10)
# for i in count:
#     print(i, end = ' ')
res = generator(count)


print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())


