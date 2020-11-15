---
layout: post
title: Solving the Jupyterlab start warning at WSL
tags: anaconda jupyterlab python
featured-image: header_using_conda_environments_from_jupyterlab.png
background-type: dark
---

Nowadays, I have all my development environment under the Windows Ubuntu subsystem. Also known as WSL, the subsystem was the best addition for Windows if you are a developer.

For those installed Jupyterlab under WSL, the following warning may be familiar. It is annoying, but very easy to solve.

<!--more-->

![_config.yml]({{ site.baseurl }}/images/img1_solving_jupyterlab_start_warning_at_wsl.jpg)

The error seems come from WSL searching for a browser to open the Jupyter UI. Although is not a critical error and will not prevent you use Jupyter, it can be simple solved. The warning will disappear as also as a browser will spawn.

First, generate the Jupyter config file if you have not it already.
{% highlight posh linenos %}
jupyter notebook --generate-config
{% endhighlight %}

Open the config file (usually in ~/.jupyter). Search for the following line and change it from True to False. 
{% highlight posh linenos %}
c.NotebookApp.use_redirect_file = False
{% endhighlight %}

I am using WSL2 (Ubuntu 20.04) and now the error is gone and the browser open as Jupyter starts.

{% highlight posh linenos %}
conda activate lab
jupyter lab
{% endhighlight %}
