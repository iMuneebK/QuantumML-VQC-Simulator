import streamlit as st
from quantum_circuit import QuantumNeuralNetwork

st.set_page_config(page_title="Quantum Machine Learning", layout="wide")
st.title("⚛️ Quantum Machine Learning & Variational Quantum Classifier (QNN)")

st.write("Simulating 4-Qubit Variational Quantum Circuit (VQC) using PennyLane / Qiskit.")
features = st.slider("Input Quantum State Angle", 0.0, 3.14, 1.57)

qnn = QuantumNeuralNetwork(num_qubits=4)
res = qnn.simulate_vqc([features, features*0.5])
st.metric("Quantum Expectation ⟨Z⟩", f"{res['expectation_value']:.4f}")
st.code(res['quantum_state_vector'])
