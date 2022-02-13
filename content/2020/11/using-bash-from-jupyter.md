Title: Run bash script from Jupyter in three simple steps
Slug: run-bash-script-from-jupyter-in-three-simple-steps
Date: 2020-11-14 14:20
Modified: 2021-12-30 18:02
Category: Article
Tags: jupyter, bash
Author: Eric M. Ribeiro
Summary: During past weeks I've gone deep in automating processes. Bash scripting was the solution to go, but I`m not a frequent Bash user. However, the possibility to write bash code at Jupyter with all the "shift enter" made it a walk in the park.


During past weeks I've gone deep in automating processes. Bash scripting was the solution to go, but I`m not a frequent Bash user. However, the possibility to write bash code at Jupyter with all the "shift enter" made it a walk in the park.

If you don't know, Jupyter can handle different language kernels beyond Python[ref]If you're interested in jupyter kernels, what about my [last article](https://ericmiguel.github.io/using-conda-environments-from-jupyterlab/) on conda envs and Jupyter?[/ref]. R and Julia are some other possibilities, not forgetting about bash.

First, make sure you have Anaconda. I recommend you the [Miniconda](https://docs.conda.io/en/latest/miniconda.html) distribution. It does not come with nothing pre-installed but the essential. To install the bash kernel on Jupyter, start creating and activating a new conda env:

    :::python
    conda create -n bashkernel python=3.8
    conda activate bashkernel

After, install the Bash Kernel:

    :::python
    conda install -c conda-forge bash_kernel

Run the following command to get it done:

    :::python
    python -m bash_kernel.install

If everything gone ok, you will see the Jupyter launcher with your brand new kernel option.
![final-result]({attach}using-bash-from-jupyter/img1.jpg)

Very simple, huh?
