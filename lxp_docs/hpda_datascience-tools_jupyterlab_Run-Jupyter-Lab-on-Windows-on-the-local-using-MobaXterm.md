# Run JupyterLab on Windows

Source: https://docs.lxp.lu/hpda/datascience-tools/jupyterlab/Run-Jupyter-Lab-on-Windows-on-the-local-using-MobaXterm/

# Run JupyterLab on Windows

This tutorial will guide you to run Jupyter Lab on MeluXina if your workstation is using Windows.

It assumes you are using MobaXterm as an SSH/SFTP/X11 client.

Connect to MeluXina with MobaXterm, for more details see the Windows/MobaXterm section in our connecting to MeluXina page.

Allocate a cluster node on MeluXina with the salloc command

For example: salloc -A YOUR_ACCOUNT -t 0:05:0 -p cpu -q short -N 1

The example above will allocate one CPU node (-p cpu) in interactive mode, with the short QoS for a rapid allocation, for 5 minutes (-t 0:05:0).

Activate Jupyter Lab

Load the JupyterLab module to be able to use it: module load JupyterLab

This will load the latest available version of JupyterLab. If you require a specific version, find if it is available in our general software stack using module available Jupyter, then load that specific version with `module load JupyterLab/VERSION'

Start Jupyter Lab

Start Jupyter Lab: jupyter-lab --app_dir=/project/home/YOUR_PROJECT/ --no-browser --port=8888 --ip=0.0.0.0

This will launch a Jupyter Lab session which resides in your project workspace, with the port 8888 and able to accept connections from the MeluXina login node - this is needed for the next steps.

Create a local port forwarding configuration with MobaSSHTunnel

The notebook server is now started on a compute node and you will need to make a connection from it to your local computer through a private and secure tunnel, using a MeluXina login node as a gateway. MobaXterm offers an interactive interface where you can set up an ssh tunnel with ease:

(1) Open Tunneling

(2) Create a new connection

(3) Local port

(4) Address of login node

(5) Port of login node

(6) Username

(7) Cluster node (server name)

(8) Port of Jupyter Lab running on cluster node (server port)

(9) Import SSH private key

You are now ready to access the Jupyter Lab on your computer!

Open your workstation's browser and connect to

- Connect to MeluXina with MobaXterm, for more details see the Windows/MobaXterm section in our connecting to MeluXina page.

Connect to MeluXina with MobaXterm, for more details see the Windows/MobaXterm section in our connecting to MeluXina page.

- Allocate a cluster node on MeluXina with the salloc command

For example: salloc -A YOUR_ACCOUNT -t 0:05:0 -p cpu -q short -N 1

The example above will allocate one CPU node (-p cpu) in interactive mode, with the short QoS for a rapid allocation, for 5 minutes (-t 0:05:0).

Allocate a cluster node on MeluXina with the salloc command

```

salloc

```

For example: salloc -A YOUR_ACCOUNT -t 0:05:0 -p cpu -q short -N 1

The example above will allocate one CPU node (-p cpu) in interactive mode, with the short QoS for a rapid allocation, for 5 minutes (-t 0:05:0).

- For example: salloc -A YOUR_ACCOUNT -t 0:05:0 -p cpu -q short -N 1

```

salloc -A YOUR_ACCOUNT -t 0:05:0 -p cpu -q short -N 1

```

- The example above will allocate one CPU node (-p cpu) in interactive mode, with the short QoS for a rapid allocation, for 5 minutes (-t 0:05:0).

- Activate Jupyter Lab

Load the JupyterLab module to be able to use it: module load JupyterLab

This will load the latest available version of JupyterLab. If you require a specific version, find if it is available in our general software stack using module available Jupyter, then load that specific version with `module load JupyterLab/VERSION'

Activate Jupyter Lab

Load the JupyterLab module to be able to use it: module load JupyterLab

This will load the latest available version of JupyterLab. If you require a specific version, find if it is available in our general software stack using module available Jupyter, then load that specific version with `module load JupyterLab/VERSION'

- Load the JupyterLab module to be able to use it: module load JupyterLab

```

module load JupyterLab

```

- This will load the latest available version of JupyterLab. If you require a specific version, find if it is available in our general software stack using module available Jupyter, then load that specific version with `module load JupyterLab/VERSION'

```

module available Jupyter

```

- Start Jupyter Lab

Start Jupyter Lab: jupyter-lab --app_dir=/project/home/YOUR_PROJECT/ --no-browser --port=8888 --ip=0.0.0.0

This will launch a Jupyter Lab session which resides in your project workspace, with the port 8888 and able to accept connections from the MeluXina login node - this is needed for the next steps.

Start Jupyter Lab

Start Jupyter Lab: jupyter-lab --app_dir=/project/home/YOUR_PROJECT/ --no-browser --port=8888 --ip=0.0.0.0

This will launch a Jupyter Lab session which resides in your project workspace, with the port 8888 and able to accept connections from the MeluXina login node - this is needed for the next steps.

- Start Jupyter Lab: jupyter-lab --app_dir=/project/home/YOUR_PROJECT/ --no-browser --port=8888 --ip=0.0.0.0

```

jupyter-lab --app_dir=/project/home/YOUR_PROJECT/ --no-browser --port=8888 --ip=0.0.0.0

```

- This will launch a Jupyter Lab session which resides in your project workspace, with the port 8888 and able to accept connections from the MeluXina login node - this is needed for the next steps.

- Create a local port forwarding configuration with MobaSSHTunnel

The notebook server is now started on a compute node and you will need to make a connection from it to your local computer through a private and secure tunnel, using a MeluXina login node as a gateway. MobaXterm offers an interactive interface where you can set up an ssh tunnel with ease:

(1) Open Tunneling

(2) Create a new connection

(3) Local port

(4) Address of login node

(5) Port of login node

(6) Username

(7) Cluster node (server name)

(8) Port of Jupyter Lab running on cluster node (server port)

(9) Import SSH private key

Create a local port forwarding configuration with MobaSSHTunnel

The notebook server is now started on a compute node and you will need to make a connection from it to your local computer through a private and secure tunnel, using a MeluXina login node as a gateway. MobaXterm offers an interactive interface where you can set up an ssh tunnel with ease:

(1) Open Tunneling

(2) Create a new connection

(3) Local port

(4) Address of login node

(5) Port of login node

(6) Username

(7) Cluster node (server name)

(8) Port of Jupyter Lab running on cluster node (server port)

(9) Import SSH private key

- The notebook server is now started on a compute node and you will need to make a connection from it to your local computer through a private and secure tunnel, using a MeluXina login node as a gateway. MobaXterm offers an interactive interface where you can set up an ssh tunnel with ease:

- (1) Open Tunneling

- (2) Create a new connection

- (3) Local port

- (4) Address of login node

- (5) Port of login node

- (6) Username

- (7) Cluster node (server name)

- (8) Port of Jupyter Lab running on cluster node (server port)

- (9) Import SSH private key

- You are now ready to access the Jupyter Lab on your computer!

Open your workstation's browser and connect to

You are now ready to access the Jupyter Lab on your computer!

Open your workstation's browser and connect to

- Open your workstation's browser and connect to