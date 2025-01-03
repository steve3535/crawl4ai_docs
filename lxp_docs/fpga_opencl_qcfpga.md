# Quantum simulation using Intel® FPGA SDK

Source: https://docs.lxp.lu/fpga/opencl/qcfpga/

# Quantum simulation using Intel® FPGA SDK

## Overview

QCFPGA is a software library which is a fork of the public QCGPU software that was designed to perform quantum computing simulations on graphics processing units (GPUs) using PyOpenCL. The main idea behind QCFPGA is to utilize the parallel processing capabilities of modern FPGAs to speed up quantum simulations, which are computationally intensive tasks that can benefit greatly from the pipeline parallelism offered by modern FPGAs.

The library provides a high-level interface for defining quantum states, applying gates, and performing measurements, much like other quantum computing frameworks. Nonetheless, the library is far from being complete as the Qiskit (IBM) or Cirq (Google).

QFPGA was adapted from QCGPU as a proof of concept with the intent to make quantum computing simulations more accessible and faster, leveraging the powerful computational capabilities of FPGAs to handle state vector manipulations typical in quantum computing.

> **WIP!**

> WIP!

WIP!

QCFPGA is a Work In Progress and may be subject to changes in the near future

Our main goal is to take advantage of kernel optimization on FPGAs and develop a multi-node version

For any problem, please contact the support team using our service desk portal

- QCFPGA is a Work In Progress and may be subject to changes in the near future

- Our main goal is to take advantage of kernel optimization on FPGAs and develop a multi-node version

- For any problem, please contact the support team using our service desk portal

## Getting started

### Interactive job

To use PyOpenCL for FPGA development on Meluxina FPGA nodes, ensure first to request a FPGA node:

1

2

3

4

5

6

7

8# Get one FPGA node with two FPGA cards

salloc -A <ACCOUNT> -t 02:00:00 -q default -p fpga -N1

# Load the PyOpenCL module

module load env/staging/2023.1

module load QCFPGA/0.0.1-foss-2023a-ifpgasdk-20.4

# Let's check that we see the Intel FPGA SDK platform

python -c "import pyopencl as cl; print(cl.get_platforms())"

file $PYOPENCL_KERNEL

1

2

3

4

5

6

7

8

```

1

2

3

4

5

6

7

8

```

# Get one FPGA node with two FPGA cards

salloc -A <ACCOUNT> -t 02:00:00 -q default -p fpga -N1

# Load the PyOpenCL module

module load env/staging/2023.1

module load QCFPGA/0.0.1-foss-2023a-ifpgasdk-20.4

# Let's check that we see the Intel FPGA SDK platform

python -c "import pyopencl as cl; print(cl.get_platforms())"

file $PYOPENCL_KERNEL

```

# Get one FPGA node with two FPGA cards

salloc -A <ACCOUNT> -t 02:00:00 -q default -p fpga -N1

# Load the PyOpenCL module

module load env/staging/2023.1

module load QCFPGA/0.0.1-foss-2023a-ifpgasdk-20.4

# Let's check that we see the Intel FPGA SDK platform

python -c "import pyopencl as cl; print(cl.get_platforms())"

file $PYOPENCL_KERNEL

```

```

# Get one FPGA node with two FPGA cards

salloc -A <ACCOUNT> -t 02:00:00 -q default -p fpga -N1

# Load the PyOpenCL module

module load env/staging/2023.1

module load QCFPGA/0.0.1-foss-2023a-ifpgasdk-20.4

# Let's check that we see the Intel FPGA SDK platform

python -c "import pyopencl as cl; print(cl.get_platforms())"

file $PYOPENCL_KERNEL

```

You should see the following output:

- You should see the following output:

[<pyopencl.Platform 'Intel(R) FPGA SDK for OpenCL(TM)' at 0x1544c17f2820>]

/apps/USE/easybuild/staging/2023.1/software/QCFPGA/0.0.1-foss-2023a-ifpgasdk-20.4/bin/kernels.aocx: ELF 32-bit LSB no file type, x86-64, version 1 (SYSV)

```

[<pyopencl.Platform 'Intel(R) FPGA SDK for OpenCL(TM)' at 0x1544c17f2820>]

/apps/USE/easybuild/staging/2023.1/software/QCFPGA/0.0.1-foss-2023a-ifpgasdk-20.4/bin/kernels.aocx: ELF 32-bit LSB no file type, x86-64, version 1 (SYSV)

```

```

[<pyopencl.Platform 'Intel(R) FPGA SDK for OpenCL(TM)' at 0x1544c17f2820>]

/apps/USE/easybuild/staging/2023.1/software/QCFPGA/0.0.1-foss-2023a-ifpgasdk-20.4/bin/kernels.aocx: ELF 32-bit LSB no file type, x86-64, version 1 (SYSV)

```

bell_state.py 1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20# Import QCFPGA

import qcfpga

# Create a new quantum register with 2 qubits

register = qcfpga.State(2)

# Apply a hadamard (H) gate to the first qubit.

# You should note that the qubits are zero indexed

register.h(0)

# Add a controlled not (CNOT/CX) gate, with the control as

# the first qubit and target as the second.

# The register will now be in the bell state.

register.cx(0, 1)

# Perform a measurement with 1000 samples

results = register.measure(samples=1000)

# Show the results

print(results)

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

```

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

```

# Import QCFPGA

import qcfpga

# Create a new quantum register with 2 qubits

register = qcfpga.State(2)

# Apply a hadamard (H) gate to the first qubit.

# You should note that the qubits are zero indexed

register.h(0)

# Add a controlled not (CNOT/CX) gate, with the control as

# the first qubit and target as the second.

# The register will now be in the bell state.

register.cx(0, 1)

# Perform a measurement with 1000 samples

results = register.measure(samples=1000)

# Show the results

print(results)

```

# Import QCFPGA

import qcfpga

# Create a new quantum register with 2 qubits

register = qcfpga.State(2)

# Apply a hadamard (H) gate to the first qubit.

# You should note that the qubits are zero indexed

register.h(0)

# Add a controlled not (CNOT/CX) gate, with the control as

# the first qubit and target as the second.

# The register will now be in the bell state.

register.cx(0, 1)

# Perform a measurement with 1000 samples

results = register.measure(samples=1000)

# Show the results

print(results)

```

```

# Import QCFPGA

import qcfpga

# Create a new quantum register with 2 qubits

register = qcfpga.State(2)

# Apply a hadamard (H) gate to the first qubit.

# You should note that the qubits are zero indexed

register.h(0)

# Add a controlled not (CNOT/CX) gate, with the control as

# the first qubit and target as the second.

# The register will now be in the bell state.

register.cx(0, 1)

# Perform a measurement with 1000 samples

results = register.measure(samples=1000)

# Show the results

print(results)

```

To execute the previous python code, python bell_state.py

```

python bell_state.py

```

> **Using Direct Memory Access (DMA)**

> Using Direct Memory Access (DMA)

Using Direct Memory Access (DMA)

DMA is enabled between host and the device if buffer data have a 64-byte alignment.

We strongly recommend you to load our jemalloc module which provides such default alignment:

module load jemalloc/5.3.0-GCCcore-12.3.0

export JEMALLOC_PRELOAD=$(jemalloc-config --libdir)/libjemalloc.so.$(jemalloc-config --revision)

LD_PRELOAD=${JEMALLOC_PRELOAD}  python bell_state.py

- DMA is enabled between host and the device if buffer data have a 64-byte alignment.

- We strongly recommend you to load our jemalloc module which provides such default alignment:

module load jemalloc/5.3.0-GCCcore-12.3.0

export JEMALLOC_PRELOAD=$(jemalloc-config --libdir)/libjemalloc.so.$(jemalloc-config --revision)

LD_PRELOAD=${JEMALLOC_PRELOAD}  python bell_state.py

```

jemalloc

```

module load jemalloc/5.3.0-GCCcore-12.3.0

export JEMALLOC_PRELOAD=$(jemalloc-config --libdir)/libjemalloc.so.$(jemalloc-config --revision)

LD_PRELOAD=${JEMALLOC_PRELOAD}  python bell_state.py

```

module load jemalloc/5.3.0-GCCcore-12.3.0

export JEMALLOC_PRELOAD=$(jemalloc-config --libdir)/libjemalloc.so.$(jemalloc-config --revision)

LD_PRELOAD=${JEMALLOC_PRELOAD}  python bell_state.py

```

```

module load jemalloc/5.3.0-GCCcore-12.3.0

export JEMALLOC_PRELOAD=$(jemalloc-config --libdir)/libjemalloc.so.$(jemalloc-config --revision)

LD_PRELOAD=${JEMALLOC_PRELOAD}  python bell_state.py

```

### Using the jlab portal

Before accessing the jlab portal, you will need to create a dedicated kernel for jupyter

Kernels are by default located in this folder $HOME/.local/share/jupyter/kernels

Apply the following command to set it up:

- Before accessing the jlab portal, you will need to create a dedicated kernel for jupyter

Before accessing the jlab portal, you will need to create a dedicated kernel for jupyter

- Kernels are by default located in this folder $HOME/.local/share/jupyter/kernels

Kernels are by default located in this folder $HOME/.local/share/jupyter/kernels

```

$HOME/.local/share/jupyter/kernels

```

- Apply the following command to set it up:

Apply the following command to set it up:

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33KERNEL="$HOME/.local/share/jupyter/kernels/qcfpga"

mkdir -p $KERNEL

PRELOAD="$KERNEL/start.sh"

JSON="$KERNEL/kernel.json"

cat << 'EOF' > $JSON

{

"argv": [

"{resource_dir}/start.sh",

"python",

"-m",

"ipykernel_launcher",

"-f",

"{connection_file}"

],

"display_name": "QCFPGA",

"language": "python",

"metadata": {

"debugger": true

}

}

EOF

cat << 'EOF' > $PRELOAD

#!/bin/bash

module load QCFPGA

module load jemalloc

export JEMALLOC_PRELOAD=$(jemalloc-config --libdir)/libjemalloc.so.$(jemalloc-config --revision)

export LD_PRELOAD=${JEMALLOC_PRELOAD}

export PYOPENCL_COMPILER_OUTPUT=1

exec "$@"

EOF

chmod u+x $PRELOAD

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

```

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

```

KERNEL="$HOME/.local/share/jupyter/kernels/qcfpga"

mkdir -p $KERNEL

PRELOAD="$KERNEL/start.sh"

JSON="$KERNEL/kernel.json"

cat << 'EOF' > $JSON

{

"argv": [

"{resource_dir}/start.sh",

"python",

"-m",

"ipykernel_launcher",

"-f",

"{connection_file}"

],

"display_name": "QCFPGA",

"language": "python",

"metadata": {

"debugger": true

}

}

EOF

cat << 'EOF' > $PRELOAD

#!/bin/bash

module load QCFPGA

module load jemalloc

export JEMALLOC_PRELOAD=$(jemalloc-config --libdir)/libjemalloc.so.$(jemalloc-config --revision)

export LD_PRELOAD=${JEMALLOC_PRELOAD}

export PYOPENCL_COMPILER_OUTPUT=1

exec "$@"

EOF

chmod u+x $PRELOAD

```

KERNEL="$HOME/.local/share/jupyter/kernels/qcfpga"

mkdir -p $KERNEL

PRELOAD="$KERNEL/start.sh"

JSON="$KERNEL/kernel.json"

cat << 'EOF' > $JSON

{

"argv": [

"{resource_dir}/start.sh",

"python",

"-m",

"ipykernel_launcher",

"-f",

"{connection_file}"

],

"display_name": "QCFPGA",

"language": "python",

"metadata": {

"debugger": true

}

}

EOF

cat << 'EOF' > $PRELOAD

#!/bin/bash

module load QCFPGA

module load jemalloc

export JEMALLOC_PRELOAD=$(jemalloc-config --libdir)/libjemalloc.so.$(jemalloc-config --revision)

export LD_PRELOAD=${JEMALLOC_PRELOAD}

export PYOPENCL_COMPILER_OUTPUT=1

exec "$@"

EOF

chmod u+x $PRELOAD

```

```

KERNEL="$HOME/.local/share/jupyter/kernels/qcfpga"

mkdir -p $KERNEL

PRELOAD="$KERNEL/start.sh"

JSON="$KERNEL/kernel.json"

cat << 'EOF' > $JSON

{

"argv": [

"{resource_dir}/start.sh",

"python",

"-m",

"ipykernel_launcher",

"-f",

"{connection_file}"

],

"display_name": "QCFPGA",

"language": "python",

"metadata": {

"debugger": true

}

}

EOF

cat << 'EOF' > $PRELOAD

#!/bin/bash

module load QCFPGA

module load jemalloc

export JEMALLOC_PRELOAD=$(jemalloc-config --libdir)/libjemalloc.so.$(jemalloc-config --revision)

export LD_PRELOAD=${JEMALLOC_PRELOAD}

export PYOPENCL_COMPILER_OUTPUT=1

exec "$@"

EOF

chmod u+x $PRELOAD

```

Start a JupyterLab session using our jlab portal

Don't forget to select the FPGA partition

Copy-paste the previous bell_state.py in a notebook and select the QCFPGA kernel

You should see the following output:

- Start a JupyterLab session using our jlab portal

Start a JupyterLab session using our jlab portal

- Don't forget to select the FPGA partition

Don't forget to select the FPGA partition

- Copy-paste the previous bell_state.py in a notebook and select the QCFPGA kernel

Copy-paste the previous bell_state.py in a notebook and select the QCFPGA kernel

```

bell_state.py

```

- You should see the following output:

You should see the following output:

## Built-In Gates

In quantum computing, gates are used to manipulate quantum registers and

to implement quantum algorithms.

There are a number of gates built into QCGPU and QCFPGA. They can all be applied

the same way:

1

2

3

4

5

6import qcfpga

register = qcfpga.State(2)

state.h(0) # Applies the Hadamard  gate to the first qubit.

state.x(1) # Applies a pauli-x  gate to the second qubit.

1

2

3

4

5

6

```

1

2

3

4

5

6

```

import qcfpga

register = qcfpga.State(2)

state.h(0) # Applies the Hadamard  gate to the first qubit.

state.x(1) # Applies a pauli-x  gate to the second qubit.

```

import qcfpga

register = qcfpga.State(2)

state.h(0) # Applies the Hadamard  gate to the first qubit.

state.x(1) # Applies a pauli-x  gate to the second qubit.

```

```

import qcfpga

register = qcfpga.State(2)

state.h(0) # Applies the Hadamard  gate to the first qubit.

state.x(1) # Applies a pauli-x  gate to the second qubit.

```

h and x can be replaced with any of the following:

```

h

```

```

x

```

The Hadamard gate: h - state.h(0)

The S gate: s - state.s(0)

The T gate: t - state.t(0)

The Pauli-X / NOT gate: x - state.x(0)

The Pauli-Y gate: y - state.y(0)

The Pauli-Z gate: z - state.z(0)

The CNOT gate: cx -state.cx(0, 1) # CNOT with control = 0, target = 1

The SWAP gate: swap -state.swap(0,1) # Swaps the 0th and 1st qubit

The Toffoli gate: toffoli -state.toffoli(0, 1, 2) # Toffoli with controls = (0, 1), target = 2

- The Hadamard gate: h - state.h(0)

The Hadamard gate: h - state.h(0)

```

state.h(0)

```

- The S gate: s - state.s(0)

The S gate: s - state.s(0)

```

state.s(0)

```

- The T gate: t - state.t(0)

The T gate: t - state.t(0)

```

state.t(0)

```

- The Pauli-X / NOT gate: x - state.x(0)

The Pauli-X / NOT gate: x - state.x(0)

```

state.x(0)

```

- The Pauli-Y gate: y - state.y(0)

The Pauli-Y gate: y - state.y(0)

```

state.y(0)

```

- The Pauli-Z gate: z - state.z(0)

The Pauli-Z gate: z - state.z(0)

```

state.z(0)

```

- The CNOT gate: cx -state.cx(0, 1) # CNOT with control = 0, target = 1

The CNOT gate: cx -state.cx(0, 1) # CNOT with control = 0, target = 1

```

state.cx(0, 1) # CNOT with control = 0, target = 1

```

- The SWAP gate: swap -state.swap(0,1) # Swaps the 0th and 1st qubit

The SWAP gate: swap -state.swap(0,1) # Swaps the 0th and 1st qubit

```

state.swap(0,1) # Swaps the 0th and 1st qubit

```

- The Toffoli gate: toffoli -state.toffoli(0, 1, 2) # Toffoli with controls = (0, 1), target = 2

The Toffoli gate: toffoli -state.toffoli(0, 1, 2) # Toffoli with controls = (0, 1), target = 2

```

state.toffoli(0, 1, 2) # Toffoli with controls = (0, 1), target = 2

```

For example, you can create a 5-qubit register and apply the  Hadamard gate on the first qubit:

1

2

3

4

5

6import qcfpga

h = qcfpga.gate.h()

register = qcfpga.State(7)

register.apply_gate(h, 0)

1

2

3

4

5

6

```

1

2

3

4

5

6

```

import qcfpga

h = qcfpga.gate.h()

register = qcfpga.State(7)

register.apply_gate(h, 0)

```

import qcfpga

h = qcfpga.gate.h()

register = qcfpga.State(7)

register.apply_gate(h, 0)

```

```

import qcfpga

h = qcfpga.gate.h()

register = qcfpga.State(7)

register.apply_gate(h, 0)

```

You can also use any of the gates as controlled gates.

Controlled gates can be used to entangle state

1

2

3

4

5

6

7

8import qcfpga

x = qcfpga.gate.x()

h = qcfpga.gate.h()

register = qcfpga.State(5)

register.apply_gate(h,0)

register.apply_controlled_gate(x, 0, 1)

1

2

3

4

5

6

7

8

```

1

2

3

4

5

6

7

8

```

import qcfpga

x = qcfpga.gate.x()

h = qcfpga.gate.h()

register = qcfpga.State(5)

register.apply_gate(h,0)

register.apply_controlled_gate(x, 0, 1)

```

import qcfpga

x = qcfpga.gate.x()

h = qcfpga.gate.h()

register = qcfpga.State(5)

register.apply_gate(h,0)

register.apply_controlled_gate(x, 0, 1)

```

```

import qcfpga

x = qcfpga.gate.x()

h = qcfpga.gate.h()

register = qcfpga.State(5)

register.apply_gate(h,0)

register.apply_controlled_gate(x, 0, 1)

```

It is also trivial to apply a gate to all qubits of a register

1

2

3

4

5

6import qcfpga

h = qcfpga.gate.h()

register = qcfpga.State(5)

register.apply_all(h)

1

2

3

4

5

6

```

1

2

3

4

5

6

```

import qcfpga

h = qcfpga.gate.h()

register = qcfpga.State(5)

register.apply_all(h)

```

import qcfpga

h = qcfpga.gate.h()

register = qcfpga.State(5)

register.apply_all(h)

```

```

import qcfpga

h = qcfpga.gate.h()

register = qcfpga.State(5)

register.apply_all(h)

```

Custom gates in QCFPGA use the qcfpga.Gate class.

```

qcfpga.Gate

```

Only single gate qubits can be defined

1

2

3

4

5

6

7

8

9

10import qcfpga

import numpy as np

# Ry(60): 60-degree rotation around the Y axes on the Bloch Sphere

gate_matrix = np.array([

[np.cos(np.pi/6), -np.sin(np.pi/6)],

[np.sin(np.pi/6),np.cos(np.pi/6)]

])

gate = qcfpga.Gate(gate_matrix)

1

2

3

4

5

6

7

8

9

10

```

1

2

3

4

5

6

7

8

9

10

```

import qcfpga

import numpy as np

# Ry(60): 60-degree rotation around the Y axes on the Bloch Sphere

gate_matrix = np.array([

[np.cos(np.pi/6), -np.sin(np.pi/6)],

[np.sin(np.pi/6),np.cos(np.pi/6)]

])

gate = qcfpga.Gate(gate_matrix)

```

import qcfpga

import numpy as np

# Ry(60): 60-degree rotation around the Y axes on the Bloch Sphere

gate_matrix = np.array([

[np.cos(np.pi/6), -np.sin(np.pi/6)],

[np.sin(np.pi/6),np.cos(np.pi/6)]

])

gate = qcfpga.Gate(gate_matrix)

```

```

import qcfpga

import numpy as np

# Ry(60): 60-degree rotation around the Y axes on the Bloch Sphere

gate_matrix = np.array([

[np.cos(np.pi/6), -np.sin(np.pi/6)],

[np.sin(np.pi/6),np.cos(np.pi/6)]

])

gate = qcfpga.Gate(gate_matrix)

```

The input to the Gate constructor is checked to be a 2x2 unitary

matrix.

```

Gate

```

## Quantum operations

Multiple operations can be performed on quantum registers with QCFPGA.

### Measurements

QCFPA follows the implementation of QCGPU which means that measuring a register in QCFPGA does not collapse the state, though this feature may be added in the future. When measuring the state, you have the option to set how many times to take samples. The result from the measure function is a dictionary containing the bitstrings of the outputs and the frequency of their measurements.

```

measure

```

A register is measured as follows,

1

2

3

4

5

6import qcfpga

register = qcfpga.State(5)

register.measure(samples=1000)

# {'00000': 1000}

1

2

3

4

5

6

```

1

2

3

4

5

6

```

import qcfpga

register = qcfpga.State(5)

register.measure(samples=1000)

# {'00000': 1000}

```

import qcfpga

register = qcfpga.State(5)

register.measure(samples=1000)

# {'00000': 1000}

```

```

import qcfpga

register = qcfpga.State(5)

register.measure(samples=1000)

# {'00000': 1000}

```

Measuring a single qubit can be performed as follows (without collapsing):

1

2

3

4

5

6

7

8import qcfpga

register = qcfpga.State(5)

register.h(0)

register.measure_qubit(0, samples=1000)

# {'1': 523, '0': 477}

1

2

3

4

5

6

7

8

```

1

2

3

4

5

6

7

8

```

import qcfpga

register = qcfpga.State(5)

register.h(0)

register.measure_qubit(0, samples=1000)

# {'1': 523, '0': 477}

```

import qcfpga

register = qcfpga.State(5)

register.h(0)

register.measure_qubit(0, samples=1000)

# {'1': 523, '0': 477}

```

```

import qcfpga

register = qcfpga.State(5)

register.h(0)

register.measure_qubit(0, samples=1000)

# {'1': 523, '0': 477}

```

### Probabilities

Probability for each state can be obtained using the probabilities method:

```

probabilities

```

1

2

3

4

5

6import qcfpga

register = qcfpga.State(1)

register.h(0)

register.probabilities() # [0.5, 0.5]

1

2

3

4

5

6

```

1

2

3

4

5

6

```

import qcfpga

register = qcfpga.State(1)

register.h(0)

register.probabilities() # [0.5, 0.5]

```

import qcfpga

register = qcfpga.State(1)

register.h(0)

register.probabilities() # [0.5, 0.5]

```

```

import qcfpga

register = qcfpga.State(1)

register.h(0)

register.probabilities() # [0.5, 0.5]

```