# Global Differential Privacy (GDP)

Global Differential Privacy (GDP) is a technique that ensures the privacy of individuals in a dataset by adding noise to the results of queries. This noise is calibrated to the sensitivity of the query and a privacy parameter, epsilon (ε).

## What is Global Differential Privacy?

Global Differential Privacy (GDP) is a framework for quantifying and providing privacy guarantees when performing data analysis. It ensures that the removal or addition of a single data point in a dataset does not significantly affect the outcome of any analysis, thereby protecting individual privacy.

### Laplace Mechanism

The Laplace mechanism is a popular method used in GDP. It adds noise drawn from the Laplace distribution to a query's result. The amount of noise added is proportional to the sensitivity of the query and inversely proportional to the privacy parameter epsilon (ε). The lower the epsilon, the higher the privacy guarantee.

### Mathematical Definition

- **Sensitivity (Δf):** The maximum change in the output of a query when a single data point in the dataset is modified. For example, if you calculate the mean of a dataset and remove one element, the maximum change in the result is the sensitivity.

- **Epsilon (ε):** A parameter that controls the trade-off between privacy and accuracy. Smaller values of ε provide stronger privacy guarantees but introduce more noise to the query results.

- **Laplace Mechanism:** Given a query function `f` with sensitivity `Δf`, the Laplace mechanism adds noise drawn from the Laplace distribution with scale `Δf/ε` to the result of `f`.

## Installation

To install the `pryvx` package, which includes the Global Differential Privacy module:

```sh
pip install pryvx
```

## Usage

### Example Code

Below is an example of how to use the GDP module to add noise to a query result using the Laplace mechanism:

```python
import numpy as np
from pryvx import GDP

# Example database
database = np.random.randint(0, 100, size=1000)
query_result = np.mean(database)

# Privacy parameters
epsilon = 0.5
sensitivity = 1

gdp1 = GDP()

# Applying Laplace mechanism
dp_query_result = gdp1.add_noise(query_result, sensitivity, epsilon)

print("True query result: ", query_result)
print("DP query result: ", dp_query_result)
```

### Functions

- **`GDP.add_noise(query_result, sensitivity, epsilon)`**: Adds Laplace noise to the query result to ensure differential privacy. It takes the true query result, the sensitivity of the query, and the privacy parameter epsilon (ε) as inputs and returns the differentially private query result.
