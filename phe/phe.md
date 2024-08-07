# Paillier Homomorphic Encryption (PHE)

Paillier Homomorphic Encryption (PHE) is a public-key cryptosystem with homomorphic properties, allowing operations on encrypted data without decrypting it.

## Mathematical Definition

### Key Generation
1. Choose two large prime numbers \( p \) and \( q \).
2. Compute $$\( n = p \times q \)$$.
3. Compute $$\( \lambda(n) = \text{lcm}(p-1, q-1) \)$$.
4. Choose \( g = n + 1 \).
5. Compute $$\( \mu = \left( \frac{L(g^{\lambda(n)} \mod n^2)}{n} \right)^{-1} \mod n \)$$, where $$\( L(u) = \frac{u - 1}{n} \)$$.

### Encryption
1. Choose a random $$\( r \in \mathbb{Z}_n^* \)$$.
2. Compute ciphertext $$\( c = g^m \cdot r^n \mod n^2 \)$$, where \( m \) is the plaintext.

### Decryption
1. Compute $$\( u = c^{\lambda(n)} \mod n^2 \)$$.
2. Compute $$\( m = L(u) \cdot \mu \mod n \)$$.

## Installation

You can install the `pryvx` package via pip:

```sh
pip install pryvx
```

## Example Usage

```python
from pryvx import PHE

phe1 = PHE()
public_key, private_key = phe1.keygen()

# Encrypt two numbers
m1 = 5
m2 = 10
c1 = phe1.encrypt(public_key, m1)
c2 = phe1.encrypt(public_key, m2)

# Perform homomorphic addition
c_sum = phe1.homomorphic_add(c1, c2, public_key)

# Decrypt the result
decrypted_sum = phe1.decrypt(public_key, private_key, c_sum)

print("Decrypted Sum:", decrypted_sum)  # Should print 15
