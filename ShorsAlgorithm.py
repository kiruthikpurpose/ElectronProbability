from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_histogram
from qiskit.circuit.library import QFT
from math import gcd
import numpy as np

def shors_algorithm(N):
    def qpe_amod15(a):
        n_count = 8
        qc = QuantumCircuit(4+n_count, n_count)
        for q in range(n_count):
            qc.h(q)
        qc.x(3+n_count)
        for q in range(n_count):
            qc.append(c_amod15(a, 2**q), [q] + [i+n_count for i in range(4)])
        qc.append(QFT(n_count).inverse(), range(n_count))
        qc.measure(range(n_count), range(n_count))
        return qc

    def c_amod15(a, power):
        U = QuantumCircuit(4)
        for iteration in range(power):
            if a in [2, 13]:
                U.swap(0, 1)
                U.swap(1, 2)
                U.swap(2, 3)
            if a in [7, 8]:
                U.swap(2, 3)
                U.swap(1, 2)
                U.swap(0, 1)
            if a in [7, 13]:
                for q in range(4):
                    U.x(q)
        U = U.to_gate()
        U.name = "%i^%i mod 15" % (a, power)
        c_U = U.control()
        return c_U

    a = 7
    qc = qpe_amod15(a)
    aer_sim = Aer.get_backend('aer_simulator')
    t_qc = transpile(qc, aer_sim)
    qobj = assemble(t_qc)
    result = aer_sim.run(qobj).result()
    counts = result.get_counts()
    plot_histogram(counts)

    phases = []
    for output in counts:
        decimal = int(output, 2)
        phase = decimal/(2**8)
        phases.append(phase)

    frac = []
    for phase in phases:
        frac.append(phase)

    r = 0
    for f in frac:
        r = f

    guess = gcd(int(a**r - 1), N)
    return guess

result = shors_algorithm(15)
print(f"A non-trivial factor of 15 is: {result}")
