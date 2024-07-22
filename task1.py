from typing import Callable


def caching_fibonacci() -> Callable[[int], int]:
    cache = {}
    
    def fibonacci(n: int) -> int:
        if n in cache:
            return cache[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci


if __name__ == '__main__':
    fibonacci = caching_fibonacci()
    while True:
        try:
            n = int(input('Please enter a number: '))
            print(f'Result is {fibonacci(n)}')
            break
        except ValueError:
            print('Invalid input. Please enter an integer.')
            continue
