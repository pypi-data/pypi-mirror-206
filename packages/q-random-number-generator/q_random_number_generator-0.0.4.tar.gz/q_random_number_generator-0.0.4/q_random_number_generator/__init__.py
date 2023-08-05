from qiskit import *
from qiskit.visualization import plot_histogram
from qiskit.tools.monitor import job_monitor
import math


def initial_circuit(q_counts: str):
    qr = QuantumRegister(q_counts)
    cr = ClassicalRegister(q_counts)

    QC = QuantumCircuit(qr, cr)
    QC.h(range(q_counts))
    QC.measure(qr, cr)
    return QC


def generate(start, end, total):
    maximum = end
    collected = 0
    qbits = 0

    # decision qubits counts
    isInt = int(math.log2(maximum)) == math.log2(maximum)
    if isInt is True:
        qbits = math.ceil(math.log2(maximum)) + 2
    else:
        qbits = math.ceil(math.log2(maximum)) + 1

    # initial circuit
    QC = initial_circuit(qbits)

    # measure
    random_list = []
    while collected < total:
        backend = BasicAer.get_backend("qasm_simulator")  # simulator
        result = backend.run(transpile(QC, backend), shots=1).result()
        counts = result.get_counts(QC)
        for i in counts:
            pn = i[0]
            if pn == "0":
                pn = +1
            else:
                pn = -1
            absolute = int(i[1:], 2)
            random_number = int(pn * absolute)
            if start <= random_number <= end:
                collected += 1
                random_list.append(random_number)
    return random_list

def randint(start, end, total):
    return generate(start, end, total)