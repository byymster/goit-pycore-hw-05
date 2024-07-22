from typing import Generator, Callable
import re


def generator_numbers(str: str) -> Generator[float, None, None]:
    for match in re.finditer(r'\d+\.\d+', str):
        yield float(match.group())


def sum_profit(text: str, func: Callable) -> float:
    return sum(func(text))


if __name__ == '__main__':
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")