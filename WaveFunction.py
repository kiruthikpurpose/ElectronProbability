import numpy as np

def wave_function(x, t):
    return np.exp(1j * (x - t)) * np.sin(x)

x_values = np.linspace(0, 2 * np.pi, 100)
t_values = np.linspace(0, 10, 100)

probabilities = np.array([np.abs(wave_function(x, t))**2 for t in t_values for x in x_values])
probabilities = probabilities.reshape(len(t_values), len(x_values))

print("Wave Function Probability Matrix:")
print(probabilities)
