import math
import random

def electron_probability(state, momentum):
    base_probability = random.uniform(0.1, 0.9)
    state_factor = math.sin(state) ** 2
    momentum_factor = math.exp(-momentum**2)
    probability = base_probability * state_factor * momentum_factor
    return probability

state = float(input("Enter the quantum state (any real number): "))
momentum = float(input("Enter the electron momentum (any real number): "))

probability = electron_probability(state, momentum)
print(f"The calculated probability of the electron's existence is: {probability:.5f}")
