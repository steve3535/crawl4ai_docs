# Introduction to containers

Source: https://docs.lxp.lu/containerization/introduction/

# Introduction to containers

Containers provide a way to package up applications, libraries, scripts, configurations and data in a way that enables applications or even complex workflows to run consistently on a laptop as well as on a supercomputer.

A container encapsulates an entire runtime environment that can be transferred, shared and deployed rapidly while being lighter on host system resources than a full virtual machine environment.

## Container systems

Multiple container systems exist, oriented to:

Enterprise: Docker, Podman

HPC: Singularity/Apptainer, Shifter, Sarus, Enroot

- Enterprise: Docker, Podman

- HPC: Singularity/Apptainer, Shifter, Sarus, Enroot

On MeluXina the Apptainer container system is provided to support containerized workloads.

Highlighted features of Apptainer:

Simplifies the creation and execution of containers, ensuring software components are encapsulated for portability and reproducibility.

Easy execution of parallel (MPI) containerized applications

Support for GPU accelerated applications

Support for creating and running encrypted containers

Support for trusted containers that are PGP-signed and verified

Support for using Docker containers and downloading them from public or private registries

Support for Open Containers Initiative (OCI) containers

- Simplifies the creation and execution of containers, ensuring software components are encapsulated for portability and reproducibility.

- Easy execution of parallel (MPI) containerized applications

- Support for GPU accelerated applications

- Support for creating and running encrypted containers

- Support for trusted containers that are PGP-signed and verified

- Support for using Docker containers and downloading them from public or private registries

- Support for Open Containers Initiative (OCI) containers

For a complete list of features, check out the Apptainer documentation.

## Apptainer/Singularity

Users of the Apptainer/Singularity container system can develop their own as well as run pre-existing containers.

The build stage requires administrative (root/sudo) privileges, and thus has to be performed on a system under user's control (laptop, workstation, server ...).

```

sudo

```

Once a container has been created, or an existing one selected from a container registry (such as Docker Hub, the Nvidia Cloud (NGC), or a private one), it can be run on one of the MeluXina computational modules.

Examples of using Apptainer on MeluXina are provided in the dedicated section.