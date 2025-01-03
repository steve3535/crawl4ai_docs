# Convert Notebook to Python

Source: https://docs.lxp.lu/hpda/datascience-tools/jupyterlab/Jupyterlab-to-Python/

# Convert Notebook to Python

In this tutorial, you will learn how to convert your Python code written in a Jupyter notebook to a single python file in order to automate testing and Machine Leaning model deployment in a production environment, after data exploratory and analysis.

We will introduce 2 simple ways in which notebooks can be casted into a python script with JupyterLab GUI and the nbconvert command.

## Prerequisites

You will need either Jupyter Notebook and nbconvert on your workstation, or to use the modules provided in the MeluXina software environment.

On your workstation you can use pip install notebook nbconvert to install them

On MeluXina you can simply use module load JupyterLab within an interactive job

- On your workstation you can use pip install notebook nbconvert to install them

```

pip install notebook nbconvert

```

- On MeluXina you can simply use module load JupyterLab within an interactive job

```

module load JupyterLab

```

## Conversion process

Make sure your code is well-factored: all code should be factored to functions and those functions must be easy tested.

As a general good practice, any unused code should be cleaned out from the Jupyter Notebook when moving to a production application.

Jupyter Lab GUI

- Jupyter Lab GUI

nbconvert:

jupyter nbconvert --to script your_notebook.ipynb

- nbconvert:

jupyter nbconvert --to script your_notebook.ipynb

nbconvert:

```

nbconvert

```

jupyter nbconvert --to script your_notebook.ipynb

```

jupyter nbconvert --to script your_notebook.ipynb

```

```

jupyter nbconvert --to script your_notebook.ipynb

```