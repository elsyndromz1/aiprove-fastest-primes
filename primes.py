import math


def count_primes(n):
    if n < 2:
        return 0
    # Odd-only sieve: s[k] is 1 iff 2*k+1 is (still) prime-candidate.
    # s[0] stands for 1 (not prime) and 2 is not in the sieve at all,
    # so the two cancel and s.count(1) is exactly the prime count.
    m = (n + 1) // 2
    s = bytearray(b'\x01') * m
    r = math.isqrt(n)
    for i in range(3, r + 1, 2):
        if s[i // 2]:
            j = i * i // 2
            s[j::i] = b'\x00' * ((m - j + i - 1) // i)
    return s.count(1)
