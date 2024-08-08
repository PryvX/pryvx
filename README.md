# PryvX

PryvX is a collection of privacy-enhancing technologies, starting with Private Set Intersection (PSI) and Paillier Homomorphic Encryption (PHE). Our goal is to develop modules or features including PSI, Secure Multi-Party Computation (SMPC), Homomorphic Encryption (HE), Federated Learning, Differential Privacy, and more.

## Modules

### [Private Set Intersection (PSI)](psi/psi.md)
Private Set Intersection (PSI) allows two parties to compute the intersection of their private sets without revealing any additional information.

For detailed information, see the [PSI README](psi/psi.md).

### [Paillier Homomorphic Encryption (PHE)](phe/phe.md)
Paillier Homomorphic Encryption (PHE) is a public-key cryptosystem with homomorphic properties, enabling operations on encrypted data without decryption.

For detailed information, see the [PHE README](phe/phe.md).

### [Global Differential Privacy (GDP)](dp/gdp.md)
Global Differential Privacy (GDP) ensures that individual data entries remain private when performing queries on a database. The GDP module implements the Laplace mechanism to add noise to query results.

For detailed information, see the [GDP README](dp/gdp.md).

### [Secure Multi-Party Computation (SMPC)](smpc/smpc.md)
Secure Multi-Party Computation (SMPC) allows multiple parties to jointly compute a function over their inputs while keeping those inputs private. The SMPC module implements additive secret sharing, enabling secure computation of sums, differences, and comparisons.

For detailed information, see the [SMPC README](smpc/smpc.md).

### [Federated Learning (FL)](federated_learning/fl.md)
Federated Learning (FL) enables decentralized model training across multiple clients without sharing their raw data. The FL module includes functionality for training models locally and securely sending model parameters to a central server.

For detailed information, see the [FL README](federated_learning/fl.md).

## Installation

You can install the `pryvx` package via pip:

```sh
pip install pryvx
