# What's new on MeluXina

Source: https://docs.lxp.lu/system/whatsnew/

# What's new on MeluXina

## SYSTEM

### 2024-09-05: Upgrade to DDN ExaScaler 6.3

The DDN Lustre storage backend has received a major upgrade from ExaScaler 5.2.8 to ExaScaler 6.3.0-3. While this does not have a direct user facing impact, it should provide improved redundancy and therefore availability of the storage system.

As part of this upgrade, compute and login nodes have been updated to version 2.14.0_ddn148 of the lustre driver.

### 2024-09-05: Slurm update to 23.11.9

SLURM has been upgraded from version 23.02.7 to 23.11.9 which addresses some accounting bugs. More details can found here.

> **Warning**

> Warning

Warning

While we expect your submission workflow to remain unaffected, there is a chance you may notice some subtle changes. Your input is invaluable to us, and we are committed to continuously improving your experience. If you encounter any issues or have any suggestions, please don’t hesitate to reach out to our support team.

### 2024-09-05: Upgrade to Rocky 8.10

The compute nodes have been migrated to Rocky Linux 8.10. This updated version will bring improved performance, security, and compatibility with the latest software packages.

The login nodes likewise have been updated to RHEL 8.10.

The compute and login nodes also received a minor MOFED point release update, a minor lustre driver update, and the GPU compute nodes a major new NVIDIA GPU driver. Lastly, the FPGA nodes received a minor BittWare driver update.

### 2024-09-05: Upgrade to MOFED 23.10-3.2.2.1

The NVIDIA MOFED driver has been upgraded to the long-term support (LTS) version 23.10-3.2.2.1. This is a minor update and adds support for the latest operating systems. For a detailed overview of the changes, please check the release notes for more information.

### 2024-09-05: NVIDIA Driver Update

To support the latest CUDA 12.6 release, we are updating the NVIDIA driver to version 560.35.03. This will enable you to take full advantage of the latest GPU-accelerated applications and frameworks.

For a detailed list of all the changes and updates brought by this NVIDIA driver version, please visit the official release notes at the following link: NVIDIA Driver release notes.

### 2024-09-05: BittWare Driver Update

The BittWare FPGA driver has been updated to version 2.0-15. This is a minor update that fixes some reliability issues.

### 2024-05-06: Upgrade to Rocky 8.9

The compute nodes have been migrated to Rocky Linux 8.9. This updated version will bring improved performance, security, and compatibility with the latest software packages.

The login nodes will remain on RHEL 8.8 for this update cycle, as it is an Extended Update Support (EUS) release.

The compute and login nodes also received a new major MOFED release, a new lustre driver, and the GPU compute nodes a new NVIDIA GPU driver.

### 2024-05-06: Upgrade to MOFED 23.10-2.1.3.1

The NVIDIA MOFED driver has been upgraded to the long-term support (LTS) version 23.10-2.1.3.1. This update includes important bug fixes and adds support for the latest operating systems. For a detailed overview of the changes, please check the release notes for more information.

### 2024-05-06: NVIDIA Driver Update

On the GPU nodes, we have updated the NVIDIA driver to version 535.161.08. This is a minor update which adds the necessary Rocky 8.9 support. Please check the release notes for more information.

### 2024-05-06: Python 3.11 added to login nodes

Python 3.11 has been added as an additional interpreter to the login nodes. The default python3 version however remains at 3.6. Python 3.11 can be invoked using python3.11. You can optionally make it default for your own environment by adding the following environment settings to your ~/.bashrc file:

```

python3.11

```

```

~/.bashrc

```

alias python3=python3.11

alias pip3=pip3.11

```

alias python3=python3.11

alias pip3=pip3.11

```

```

alias python3=python3.11

alias pip3=pip3.11

```

Python 3.11 is of course also available on the compute nodes via Lmod. To see available Python versions via modules, simply run:

module spider Python

```

module spider Python

```

```

module spider Python

```

### 2024-05-06: Limits introduced on login nodes

CPU, memory and process limits have been set on the login nodes, to prevent a single user from monopolizing them.

Keep in mind that login nodes are shared resources, and only meant for data transfer, launching jobs, filesystem operations and light editing work. Any computational or memory intensive work must be done on compute nodes.

### 2023-10-30: Upgrade to MOFED 5.8-3.0.7.0

The NVIDIA MOFED driver has been upgraded to the long-term support (LTS) version 5.8-3.0.7.0. This update includes important bug fixes and adds support for the latest operating systems. For a detailed overview of the changes, please check the release note for the detailed changes.

### 2023-10-30: NVIDIA Driver Update

To support the latest CUDA 12.x releases, we are updating the NVIDIA driver to version 535.104.12. This will enable you to take full advantage of the latest GPU-accelerated applications and frameworks.

For a detailed list of all the changes and updates brought by NVIDIA driver version 535.104.12, please visit the official release notes at the following link: NVIDIA Driver Version 535.104.12 Release Notes.

### 2023-10-30: Upgrade to Rocky 8.8

The login and compute nodes have been migrated to RHEL/Rocky 8.8. This updated version will bring improved performance, security, and compatibility with the latest software packages.

### 2023-08-10: Changes to the default Lustre striping policy

A default OST (Object Storage Target) striping policy has been set on both Tier1 (scratch) and Tier2 (project/home) lustre filesystems.

This will affect only new files, with existing files not impacted.

Previously no policy was set, meaning files were not striped by default over multiple OSTs.

See the Lustre OST striping section for more details.

> **Info**

> Info

Info

The new policy is meant to improve resiliency and potentially data access performance.

If this is not the case for your workload, you can revert a directory and its subdirectories to the prior behaviour with the following command:

lfs setstripe -E -1 -c 1 -S 1M <directory>

```

lfs setstripe -E -1 -c 1 -S 1M <directory>

```

### 2023-06-15: Upgrade to Rocky 8.7

The compute nodes OS has been upgraded from Rocky Linux version 8.6 to 8.7 with latest bug fixes and security patches.

> **Info**

> Info

Info

No impact on user applications is expected and there are no changes to the MeluXina software stack.

### 2023-06-15: Upgrade to MOFED 5.8-2.0.3.0

The NVIDIA MOFED driver has been upgraded to LTS version 5.8-2.0.3.0 with critical bug fixes and support for the new OS. See release note for the detailed changes.

### 2023-06-15: Upgrade to Nvidia driver 515.105.01

Upgrade of Nvidia driver on GPU nodes fixes the following issue:

Resolved an issue that sometimes caused abnormal BAR1 memory usage.

Fixed a race condition that can arise when calling cudaFreeAsync() and cudaDeviceSynchronize() from different threads.

Fixed an issue where the NVIDIA Linux GPU kernel driver was calling the Linux kernel scheduler while holding a lock with preemption disabled during event notification.

- Resolved an issue that sometimes caused abnormal BAR1 memory usage.

- Fixed a race condition that can arise when calling cudaFreeAsync() and cudaDeviceSynchronize() from different threads.

- Fixed an issue where the NVIDIA Linux GPU kernel driver was calling the Linux kernel scheduler while holding a lock with preemption disabled during event notification.

> **Info**

> Info

Info

The CUDA Toolkit 11 version remains 11.7.

### 2023-06-15: Upgrade to Lustre client driver 2.14.0

The Lustre client driver has been upgraded to the 2.14 release, with expected performance improvements.

## SLURM & ParaStation

### 2023-12-15: Slurm update to 23.02.7

SLURM has been upgraded from version 22.02.6 to 23.02.7 that addresses a range of recently discovered security issues, which are identified by CVE-2023-49933 through CVE-2023-49938.

More details can found here.

### 2023-10-30: Slurm update to 23.02.6 and new energy monitoring

SLURM has been upgraded from version 22.05.9 to 23.02.6 with additional functionality and numerous fixes.

> **Info**

> Info

Info

No impact on user jobs or launcher scripts are expected with the new Slurm version.

New energy monitoring is now in place for Slurm jobs using the srun launcher, see the complete details in energy monitoring.

```

srun

```

For a full list of changes since SLURM 22.05.9 please see the SchedMD SLURM release notes. Note that not all updates may apply to MeluXina, as the job launcher daemon on the compute nodes is not the upstream slurmd.

```

slurmd

```

### 2023-10-30: Upgrade to psmgmt 5.1.57-2

psmgmt has been upgraded from version 5.1.55-5 to 5.1.57-2 with bug fixes. For a full list of changes since version 5.1.55-5 please see the psmgmt Change log.

> **Info**

> Info

Info

Message Passing Interface (PMIx) component has been updated to 4.2.6, improving inter-process communication and resource management for your applications. The new upcoming software stack (2023.1) will therefore feature PMIx 4.2.6.

### 2023-06-15: Upgrade to SLURM 22.05.9

SLURM has been upgraded from version 22.05.5 to 22.05.9 with additional functionality and numerous fixes.

> **Info**

> Info

Info

No impact on user jobs or launcher scripts are expected.

For a full list of changes since SLURM 22.05.5 please see the SchedMD SLURM release notes. Note that not all updates may apply to MeluXina, as the job launcher daemon on the compute nodes is not the upstream slurmd.

```

slurmd

```

### 2023-06-15: Upgrade to psmgmt 5.1.55-2

psmgmt has been upgraded from version 5.1.52-5 to 5.1.55-2 with bug fixes. For a full list of changes since version 5.1.52-5 please see the psmgmt Change log.

### 2022-11-24: Upgrade to psmgmt 5.1.52-5

psmgmt has been upgraded to version 5.1.52-5 with some of the following bug fixes:

> **Info**

> Info

Info

Bugfix: prevent segfault due to late REQUEST_LAUNCH_TASKS message. This fix prevent large scale jobs from hanging.

Bugfix: prevent psslurm from segfault by tracking init of basic configuration.

- Bugfix: prevent segfault due to late REQUEST_LAUNCH_TASKS message. This fix prevent large scale jobs from hanging.

- Bugfix: prevent psslurm from segfault by tracking init of basic configuration.

For a full list of changes since psmgmt 5.1.52-2 please see psmgmt Change log.

### 2022-11-14: Upgrade to SLURM 22.05.5

SLURM has been upgraded from 21.08.8-2 to 22.05.5, a major new version with additional functionality, security fixes and also breaking changes.

> **Warn**

> Warn

Warn

Highlighted change in this release that may impact your jobs: srun will no longer read in SLURM_CPUS_PER_TASK. This means you will explicitly have to specify --cpus-per-task (or -c) in your srun calls, or set the new SRUN_CPUS_PER_TASK environment variable get the correct result.

```

SLURM_CPUS_PER_TASK

```

```

--cpus-per-task

```

```

-c

```

```

SRUN_CPUS_PER_TASK

```

For a full list of changes since SLURM 21.08.8-2 please see the SchedMD SLURM release notes. Note that not all updates may apply to MeluXina, as the job launcher daemon on the compute nodes is not the upstream slurmd.

```

slurmd

```

## Software stacks

### 2024-12-15: New 2024.1 software stack release

We are thrilled to announce that our latest (2024.1) MeluXina User Software Environment is now available for use!

> **Info**

> Info

Info

Until 14 February 2025 try the new release by using module load env/release/2024.1 in your job scripts.

```

module load env/release/2024.1

```

> **Warning**

> Warning

Warning

The previous stable release 2023.1 is kept as default on MeluXina during a transition period until 14 February 2025. On 15 February, the env/release/2024.1 stack will become default in your jobs on MeluXina.

To keep using a non-default/outdated software stack, explicitely write in your scripts module load env/release/2023.1. Please use the staging/2024.1 release in the transition period and let us know of your impressions and any problems by contacting our service desk.

```

module load env/release/2023.1

```

Details on the software changes between the env/release/2023.1 and the env/release/2024.1 stacks can be found here.

Highlights in this release:

```

env/release/2023.1

```

```

env/release/2024.1

```

Compilers: AOCC 5.0.0, GCC 13.3.0, Intel 2024.2.1, NVIDIA HPC SDK / NVHPC 24.9, OneAPI 2024.2.1

Languages: Python 3.12.3, R 4.4.1, Julia 1.11.10, Go 1.22.1

Performance Engineering: Linaro-Forge 24.0.5, Score-P 8.4 (with and without CUDA support), AMD-uPROF 5.0.1479, Extrae 4.2.0

MPI, parallelization & acceleration: OpenMPI 5.0.3 (with UCC 1.3.0 and UCX 1.16.0), iimpi 2024a, CUDA 12.6.0, PETSc 3.22.0, Kokkos 4.4.1, cuDNN 9.5.0.50, NCCL 2.22.3

Data science: JupyterHub 5.2.0, JupyterLab 4.2.5, jupyter-server 2.14.2, RAPIDS 24.10

AI, Machine Learning, Deep Learning: PyTorch 2.3.0, MLFlow 2.17.2

Physics & chemistry: GROMACS 2024.3, 7.2.2, ORCA 6.0.0

CFD: OpenFOAM 12-foss-2024a

Visualisation & computer vision: ParaView 5.13.0

Quantum simulators: QSimCirq 0.21.0, cirq-core 1.4.1, cuQuantum 24.08.0.5

Container systems: Apptainer 1.3.4

- Compilers: AOCC 5.0.0, GCC 13.3.0, Intel 2024.2.1, NVIDIA HPC SDK / NVHPC 24.9, OneAPI 2024.2.1

- Languages: Python 3.12.3, R 4.4.1, Julia 1.11.10, Go 1.22.1

- Performance Engineering: Linaro-Forge 24.0.5, Score-P 8.4 (with and without CUDA support), AMD-uPROF 5.0.1479, Extrae 4.2.0

- MPI, parallelization & acceleration: OpenMPI 5.0.3 (with UCC 1.3.0 and UCX 1.16.0), iimpi 2024a, CUDA 12.6.0, PETSc 3.22.0, Kokkos 4.4.1, cuDNN 9.5.0.50, NCCL 2.22.3

- Data science: JupyterHub 5.2.0, JupyterLab 4.2.5, jupyter-server 2.14.2, RAPIDS 24.10

- AI, Machine Learning, Deep Learning: PyTorch 2.3.0, MLFlow 2.17.2

- Physics & chemistry: GROMACS 2024.3, 7.2.2, ORCA 6.0.0

- CFD: OpenFOAM 12-foss-2024a

- Visualisation & computer vision: ParaView 5.13.0

- Quantum simulators: QSimCirq 0.21.0, cirq-core 1.4.1, cuQuantum 24.08.0.5

- Container systems: Apptainer 1.3.4

### 2023-12-15: New 2023.1 software stack release

We are thrilled to announce that our latest (2023.1) MeluXina User Software Environment is now available for use!

> **Info**

> Info

Info

Until 14 February 2024 try the new release by using module load env/release/2023.1 or module load env/staging/2023.1 in your job scripts.

```

module load env/release/2023.1

```

```

module load env/staging/2023.1

```

> **Warn**

> Warn

Warn

The previous stable release 2022.1 is kept as default on MeluXina during a transition period until 14 February 2024. On 15 February, the 2023.1 release will become default in your jobs on MeluXina. To keep using the deprecated software stack, use module load env/release/2022.1. Please use the 2023.1 release in the transition period and let us know of your impressions and any problems by contacting our service desk. 2021.3 and 2021.5 software stacks will not be accessible anymore from 15 February 2024.

```

module load env/release/2022.1

```

The new 2023.1 software stack release brings new versions of most tools, build on latest compiler toolchains.

Highlights in this release:

Compilers: AOCC 4.0.0, GCC 12.3.0, Intel 2023.1, NVIDIA HPC SDK / NVHPC 23.7

Languages: Python 3.11.3, R 4.3.2, Julia 1.9.3, Go 1.20.4

Performance Engineering: Linaro-Forge 23.0.3 (replacing Arm-Forge), Scalasca 2.6.1, AMD-uPROF 4.1.424, Extrae 4.0.6, gperf 3.1, omnitrace 1.10.4

MPI, parallelization & acceleration: OpenMPI 4.1.5 (with UCC 1.2.0 and UCX 1.14.1), IntelMPI 2021.9.0, psmpi 5.9.2-1, CUDA 12.2.0 and 11.7.0, TBB 2021.10, PETSc 3.19.4, Kokkos 4.1.0, cuDNN 8.9.2.26, NCCL 2.18.3

Data science: JupyterHub 4.0.2, JupyterLab 4.0.5, jupyter-server 2.7.2, NVIDIA rapidsai suite 23.10

AI, Machine Learning, Deep Learning: PyTorch 1.13.1 (containerized version), TensorFlow 2.13.0, Keras 2.9, Horovod 0.26.0, Spark 3.3.0

Physics & chemistry: GROMACS 2023.3, NWChem 7.2.2, NAMD 3.0b5, QuantumESPRESSO 7.2, ORCA 5.0.4, DualSPHysics: 5.0.233, QUDA 1.1.0

CFD: OpenFOAM 10/v2306

Visualisation & computer vision: ParaView 5.11.2, VMD 1.9.4a57, OpenCV 4.8.1,

API interaction and data transfer: aws-cli 2.7.1, s3cmd 2.2.0, aria2 1.36.0

Quantum simulators: QSimCirq 0.17.0, cirq-core 1.2.0, NVIDIA cuQuantum suite

Container systems: Apptainer 1.2.4 (replacing Singularity)

- Compilers: AOCC 4.0.0, GCC 12.3.0, Intel 2023.1, NVIDIA HPC SDK / NVHPC 23.7

- Languages: Python 3.11.3, R 4.3.2, Julia 1.9.3, Go 1.20.4

- Performance Engineering: Linaro-Forge 23.0.3 (replacing Arm-Forge), Scalasca 2.6.1, AMD-uPROF 4.1.424, Extrae 4.0.6, gperf 3.1, omnitrace 1.10.4

- MPI, parallelization & acceleration: OpenMPI 4.1.5 (with UCC 1.2.0 and UCX 1.14.1), IntelMPI 2021.9.0, psmpi 5.9.2-1, CUDA 12.2.0 and 11.7.0, TBB 2021.10, PETSc 3.19.4, Kokkos 4.1.0, cuDNN 8.9.2.26, NCCL 2.18.3

- Data science: JupyterHub 4.0.2, JupyterLab 4.0.5, jupyter-server 2.7.2, NVIDIA rapidsai suite 23.10

- AI, Machine Learning, Deep Learning: PyTorch 1.13.1 (containerized version), TensorFlow 2.13.0, Keras 2.9, Horovod 0.26.0, Spark 3.3.0

- Physics & chemistry: GROMACS 2023.3, NWChem 7.2.2, NAMD 3.0b5, QuantumESPRESSO 7.2, ORCA 5.0.4, DualSPHysics: 5.0.233, QUDA 1.1.0

- CFD: OpenFOAM 10/v2306

- Visualisation & computer vision: ParaView 5.11.2, VMD 1.9.4a57, OpenCV 4.8.1,

- API interaction and data transfer: aws-cli 2.7.1, s3cmd 2.2.0, aria2 1.36.0

- Quantum simulators: QSimCirq 0.17.0, cirq-core 1.2.0, NVIDIA cuQuantum suite

- Container systems: Apptainer 1.2.4 (replacing Singularity)

#### NVIDIA NGC Containers

We are thrilled to announce that our latest software stack update features integration with containers from the NVIDIA NGC Catalog, providing users with enhanced capabilities and unparalleled performance.

Key Highlights:

NGC Container Integration: Leverage the power of NVIDIA optimized, pre-built containers for AI and HPC applications.

Easy Module Deployment: The stack is structured as a module, making it incredibly straightforward to deploy in your existing environment.

Boosted Performance: Experience significant performance improvements in your computational tasks, thanks to NVIDIA's state-of-the-art technology.

Wide Application Range: Ideal for AI, machine learning, deep learning, and high-performance computing tasks.

- NGC Container Integration: Leverage the power of NVIDIA optimized, pre-built containers for AI and HPC applications.

NGC Container Integration: Leverage the power of NVIDIA optimized, pre-built containers for AI and HPC applications.

- Easy Module Deployment: The stack is structured as a module, making it incredibly straightforward to deploy in your existing environment.

Easy Module Deployment: The stack is structured as a module, making it incredibly straightforward to deploy in your existing environment.

- Boosted Performance: Experience significant performance improvements in your computational tasks, thanks to NVIDIA's state-of-the-art technology.

Boosted Performance: Experience significant performance improvements in your computational tasks, thanks to NVIDIA's state-of-the-art technology.

- Wide Application Range: Ideal for AI, machine learning, deep learning, and high-performance computing tasks.

Wide Application Range: Ideal for AI, machine learning, deep learning, and high-performance computing tasks.

> **Info**

> Info

Info

The containers are available through the modules system, currently in the 2023.1 staging stack. Additional documentation on using containerized applications will follow in our dedicated section on using containers.

module load env/staging/2023.1

module use /apps/USE/containers/staging/2023.1/modules/all/

module avail

------------------------------------------- /apps/USE/containers/staging/2023.1/modules/all --------------------------------------------

CP2K/2023.1-CUDA-12.2.0-NGC-23.10               QMCPACK/v3.16.0-CUDA-12.2.0-NGC-23.10

GROMACS/2023.2-CUDA-12.2.0-NGC-23.10            QuantumESPRESSO/7.1-CUDA-12.2.0-NGC-23.10

LAMMPS/patch_15Jun2023-CUDA-12.2.0-NGC-23.10    TensorFlow/2.13.0-CUDA-12.2.0-NGC-23.10

PyTorch/2.1.0-CUDA-12.2.0-NGC-23.10

```

module load env/staging/2023.1

module use /apps/USE/containers/staging/2023.1/modules/all/

module avail

------------------------------------------- /apps/USE/containers/staging/2023.1/modules/all --------------------------------------------

CP2K/2023.1-CUDA-12.2.0-NGC-23.10               QMCPACK/v3.16.0-CUDA-12.2.0-NGC-23.10

GROMACS/2023.2-CUDA-12.2.0-NGC-23.10            QuantumESPRESSO/7.1-CUDA-12.2.0-NGC-23.10

LAMMPS/patch_15Jun2023-CUDA-12.2.0-NGC-23.10    TensorFlow/2.13.0-CUDA-12.2.0-NGC-23.10

PyTorch/2.1.0-CUDA-12.2.0-NGC-23.10

```

```

module load env/staging/2023.1

module use /apps/USE/containers/staging/2023.1/modules/all/

module avail

------------------------------------------- /apps/USE/containers/staging/2023.1/modules/all --------------------------------------------

CP2K/2023.1-CUDA-12.2.0-NGC-23.10               QMCPACK/v3.16.0-CUDA-12.2.0-NGC-23.10

GROMACS/2023.2-CUDA-12.2.0-NGC-23.10            QuantumESPRESSO/7.1-CUDA-12.2.0-NGC-23.10

LAMMPS/patch_15Jun2023-CUDA-12.2.0-NGC-23.10    TensorFlow/2.13.0-CUDA-12.2.0-NGC-23.10

PyTorch/2.1.0-CUDA-12.2.0-NGC-23.10

```

Support & Feedback:

Your feedback is crucial for our continuous improvement. If you encounter any issues or have suggestions, please contact our support team.

### 2023-01-15: 2022.1 software stack set as default

The 2022.1 software stack announced and installed on MeluXina in mid November 2022 is now the default stack in on the compute nodes. For details into the new tools available vs the previous release please see the notice below.

You can still use the previous production software stack by using module load env/release/2021.3 in your job scripts.

```

module load env/release/2021.3

```

> **Info**

> Info

Info

The myquota tool (v0.3.1) for monitoring the usage of your resource allocations is now available on compute nodes through the module system, and loaded by default.

```

myquota

```

### 2022-11-14: New 2022.1 software stack release

A new MeluXina User Software Environment release is now available: version 2022.1.

> **Info**

> Info

Info

Until 14 January 2023 try the new release by using module load env/release/2022.1 in your job scripts.

```

module load env/release/2022.1

```

> **Warn**

> Warn

Warn

The previous stable release 2021.3 is kept as default on MeluXina during a transition period until 14 January 2023. On 15 January, the 2022.1 release will become default in your jobs on MeluXina. To keep using the deprecated software stack, use module load env/release/2021.3. Please use the 2022.1 release in the transition period and let us know of your impressions and any problems by contacting our service desk. All staging software stacks will be cleaned and not be accessible from 15 January 2023.

```

module load env/release/2021.3

```

The new 2022.1 software stack release brings new versions of most tools, build on latest compiler toolchains.

Highlights in this release:

Compilers: AOCC 3.2, GCC 11.3, Intel 2022.1, NVIDIA HPC SDK / NVHPC 22.7

Languages: Python 3.10.4, R 4.2.1, Julia 1.8.2, Go 1.19.1

Performance Engineering: ARM Forge 22.0.4, Scalasca 2.6, AMD-uPROF 3.6.449

MPI, parallelization & acceleration: OpenMPI 4.1.4 (with hcoll 4.7.3202, xpmem 2.6.5-36 and knem 1.1.4), CUDA 11.7, TBB 2021.5, PETSc 3.18, Kokkos 3.6.01, cuDNN 8.4.1.50, NCCL 2.12.12

Data science: JupyterHub 2.3.1, JupyterLab 3.2.8

AI, Machine Learning, Deep Learning: PyTorch 1.12, TensorFlow 2.9.1, Keras 2.9, Horovod 0.26.0, Spark 3.3.0

Physics & chemistry: GROMACS 2022.3, NWChem 7.0.2, NAMD 2.14, LAMMPS 23Jun2022, QuantumESPRESSO 7.1, ORCA 5.0.3, DualSPHysics: 5.0.175, QUDA 1.1.0

CFD: OpenFOAM 9/v2206

Visualisation & computer vision: ParaView 5.10.1, VMD 1.9.4a57, OpenCV 4.6

API interaction and data transfer: aws-cli 2.7.1, s3cmd, aria2 1.36.0

Quantum simulators: QSimCirq 0.14.0

Container systems: Singularity-CE 3.10.2

- Compilers: AOCC 3.2, GCC 11.3, Intel 2022.1, NVIDIA HPC SDK / NVHPC 22.7

- Languages: Python 3.10.4, R 4.2.1, Julia 1.8.2, Go 1.19.1

- Performance Engineering: ARM Forge 22.0.4, Scalasca 2.6, AMD-uPROF 3.6.449

- MPI, parallelization & acceleration: OpenMPI 4.1.4 (with hcoll 4.7.3202, xpmem 2.6.5-36 and knem 1.1.4), CUDA 11.7, TBB 2021.5, PETSc 3.18, Kokkos 3.6.01, cuDNN 8.4.1.50, NCCL 2.12.12

- Data science: JupyterHub 2.3.1, JupyterLab 3.2.8

- AI, Machine Learning, Deep Learning: PyTorch 1.12, TensorFlow 2.9.1, Keras 2.9, Horovod 0.26.0, Spark 3.3.0

- Physics & chemistry: GROMACS 2022.3, NWChem 7.0.2, NAMD 2.14, LAMMPS 23Jun2022, QuantumESPRESSO 7.1, ORCA 5.0.3, DualSPHysics: 5.0.175, QUDA 1.1.0

- CFD: OpenFOAM 9/v2206

- Visualisation & computer vision: ParaView 5.10.1, VMD 1.9.4a57, OpenCV 4.6

- API interaction and data transfer: aws-cli 2.7.1, s3cmd, aria2 1.36.0

- Quantum simulators: QSimCirq 0.14.0

- Container systems: Singularity-CE 3.10.2