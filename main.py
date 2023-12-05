#!/usr/bin/env python3
from os import get_terminal_size
from functools import cache

@cache
def fatorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1

    if n < 0:
        raise ValueError('math domain error')

    return n * fatorial(n-1)

def combinacao(n: int, p: int) -> int:
    return int(fatorial(n)  // (fatorial(p) * fatorial(n-p)))

def l_pascal(n: int):
    for i in range(n):
        yield combinacao(n, i)

    yield 1

def main():
    linhas = int(input('Quantas linhas você quer? '))

    print()

    for n in range(linhas):
        lines = '   '.join(map(str, l_pascal(n)))
        print(f'{lines.center(get_terminal_size()[0])}')
        print()

if __name__ == '__main__':
    main()
