# PyOpenCL using Intel® FPGA SDK

Source: https://docs.lxp.lu/fpga/opencl/pyopencl_ifpgasdk/

# PyOpenCL using Intel® FPGA SDK

## Overview

PyOpenCL is a Python library designed to enable high-performance parallel computing on heterogeneous platforms using OpenCL, including FPGAs (Field-Programmable Gate Arrays). By exploiting PyOpenCL, developers can program FPGAs efficiently to accelerate computational tasks while leveraging Python's user-friendly syntax and extensive ecosystem.

## Key Features

FPGA Support: PyOpenCL facilitates the use of FPGAs as compute devices in a heterogeneous environment, alongside CPUs and GPUs.

Integration with Python: Offers a Pythonic interface to the OpenCL API, making it accessible to both novice and experienced Python programmers.

Memory Management: Simplifies data transfer between host and FPGA devices, maximizing data throughput and minimizing overhead.

Cross-Platform: Works across different platforms and vendors, allowing for flexible deployment of applications.

- FPGA Support: PyOpenCL facilitates the use of FPGAs as compute devices in a heterogeneous environment, alongside CPUs and GPUs.

- Integration with Python: Offers a Pythonic interface to the OpenCL API, making it accessible to both novice and experienced Python programmers.

- Memory Management: Simplifies data transfer between host and FPGA devices, maximizing data throughput and minimizing overhead.

- Cross-Platform: Works across different platforms and vendors, allowing for flexible deployment of applications.

## Getting started

To use PyOpenCL for FPGA development on Meluxina FPGA nodes, ensure first to request a FPGA node:

1

2

3

4

5

6

7# Get one FPGA node with two FPGA cards

salloc -A <ACCOUNT> -t 02:00:00 -q default -p fpga -N1

# Load the PyOpenCL module

module load env/staging/2023.1

module load PyOpenCL/2023.1.4-foss-2023a-ifpgasdk-20.4

# Let's check that we see the Intel FPGA SDK platform

python -c "import pyopencl as cl; print(cl.get_platforms())"

1

2

3

4

5

6

7

```

1

2

3

4

5

6

7

```

# Get one FPGA node with two FPGA cards

salloc -A <ACCOUNT> -t 02:00:00 -q default -p fpga -N1

# Load the PyOpenCL module

module load env/staging/2023.1

module load PyOpenCL/2023.1.4-foss-2023a-ifpgasdk-20.4

# Let's check that we see the Intel FPGA SDK platform

python -c "import pyopencl as cl; print(cl.get_platforms())"

```

# Get one FPGA node with two FPGA cards

salloc -A <ACCOUNT> -t 02:00:00 -q default -p fpga -N1

# Load the PyOpenCL module

module load env/staging/2023.1

module load PyOpenCL/2023.1.4-foss-2023a-ifpgasdk-20.4

# Let's check that we see the Intel FPGA SDK platform

python -c "import pyopencl as cl; print(cl.get_platforms())"

```

```

# Get one FPGA node with two FPGA cards

salloc -A <ACCOUNT> -t 02:00:00 -q default -p fpga -N1

# Load the PyOpenCL module

module load env/staging/2023.1

module load PyOpenCL/2023.1.4-foss-2023a-ifpgasdk-20.4

# Let's check that we see the Intel FPGA SDK platform

python -c "import pyopencl as cl; print(cl.get_platforms())"

```

You should see the following output [<pyopencl.Platform 'Intel(R) FPGA SDK for OpenCL(TM)' at 0x1544c17f2820>]

```

[<pyopencl.Platform 'Intel(R) FPGA SDK for OpenCL(TM)' at 0x1544c17f2820>]

```

## Example: Vector addition

Here's a simple example of using PyOpenCL to perform vector addition on an FPGA:

kernel.cl is the code running on the FPGA accelerator

vector_add.py is the python host code calling the kernel

- kernel.cl is the code running on the FPGA accelerator

- vector_add.py is the python host code calling the kernel

kernel.cl 1

2

3

4

5

6

7

8

9

10__kernel void vector_add(__global const float *x,

__global const float *y,

__global float *restrict z)

{

// get index of the work item

int index = get_global_id(0);

// add the vector elements

z[index] = x[index] + y[index];

}

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

__kernel void vector_add(__global const float *x,

__global const float *y,

__global float *restrict z)

{

// get index of the work item

int index = get_global_id(0);

// add the vector elements

z[index] = x[index] + y[index];

}

```

__kernel void vector_add(__global const float *x,

__global const float *y,

__global float *restrict z)

{

// get index of the work item

int index = get_global_id(0);

// add the vector elements

z[index] = x[index] + y[index];

}

```

```

__kernel void vector_add(__global const float *x,

__global const float *y,

__global float *restrict z)

{

// get index of the work item

int index = get_global_id(0);

// add the vector elements

z[index] = x[index] + y[index];

}

```

vector_add.py 1

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

34

35

36

37

38

39

40

41

42

43

44

45

46

47import pyopencl as cl

import numpy as np

def load_binary_from_file(file_path, ctx):

with open(file_path, "rb") as f:

binary = f.read()

return binary

def main():

# Choose platform and create context

platform = cl.get_platforms()[0]  # Select the first platform

device = platform.get_devices()[0]  # Select the first device on this platform

context = cl.Context([device])  # Create a context with the above device

# Load binary file

binary_path = "kernel.aocx"  # Path to your binary file

binary = load_binary_from_file(binary_path, context)

# Create program from binary

program = cl.Program(context, [device], [binary]).build()

# Prepare data and buffers

size = 1024

a_np = np.random.rand(size).astype(np.float32)

b_np = np.random.rand(size).astype(np.float32)

# Create memory buffers

mf = cl.mem_flags

a_g = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a_np)

b_g = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b_np)

res_g = cl.Buffer(context, mf.WRITE_ONLY, a_np.nbytes)

# Create a command queue

queue = cl.CommandQueue(context)

# Execute the kernel

kernel = program.vector_add  # Replace 'kernel_name' with your kernel's function name

kernel(queue, a_np.shape, None, a_g, b_g, res_g)

# Read the result

res_np = np.empty_like(a_np)

cl.enqueue_copy(queue, res_np, res_g).wait()

print("Result:", res_np)

if __name__ == "__main__":

main()

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

34

35

36

37

38

39

40

41

42

43

44

45

46

47

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

34

35

36

37

38

39

40

41

42

43

44

45

46

47

```

import pyopencl as cl

import numpy as np

def load_binary_from_file(file_path, ctx):

with open(file_path, "rb") as f:

binary = f.read()

return binary

def main():

# Choose platform and create context

platform = cl.get_platforms()[0]  # Select the first platform

device = platform.get_devices()[0]  # Select the first device on this platform

context = cl.Context([device])  # Create a context with the above device

# Load binary file

binary_path = "kernel.aocx"  # Path to your binary file

binary = load_binary_from_file(binary_path, context)

# Create program from binary

program = cl.Program(context, [device], [binary]).build()

# Prepare data and buffers

size = 1024

a_np = np.random.rand(size).astype(np.float32)

b_np = np.random.rand(size).astype(np.float32)

# Create memory buffers

mf = cl.mem_flags

a_g = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a_np)

b_g = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b_np)

res_g = cl.Buffer(context, mf.WRITE_ONLY, a_np.nbytes)

# Create a command queue

queue = cl.CommandQueue(context)

# Execute the kernel

kernel = program.vector_add  # Replace 'kernel_name' with your kernel's function name

kernel(queue, a_np.shape, None, a_g, b_g, res_g)

# Read the result

res_np = np.empty_like(a_np)

cl.enqueue_copy(queue, res_np, res_g).wait()

print("Result:", res_np)

if __name__ == "__main__":

main()

```

import pyopencl as cl

import numpy as np

def load_binary_from_file(file_path, ctx):

with open(file_path, "rb") as f:

binary = f.read()

return binary

def main():

# Choose platform and create context

platform = cl.get_platforms()[0]  # Select the first platform

device = platform.get_devices()[0]  # Select the first device on this platform

context = cl.Context([device])  # Create a context with the above device

# Load binary file

binary_path = "kernel.aocx"  # Path to your binary file

binary = load_binary_from_file(binary_path, context)

# Create program from binary

program = cl.Program(context, [device], [binary]).build()

# Prepare data and buffers

size = 1024

a_np = np.random.rand(size).astype(np.float32)

b_np = np.random.rand(size).astype(np.float32)

# Create memory buffers

mf = cl.mem_flags

a_g = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a_np)

b_g = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b_np)

res_g = cl.Buffer(context, mf.WRITE_ONLY, a_np.nbytes)

# Create a command queue

queue = cl.CommandQueue(context)

# Execute the kernel

kernel = program.vector_add  # Replace 'kernel_name' with your kernel's function name

kernel(queue, a_np.shape, None, a_g, b_g, res_g)

# Read the result

res_np = np.empty_like(a_np)

cl.enqueue_copy(queue, res_np, res_g).wait()

print("Result:", res_np)

if __name__ == "__main__":

main()

```

```

import pyopencl as cl

import numpy as np

def load_binary_from_file(file_path, ctx):

with open(file_path, "rb") as f:

binary = f.read()

return binary

def main():

# Choose platform and create context

platform = cl.get_platforms()[0]  # Select the first platform

device = platform.get_devices()[0]  # Select the first device on this platform

context = cl.Context([device])  # Create a context with the above device

# Load binary file

binary_path = "kernel.aocx"  # Path to your binary file

binary = load_binary_from_file(binary_path, context)

# Create program from binary

program = cl.Program(context, [device], [binary]).build()

# Prepare data and buffers

size = 1024

a_np = np.random.rand(size).astype(np.float32)

b_np = np.random.rand(size).astype(np.float32)

# Create memory buffers

mf = cl.mem_flags

a_g = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a_np)

b_g = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b_np)

res_g = cl.Buffer(context, mf.WRITE_ONLY, a_np.nbytes)

# Create a command queue

queue = cl.CommandQueue(context)

# Execute the kernel

kernel = program.vector_add  # Replace 'kernel_name' with your kernel's function name

kernel(queue, a_np.shape, None, a_g, b_g, res_g)

# Read the result

res_np = np.empty_like(a_np)

cl.enqueue_copy(queue, res_np, res_g).wait()

print("Result:", res_np)

if __name__ == "__main__":

main()

```

Before calling the vector_add.py file using python, you will need to build the FPGA image

Synthesis, placement, and routing of FPGA designs requires long processing times

We strongly advise to submit a passive job for this purpose using the following launcher:

- Before calling the vector_add.py file using python, you will need to build the FPGA image

```

vector_add.py

```

- Synthesis, placement, and routing of FPGA designs requires long processing times

- We strongly advise to submit a passive job for this purpose using the following launcher:

#!/bin/bash -l

#SBATCH -N 1

#SBATCH --ntasks=1

#SBATCH --cpus-per-task=128

#SBATCH -p fpga

#SBATCH -q default

#SBATCH --time 48:00:00

#SBATCH --account <ACCOUNT>

#Load Intel FPGA SDK module and supporting packages

module load ifpgasdk/20.4

module load 520nmx/20.4

#Compile OpenCL program with Intel FPGA SDK

aoc -v -board=p520_hpc_m210h_g3x16 -fast-compile -parallel=${SLURM_CPUS_PER_TASK} -fp-relaxed -o kernel.aocx kernel.cl

```

#!/bin/bash -l

#SBATCH -N 1

#SBATCH --ntasks=1

#SBATCH --cpus-per-task=128

#SBATCH -p fpga

#SBATCH -q default

#SBATCH --time 48:00:00

#SBATCH --account <ACCOUNT>

#Load Intel FPGA SDK module and supporting packages

module load ifpgasdk/20.4

module load 520nmx/20.4

#Compile OpenCL program with Intel FPGA SDK

aoc -v -board=p520_hpc_m210h_g3x16 -fast-compile -parallel=${SLURM_CPUS_PER_TASK} -fp-relaxed -o kernel.aocx kernel.cl

```

```

#!/bin/bash -l

#SBATCH -N 1

#SBATCH --ntasks=1

#SBATCH --cpus-per-task=128

#SBATCH -p fpga

#SBATCH -q default

#SBATCH --time 48:00:00

#SBATCH --account <ACCOUNT>

#Load Intel FPGA SDK module and supporting packages

module load ifpgasdk/20.4

module load 520nmx/20.4

#Compile OpenCL program with Intel FPGA SDK

aoc -v -board=p520_hpc_m210h_g3x16 -fast-compile -parallel=${SLURM_CPUS_PER_TASK} -fp-relaxed -o kernel.aocx kernel.cl

```

> **Fast compilation**

> Fast compilation

Fast compilation

Offline compilation (synthesis, placement, and routing) can be accelerated using the -fast-compile parameter

The -fast-compile will nevertheless generate non-optimized designs impacting performance

- Offline compilation (synthesis, placement, and routing) can be accelerated using the -fast-compile parameter

```

-fast-compile

```

- The -fast-compile will nevertheless generate non-optimized designs impacting performance

```

-fast-compile

```

Once the file kernel.aocx image has been generated, you are now able to execute the vector_add.py script:

```

kernel.aocx

```

```

vector_add.py

```

# Get one FPGA node with two FPGA cards

salloc -A <ACCOUNT> -t 02:00:00 -q default -p fpga -N1

# Load the PyOpenCL module

module load env/staging/2023.1

module load PyOpenCL/2023.1.4-foss-2023a-ifpgasdk-20.4

PYOPENCL_COMPILER_OUTPUT=1 python vector_add.py

```

# Get one FPGA node with two FPGA cards

salloc -A <ACCOUNT> -t 02:00:00 -q default -p fpga -N1

# Load the PyOpenCL module

module load env/staging/2023.1

module load PyOpenCL/2023.1.4-foss-2023a-ifpgasdk-20.4

PYOPENCL_COMPILER_OUTPUT=1 python vector_add.py

```

```

# Get one FPGA node with two FPGA cards

salloc -A <ACCOUNT> -t 02:00:00 -q default -p fpga -N1

# Load the PyOpenCL module

module load env/staging/2023.1

module load PyOpenCL/2023.1.4-foss-2023a-ifpgasdk-20.4

PYOPENCL_COMPILER_OUTPUT=1 python vector_add.py

```

> **Using Direct Memory Access (DMA)**

> Using Direct Memory Access (DMA)

Using Direct Memory Access (DMA)

DMA is enabled between host and the device if buffer data have a 64-byte alignment.

Using pyopencl, we strongly recommend you to load our jemalloc module which provides such default alignment:

module load jemalloc/5.3.0-GCCcore-12.3.0

export JEMALLOC_PRELOAD=$(jemalloc-config --libdir)/libjemalloc.so.$(jemalloc-config --revision)

LD_PRELOAD=${JEMALLOC_PRELOAD} PYOPENCL_COMPILER_OUTPUT=1 python vector_add.py

- DMA is enabled between host and the device if buffer data have a 64-byte alignment.

- Using pyopencl, we strongly recommend you to load our jemalloc module which provides such default alignment:

module load jemalloc/5.3.0-GCCcore-12.3.0

export JEMALLOC_PRELOAD=$(jemalloc-config --libdir)/libjemalloc.so.$(jemalloc-config --revision)

LD_PRELOAD=${JEMALLOC_PRELOAD} PYOPENCL_COMPILER_OUTPUT=1 python vector_add.py

```

jemalloc

```

module load jemalloc/5.3.0-GCCcore-12.3.0

export JEMALLOC_PRELOAD=$(jemalloc-config --libdir)/libjemalloc.so.$(jemalloc-config --revision)

LD_PRELOAD=${JEMALLOC_PRELOAD} PYOPENCL_COMPILER_OUTPUT=1 python vector_add.py

```

module load jemalloc/5.3.0-GCCcore-12.3.0

export JEMALLOC_PRELOAD=$(jemalloc-config --libdir)/libjemalloc.so.$(jemalloc-config --revision)

LD_PRELOAD=${JEMALLOC_PRELOAD} PYOPENCL_COMPILER_OUTPUT=1 python vector_add.py

```

```

module load jemalloc/5.3.0-GCCcore-12.3.0

export JEMALLOC_PRELOAD=$(jemalloc-config --libdir)/libjemalloc.so.$(jemalloc-config --revision)

LD_PRELOAD=${JEMALLOC_PRELOAD} PYOPENCL_COMPILER_OUTPUT=1 python vector_add.py

```

## Best Practices

Try to optimize Data Transfers: Minimize the frequency and size of data transfers between the host and FPGA.

Use Kernel Optimizations: Design and optimize OpenCL kernels to take full advantage of FPGA architectures.

Take advantage of asynchronous execution: Utilize asynchronous operations to overlap data transfers and computation, maximizing throughput.

- Try to optimize Data Transfers: Minimize the frequency and size of data transfers between the host and FPGA.

- Use Kernel Optimizations: Design and optimize OpenCL kernels to take full advantage of FPGA architectures.

- Take advantage of asynchronous execution: Utilize asynchronous operations to overlap data transfers and computation, maximizing throughput.