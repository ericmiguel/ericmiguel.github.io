Title: Solving the Jupyterlab start warning at WSL
Slug: solving-the-jupyterlab-start-warning-at-wsl
Date: 2020-11-15 17:50
Modified: 2021-12-30 18:02
Category: Article
Tags: python, jupyter
Author: Eric M. Ribeiro
Summary: Nowadays, I have all my development environment under the Ubuntu subsystem for Windows. Also known as WSL, the subsystem was the best addition for Windows if you are a developer. But there is a problem...

Nowadays, I have all my development environment under the Windows Ubuntu subsystem. Also known as WSL, the subsystem was the best addition for Windows if you are a developer.

For those installed Jupyterlab under WSL, the following warning may be familiar. It is annoying, but very easy to solve.

![final-result]({attach}solving-jupyterlab-start-warning-at-wsl/img1.jpg)

The error seems come from WSL searching for a browser to open the Jupyter UI. Although is not a critical error and will not prevent you from use Jupyter, it deserves to be solved. The warning will disappear as also as a browser will spawn.

First, generate the Jupyter config file if you have not it already.

    :::python
    jupyter notebook --generate-config

Open the config file (usually in ~/.jupyter). Search for the following line and change it from True to False.

    :::python
    c.NotebookApp.use_redirect_file = False

I am using WSL2 (Ubuntu 20.04) and now the error is gone and the browser opens as also as Jupyter starts without warning.
