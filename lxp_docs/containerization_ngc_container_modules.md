# Module Environment for NVIDIA GPU Containers (NGC)

Source: https://docs.lxp.lu/containerization/ngc_container_modules/

# Module Environment for NVIDIA GPU Containers (NGC)

## Introduction

Starting in January 2024, our software suite has been enhanced to include Nvidia GPU Containers (NGC). This integration brings a significant upgrade to our capabilities, offering advanced GPU-accelerated applications and tools designed by Nvidia. With NGC, users will have access to a comprehensive catalog of GPU-optimized software for deep learning, machine learning, and high-performance computing (HPC) applications. This addition is part of our commitment to providing the most advanced and efficient tools to our users, ensuring they have access to cutting-edge technology for their computational needs.

NGC container environment modules act as efficient interfaces, designed to seamlessly integrate NGC containers with our existing environment modules. By using these modules, you gain the ability to leverage the power of NGC containers without the need for extensive configuration or compatibility adjustments. This integration simplifies the process of adopting advanced NVIDIA GPU Container capabilities, ensuring that you can easily access and utilize cutting-edge software and tools. The key benefits include streamlined workflows, enhanced compatibility with existing systems, and a reduction in the time and effort required to set up and maintain complex environments.

## Available container modules

As of January 2024 and NGC stack 2023.1 the following container module are available:

CP2K/2023.1-CUDA-12.1-NGC-23.10

QMCPACK/v3.16.0-CUDA-11.8.0-NGC-23.10

GROMACS/2023.2-CUDA-12.1.0-NGC-23.10

QuantumESPRESSO/7.1-CUDA-12.2.0-NGC-23.10

LAMMPS/patch_15Jun2023-CUDA-12.2.0-NGC-23.10

TensorFlow/2.13.0-CUDA-12.2.0-NGC-23.10

PyTorch/2.1.0-CUDA-12.2.0-NGC-23.10

- CP2K/2023.1-CUDA-12.1-NGC-23.10

- QMCPACK/v3.16.0-CUDA-11.8.0-NGC-23.10

- GROMACS/2023.2-CUDA-12.1.0-NGC-23.10

- QuantumESPRESSO/7.1-CUDA-12.2.0-NGC-23.10

- LAMMPS/patch_15Jun2023-CUDA-12.2.0-NGC-23.10

- TensorFlow/2.13.0-CUDA-12.2.0-NGC-23.10

- PyTorch/2.1.0-CUDA-12.2.0-NGC-23.10

Each of these modules is built to leverage the power of CUDA 11 and 12 and the NGC-23.10 framework, ensuring optimal performance and compatibility with the latest GPU technologies. This diverse range of modules supports a wide array of computational tasks, from data science to AI, offering our users the flexibility and power to tackle their most demanding computational challenges.

> **Important**

> Important

Important

The NGC container modules are to be run with mpirun and does not work with srun.

### Options for mpirun

```

mpirun

```

As specified above, the NGC modules only support mpirun for parallel run. The following mpirun options can be used to properly used NGC modules:

```

mpirun

```

```

mpirun

```

--report-bindings: Report any bindings for launched processes. This can be ignored as it is only for debug purposes.

--display-allocation: Display the detected resource allocation by mpirun. This can be ignored as it is only for debug purposes.

--bind-to object: Bind processes to the specified object. Supported options include slot, hwthread, core, l1cache, l2cache, l3cache, socket, numa, board, cpu-list, and none. By default, it binds processes to separate physical cores.

ppr:n:unit: For n processes per unit ressource where unit resource can be slot, hwthread, core, l1cache, l2cache, l3cache, socket, numa, board, cpu-list, and none. This is useful for binding mpi processes/ranks to a specific unit resource.

pe:p: For p processing element. This specifies the number of slot each mpi ranks/processes can run up to. Useful for multi-threading.

-map-by ppr:n:unit:pe=p_: Launch n processes per unit on each node (unit can also be a node). Each process will occupy p slots on a given unit.

- --report-bindings: Report any bindings for launched processes. This can be ignored as it is only for debug purposes.

```

--report-bindings

```

- --display-allocation: Display the detected resource allocation by mpirun. This can be ignored as it is only for debug purposes.

```

--display-allocation

```

```

mpirun

```

- --bind-to object: Bind processes to the specified object. Supported options include slot, hwthread, core, l1cache, l2cache, l3cache, socket, numa, board, cpu-list, and none. By default, it binds processes to separate physical cores.

```

--bind-to object

```

```

slot, hwthread, core, l1cache, l2cache, l3cache, socket, numa, board, cpu-list, and none

```

- ppr:n:unit: For n processes per unit ressource where unit resource can be slot, hwthread, core, l1cache, l2cache, l3cache, socket, numa, board, cpu-list, and none. This is useful for binding mpi processes/ranks to a specific unit resource.

```

ppr:n:unit

```

```

n processes per unit ressource

```

```

slot, hwthread, core, l1cache, l2cache, l3cache, socket, numa, board, cpu-list, and none

```

- pe:p: For p processing element. This specifies the number of slot each mpi ranks/processes can run up to. Useful for multi-threading.

```

p processing element

```

```

slot

```

```

mpi ranks/processes

```

- -map-by ppr:n:unit:pe=p_: Launch n processes per unit on each node (unit can also be a node). Each process will occupy p slots on a given unit.

```

-map-by ppr:n:unit:pe=p

```

```

n

```

```

unit

```

```

node

```

```

process

```

```

p

```

```

unit

```

The following example: mpirun -bind-to core -map-by ppr:4:node:pe=16 --report-bindings --display-allocation -n 8 ... will bind 8 mpi ranks/processes to physical cores in total, with 4 processes per node, 2 nodes in total and each process can run on up to 16 physical cores.

```

mpirun -bind-to core -map-by ppr:4:node:pe=16 --report-bindings --display-allocation -n 8 ...

```

### Running CP2K 2023.1

CP2K/2023.1-CUDA-12.1-NGC-23.10 is a highly efficient module in our software stack, optimized for complex molecular simulations. This version of CP2K harnesses the power of CUDA 12.1 and is fully compatible with the NGC-23.10 framework, ensuring accelerated performance and precision in computational chemistry and solid-state physics tasks. It's an ideal choice for users requiring advanced capabilities in atomistic simulations, electronic structure analysis, and quantum chemistry computations, all enhanced by the latest GPU technologies.

To have access to the module:

module load env/staging

module use /apps/USE/containers/staging/2023.1/modules/all/

```

module load env/staging

module use /apps/USE/containers/staging/2023.1/modules/all/

```

```

module load env/staging

module use /apps/USE/containers/staging/2023.1/modules/all/

```

In interactive or batch modes, simply load the CP2K module and run your application with mpirun:

- In interactive or batch modes, simply load the CP2K module and run your application with mpirun:

module load env/staging

module use /apps/USE/containers/staging/2023.1/modules/all/

module load CP2K/2023.1-CUDA-12.1-NGC-23.10

mpirun --bind-to none --report-bindings --display-allocation -n 2 cp2k.psmp -i H2O-dft-ls.NREP2.inp

```

module load env/staging

module use /apps/USE/containers/staging/2023.1/modules/all/

module load CP2K/2023.1-CUDA-12.1-NGC-23.10

mpirun --bind-to none --report-bindings --display-allocation -n 2 cp2k.psmp -i H2O-dft-ls.NREP2.inp

```

```

module load env/staging

module use /apps/USE/containers/staging/2023.1/modules/all/

module load CP2K/2023.1-CUDA-12.1-NGC-23.10

mpirun --bind-to none --report-bindings --display-allocation -n 2 cp2k.psmp -i H2O-dft-ls.NREP2.inp

```

> **Important**

> Important

Important

Pinning is very important in multinodes runs as mpirun sometimes does not handle it correctly. For example, running a job on 2 nodes with 8 tasks could result in the following binding where 5 tasks are allocated to the first node and 3 to the second node.

[mel2169:28351] MCW rank 0 bound to socket 0[core 24[hwt 0-1]], socket 0[core 25[hwt 0-1]], socket 0[core 26[hwt 0-1]], socket 0[core 27[hwt 0-1]], socket 0[core 28[hwt 0-1]], socket 0[core 29[hwt 0-1]], socket 0[core 30[hwt 0-1]], socket 0[core 31[hwt 0-1]]: [../../../../../../../../../../../../../../../../../../../../../../../../BB/BB/BB/BB/BB/BB/BB/BB][../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../..]

[mel2169:28351] MCW rank 1 bound to socket 0[core 8[hwt 0-1]], socket 0[core 9[hwt 0-1]], socket 0[core 10[hwt 0-1]], socket 0[core 11[hwt 0-1]], socket 0[core 12[hwt 0-1]], socket 0[core 13[hwt 0-1]], socket 0[core 14[hwt 0-1]], socket 0[core 15[hwt 0-1]]: [../../../../../../../../BB/BB/BB/BB/BB/BB/BB/BB/../../../../../../../../../../../../../../../..][../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../..]

[mel2169:28351] MCW rank 2 bound to socket 1[core 56[hwt 0-1]], socket 1[core 57[hwt 0-1]], socket 1[core 58[hwt 0-1]], socket 1[core 59[hwt 0-1]], socket 1[core 60[hwt 0-1]], socket 1[core 61[hwt 0-1]], socket 1[core 62[hwt 0-1]], socket 1[core 63[hwt 0-1]]: [../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../..][../../../../../../../../../../../../../../../../../../../../../../../../BB/BB/BB/BB/BB/BB/BB/BB]

[mel2169:28351] MCW rank 3 bound to socket 1[core 40[hwt 0-1]], socket 1[core 41[hwt 0-1]], socket 1[core 42[hwt 0-1]], socket 1[core 43[hwt 0-1]], socket 1[core 44[hwt 0-1]], socket 1[core 45[hwt 0-1]], socket 1[core 46[hwt 0-1]], socket 1[core 47[hwt 0-1]]: [../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../..][../../../../../../../../BB/BB/BB/BB/BB/BB/BB/BB/../../../../../../../../../../../../../../../..]

[mel2169:28351] MCW rank 4 bound to socket 0[core 24[hwt 0-1]], socket 0[core 25[hwt 0-1]], socket 0[core 26[hwt 0-1]], socket 0[core 27[hwt 0-1]], socket 0[core 28[hwt 0-1]], socket 0[core 29[hwt 0-1]], socket 0[core 30[hwt 0-1]], socket 0[core 31[hwt 0-1]]: [../../../../../../../../../../../../../../../../../../../../../../../../BB/BB/BB/BB/BB/BB/BB/BB][../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../..]

[mel2170:23857] MCW rank 5 bound to socket 0[core 8[hwt 0-1]], socket 0[core 9[hwt 0-1]], socket 0[core 10[hwt 0-1]], socket 0[core 11[hwt 0-1]], socket 0[core 12[hwt 0-1]], socket 0[core 13[hwt 0-1]], socket 0[core 14[hwt 0-1]], socket 0[core 15[hwt 0-1]]: [../../../../../../../../BB/BB/BB/BB/BB/BB/BB/BB/../../../../../../../../../../../../../../../..][../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../..]

[mel2170:23857] MCW rank 6 bound to socket 1[core 56[hwt 0-1]], socket 1[core 57[hwt 0-1]], socket 1[core 58[hwt 0-1]], socket 1[core 59[hwt 0-1]], socket 1[core 60[hwt 0-1]], socket 1[core 61[hwt 0-1]], socket 1[core 62[hwt 0-1]], socket 1[core 63[hwt 0-1]]: [../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../..][../../../../../../../../../../../../../../../../../../../../../../../../BB/BB/BB/BB/BB/BB/BB/BB]

[mel2170:23857] MCW rank 7 bound to socket 1[core 40[hwt 0-1]], socket 1[core 41[hwt 0-1]], socket 1[core 42[hwt 0-1]], socket 1[core 43[hwt 0-1]], socket 1[core 44[hwt 0-1]], socket 1[core 45[hwt 0-1]], socket 1[core 46[hwt 0-1]], socket 1[core 47[hwt 0-1]]: [../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../..][../../../../../../../../BB/BB/BB/BB/BB/BB/BB/BB/../../../../../../../../../../../../../../../..]

```

[mel2169:28351] MCW rank 0 bound to socket 0[core 24[hwt 0-1]], socket 0[core 25[hwt 0-1]], socket 0[core 26[hwt 0-1]], socket 0[core 27[hwt 0-1]], socket 0[core 28[hwt 0-1]], socket 0[core 29[hwt 0-1]], socket 0[core 30[hwt 0-1]], socket 0[core 31[hwt 0-1]]: [../../../../../../../../../../../../../../../../../../../../../../../../BB/BB/BB/BB/BB/BB/BB/BB][../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../..]

[mel2169:28351] MCW rank 1 bound to socket 0[core 8[hwt 0-1]], socket 0[core 9[hwt 0-1]], socket 0[core 10[hwt 0-1]], socket 0[core 11[hwt 0-1]], socket 0[core 12[hwt 0-1]], socket 0[core 13[hwt 0-1]], socket 0[core 14[hwt 0-1]], socket 0[core 15[hwt 0-1]]: [../../../../../../../../BB/BB/BB/BB/BB/BB/BB/BB/../../../../../../../../../../../../../../../..][../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../..]

[mel2169:28351] MCW rank 2 bound to socket 1[core 56[hwt 0-1]], socket 1[core 57[hwt 0-1]], socket 1[core 58[hwt 0-1]], socket 1[core 59[hwt 0-1]], socket 1[core 60[hwt 0-1]], socket 1[core 61[hwt 0-1]], socket 1[core 62[hwt 0-1]], socket 1[core 63[hwt 0-1]]: [../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../..][../../../../../../../../../../../../../../../../../../../../../../../../BB/BB/BB/BB/BB/BB/BB/BB]

[mel2169:28351] MCW rank 3 bound to socket 1[core 40[hwt 0-1]], socket 1[core 41[hwt 0-1]], socket 1[core 42[hwt 0-1]], socket 1[core 43[hwt 0-1]], socket 1[core 44[hwt 0-1]], socket 1[core 45[hwt 0-1]], socket 1[core 46[hwt 0-1]], socket 1[core 47[hwt 0-1]]: [../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../..][../../../../../../../../BB/BB/BB/BB/BB/BB/BB/BB/../../../../../../../../../../../../../../../..]

[mel2169:28351] MCW rank 4 bound to socket 0[core 24[hwt 0-1]], socket 0[core 25[hwt 0-1]], socket 0[core 26[hwt 0-1]], socket 0[core 27[hwt 0-1]], socket 0[core 28[hwt 0-1]], socket 0[core 29[hwt 0-1]], socket 0[core 30[hwt 0-1]], socket 0[core 31[hwt 0-1]]: [../../../../../../../../../../../../../../../../../../../../../../../../BB/BB/BB/BB/BB/BB/BB/BB][../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../..]

[mel2170:23857] MCW rank 5 bound to socket 0[core 8[hwt 0-1]], socket 0[core 9[hwt 0-1]], socket 0[core 10[hwt 0-1]], socket 0[core 11[hwt 0-1]], socket 0[core 12[hwt 0-1]], socket 0[core 13[hwt 0-1]], socket 0[core 14[hwt 0-1]], socket 0[core 15[hwt 0-1]]: [../../../../../../../../BB/BB/BB/BB/BB/BB/BB/BB/../../../../../../../../../../../../../../../..][../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../..]

[mel2170:23857] MCW rank 6 bound to socket 1[core 56[hwt 0-1]], socket 1[core 57[hwt 0-1]], socket 1[core 58[hwt 0-1]], socket 1[core 59[hwt 0-1]], socket 1[core 60[hwt 0-1]], socket 1[core 61[hwt 0-1]], socket 1[core 62[hwt 0-1]], socket 1[core 63[hwt 0-1]]: [../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../..][../../../../../../../../../../../../../../../../../../../../../../../../BB/BB/BB/BB/BB/BB/BB/BB]

[mel2170:23857] MCW rank 7 bound to socket 1[core 40[hwt 0-1]], socket 1[core 41[hwt 0-1]], socket 1[core 42[hwt 0-1]], socket 1[core 43[hwt 0-1]], socket 1[core 44[hwt 0-1]], socket 1[core 45[hwt 0-1]], socket 1[core 46[hwt 0-1]], socket 1[core 47[hwt 0-1]]: [../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../..][../../../../../../../../BB/BB/BB/BB/BB/BB/BB/BB/../../../../../../../../../../../../../../../..]

```

```

[mel2169:28351] MCW rank 0 bound to socket 0[core 24[hwt 0-1]], socket 0[core 25[hwt 0-1]], socket 0[core 26[hwt 0-1]], socket 0[core 27[hwt 0-1]], socket 0[core 28[hwt 0-1]], socket 0[core 29[hwt 0-1]], socket 0[core 30[hwt 0-1]], socket 0[core 31[hwt 0-1]]: [../../../../../../../../../../../../../../../../../../../../../../../../BB/BB/BB/BB/BB/BB/BB/BB][../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../..]

[mel2169:28351] MCW rank 1 bound to socket 0[core 8[hwt 0-1]], socket 0[core 9[hwt 0-1]], socket 0[core 10[hwt 0-1]], socket 0[core 11[hwt 0-1]], socket 0[core 12[hwt 0-1]], socket 0[core 13[hwt 0-1]], socket 0[core 14[hwt 0-1]], socket 0[core 15[hwt 0-1]]: [../../../../../../../../BB/BB/BB/BB/BB/BB/BB/BB/../../../../../../../../../../../../../../../..][../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../..]

[mel2169:28351] MCW rank 2 bound to socket 1[core 56[hwt 0-1]], socket 1[core 57[hwt 0-1]], socket 1[core 58[hwt 0-1]], socket 1[core 59[hwt 0-1]], socket 1[core 60[hwt 0-1]], socket 1[core 61[hwt 0-1]], socket 1[core 62[hwt 0-1]], socket 1[core 63[hwt 0-1]]: [../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../..][../../../../../../../../../../../../../../../../../../../../../../../../BB/BB/BB/BB/BB/BB/BB/BB]

[mel2169:28351] MCW rank 3 bound to socket 1[core 40[hwt 0-1]], socket 1[core 41[hwt 0-1]], socket 1[core 42[hwt 0-1]], socket 1[core 43[hwt 0-1]], socket 1[core 44[hwt 0-1]], socket 1[core 45[hwt 0-1]], socket 1[core 46[hwt 0-1]], socket 1[core 47[hwt 0-1]]: [../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../..][../../../../../../../../BB/BB/BB/BB/BB/BB/BB/BB/../../../../../../../../../../../../../../../..]

[mel2169:28351] MCW rank 4 bound to socket 0[core 24[hwt 0-1]], socket 0[core 25[hwt 0-1]], socket 0[core 26[hwt 0-1]], socket 0[core 27[hwt 0-1]], socket 0[core 28[hwt 0-1]], socket 0[core 29[hwt 0-1]], socket 0[core 30[hwt 0-1]], socket 0[core 31[hwt 0-1]]: [../../../../../../../../../../../../../../../../../../../../../../../../BB/BB/BB/BB/BB/BB/BB/BB][../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../..]

[mel2170:23857] MCW rank 5 bound to socket 0[core 8[hwt 0-1]], socket 0[core 9[hwt 0-1]], socket 0[core 10[hwt 0-1]], socket 0[core 11[hwt 0-1]], socket 0[core 12[hwt 0-1]], socket 0[core 13[hwt 0-1]], socket 0[core 14[hwt 0-1]], socket 0[core 15[hwt 0-1]]: [../../../../../../../../BB/BB/BB/BB/BB/BB/BB/BB/../../../../../../../../../../../../../../../..][../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../..]

[mel2170:23857] MCW rank 6 bound to socket 1[core 56[hwt 0-1]], socket 1[core 57[hwt 0-1]], socket 1[core 58[hwt 0-1]], socket 1[core 59[hwt 0-1]], socket 1[core 60[hwt 0-1]], socket 1[core 61[hwt 0-1]], socket 1[core 62[hwt 0-1]], socket 1[core 63[hwt 0-1]]: [../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../..][../../../../../../../../../../../../../../../../../../../../../../../../BB/BB/BB/BB/BB/BB/BB/BB]

[mel2170:23857] MCW rank 7 bound to socket 1[core 40[hwt 0-1]], socket 1[core 41[hwt 0-1]], socket 1[core 42[hwt 0-1]], socket 1[core 43[hwt 0-1]], socket 1[core 44[hwt 0-1]], socket 1[core 45[hwt 0-1]], socket 1[core 46[hwt 0-1]], socket 1[core 47[hwt 0-1]]: [../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../../..][../../../../../../../../BB/BB/BB/BB/BB/BB/BB/BB/../../../../../../../../../../../../../../../..]

```

The example below can be used to bind the processes per node and to cores:

mpirun -bind-to core -map-by ppr:4:node:pe=16 --report-bindings --display-allocation -n 8 cp2k.psmp -i H2O-dft-ls.NREP2.inp

```

mpirun -bind-to core -map-by ppr:4:node:pe=16 --report-bindings --display-allocation -n 8 cp2k.psmp -i H2O-dft-ls.NREP2.inp

```

```

mpirun -bind-to core -map-by ppr:4:node:pe=16 --report-bindings --display-allocation -n 8 cp2k.psmp -i H2O-dft-ls.NREP2.inp

```

### Running QMCPACK v3.16.0

QMCPACK/v3.16.0-CUDA-11.8.0-NGC-23.10 module is designed for high-precision quantum Monte Carlo simulations. This release integrates CUDA 11.8.0, ensuring full compatibility with the NGC-23.10 environment. It's particularly suitable for quantum materials science, electronic properties investigations, and advanced quantum simulations.

To have access to the module:

module load env/staging

module use /apps/USE/containers/staging/2023.1/modules/all/

```

module load env/staging

module use /apps/USE/containers/staging/2023.1/modules/all/

```

```

module load env/staging

module use /apps/USE/containers/staging/2023.1/modules/all/

```

In interactive or batch modes, simply load the QMCPACK module and run your application with mpirun:

- In interactive or batch modes, simply load the QMCPACK module and run your application with mpirun:

module load env/staging

module use /apps/USE/containers/staging/2023.1/modules/all/

module load QMCPACK/v3.16.0-CUDA-11.8.0-NGC-23.10

#On two nodes

mpirun -bind-to core -map-by ppr:4:node:pe=16 --report-bindings --display-allocation -n 8 qmcpack NiO-fcc-S32-dmc.xml

```

module load env/staging

module use /apps/USE/containers/staging/2023.1/modules/all/

module load QMCPACK/v3.16.0-CUDA-11.8.0-NGC-23.10

#On two nodes

mpirun -bind-to core -map-by ppr:4:node:pe=16 --report-bindings --display-allocation -n 8 qmcpack NiO-fcc-S32-dmc.xml

```

```

module load env/staging

module use /apps/USE/containers/staging/2023.1/modules/all/

module load QMCPACK/v3.16.0-CUDA-11.8.0-NGC-23.10

#On two nodes

mpirun -bind-to core -map-by ppr:4:node:pe=16 --report-bindings --display-allocation -n 8 qmcpack NiO-fcc-S32-dmc.xml

```

### Running GROMACS 2023.2

GROMACS/2023.2-CUDA-12.1.0-NGC-23.10 module give access to the open-source software suite for high-performance molecular dynamics and output analysis. This version of GROMACS capitalizes on the capabilities of CUDA 12.1.0 and seamlessly integrates with the NGC-23.10 framework, guaranteeing accelerated and precise computational workflows in the realms of biochemistry, biophysics, and material science.

With a focus on leveraging the latest GPU technologies, GROMACS/2023.2-CUDA-12.1.0-NGC-23.10 is tailored for users demanding advanced features in the exploration of biomolecular systems, protein-ligand interactions, and structural dynamics. The integration of CUDA 12.1.0 ensures optimal utilization of GPU resources, enhancing the overall efficiency of molecular dynamics simulations.

Whether tackling complex biological processes or investigating materials at the atomic level, this version of GROMACS provides a robust platform for researchers and scientists seeking state-of-the-art tools for their computational chemistry and biophysics endeavors.

To have access to the module:

module load env/staging

module use /apps/USE/containers/staging/2023.1/modules/all/

```

module load env/staging

module use /apps/USE/containers/staging/2023.1/modules/all/

```

```

module load env/staging

module use /apps/USE/containers/staging/2023.1/modules/all/

```

In interactive, simply load the NGC GROMACS module and run your application with mpirun:

- In interactive, simply load the NGC GROMACS module and run your application with mpirun:

module load env/staging

module use /apps/USE/containers/staging/2023.1/modules/all/

module load GROMACS/2023.2-CUDA-12.1.0-NGC-23.10

export GMX_ENABLE_DIRECT_GPU_COMM=1

gmx mdrun -ntmpi 8 -ntomp 16 -nb gpu -pme gpu -npme 1 -update gpu -bonded gpu -nsteps 100000 -resetstep 90000 -noconfout -dlb no -nstlist 300 -pin on -v -gpu_id 0123

```

module load env/staging

module use /apps/USE/containers/staging/2023.1/modules/all/

module load GROMACS/2023.2-CUDA-12.1.0-NGC-23.10

export GMX_ENABLE_DIRECT_GPU_COMM=1

gmx mdrun -ntmpi 8 -ntomp 16 -nb gpu -pme gpu -npme 1 -update gpu -bonded gpu -nsteps 100000 -resetstep 90000 -noconfout -dlb no -nstlist 300 -pin on -v -gpu_id 0123

```

```

module load env/staging

module use /apps/USE/containers/staging/2023.1/modules/all/

module load GROMACS/2023.2-CUDA-12.1.0-NGC-23.10

export GMX_ENABLE_DIRECT_GPU_COMM=1

gmx mdrun -ntmpi 8 -ntomp 16 -nb gpu -pme gpu -npme 1 -update gpu -bonded gpu -nsteps 100000 -resetstep 90000 -noconfout -dlb no -nstlist 300 -pin on -v -gpu_id 0123

```

> **Important**

> Important

Important

The current module does not support multi-node simulations.