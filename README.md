# OEIS A109908 — Reproducible Number Theory Research

**Status: OPEN / UNSOLVED (10 October 2026).** This repository does not claim a proof or counterexample.

**Author:** King ([@kid19874-cmd](https://github.com/kid19874-cmd))  
**AI research collaborator:** ChatGPT (GPT-6, OpenAI)

## The conjecture

For every integer `n > 3`, does there exist `1 <= k <= floor(n/2)` such that

```text
F_n(k) = k(n-k) - 1
```

is prime? Source: [OEIS A109908](https://oeis.org/A109908).

## Read the research note

**[Prime Values of k(n-k)-1: Infinite Families and Open Directions](docs/RESEARCH_ARTICLE.md)**

The article contains an elementary proof that for every fixed `J >= 1`, infinitely many even integers `n` have their first successful candidate at `k=2J`. This uses the Chinese remainder theorem and Dirichlet's theorem and **does not** resolve A109908. Novelty is not claimed.

## Potential routes toward a proof

- Prove a **uniform positive lower bound** for the prime count `S(n)` as `n` varies.
- Investigate the two sparse additive families `m^2 - 1 = p + u^2` and `m(m+1) - 1 = p + u(u+1)`.
- Audit candidate dimension-two sieve estimates for almost-primes. A proposed `P_6` result **requires independent checking**.
- Identify a rigorous way around the **sieve parity barrier** to prove the existence of actual primes.
- Use CRT-certified composite prefixes to stress-test candidate proof strategies, never as alleged counterexamples.

## Reproducibility

An accompanying verification package is available separately until the scripts and data have been fully committed. Tests and graphs, however large, do not constitute a proof for all integers.

## Attribution and limitations

The account holder **King** is listed as author; **ChatGPT (GPT-6, OpenAI)** assisted with research and writing. The work is a public research note, **not peer-reviewed**, and may contain known results. Corrections, independent audits, and earlier citations are welcome. No personal credentials, network information, or private environment data are included.

## References

- [OEIS A109908](https://oeis.org/A109908)
- [Zhi-Wei Sun, *On sums of primes and triangular numbers*](https://arxiv.org/abs/0803.3737)
- [Kenny Applegate and Kyle Pratt, *Computational Results on Sums of a Prime with Squares or Cubes* (2026)](https://arxiv.org/abs/2609.20505)
