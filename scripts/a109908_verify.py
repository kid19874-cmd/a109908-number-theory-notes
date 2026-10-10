#!/usr/bin/env python3
"""OEIS A109908 exploratory checker. Exact for candidate values below 2**64.

Use: python a109908_verify.py --limit 10000
     python a109908_verify.py --n 524
Not a proof of the open conjecture. No external dependencies.
"""
import argparse

# Deterministic Miller-Rabin bases for every unsigned 64-bit integer.
BASES = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)


def is_prime64(value: int) -> bool:
    if not 0 <= value < (1 << 64):
        raise ValueError('Deterministic guarantee only for 0 <= value < 2**64')
    if value < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if value % p == 0:
            return value == p
    d, s = value - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in BASES:
        a %= value
        if a == 0:
            continue
        x = pow(a, d, value)
        if x == 1 or x == value - 1:
            continue
        for _ in range(s - 1):
            x = x * x % value
            if x == value - 1:
                break
        else:
            return False
    return True


def first_success(n: int):
    if n <= 3:
        raise ValueError('n must exceed 3')
    if n * n // 4 >= (1 << 64):
        raise ValueError('n too large for 64-bit deterministic test')
    for k in range(1, n // 2 + 1):
        candidate = k * (n - k) - 1
        if is_prime64(candidate):
            return k, candidate
    return None


def scan(limit: int):
    checked = 0
    record = (0, 0)
    for n in range(4, limit + 1):
        found = first_success(n)
        checked += 1
        if found is None:
            print('Potential exception (requires independent audit):', n)
            return
        if found[0] > record[1]:
            record = (n, found[0])
    print('Checked:', checked, 'No missing prime in finite range [4,', limit, ']')
    print('Largest first-success index:', record[1], 'at n =', record[0])
    print('Finite computation is NOT a proof for all n.')


def self_test():
    expected = {4: (1, 2), 6: (2, 7), 10: (4, 23),
                28: (6, 131), 524: (8, 4127)}
    for n, value in expected.items():
        assert first_success(n) == value, (n, first_success(n), value)
    for value in range(2, 5000):
        naive = all(value % x for x in range(2, int(value ** .5) + 1))
        assert is_prime64(value) == naive, value
    print('Self-test passed.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=10000)
    parser.add_argument('--n', type=int)
    args = parser.parse_args()
    self_test()
    if args.n is not None:
        print('n =', args.n, 'first success =', first_success(args.n))
    else:
        scan(args.limit)
