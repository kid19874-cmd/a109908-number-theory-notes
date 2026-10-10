# Prime Values of k(n-k)-1: Infinite Families and Open Directions

**Research note — 10 October 2026**

**Author:** King (GitHub: @kid19874-cmd)  
**AI research collaborator:** ChatGPT (GPT-6, OpenAI)

> **Open problem.** This document does NOT prove OEIS A109908. The infinite-family statement below is derived using classical theorems; originality and publication priority are NOT claimed. Independent mathematical review is welcome.

## Abstract

We study prime values of F_n(k) = k(n-k)-1, for integers n > 3 and 1 <= k <= floor(n/2). We provide exact transformations into prime-plus-square and prime-plus-pronic representation problems, the local root-count formula, and an elementary proof that every fixed even first-success index occurs for infinitely many even n. This does not settle the universal prime-existence conjecture.

## 1. The conjecture

OEIS [A109908](https://oeis.org/A109908) asks whether, for every integer n > 3, at least one admissible k gives a prime number

$$F_n(k)=k(n-k)-1.$$

Write b(n) for the smallest such k **when a successful k exists**. Our b(n) is only local notation.

The original conjecture is equivalent to

$$S(n)=\sum_{1\le k\le \lfloor n/2\rfloor} 1_{\rm prime}(F_n(k)) > 0$$

for every integer n > 3. Finite computational checks cannot establish this universal claim.

## 2. Two exact transformations

For even n = 2m, let u = m-k. Then 0 <= u < m and

$$F_{2m}(k)=m^2-1-u^2.$$

Thus the even case concerns representations of m^2-1 as a prime plus a square.

For odd n = 2m+1, the same substitution gives

$$F_{2m+1}(k)=m(m+1)-1-u(u+1).$$

The odd case concerns a prime plus a pronic number, related to a broader conjecture of Zhi-Wei Sun; this broader conjecture is not being assumed.

If even n >= 6, odd k gives an even value strictly greater than 2. Thus any successful k is even. Writing k = 2j,

$$F_{2m}(2j)=4j(m-j)-1.$$

For the boundary case n = 4, k = 1 already gives the prime 2.

## 3. Local modular structure

Let rho_n(p) be the number of roots modulo prime p of F_n(k) = 0 (mod p). For any odd prime p,

$$(2k-n)^2 \equiv n^2-4 \pmod p,$$

so

$$\rho_n(p)=1+\left(\frac{n^2-4}{p}\right),$$

where the last expression is the Legendre symbol. At p = 2, direct checking gives rho_n(2) = 1 for even n and rho_n(2) = 0 for odd n.

Consequently rho_n(p) < p for every prime p. This excludes a single-prime local obstruction, but it does not prove the existence of a prime among the entire candidate set.

## 4. An elementary infinite-family theorem

**Theorem.** For every fixed integer J >= 1, infinitely many even integers n have b(n) = 2J.

**Proof.** Put n = 2m and define

$$G_j(m)=4j(m-j)-1.$$

For J = 1, the target G_1(m) = 4m-5 varies along a reduced residue class modulo 4. Dirichlet's theorem provides infinitely many prime values for arbitrarily large m. For such m, earlier odd indices fail by parity.

Suppose J >= 2. Choose distinct primes q_1,...,q_(J-1), each greater than 4J^2. For every j = 1,...,J-1 impose

$$m \equiv j+(4j)^{-1} \pmod {q_j}.$$

The Chinese remainder theorem gives an arithmetic progression m = R+tQ, where Q = q_1...q_(J-1). For each smaller j,

$$G_j(m) \equiv 0 \pmod {q_j}.$$

For sufficiently large t, G_j(m) > q_j, so these values are composite.

The target candidate is

$$G_J(R+tQ)=4JQt + A,\qquad A=4J(R-J)-1.$$

We show gcd(A,4JQ) = 1. First A = -1 (mod 4J). For each j < J, the imposed congruence yields

$$jA \equiv (J-j)(1-4Jj) \pmod {q_j}.$$

Both factors on the right are nonzero modulo q_j because q_j > 4J^2; j itself is invertible modulo q_j. Therefore q_j does not divide A. Hence gcd(A,4JQ) = 1.

Dirichlet's theorem now gives infinitely many prime values of 4JQt+A. Taking t sufficiently large guarantees m >= 2J, all earlier even candidates are composite, and all earlier odd candidates fail by parity. Consequently b(2m) = 2J for infinitely many m. QED.

**Examples:** (n, b(n), prime) = (6,2,7), (10,4,23), (28,6,131), (524,8,4127).

This theorem establishes sparse infinite families. It does NOT establish the A109908 conjecture for every n, or even for almost all n. The method applies classical theorems and may already be known.

## 5. Research directions that might help

1. **Uniform prime counting:** Find a rigorous positive lower bound for S(n) uniform in n, rather than an average or a heuristic estimate.
2. **Sparse additive representations:** Analyze m^2-1 = p+u^2 and m(m+1)-1 = p+u(u+1) with the exact permitted range 0 <= u < m.
3. **Sieve parity barrier:** Sieve methods may produce almost-prime values, but their parity limitation prevents a direct jump to actual primes.
4. **Auditing weighted-sieve claims:** A proposed uniform bound of at most six prime factors remains unverified here. It is NOT presented as a theorem.
5. **Adversarial CRT cases:** Construct long composite prefixes as reproducible algorithm stress tests, not as counterexamples to A109908.

## 6. References and disclosure

- [OEIS A109908](https://oeis.org/A109908).
- Zhi-Wei Sun, [On sums of primes and triangular numbers](https://arxiv.org/abs/0803.3737).
- Kenny Applegate and Kyle Pratt, [Computational Results on Sums of a Prime with Squares or Cubes](https://arxiv.org/abs/2609.20505).
- Classical Chinese remainder theorem and Dirichlet's theorem on primes in arithmetic progressions.

**Disclosure:** Prepared by King with research assistance from ChatGPT (GPT-6, OpenAI). The results have not undergone independent peer review. Corrections, earlier references, and rigorous extensions are welcome.
