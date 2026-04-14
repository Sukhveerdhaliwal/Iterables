class fibonacci:
    def __init__(self, n):
        if not isinstance(n, int):
            raise ValueError("Input must be an integer")
        self.n = n
    def __iter__(self):
        self.count = 0
        self.a, self.b = 0, 1
        return self
    def __next__(self):
        if self.n < 0:
            raise StopIteration
        if self.count > self.n:
            raise StopIteration
        if self.count == 0:
            self.count += 1
            return 0
        elif self.count == 1:
            self.count += 1
            return 1
        else:
            val = self.a + self.b
            self.a, self.b = self.b, val
            return val
