# Here are the pip pre-requisites that I will be using.
# pip install: qiskit       numpy       (jupyterlab)X       matplotlib      qiskit-ibmq-provider
# pip install --upgrade --force-reinstall qiskit-ibmq-provider (in case shit gets brokennnn)
# To get the token: https://quantum-computing.ibm.com/      
# Token: bc5b968e3af431a9c6381598c66f8272d1ce591e6bbdff50a61e9a758edbff0a8f83316a8d8782360d2fddcb72d73716bfe48512d3cd6ddc33ff3dd13182f108

import qiskit as q
#%matplotlib inline                                                                 # Only needed for jupyter notebooks

# Creating a basic circuit. Starting at the "bit" level
circuit = q.QuantumCircuit(2, 2)                                                    # 2 qubits, 2 classical bits

# Currently: (0,0)
circuit.x(0)                                                                        # This is a "not" gate

# Currently: (1,0)      
circuit.cx(0,1)                                                                        # This is a "control not", passes 2 qubits. Flips 2nd qubit value IF 1st qubit value = 1 

# Currently (1,1) <- 2nd value flipped to a 1
circuit.measure([0,1], [0,1])                                                       # Specify qubit register, how it is going to map to CLASSICAL bit register. Should get 1,1 as classical bits.
circuit.draw()
#print(circuit.draw())
circuit.draw(output = "mpl")
