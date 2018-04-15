class LFG:
    __slots__ = ["j", "k", "m", "x"]
    def __init__(self, j, k, m, fib):
        self.j = j
        self.k = k
        self.m = 2**m
        self.x = [next(fib) for _ in range(k)]

    def __next__(self):
        n = len(self.x)
        result = (self.x[n-self.j]^self.x[n-self.k])%self.m
        self.x.append(result)
        return result
