# Secure Multiparty Computation (SMPC) - Additive Secret Sharing

Secure Multiparty Computation (SMPC) enables multiple parties to jointly compute a function over their inputs while keeping those inputs private. Additive Secret Sharing is a fundamental technique in SMPC that allows a secret to be split into multiple shares, distributed among participants, and securely reconstructed.

## What is Additive Secret Sharing?

Additive Secret Sharing is a method to split a secret value into multiple shares such that the sum of all shares modulo a predefined field equals the original secret. Each share on its own provides no information about the secret. This technique is commonly used in SMPC protocols to ensure that computations can be performed on the shares without revealing the underlying secrets.

### Mathematical Definition

- **Additive Shares:** Given a secret `m`, a field size `q`, and `N` parties, the secret is split into `N` shares `(s1, s2, ..., sN)` such that `m ≡ (s1 + s2 + ... + sN) mod q`. Each share `si` is generated randomly except for the last one, which is computed as `(m - (s1 + s2 + ... + s(N-1))) mod q`.

- **Reconstruction:** To reconstruct the secret from the shares, simply compute the sum of all shares modulo the field size `q`.

## Installation

To install the `pryvx` package, which includes the SMPC module:

```sh
pip install pryvx
```

## Usage

### Example Code

Below is an example of how to use the SMPC module with Additive Secret Sharing:

```python
from pryvx import SMPC

# Example values
a = 35
b = 50
total_parties = 2

smpc1 = SMPC()

# Generate secret shares for each value
shares_a = smpc1.get_secret_shares(a, total_parties)
shares_b = smpc1.get_secret_shares(b, total_parties)

# Perform secure addition on the shares
print("Secure Addition:", smpc1.addition([shares_a, shares_b]))

# Perform secure difference on the shares
print("Secure Difference:", smpc1.difference(shares_a, shares_b))

# Perform secure comparison on the shares
print("Secure Comparison:", smpc1.compare(shares_a, shares_b))
```

### Functions

- **`SMPC.get_secret_shares(m, N)`**: Splits the secret `m` into `N` additive shares.
- **`SMPC.addition(shares_list)`**: Securely adds multiple sets of shares.
- **`SMPC.difference(shares_a, shares_b)`**: Securely computes the difference between two sets of shares.
- **`SMPC.compare(shares_a, shares_b)`**: Securely compares two sets of shares.

### Advanced Features

- **Encoding and Decoding:** The module supports encoding rational numbers into a finite field and decoding them back into rational numbers. This is crucial for operations where fractional values are involved.
- **Comparison Operation:** The module can securely compare two secrets based on their shares.
- 
