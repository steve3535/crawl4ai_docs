# Quick start

Source: https://docs.lxp.lu/first-steps/quick_start/

# Quick start

> Within this section you will find essential information to get you started on MeluXina if you are already used to a supercomputer's environment.

For additional details on using our supercomputer facilities see the following sections, starting with the Connecting page.

UPPERCASE words in command sections below highlight information that you should replace with the actual value, e.g. THEQOS -> short.

Within this section you will find essential information to get you started on MeluXina if you are already used to a supercomputer's environment.

For additional details on using our supercomputer facilities see the following sections, starting with the Connecting page.

UPPERCASE words in command sections below highlight information that you should replace with the actual value, e.g. THEQOS -> short.

```

command sections

```

Access MeluXina by SSH with the user account you've received: ssh YOURUSER@login.lxp.lu -p 8822

```

ssh YOURUSER@login.lxp.lu -p 8822

```

Access is performed using SSH keys, to log into MeluXina you'll need the private key counterpart to the public key you've provided us.

MeluXina has 4 login nodes, accessing login.lxp.lu should be preferred, but connecting to login[01-04].lxp.lu directly is possible (depending on availability).

Login nodes are meant only for job submission and monitoring, not for computation or long running tasks (including data-intensive processes).

Login nodes do not have access to the user software environment (it's only present on compute nodes), compilation/execution tasks must be performed on compute nodes.

- Access is performed using SSH keys, to log into MeluXina you'll need the private key counterpart to the public key you've provided us.

- MeluXina has 4 login nodes, accessing login.lxp.lu should be preferred, but connecting to login[01-04].lxp.lu directly is possible (depending on availability).

```

login.lxp.lu

```

```

login[01-04].lxp.lu

```

- Login nodes are meant only for job submission and monitoring, not for computation or long running tasks (including data-intensive processes).

- Login nodes do not have access to the user software environment (it's only present on compute nodes), compilation/execution tasks must be performed on compute nodes.

SLURM is the MeluXina job scheduler and resource management system:

See the available partitions (queues), their node count and state with: sinfo

See the current job queue with: squeue -l

See the list of SLURM accounts you have access to with: sacctmgr show user $USER withassoc

See the list of QOS that prioritize and set job constraints with: sacctmgr show qos

For performance assurance and security, job scheduling is done with full nodes. Requesting one task on one compute node will give you access to the complete node, all of its cores, memory and (if applicable) GPU or FPGA accelerators.

Compute nodes have HyperThreading enabled, to ensure the use of only physical cores, use the --hint=nomultithread option at job submission.

See the hardware configuration for compute nodes with: scontrol show node THENODE

See the list of SLURM features defined on compute nodes with: sinfo -o %N,%f

See the node reservations you have access to: sinfo -T or scontrol show res

- See the available partitions (queues), their node count and state with: sinfo

```

sinfo

```

- See the current job queue with: squeue -l

```

squeue -l

```

- See the list of SLURM accounts you have access to with: sacctmgr show user $USER withassoc

```

sacctmgr show user $USER withassoc

```

- See the list of QOS that prioritize and set job constraints with: sacctmgr show qos

```

sacctmgr show qos

```

- For performance assurance and security, job scheduling is done with full nodes. Requesting one task on one compute node will give you access to the complete node, all of its cores, memory and (if applicable) GPU or FPGA accelerators.

- Compute nodes have HyperThreading enabled, to ensure the use of only physical cores, use the --hint=nomultithread option at job submission.

```

--hint=nomultithread

```

- See the hardware configuration for compute nodes with: scontrol show node THENODE

```

scontrol show node THENODE

```

- See the list of SLURM features defined on compute nodes with: sinfo -o %N,%f

```

sinfo -o %N,%f

```

- See the node reservations you have access to: sinfo -T or scontrol show res

```

sinfo -T

```

```

scontrol show res

```

SLURM partitions defined on MeluXina:

QOS for jobs on MeluXina, enabling various usage modes of the computational resources:

Development/interactive jobs using the dev QOS must be run within the following SLURM reservations:

```

dev

```

The above reservations are self-extending, trying to maintain a pool of compute nodes readily available for interactive development.

Running jobs:

Interactive jobs are run with: salloc + options

Job steps are run with srun + options

Passive/batch jobs are run with: sbatch + options

You always need to specify the project account your job will charge: salloc/sbatch -A YOURPROJECT

You always need to specify the QOS your job will use: salloc/sbatch -q THEQOS

- Interactive jobs are run with: salloc + options

```

salloc

```

- Job steps are run with srun + options

```

srun

```

- Passive/batch jobs are run with: sbatch + options

```

sbatch

```

- You always need to specify the project account your job will charge: salloc/sbatch -A YOURPROJECT

```

salloc/sbatch -A YOURPROJECT

```

- You always need to specify the QOS your job will use: salloc/sbatch -q THEQOS

```

salloc/sbatch -q THEQOS

```

A few examples:

Run an interactive development job on a CPU node for 2 hours: salloc -A YOURPROJECT --res cpudev -q dev -N 1 -t 2:0:0

Run a job script on 140 GPU nodes (560 GPUs) for 12 hours: sbatch -A YOURPROJECT -p gpu -q large -N 140 -t 12:0:0 YOURSCRIPT

- Run an interactive development job on a CPU node for 2 hours: salloc -A YOURPROJECT --res cpudev -q dev -N 1 -t 2:0:0

```

salloc -A YOURPROJECT --res cpudev -q dev -N 1 -t 2:0:0

```

- Run a job script on 140 GPU nodes (560 GPUs) for 12 hours: sbatch -A YOURPROJECT -p gpu -q large -N 140 -t 12:0:0 YOURSCRIPT

```

sbatch -A YOURPROJECT -p gpu -q large -N 140 -t 12:0:0 YOURSCRIPT

```

Data locations:

Users have a private Home directory /home/users/YOURUSER, and access to Project directories they're part of.

Projects have:

a Home directory /project/home/THEPROJECT, and/or

a Scratch directory /project/scratch/THEPROJECT

Compute & data resource allocation quotas and utilization in the current scheduling period can be viewed with the myquota tool on the login nodes

- Users have a private Home directory /home/users/YOURUSER, and access to Project directories they're part of.

```

/home/users/YOURUSER

```

- Projects have:

a Home directory /project/home/THEPROJECT, and/or

a Scratch directory /project/scratch/THEPROJECT

a Home directory /project/home/THEPROJECT, and/or

a Scratch directory /project/scratch/THEPROJECT

- a Home directory /project/home/THEPROJECT, and/or

```

/project/home/THEPROJECT

```

- a Scratch directory /project/scratch/THEPROJECT

```

/project/scratch/THEPROJECT

```

- Compute & data resource allocation quotas and utilization in the current scheduling period can be viewed with the myquota tool on the login nodes

```

myquota

```

Software environment:

We're using EasyBuild and LMod for the user software environment.

The software environment is only available on compute nodes.

Discover the modules providing access to the different software packages with: module available.

Search for a specific application in the current production software environment with: module av THESOFTWARE.

Load the profile of a specific application together with its dependencies with: module load THESOFTWARE.

- We're using EasyBuild and LMod for the user software environment.

- The software environment is only available on compute nodes.

- Discover the modules providing access to the different software packages with: module available.

```

module available

```

- Search for a specific application in the current production software environment with: module av THESOFTWARE.

```

module av THESOFTWARE

```

- Load the profile of a specific application together with its dependencies with: module load THESOFTWARE.

```

module load THESOFTWARE

```

> We welcome your requests for information and support either at: servicedesk.lxp.lu or by mail to servicedesk [at] lxp.lu

We welcome your requests for information and support either at: servicedesk.lxp.lu or by mail to servicedesk [at] lxp.lu