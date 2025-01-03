# Run JupyterLab on Linux

Source: https://docs.lxp.lu/hpda/datascience-tools/jupyterlab/Jupyter-Linux/

# Run JupyterLab on Linux

## Step 1: Launching a job in MeluXina

Jupyter Lab is one of the most widely used IDEs in the data science community. They are the choice of tool for many data scientists when it comes to quick prototyping and exploratory analysis. A JupyterLab neatly bundles many functionalities together, enabling collaborative, extensible, and scalable data science.

To launch an instance of Jupyter Lab in MeluXina we need to take into account the following criteria when constructing our sbatch script:

Choose the right SLURM options for this task

Load the necessary modules and dependencies

Execute Jupyter lab

- Choose the right SLURM options for this task

- Load the necessary modules and dependencies

- Execute Jupyter lab

The following is a working template that includes all these considerations:

#!/bin/bash -l

#SBATCH --account=my_account

#SBATCH --job-name=JUPYTER

#SBATCH --partition=cpu/gpu/largemem/fpga

#SBATCH --qos=short

#SBATCH --time=HH:MM:SS

#SBATCH --nodes=1

#SBATCH --ntasks-per-node=128

#SBATCH --hint=nomultithread

# Load Modules

module load Python/3.9.5-GCCcore-10.3.0

pip install --user --upgrade pip

pip install --user lib1, lib2, lib3, etc.

module load JupyterLab/3.0.16-GCCcore-10.3.0

# Launch jupyter notebook

srun --exact --ntasks 128 jupyter lab --no-browser --ip "*" --notebook-dir my_dir  --port 8888

```

#!/bin/bash -l

#SBATCH --account=my_account

#SBATCH --job-name=JUPYTER

#SBATCH --partition=cpu/gpu/largemem/fpga

#SBATCH --qos=short

#SBATCH --time=HH:MM:SS

#SBATCH --nodes=1

#SBATCH --ntasks-per-node=128

#SBATCH --hint=nomultithread

# Load Modules

module load Python/3.9.5-GCCcore-10.3.0

pip install --user --upgrade pip

pip install --user lib1, lib2, lib3, etc.

module load JupyterLab/3.0.16-GCCcore-10.3.0

# Launch jupyter notebook

srun --exact --ntasks 128 jupyter lab --no-browser --ip "*" --notebook-dir my_dir  --port 8888

```

```

#!/bin/bash -l

#SBATCH --account=my_account

#SBATCH --job-name=JUPYTER

#SBATCH --partition=cpu/gpu/largemem/fpga

#SBATCH --qos=short

#SBATCH --time=HH:MM:SS

#SBATCH --nodes=1

#SBATCH --ntasks-per-node=128

#SBATCH --hint=nomultithread

# Load Modules

module load Python/3.9.5-GCCcore-10.3.0

pip install --user --upgrade pip

pip install --user lib1, lib2, lib3, etc.

module load JupyterLab/3.0.16-GCCcore-10.3.0

# Launch jupyter notebook

srun --exact --ntasks 128 jupyter lab --no-browser --ip "*" --notebook-dir my_dir  --port 8888

```

We will now assume that the job has been not only submitted but also is running on the mel0000 node in MeluXina.

```

mel0000

```

## Step 2: Forwarding the port to our local machine

On our local machine, we will follow these instructions:

Connect to MeluXina via the following ssh command (see the section on connecting for more details):

ssh -L 8888:localhost:8888 my_username@login.lxp.lu -p 8822

Once connected to MeluXina and on the login node, we will forward the port to the compute node via the following ssh command:

ssh -L 8888:localhost:8888 mel0000

Once the two ssh commands have been executed and we have a terminal session logged into the compute node mel0000, we leave that terminal session untouched and redirect our internet browser to the following address:

- Connect to MeluXina via the following ssh command (see the section on connecting for more details):

ssh -L 8888:localhost:8888 my_username@login.lxp.lu -p 8822

Connect to MeluXina via the following ssh command (see the section on connecting for more details):

ssh -L 8888:localhost:8888 my_username@login.lxp.lu -p 8822

```

ssh -L 8888:localhost:8888 my_username@login.lxp.lu -p 8822

```

```

ssh -L 8888:localhost:8888 my_username@login.lxp.lu -p 8822

```

- Once connected to MeluXina and on the login node, we will forward the port to the compute node via the following ssh command:

ssh -L 8888:localhost:8888 mel0000

Once connected to MeluXina and on the login node, we will forward the port to the compute node via the following ssh command:

ssh -L 8888:localhost:8888 mel0000

```

ssh -L 8888:localhost:8888 mel0000

```

```

ssh -L 8888:localhost:8888 mel0000

```

- Once the two ssh commands have been executed and we have a terminal session logged into the compute node mel0000, we leave that terminal session untouched and redirect our internet browser to the following address:

Once the two ssh commands have been executed and we have a terminal session logged into the compute node mel0000, we leave that terminal session untouched and redirect our internet browser to the following address:

```

mel0000

```

localhost:8888

```

localhost:8888

```

## Step 3: Enjoy

Congrats! This should result in a fully-functional Jupyter Lab session in our browser corresponding to the slurm job being executed on the mel0000 node in MeluXina.

```

mel0000

```