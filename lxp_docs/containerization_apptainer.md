# Apptainer

Source: https://docs.lxp.lu/containerization/apptainer/

# Apptainer

The Apptainer container system (v1.2.4 or newer) is available on MeluXina, and is provided as a module that can be loaded on compute nodes:

module load Apptainer/1.2.4-GCCcore-12.3.0

apptainer --help

```

module load Apptainer/1.2.4-GCCcore-12.3.0

apptainer --help

```

```

module load Apptainer/1.2.4-GCCcore-12.3.0

apptainer --help

```

> **Important**

> Important

Important

Once built, container images are immutable (see apptainer help build).

By default, containers have access only to the user home directory. If any data is required from project or project-scratch directories, the relevant paths must be explicitly bind-mounted into the container.

See apptainer help run for the --bind option

Also the upstream documentation on bind paths and mounts

When running GPU-enabled applications on MeluXina GPU nodes, containers must be run using the --nv flag that enables NVIDIA support within the container.

See also the upstream documentation on NVIDIA GPUs support

MPI-enabled applications that are containerized can be run provided that a compatible MPI implementation is used in the outer (MeluXina) software stack and in the inner (container-based) application environment.

See the upstream documentation on MPI support

On MeluXina, the Slurm srun parallel launcher should be used e.g. to launch containerized applications linked to OpenMPI

For improved security we are using Apptainer in non-privileged mode.

- Once built, container images are immutable (see apptainer help build).

```

apptainer help build

```

- By default, containers have access only to the user home directory. If any data is required from project or project-scratch directories, the relevant paths must be explicitly bind-mounted into the container.

See apptainer help run for the --bind option

Also the upstream documentation on bind paths and mounts

See apptainer help run for the --bind option

Also the upstream documentation on bind paths and mounts

- See apptainer help run for the --bind option

```

apptainer help run

```

```

--bind

```

- Also the upstream documentation on bind paths and mounts

- When running GPU-enabled applications on MeluXina GPU nodes, containers must be run using the --nv flag that enables NVIDIA support within the container.

See also the upstream documentation on NVIDIA GPUs support

```

--nv

```

See also the upstream documentation on NVIDIA GPUs support

- See also the upstream documentation on NVIDIA GPUs support

- MPI-enabled applications that are containerized can be run provided that a compatible MPI implementation is used in the outer (MeluXina) software stack and in the inner (container-based) application environment.

See the upstream documentation on MPI support

On MeluXina, the Slurm srun parallel launcher should be used e.g. to launch containerized applications linked to OpenMPI

See the upstream documentation on MPI support

On MeluXina, the Slurm srun parallel launcher should be used e.g. to launch containerized applications linked to OpenMPI

- See the upstream documentation on MPI support

- On MeluXina, the Slurm srun parallel launcher should be used e.g. to launch containerized applications linked to OpenMPI

```

srun

```

- For improved security we are using Apptainer in non-privileged mode.

## Running existing containers

### Apptainer Hub containers

As a first test, we will download a pre-existing "Hello World" container from the Apptainer Hub registry and run it:

(compute)$ apptainer pull shub://vsoch/hello-world

INFO:    Downloading shub image

59.8MiB / 59.8MiB [=============================================================================================================================================] 100 %

(compute)$ apptainer run hello-world_latest.sif

RaawwWWWWWRRRR!! Avocado!

```

(compute)$ apptainer pull shub://vsoch/hello-world

INFO:    Downloading shub image

59.8MiB / 59.8MiB [=============================================================================================================================================] 100 %

(compute)$ apptainer run hello-world_latest.sif

RaawwWWWWWRRRR!! Avocado!

```

```

(compute)$ apptainer pull shub://vsoch/hello-world

INFO:    Downloading shub image

59.8MiB / 59.8MiB [=============================================================================================================================================] 100 %

(compute)$ apptainer run hello-world_latest.sif

RaawwWWWWWRRRR!! Avocado!

```

We can see that the container was downloaded as a Apptainer Image File, and we can run the embedded command that prints a simple message.

If a container has multiple applications inside, you can specify the command to run inside the container with apptainer run <container> <command>.

```

apptainer run <container> <command>

```

### Docker Hub containers

For a second example, we will take a reference Docker container from the Docker Hub which contains Python and run the embedded Python:

(compute)$ apptainer pull docker://python:3.9.7-slim-bullseye

(compute)$ apptainer run python_3.9.7-slim-bullseye.sif

Python 3.9.7 (default, Sep 28 2021, 18:41:28)

[GCC 10.2.1 20210110] on linux

Type "help", "copyright", "credits" or "license" for more information.

```

(compute)$ apptainer pull docker://python:3.9.7-slim-bullseye

(compute)$ apptainer run python_3.9.7-slim-bullseye.sif

Python 3.9.7 (default, Sep 28 2021, 18:41:28)

[GCC 10.2.1 20210110] on linux

Type "help", "copyright", "credits" or "license" for more information.

```

```

(compute)$ apptainer pull docker://python:3.9.7-slim-bullseye

(compute)$ apptainer run python_3.9.7-slim-bullseye.sif

Python 3.9.7 (default, Sep 28 2021, 18:41:28)

[GCC 10.2.1 20210110] on linux

Type "help", "copyright", "credits" or "license" for more information.

```

### GPU-enabled containers

Example of a GPU-enabled application that is being downloaded to a Project directory and ran on a MeluXina GPU node:

(login)$ salloc -A ACCOUNT -t 01:00:00 -p gpu -q short -N 1 -G 4

(compute)$ cd /project/home/lxp/test

(compute)$ module load Apptainer/1.2.4-GCCcore-12.3.0

(compute)$ apptainer pull docker://tensorflow/tensorflow:latest-gpu

(compute)$ echo -e "import tensorflow as tf\nprint(tf.config.list_physical_devices('GPU'))" > list_gpus_visible_by_tensorflow.py

(compute)$ cat list_gpus_visible_by_tensorflow.py

import tensorflow as tf

print(tf.config.list_physical_devices('GPU'))

(compute)$ apptainer run --nv --bind /project/home/lxp/test:/project/home/lxp/test tensorflow_latest-gpu.sif python3 list_gpus_visible_by_tensorflow.py

[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU'), PhysicalDevice(name='/physical_device:GPU:1', device_type='GPU'), PhysicalDevice(name='/physical_device:GPU:2', device_type='GPU'), PhysicalDevice(name='/physical_device:GPU:3', device_type='GPU')]

```

(login)$ salloc -A ACCOUNT -t 01:00:00 -p gpu -q short -N 1 -G 4

(compute)$ cd /project/home/lxp/test

(compute)$ module load Apptainer/1.2.4-GCCcore-12.3.0

(compute)$ apptainer pull docker://tensorflow/tensorflow:latest-gpu

(compute)$ echo -e "import tensorflow as tf\nprint(tf.config.list_physical_devices('GPU'))" > list_gpus_visible_by_tensorflow.py

(compute)$ cat list_gpus_visible_by_tensorflow.py

import tensorflow as tf

print(tf.config.list_physical_devices('GPU'))

(compute)$ apptainer run --nv --bind /project/home/lxp/test:/project/home/lxp/test tensorflow_latest-gpu.sif python3 list_gpus_visible_by_tensorflow.py

[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU'), PhysicalDevice(name='/physical_device:GPU:1', device_type='GPU'), PhysicalDevice(name='/physical_device:GPU:2', device_type='GPU'), PhysicalDevice(name='/physical_device:GPU:3', device_type='GPU')]

```

```

(login)$ salloc -A ACCOUNT -t 01:00:00 -p gpu -q short -N 1 -G 4

(compute)$ cd /project/home/lxp/test

(compute)$ module load Apptainer/1.2.4-GCCcore-12.3.0

(compute)$ apptainer pull docker://tensorflow/tensorflow:latest-gpu

(compute)$ echo -e "import tensorflow as tf\nprint(tf.config.list_physical_devices('GPU'))" > list_gpus_visible_by_tensorflow.py

(compute)$ cat list_gpus_visible_by_tensorflow.py

import tensorflow as tf

print(tf.config.list_physical_devices('GPU'))

(compute)$ apptainer run --nv --bind /project/home/lxp/test:/project/home/lxp/test tensorflow_latest-gpu.sif python3 list_gpus_visible_by_tensorflow.py

[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU'), PhysicalDevice(name='/physical_device:GPU:1', device_type='GPU'), PhysicalDevice(name='/physical_device:GPU:2', device_type='GPU'), PhysicalDevice(name='/physical_device:GPU:3', device_type='GPU')]

```

Important elements above are the use of the --nv option to enable the container to use NVIDIA GPUs, and the use of --bind to enable the container to have access to a specific project folder (with the same location as on the MeluXina filesystem, such that any scripts referencing the path can be used without modification).

```

--nv

```

```

--bind

```

### MPI-enabled containers

Example of running an MPI-enabled containerized application**:

(login)$ salloc -A ACCOUNT -t 1:00:00 -p cpu -q short -N 2 --ntasks-per-node=4

salloc: Nodes mel0*** are ready for job

(compute)$ module load Apptainer/1.2.4-GCCcore-12.3.0

(compute)$ module load OpenMPI/4.1.5-GCC-12.3.0

(compute)$ srun mpi-test-container.sif mpicode

```

(login)$ salloc -A ACCOUNT -t 1:00:00 -p cpu -q short -N 2 --ntasks-per-node=4

salloc: Nodes mel0*** are ready for job

(compute)$ module load Apptainer/1.2.4-GCCcore-12.3.0

(compute)$ module load OpenMPI/4.1.5-GCC-12.3.0

(compute)$ srun mpi-test-container.sif mpicode

```

```

(login)$ salloc -A ACCOUNT -t 1:00:00 -p cpu -q short -N 2 --ntasks-per-node=4

salloc: Nodes mel0*** are ready for job

(compute)$ module load Apptainer/1.2.4-GCCcore-12.3.0

(compute)$ module load OpenMPI/4.1.5-GCC-12.3.0

(compute)$ srun mpi-test-container.sif mpicode

```

Here, the mpicode application is run from inside the container, using the OpenMPI library from the MeluXina User Software Environment. The mpicode application must have been compiled using a compatible MPI library for the above to work.

See the following section for an example of creating a container with MPI support.

```

mpicode

```

```

mpicode

```

### Accessing data directories

To give a container access to your data hosted in a project directory (under Tier1/scratch and/or Tier2/Project home) you will need to ensure

that the filesystem paths on the compute nodes are bind-mounted within the container, either through the APPTAINER_BINDPATH environment variable

or through the command line option --bind, which allow comma separated src[:dest[:opts]] tuples.

```

APPTAINER_BINDPATH

```

```

--bind

```

```

src[:dest[:opts]]

```

Example of enabling a container to use a project's home directory (e.g. /project/home/p299999):

```

/project/home/p299999

```

(login)$ salloc -A ACCOUNT -t 01:00:00 -p cpu -q short -N 1 -n 1

(compute)$ module load Apptainer/1.2.4-GCCcore-12.3.0

(compute)$ apptainer exec --bind "/mnt/tier2,/project/home/p2999999/" my_container.sif my_code

```

(login)$ salloc -A ACCOUNT -t 01:00:00 -p cpu -q short -N 1 -n 1

(compute)$ module load Apptainer/1.2.4-GCCcore-12.3.0

(compute)$ apptainer exec --bind "/mnt/tier2,/project/home/p2999999/" my_container.sif my_code

```

```

(login)$ salloc -A ACCOUNT -t 01:00:00 -p cpu -q short -N 1 -n 1

(compute)$ module load Apptainer/1.2.4-GCCcore-12.3.0

(compute)$ apptainer exec --bind "/mnt/tier2,/project/home/p2999999/" my_container.sif my_code

```

Example of enabling a container to use both the project home and scratch directories (e.g. /project/{home,scratch}/p299999):

```

/project/{home,scratch}/p299999

```

(login)$ salloc -A ACCOUNT -t 01:00:00 -p cpu -q short -N 1 -n 1

(compute)$ module load Apptainer/1.2.4-GCCcore-12.3.0

(compute)$ export SINGULARITY_BINDPATH="/mnt/tier1,/project/scratch/p299999,/mnt/tier2,/project/home/p299999"

(compute)$ apptainer exec my_container.sif my_code

```

(login)$ salloc -A ACCOUNT -t 01:00:00 -p cpu -q short -N 1 -n 1

(compute)$ module load Apptainer/1.2.4-GCCcore-12.3.0

(compute)$ export SINGULARITY_BINDPATH="/mnt/tier1,/project/scratch/p299999,/mnt/tier2,/project/home/p299999"

(compute)$ apptainer exec my_container.sif my_code

```

```

(login)$ salloc -A ACCOUNT -t 01:00:00 -p cpu -q short -N 1 -n 1

(compute)$ module load Apptainer/1.2.4-GCCcore-12.3.0

(compute)$ export SINGULARITY_BINDPATH="/mnt/tier1,/project/scratch/p299999,/mnt/tier2,/project/home/p299999"

(compute)$ apptainer exec my_container.sif my_code

```

## Building Apptainer images

There are two main approaches to building Apptainer images:

Sandbox: you can build a container interactively within a sandbox environment (filesystem chroot), using a pre-existing image as base. This requires:

an existing container, e.g. downloaded from a registry: apptainer build --sandbox my_container docker://ubuntu:latest

running a shell within and installing/configuring manually the packages and code inside, e.g. apptainer shell --writable my_container

for 'production' use, the container should then be converted to an image file, e.g. apptainer build my_ubuntu_container.sif my_container

From a Apptainer Definition File: this is Apptainer’s equivalent to building a Docker container from a Dockerfile, see examples below.

- Sandbox: you can build a container interactively within a sandbox environment (filesystem chroot), using a pre-existing image as base. This requires:

an existing container, e.g. downloaded from a registry: apptainer build --sandbox my_container docker://ubuntu:latest

running a shell within and installing/configuring manually the packages and code inside, e.g. apptainer shell --writable my_container

for 'production' use, the container should then be converted to an image file, e.g. apptainer build my_ubuntu_container.sif my_container

Sandbox: you can build a container interactively within a sandbox environment (filesystem chroot), using a pre-existing image as base. This requires:

an existing container, e.g. downloaded from a registry: apptainer build --sandbox my_container docker://ubuntu:latest

running a shell within and installing/configuring manually the packages and code inside, e.g. apptainer shell --writable my_container

for 'production' use, the container should then be converted to an image file, e.g. apptainer build my_ubuntu_container.sif my_container

- an existing container, e.g. downloaded from a registry: apptainer build --sandbox my_container docker://ubuntu:latest

```

apptainer build --sandbox my_container docker://ubuntu:latest

```

- running a shell within and installing/configuring manually the packages and code inside, e.g. apptainer shell --writable my_container

```

apptainer shell --writable my_container

```

- for 'production' use, the container should then be converted to an image file, e.g. apptainer build my_ubuntu_container.sif my_container

```

apptainer build my_ubuntu_container.sif my_container

```

- From a Apptainer Definition File: this is Apptainer’s equivalent to building a Docker container from a Dockerfile, see examples below.

From a Apptainer Definition File: this is Apptainer’s equivalent to building a Docker container from a Dockerfile, see examples below.

### Creating a simple Apptainer Definition File

A Apptainer Definition File is a text file that contains a series of statements and instructions for building the container image, as shown below:

Bootstrap: docker

From: ubuntu:20.04

%post

apt-get -y update && apt-get install -y python

%runscript

python -c 'print("Hello World! Hello from our custom Apptainer image!")'

```

Bootstrap: docker

From: ubuntu:20.04

%post

apt-get -y update && apt-get install -y python

%runscript

python -c 'print("Hello World! Hello from our custom Apptainer image!")'

```

```

Bootstrap: docker

From: ubuntu:20.04

%post

apt-get -y update && apt-get install -y python

%runscript

python -c 'print("Hello World! Hello from our custom Apptainer image!")'

```

The first two lines define a pre-existing container to use as base image that can then be customized.

The Bootstrap: docker instruction is similar to prefixing an image path with docker:// when using the apptainer pull command.

A range of different bootstrap options are supported, From: ubuntu:20.04 defines that we will use an Ubuntu 20.04 base.

```

Bootstrap: docker

```

```

docker://

```

```

apptainer pull

```

```

From: ubuntu:20.04

```

Next we have the %post section of the definition file, defining commands to be run within the image to customize it:

```

%post

```

%post

apt-get -y update && apt-get install -y python

```

%post

apt-get -y update && apt-get install -y python

```

```

%post

apt-get -y update && apt-get install -y python

```

This section serves to provide shell commands performing a variety of tasks such as package installation, pulling data files from remote locations and setting local configurations within the image.

In our example, we use the Ubuntu package manager to install python.

The %runscript section is used to define a script to be executed when the container is run with apptainer run without any additional command.

```

%runscript

```

```

apptainer run

```

### Creating an MPI-enabled container

The following example shows how to build a container that includes libraries compatible with the software environment available on MeluXina (as of December 2023).

The example mpi-test-container.def definition file provides for a container with a Rocky Linux 8.8 base, with OpenMPI and the PMIx interface, Mellanox InfiniBand support (MOFED) and the OSU Micro-benchmarks as set of MPI-enabled applications.

```

mpi-test-container.def

```

BootStrap: yum

OSVersion: 8.8

MirrorURL: http://dl.rockylinux.org/pub/rocky/%{OSVERSION}/BaseOS/x86_64/os/

Include: dnf

%environment

export OMPI_DIR=/usr/local

export APPTAINER_OMPI_DIR=$OMPI_DIR

export APPTAINERENV_APPEND_PATH=$OMPI_DIR/bin

export APPTAINERENV_APPEND_LD_LIBRARY_PATH=$OMPI_DIR/lib

%post

## Prerequisites

dnf update

dnf install -y dnf-plugins-core

dnf config-manager --set-enabled powertools

dnf groupinstall -y 'Development Tools'

dnf install -y wget git bash hostname gcc gcc-gfortran gcc-c++ make file autoconf automake libtool zlib-devel python3

dnf install -y libmnl lsof numactl-libs ethtool tcl tk

## Packages required for OpenMPI and PMIx

dnf install -y libnl3 libnl3-devel

dnf install -y libevent libevent-devel

dnf install -y munge munge-devel

# Mellanox OFED matching MeluXina

mkdir -p /tmp/mofed

cd /tmp/mofed

wget -c https://content.mellanox.com/ofed/MLNX_OFED-5.8-3.0.7.0/MLNX_OFED_LINUX-5.8-3.0.7.0-rhel8.5-x86_64.tgz

tar xf MLNX_OFED_LINUX-*.tgz

cd MLNX_OFED_LINUX-5.8-3.0.7.0-rhel8.5-x86_64

./mlnxofedinstall --basic --user-space-only --without-fw-update --distro rhel8.8 --force

# HWLOC for PMIx and OpenMPI

mkdir -p /tmp/hwloc

cd /tmp/hwloc

wget https://download.open-mpi.org/release/hwloc/v2.9/hwloc-2.9.3.tar.bz2

tar xf hwloc-2.9.3.tar.bz2

cd hwloc-2.9.3/

./configure --prefix=/usr/local

make -j

make install

# PMIx

mkdir -p /tmp/pmix

cd /tmp/pmix

wget -c https://github.com/openpmix/openpmix/releases/download/v4.2.6/pmix-4.2.6.tar.gz

tar xf pmix-4.2.6.tar.gz

cd pmix-4.2.6

./configure --prefix=/usr/local --with-munge=/usr --with-libevent=/usr --with-zlib=/usr --enable-pmix-binaries --with-hwloc=/usr/local && \

make -j

make install

# libfabric

mkdir -p /tmp/libfabric

cd /tmp/libfabric

wget -c https://github.com/ofiwg/libfabric/releases/download/v1.18.0/libfabric-1.18.0.tar.bz2

tar xf libfabric*tar.bz2

cd libfabric-1.18.0

./configure --prefix=/usr/local && \

make -j

make install

## OpenMPI installation

echo "Installing Open MPI"

export OMPI_DIR=/usr/local

export OMPI_VERSION=4.1.5

export OMPI_URL="https://download.open-mpi.org/release/open-mpi/v4.1/openmpi-$OMPI_VERSION.tar.bz2"

mkdir -p /tmp/ompi

cd /tmp/ompi

wget -c -O openmpi-$OMPI_VERSION.tar.bz2 $OMPI_URL && tar -xjf openmpi-$OMPI_VERSION.tar.bz2

# Compile and install

cd /tmp/ompi/openmpi-$OMPI_VERSION

./configure --prefix=$OMPI_DIR --with-pmix=/usr/local --with-libevent=/usr --with-ompi-pmix-rte --with-orte=no --disable-oshmem --enable-mpirun-prefix-by-default --enable-shared --with-ofi=/usr/local --without-verbs --with-hwloc

make -j

make install

# Set env variables so we can compile our applications

export PATH=$OMPI_DIR/bin:$PATH

export LD_LIBRARY_PATH=$OMPI_DIR/lib:$LD_LIBRARY_PATH

export MANPATH=$OMPI_DIR/share/man:$MANPATH

## Example MPI applications installation - OSU microbenchmarks

cd /root

wget -c https://mvapich.cse.ohio-state.edu/download/mvapich/osu-micro-benchmarks-7.2.tar.gz

tar xf osu-micro-benchmarks-7.2.tar.gz

cd osu-micro-benchmarks-7.2/

echo "Configuring and building OSU Micro-Benchmarks..."

./configure --prefix=/usr/local/osu CC=$(which mpicc) CXX=$(which mpicxx) CFLAGS=-I$(pwd)/util

make -j

make install

%runscript

echo "Container will run: /usr/local/osu/libexec/osu-micro-benchmarks/mpi/$*"

exec /usr/local/osu/libexec/osu-micro-benchmarks/mpi/$*

```

BootStrap: yum

OSVersion: 8.8

MirrorURL: http://dl.rockylinux.org/pub/rocky/%{OSVERSION}/BaseOS/x86_64/os/

Include: dnf

%environment

export OMPI_DIR=/usr/local

export APPTAINER_OMPI_DIR=$OMPI_DIR

export APPTAINERENV_APPEND_PATH=$OMPI_DIR/bin

export APPTAINERENV_APPEND_LD_LIBRARY_PATH=$OMPI_DIR/lib

%post

## Prerequisites

dnf update

dnf install -y dnf-plugins-core

dnf config-manager --set-enabled powertools

dnf groupinstall -y 'Development Tools'

dnf install -y wget git bash hostname gcc gcc-gfortran gcc-c++ make file autoconf automake libtool zlib-devel python3

dnf install -y libmnl lsof numactl-libs ethtool tcl tk

## Packages required for OpenMPI and PMIx

dnf install -y libnl3 libnl3-devel

dnf install -y libevent libevent-devel

dnf install -y munge munge-devel

# Mellanox OFED matching MeluXina

mkdir -p /tmp/mofed

cd /tmp/mofed

wget -c https://content.mellanox.com/ofed/MLNX_OFED-5.8-3.0.7.0/MLNX_OFED_LINUX-5.8-3.0.7.0-rhel8.5-x86_64.tgz

tar xf MLNX_OFED_LINUX-*.tgz

cd MLNX_OFED_LINUX-5.8-3.0.7.0-rhel8.5-x86_64

./mlnxofedinstall --basic --user-space-only --without-fw-update --distro rhel8.8 --force

# HWLOC for PMIx and OpenMPI

mkdir -p /tmp/hwloc

cd /tmp/hwloc

wget https://download.open-mpi.org/release/hwloc/v2.9/hwloc-2.9.3.tar.bz2

tar xf hwloc-2.9.3.tar.bz2

cd hwloc-2.9.3/

./configure --prefix=/usr/local

make -j

make install

# PMIx

mkdir -p /tmp/pmix

cd /tmp/pmix

wget -c https://github.com/openpmix/openpmix/releases/download/v4.2.6/pmix-4.2.6.tar.gz

tar xf pmix-4.2.6.tar.gz

cd pmix-4.2.6

./configure --prefix=/usr/local --with-munge=/usr --with-libevent=/usr --with-zlib=/usr --enable-pmix-binaries --with-hwloc=/usr/local && \

make -j

make install

# libfabric

mkdir -p /tmp/libfabric

cd /tmp/libfabric

wget -c https://github.com/ofiwg/libfabric/releases/download/v1.18.0/libfabric-1.18.0.tar.bz2

tar xf libfabric*tar.bz2

cd libfabric-1.18.0

./configure --prefix=/usr/local && \

make -j

make install

## OpenMPI installation

echo "Installing Open MPI"

export OMPI_DIR=/usr/local

export OMPI_VERSION=4.1.5

export OMPI_URL="https://download.open-mpi.org/release/open-mpi/v4.1/openmpi-$OMPI_VERSION.tar.bz2"

mkdir -p /tmp/ompi

cd /tmp/ompi

wget -c -O openmpi-$OMPI_VERSION.tar.bz2 $OMPI_URL && tar -xjf openmpi-$OMPI_VERSION.tar.bz2

# Compile and install

cd /tmp/ompi/openmpi-$OMPI_VERSION

./configure --prefix=$OMPI_DIR --with-pmix=/usr/local --with-libevent=/usr --with-ompi-pmix-rte --with-orte=no --disable-oshmem --enable-mpirun-prefix-by-default --enable-shared --with-ofi=/usr/local --without-verbs --with-hwloc

make -j

make install

# Set env variables so we can compile our applications

export PATH=$OMPI_DIR/bin:$PATH

export LD_LIBRARY_PATH=$OMPI_DIR/lib:$LD_LIBRARY_PATH

export MANPATH=$OMPI_DIR/share/man:$MANPATH

## Example MPI applications installation - OSU microbenchmarks

cd /root

wget -c https://mvapich.cse.ohio-state.edu/download/mvapich/osu-micro-benchmarks-7.2.tar.gz

tar xf osu-micro-benchmarks-7.2.tar.gz

cd osu-micro-benchmarks-7.2/

echo "Configuring and building OSU Micro-Benchmarks..."

./configure --prefix=/usr/local/osu CC=$(which mpicc) CXX=$(which mpicxx) CFLAGS=-I$(pwd)/util

make -j

make install

%runscript

echo "Container will run: /usr/local/osu/libexec/osu-micro-benchmarks/mpi/$*"

exec /usr/local/osu/libexec/osu-micro-benchmarks/mpi/$*

```

```

BootStrap: yum

OSVersion: 8.8

MirrorURL: http://dl.rockylinux.org/pub/rocky/%{OSVERSION}/BaseOS/x86_64/os/

Include: dnf

%environment

export OMPI_DIR=/usr/local

export APPTAINER_OMPI_DIR=$OMPI_DIR

export APPTAINERENV_APPEND_PATH=$OMPI_DIR/bin

export APPTAINERENV_APPEND_LD_LIBRARY_PATH=$OMPI_DIR/lib

%post

## Prerequisites

dnf update

dnf install -y dnf-plugins-core

dnf config-manager --set-enabled powertools

dnf groupinstall -y 'Development Tools'

dnf install -y wget git bash hostname gcc gcc-gfortran gcc-c++ make file autoconf automake libtool zlib-devel python3

dnf install -y libmnl lsof numactl-libs ethtool tcl tk

## Packages required for OpenMPI and PMIx

dnf install -y libnl3 libnl3-devel

dnf install -y libevent libevent-devel

dnf install -y munge munge-devel

# Mellanox OFED matching MeluXina

mkdir -p /tmp/mofed

cd /tmp/mofed

wget -c https://content.mellanox.com/ofed/MLNX_OFED-5.8-3.0.7.0/MLNX_OFED_LINUX-5.8-3.0.7.0-rhel8.5-x86_64.tgz

tar xf MLNX_OFED_LINUX-*.tgz

cd MLNX_OFED_LINUX-5.8-3.0.7.0-rhel8.5-x86_64

./mlnxofedinstall --basic --user-space-only --without-fw-update --distro rhel8.8 --force

# HWLOC for PMIx and OpenMPI

mkdir -p /tmp/hwloc

cd /tmp/hwloc

wget https://download.open-mpi.org/release/hwloc/v2.9/hwloc-2.9.3.tar.bz2

tar xf hwloc-2.9.3.tar.bz2

cd hwloc-2.9.3/

./configure --prefix=/usr/local

make -j

make install

# PMIx

mkdir -p /tmp/pmix

cd /tmp/pmix

wget -c https://github.com/openpmix/openpmix/releases/download/v4.2.6/pmix-4.2.6.tar.gz

tar xf pmix-4.2.6.tar.gz

cd pmix-4.2.6

./configure --prefix=/usr/local --with-munge=/usr --with-libevent=/usr --with-zlib=/usr --enable-pmix-binaries --with-hwloc=/usr/local && \

make -j

make install

# libfabric

mkdir -p /tmp/libfabric

cd /tmp/libfabric

wget -c https://github.com/ofiwg/libfabric/releases/download/v1.18.0/libfabric-1.18.0.tar.bz2

tar xf libfabric*tar.bz2

cd libfabric-1.18.0

./configure --prefix=/usr/local && \

make -j

make install

## OpenMPI installation

echo "Installing Open MPI"

export OMPI_DIR=/usr/local

export OMPI_VERSION=4.1.5

export OMPI_URL="https://download.open-mpi.org/release/open-mpi/v4.1/openmpi-$OMPI_VERSION.tar.bz2"

mkdir -p /tmp/ompi

cd /tmp/ompi

wget -c -O openmpi-$OMPI_VERSION.tar.bz2 $OMPI_URL && tar -xjf openmpi-$OMPI_VERSION.tar.bz2

# Compile and install

cd /tmp/ompi/openmpi-$OMPI_VERSION

./configure --prefix=$OMPI_DIR --with-pmix=/usr/local --with-libevent=/usr --with-ompi-pmix-rte --with-orte=no --disable-oshmem --enable-mpirun-prefix-by-default --enable-shared --with-ofi=/usr/local --without-verbs --with-hwloc

make -j

make install

# Set env variables so we can compile our applications

export PATH=$OMPI_DIR/bin:$PATH

export LD_LIBRARY_PATH=$OMPI_DIR/lib:$LD_LIBRARY_PATH

export MANPATH=$OMPI_DIR/share/man:$MANPATH

## Example MPI applications installation - OSU microbenchmarks

cd /root

wget -c https://mvapich.cse.ohio-state.edu/download/mvapich/osu-micro-benchmarks-7.2.tar.gz

tar xf osu-micro-benchmarks-7.2.tar.gz

cd osu-micro-benchmarks-7.2/

echo "Configuring and building OSU Micro-Benchmarks..."

./configure --prefix=/usr/local/osu CC=$(which mpicc) CXX=$(which mpicxx) CFLAGS=-I$(pwd)/util

make -j

make install

%runscript

echo "Container will run: /usr/local/osu/libexec/osu-micro-benchmarks/mpi/$*"

exec /usr/local/osu/libexec/osu-micro-benchmarks/mpi/$*

```

To build this container you require Apptainer on your workstation or server, then simply run:

sudo apptainer build mpi-test-container.sif mpi-test-container.def

```

sudo apptainer build mpi-test-container.sif mpi-test-container.def

```

```

sudo apptainer build mpi-test-container.sif mpi-test-container.def

```

The container image mpi-test-container.sif can then be transferred to MeluXina, and a job launcher mpi-container-launcher.sh created to run it:

```

mpi-test-container.sif

```

```

mpi-container-launcher.sh

```

#!/bin/bash -l

#SBATCH -J MPIContainerTest

#SBATCH -A YOURACCOUNT

#SBATCH -p cpu

#SBATCH -q short

#SBATCH -N 2

#SBATCH --ntasks-per-node=4

#SBATCH -t 0:5:0

module load Apptainer/1.2.4-GCCcore-12.3.0

module load OpenMPI/4.1.5-GCC-12.3.0

srun mpi-test-container.sif pt2pt/osu_mbw_mr

```

#!/bin/bash -l

#SBATCH -J MPIContainerTest

#SBATCH -A YOURACCOUNT

#SBATCH -p cpu

#SBATCH -q short

#SBATCH -N 2

#SBATCH --ntasks-per-node=4

#SBATCH -t 0:5:0

module load Apptainer/1.2.4-GCCcore-12.3.0

module load OpenMPI/4.1.5-GCC-12.3.0

srun mpi-test-container.sif pt2pt/osu_mbw_mr

```

```

#!/bin/bash -l

#SBATCH -J MPIContainerTest

#SBATCH -A YOURACCOUNT

#SBATCH -p cpu

#SBATCH -q short

#SBATCH -N 2

#SBATCH --ntasks-per-node=4

#SBATCH -t 0:5:0

module load Apptainer/1.2.4-GCCcore-12.3.0

module load OpenMPI/4.1.5-GCC-12.3.0

srun mpi-test-container.sif pt2pt/osu_mbw_mr

```

In the launcher above, the MPI application OSU "Multiple Bandwidth / Message Rate Test" is being run from the container using the system OpenMPI installation.

The launcher is then submitted to SLURM using sbatch mpi-container-launcher.sh.

```

sbatch mpi-container-launcher.sh

```