class CounterIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.n:
            raise StopIteration
        self.current += 1
        return self.current


for i in CounterIterator(5):
    print(i)
