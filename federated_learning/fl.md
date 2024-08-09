# Federated Learning

Federated Learning is a decentralized approach to machine learning where multiple devices or servers collaboratively train a model while keeping their data localized. This ensures data privacy and security, as raw data is never shared between participants. Instead, only the model updates (like gradients) are aggregated centrally.

## Types of Federated Learning

### 1. **Horizontal Federated Learning (HFL)**
- **Scenario**: Participants have datasets with the same feature space but different samples.
- **Use Case**: When institutions in the same industry, like multiple hospitals, want to collaborate on training a model while keeping their patient data private.
- **Working**: Each participant trains a model on their local data. The model updates (e.g., gradients) are then shared with a central server to aggregate and update the global model.

### 2. **Vertical Federated Learning (VFL)**
- **Scenario**: Participants have datasets with different feature spaces but share the same sample ID.
- **Use Case**: When two companies, like a bank and an e-commerce platform, want to collaborate to build a model while keeping their respective customer data private.
- **Working**: Each participant computes partial model updates corresponding to their features. These updates are securely combined (often using techniques like secure multi-party computation) to train a global model.

### 3. **Federated Transfer Learning (FTL)**
- **Scenario**: Participants have datasets with different feature spaces and only a small number of overlapping sample IDs.
- **Use Case**: When organizations with different businesses want to collaborate, such as a hospital and a university with limited common patients or students.
- **Working**: Combines transfer learning and federated learning. The model is trained by sharing only the knowledge gained from overlapping parts of the data.

## Working Architecture or Principle

1. **Initialization**:
   - A global model is initialized by the central server and shared with all participants (clients).

2. **Local Training**:
   - Each participant trains the global model locally using their private data. The model's weights are updated based on local data.

3. **Model Update**:
   - The locally trained model updates (e.g., gradients) are sent back to the central server. Importantly, no raw data leaves the participants.

4. **Aggregation**:
   - The central server aggregates the updates from all participants to update the global model. Common aggregation methods include Federated Averaging (FedAvg).

5. **Iteration**:
   - Steps 2-4 are repeated iteratively until the global model converges to an acceptable performance level.

6. **Final Model**:
   - Once the model is fully trained, the final global model is shared with all participants.

## Benefits of Federated Learning

- **Data Privacy**: Raw data never leaves the participant’s device, ensuring privacy and compliance with regulations like GDPR.
- **Scalability**: Enables training on massive datasets distributed across multiple devices or institutions.
- **Personalization**: Participants can use the global model as a starting point and fine-tune it for their specific needs using their local data.

## Challenges and Considerations

- **Communication Costs**: Frequent model updates can lead to significant communication overhead.
- **Model Security**: Protecting the model updates from tampering or inference attacks is crucial.
- **Data Heterogeneity**: Different participants may have varying data distributions, leading to challenges in model convergence and performance.

## Installation

To install the `pryvx` package, which includes the SMPC module:

```sh
pip install pryvx
```

## Usage

### Example FL Server Code
```sh
from pryvx_fl.fl_server import start_server

start_server()
```

### Example FL Client Code
```sh
from pryvx_fl.fl_client import train, send_params

features = [[0, 0], [1, 1]]
labels = [0, 1]

model = train(features, labels)
send_params(model, 'localhost:50051')
```
