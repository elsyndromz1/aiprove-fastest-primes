# fastest-primes — AIProve entry

`primes.py` exposes `count_primes(n)`: number of primes `<= n`.

- Odd-only bytearray sieve, stdlib only (`math.isqrt`).
  Slice assignment does the marking in C, so it is fast in pure Python.
- No file I/O, no network, no `subprocess`, no `eval`/`exec`.
- Verified on the public cases (10→4, 100→25, 1000→168,
  100000→9592, 1000000→78498) and 5000000→348513.
- Local timing (this VM): 1,000,000 in ~2.2 ms, 5,000,000 in ~10.9 ms.

Test: `python3 -c "from primes import count_primes; print(count_primes(1000000))"`
