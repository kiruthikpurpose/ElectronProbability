import random
import math

def quantum_uncertainty_probability(position, momentum):
    position_factor = 1 / (1 + math.exp(-position))
    momentum_factor = math.exp(-momentum ** 2 / 2)
    uncertainty_factor = random.uniform(0.2, 0.8)
    probability = position_factor * momentum_factor * uncertainty_factor
    return min(max(probability, 0), 1)

position = float(input("Enter the electron's position: "))
momentum = float(input("Enter the electron's momentum: "))

probability = quantum_uncertainty_probability(position, momentum)
print(f"Electron existence probability: {probability:.5f}")
