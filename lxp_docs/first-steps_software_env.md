# Software environment

Source: https://docs.lxp.lu/first-steps/software_env/

# Software environment

A rich user software environment is available on MeluXina and can be used through environment modules.

It comprises:

tools for HPC, HPDA and AI application development

compilers & programming languages

common use libraries for math & data

tools for performance engineering

scientific computing applications, libraries and frameworks

general-purpose HPC, HPDA or AI

or domain-specific

- tools for HPC, HPDA and AI application development

compilers & programming languages

common use libraries for math & data

tools for performance engineering

tools for HPC, HPDA and AI application development

compilers & programming languages

common use libraries for math & data

tools for performance engineering

- compilers & programming languages

- common use libraries for math & data

- tools for performance engineering

- scientific computing applications, libraries and frameworks

general-purpose HPC, HPDA or AI

or domain-specific

scientific computing applications, libraries and frameworks

general-purpose HPC, HPDA or AI

or domain-specific

- general-purpose HPC, HPDA or AI

- or domain-specific

## The MeluXina User Software Environment (MUSE)

The EasyBuild system is used on MeluXina to deploy software stacks,

with applications and libraries provided in several revisions: compiled with different compilers, MPI suites,

accelerated and non-accelerated versions. EasyBuild automatically generated software modules that enables

the use of the different application revisions, and dependencies on particular support libraries.

The naming scheme used for the modules follows the application/version schema, e.g. NAMD/2.14-foss-2022a-ucx-CUDA-11.7.0

which shows that the NAMD application is available in version 2.14 built with the foss toolchain in

the 2022a release, and with CUDA support.

```

NAMD/2.14-foss-2022a-ucx-CUDA-11.7.0

```

For a deeper overview on versioning and toolchains see the EasyBuild documentation

specific to Common toolchains and

Available toolchains.

Terminology : A software stack that is also sometimes called stack for short refers to a collection of software packages and their dependencies that are built and configured using a specific EasyBuild toolchain.

We release a new software stack at least once a year. The software stacks can be either: Production (current), Staging (preproduction envioronment for testing purposes), Maintained (previous, not updated with new tools/versions) or Retired (not maintained and should not be used any more).

> **Using different MUSE releases**

> Using different MUSE releases

Using different MUSE releases

To load modules from a software release other than the default Production stack, you can:

Use the dedicated software environment modules in the 'env/' branch, e.g. module load env/staging/2022.1

Or directly configure LMod to use the appropriate modules path, e.g.:

module use /apps/USE/easybuild/staging/2022.1/modules/all/

- Use the dedicated software environment modules in the 'env/' branch, e.g. module load env/staging/2022.1

```

module load env/staging/2022.1

```

- Or directly configure LMod to use the appropriate modules path, e.g.:

module use /apps/USE/easybuild/staging/2022.1/modules/all/

```

module use /apps/USE/easybuild/staging/2022.1/modules/all/

```

The following table lists highlighted HPC applications, libraries and support tools available in the available releases of the MeluXina User Software Environment.

### The 2024 production stack

The table below summarizes the software version changes between the 2023.1 release and the 2024.1 release stacks. If you choose to use this new stack, remember to update the software versions in your bash script for launching a SLURM job, as outlined in the table.

Additionally, note that new software has been added to the stack alongside the version changes. These additions are summarized below.

### The 2024 staging stack

The table below lists the software included in the 2024 staging stack, along with their respective versions and the toolchain versions used for their build.

### The current default stack - 2023.1

### The 2023 staging stack

### Requesting new software and features

You may request the installation of new applications or features through the servicedesk.lxp.lu.

Depending on a project's requirements, new software may be installed in the corresponding project directory or in the global software stack.

All new tools are first deployed in the Staging area for testing.

## Environment modules

The environment modules system simplifies the use of applications and supporting libraries that may come in different versions and revisions. The software modules provide a way to easily

switch between e.g. multiple revisions of the same application, where one revision

may provide a set of functionality not available in another revision.

The core command by which software modules can be listed, loaded (activated),

and unloaded (deactivated) is module, followed by an appropriate command.

```

module

```

The modules work by setting specific environment variables needed for the

respective software program when the software module corresponding to the

application is loaded. Often, this is simply adding the program to the $PATH

variable, but software containing libraries and headers will also set $LD_LIBRARY_PATH.

Any other variable that the software may need can be set and so the contents of the

modules can be fairly simple or complex.

```

$PATH

```

```

$LD_LIBRARY_PATH

```

There are several advantages to using software modules to set up your environment,

especially on a supercomputer:

ease of use

ability to revert to your previous environment

ability to easily switch your environment to try different versions of a program

e.g. when single and double-precision versions of the program exist

e.g. when a program has been compiled with different features that cannot coexist in a single build of the program

e.g. when a program has been compiled with different compilers or MPI suites

- ease of use

- ability to revert to your previous environment

- ability to easily switch your environment to try different versions of a program

e.g. when single and double-precision versions of the program exist

e.g. when a program has been compiled with different features that cannot coexist in a single build of the program

e.g. when a program has been compiled with different compilers or MPI suites

e.g. when single and double-precision versions of the program exist

e.g. when a program has been compiled with different features that cannot coexist in a single build of the program

e.g. when a program has been compiled with different compilers or MPI suites

- e.g. when single and double-precision versions of the program exist

- e.g. when a program has been compiled with different features that cannot coexist in a single build of the program

- e.g. when a program has been compiled with different compilers or MPI suites

> **Using modules**

> Using modules

Using modules

The module command is only available on compute nodes and not on the login nodes.

The applications provided through the software modules system must be used only on compute nodes.

```

module

```

MeluXina uses the Lmod software modules system,

the table below summarizes the most common module commands:

```

module

```

### Using environment modules

Finding applications: module avail

- Finding applications: module avail

To lists all available (loadable) modules and module groups. With the information of these two commands:

module avail

```

module avail

```

```

module avail

```

Listing loaded application profiles: module list

- Listing loaded application profiles: module list

To get a list of all currently loaded modules:

module list

```

module list

```

```

module list

```

Loading or unloading application profiles: module load/unload

- Loading or unloading application profiles: module load/unload

To load a specific module

module load <module_name>

```

module load <module_name>

```

```

module load <module_name>

```

> **Default version**

> Default version

Default version

In case of multiple software versions, one version will always be defined as the default version, and can be identified by its (D) mark in the module avail output.

When loading a software module, if the version is not specified, the default is loaded (e.g. module load FFTW will activate FFTW/3.3.8-gompic-2020b if this is the default).

Fully specifying the software module (name+version) should always be preferred to ensure that the correct version is being activated.

```

module avail

```

```

module load FFTW

```

```

FFTW/3.3.8-gompic-2020b

```

Unloading an environment module will undo the changes that module made to the environment,

restoring any variables set to their previous values. To unload a specific module you can

use the following:

module unload <module_name>

```

module unload <module_name>

```

```

module unload <module_name>

```

Unloading all profiles: module purge

- Unloading all profiles: module purge

module purge

```

module purge

```

```

module purge

```

Switching profiles: module switch

- Switching profiles: module switch

To swap a specific module for another one (especially useful to switch between different

versions of the same program) use the following:

module switch <old_module_name> <new_module_name>

```

module switch <old_module_name> <new_module_name>

```

```

module switch <old_module_name> <new_module_name>

```

### NVIDIA GPU Containers (NGC) modules

Our software suite has been enhanced to include Nvidia GPU Containers (NGC). This integration brings a significant upgrade to our capabilities, offering advanced GPU-accelerated applications and tools designed by Nvidia. With NGC, users will have access to a comprehensive catalog of GPU-optimized software for deep learning, machine learning, and high-performance computing (HPC) applications. This addition is part of our commitment to providing the most advanced and efficient tools to our users, ensuring they have access to cutting-edge technology for their computational needs.

Please see here for more on NGC modules.

## MPI runtimes

MeluXina User Software Envronment (MUSE) main MPI runtime is the widely used OpenMPI  which is capable of handling direct communication with GPU memory, making it CUDA-aware by default. MUSE also offers two more MPI runtimes: ParaStationMPI (which is also CUDA-aware) and IntelMPI.

The OpenMPI runtime automatically load a new standard module, referred to as ompi-configs, designed to configure the system suitably for the majority of users. The MeluXina User Software Envronment (MUSE) provides various versions of these configuration modules tailored to different scenarios. It’s important to note that the available MPI runtimes are highly adaptable, and the modules provided in MUSE represent just a selection of the possible configurations. It may be beneficial to experiment with the different possibilities in order to find the most suitable configuration for your application/run. The different provided configuration modules should give at least acceptable if not optimal configuration for all users cases.

These module configs use UCX and UCC to configure the OpenMPI runtime (They will be extended to ParaSatationMPI and IntelMPI runtimes in a near future).

UCX (Unified Communication X) and UCC (Unified Collective Communication) are frameworks designed to enhance the performance and scalability of applications running on high-performance computing (HPC) and cloud infrastructures. UCX provides an optimized communication layer that facilitates efficient data transfer between devices in a network, supporting a variety of high-speed networking technologies like InfiniBand, RoCE, and more. It's particularly known for its use in facilitating efficient message passing and remote memory access, essential for modern computing applications. On the other hand, UCC focuses specifically on collective communication operations such as broadcasts, reductions and all to all which are common in parallel computing frameworks. UCC works to streamline and optimize these operations across different hardware and network configurations, aiming to improve overall computational efficiency and performance in large-scale environments. Together, UCX and UCC provide a comprehensive suite of tools that address the communication needs of advanced computing systems, supporting a wide range of HPC applications and frameworks.

The following ompi_configs modules are available on MUSE:

ompi-configs/ucx: This is the default ompi_configs module for CPU and largemem nodes which is set up to take advantage of UCX as the primary communication library. Additional configuration options are accessible via ompi_info -a.

ompi-configs/ucx-cuda: Similar to the  ompi-configs/ucx module, this version establish the activation of CUDA transports within the UCX module, thus facilitating CUDA-aware operations. It is provided as the standard ompi_configs module GPU nodes.

ompi-configs/ucx-ucc: This configuration mirrors the ompi-configs/ucx module but defaults and prioritizes to using UCC for collective communication.

ompi-configs/ucx-cuda-ucc: This configuration mirrors the ompi-configs/ucx-cuda and integrates UCC as the default framwork for collective communication.

- ompi-configs/ucx: This is the default ompi_configs module for CPU and largemem nodes which is set up to take advantage of UCX as the primary communication library. Additional configuration options are accessible via ompi_info -a.

ompi-configs/ucx: This is the default ompi_configs module for CPU and largemem nodes which is set up to take advantage of UCX as the primary communication library. Additional configuration options are accessible via ompi_info -a.

```

ompi_info -a

```

- ompi-configs/ucx-cuda: Similar to the  ompi-configs/ucx module, this version establish the activation of CUDA transports within the UCX module, thus facilitating CUDA-aware operations. It is provided as the standard ompi_configs module GPU nodes.

ompi-configs/ucx-cuda: Similar to the  ompi-configs/ucx module, this version establish the activation of CUDA transports within the UCX module, thus facilitating CUDA-aware operations. It is provided as the standard ompi_configs module GPU nodes.

- ompi-configs/ucx-ucc: This configuration mirrors the ompi-configs/ucx module but defaults and prioritizes to using UCC for collective communication.

ompi-configs/ucx-ucc: This configuration mirrors the ompi-configs/ucx module but defaults and prioritizes to using UCC for collective communication.

- ompi-configs/ucx-cuda-ucc: This configuration mirrors the ompi-configs/ucx-cuda and integrates UCC as the default framwork for collective communication.

ompi-configs/ucx-cuda-ucc: This configuration mirrors the ompi-configs/ucx-cuda and integrates UCC as the default framwork for collective communication.

In the context of UCX, a transport refers to the underlying communication technology used for data transfer between nodes in a network. UCX supports various types of transports, each designed to optimize communications under different network configurations and hardware. These transports handle the actual movement of data across the network, and they can be tailored for specific types of hardware interfaces and communication protocols, such as InfiniBand, RDMA (Remote Direct Memory Access), shared memory, TCP/IP, and more.

The choice of transport affects performance characteristics such as latency, bandwidth, and scalability. We, therefore, also provides modules for pre-configuring UCX transport selection:

ucx-configs/ud exclusively activates the Unreliable Datagram (UD) transport, which is also known for its lower memory usage and suitability for small and medium-sized simulations. Due to problems on MeluXina with RC transport, UD remains the preferred transport for general use, even on large scall simulations.

ucx-configs/ud-cuda activates both the Unreliable Datagram (UD) and CUDA transports. UD is known for its smaller memory requirement compared to RC and is preferred for all general GPU simulations.

ucx-configs/dc turns on the Dynamically Connected (DC) transport, which is the Nvidia/Mellanox scalable offloaded dynamic connection transport. Although DC is characterized by a low memory footprint, making it potentially suitable for large-scale simulations, it has proved to be a much slower transport than UD for medium and large scale simulations.

ucx-configs/dc-cuda includes both the Dynamically Connected (DC) transport and CUDA. It is known for its low memory usage and is potentially suitable for very large GPU simulations.

ucx-configs/rc configures the system for the Reliable Connected (RC) transport alone. It has many known issues on our system and we don't advise using it for now.

ucx-configs/rc-cuda configures the system to utilize both the Reliable Connected (RC) and CUDA transports. It has many known issues on our system and we don't advise using it for now.

ucx-configs/plain removes any specific transport restrictions, allowing UCX to freely select the most appropriate transport based on its internal heuristics. This setting is similar to not using any ucx-configs module, giving full control back to UCX’s default decision-making processes.

- ucx-configs/ud exclusively activates the Unreliable Datagram (UD) transport, which is also known for its lower memory usage and suitability for small and medium-sized simulations. Due to problems on MeluXina with RC transport, UD remains the preferred transport for general use, even on large scall simulations.

ucx-configs/ud exclusively activates the Unreliable Datagram (UD) transport, which is also known for its lower memory usage and suitability for small and medium-sized simulations. Due to problems on MeluXina with RC transport, UD remains the preferred transport for general use, even on large scall simulations.

- ucx-configs/ud-cuda activates both the Unreliable Datagram (UD) and CUDA transports. UD is known for its smaller memory requirement compared to RC and is preferred for all general GPU simulations.

ucx-configs/ud-cuda activates both the Unreliable Datagram (UD) and CUDA transports. UD is known for its smaller memory requirement compared to RC and is preferred for all general GPU simulations.

- ucx-configs/dc turns on the Dynamically Connected (DC) transport, which is the Nvidia/Mellanox scalable offloaded dynamic connection transport. Although DC is characterized by a low memory footprint, making it potentially suitable for large-scale simulations, it has proved to be a much slower transport than UD for medium and large scale simulations.

ucx-configs/dc turns on the Dynamically Connected (DC) transport, which is the Nvidia/Mellanox scalable offloaded dynamic connection transport. Although DC is characterized by a low memory footprint, making it potentially suitable for large-scale simulations, it has proved to be a much slower transport than UD for medium and large scale simulations.

- ucx-configs/dc-cuda includes both the Dynamically Connected (DC) transport and CUDA. It is known for its low memory usage and is potentially suitable for very large GPU simulations.

ucx-configs/dc-cuda includes both the Dynamically Connected (DC) transport and CUDA. It is known for its low memory usage and is potentially suitable for very large GPU simulations.

- ucx-configs/rc configures the system for the Reliable Connected (RC) transport alone. It has many known issues on our system and we don't advise using it for now.

ucx-configs/rc configures the system for the Reliable Connected (RC) transport alone. It has many known issues on our system and we don't advise using it for now.

- ucx-configs/rc-cuda configures the system to utilize both the Reliable Connected (RC) and CUDA transports. It has many known issues on our system and we don't advise using it for now.

ucx-configs/rc-cuda configures the system to utilize both the Reliable Connected (RC) and CUDA transports. It has many known issues on our system and we don't advise using it for now.

- ucx-configs/plain removes any specific transport restrictions, allowing UCX to freely select the most appropriate transport based on its internal heuristics. This setting is similar to not using any ucx-configs module, giving full control back to UCX’s default decision-making processes.

ucx-configs/plain removes any specific transport restrictions, allowing UCX to freely select the most appropriate transport based on its internal heuristics. This setting is similar to not using any ucx-configs module, giving full control back to UCX’s default decision-making processes.