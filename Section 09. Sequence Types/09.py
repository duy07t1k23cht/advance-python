from functools import lru_cache


class Fibonacci:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0 or index > self.n - 1:
                raise IndexError

            return Fibonacci.fib(index)
        else:
            indices = index.indices(self.n)
            return [Fibonacci.fib(k) for k in range(*indices)]

    @staticmethod
    @lru_cache  # Stand for Least Recent Used
    def fib(n):
        if n < 2:
            return 1
        print(f"Calc fib ({n})")
        return Fibonacci.fib(n - 2) + Fibonacci.fib(n - 1)


# fibonacci = Fibonacci(100)
print(Fibonacci.fib(20))

square_list = [n**2 for n in range(10)]
for n in square_list:
    print(n)
