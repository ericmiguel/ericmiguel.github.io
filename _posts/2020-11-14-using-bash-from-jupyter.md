---
layout: post
title: Run bash script from Jupyter in three simple steps
tags: jupyterlab bash
featured-image: header_run_bash_script_from_jupyter_in_three_simple_steps.png
background-type: dark
---

During past weeks I've gone deep in automating processes. Bash scripting was the solution to go, but I`m not a frequent Bash user. However, the possibility to write bash code at Jupyter with all the "shift enter" made it a walk in the park.

<!--more-->

If you don't know, Jupyter can handle different language kernels beyond Python. R and Julia are some other possibilities, not forgetting about bash.

To install the bash kernel at Jupyter, start creating and activating a new conda env:

{% highlight posh linenos %}
conda create -n bashkernel python=3.8
conda activate bashkernel
{% endhighlight %}

After, install the Bash Kernel:
{% highlight posh linenos %}
conda install -c conda-forge bash_kernel
{% endhighlight %}

After installing the package, type the following command:
{% highlight posh linenos %}
python -m bash_kernel.install
{% endhighlight %}

If everything is ok, you will see the Jupyter launcher with you brand new kernel option.
![_config.yml]({{ site.baseurl }}/images/img1_run_bash_script_from_jupyter_in_three_simple_steps.jpg)


Very simple, don't? 

If you're interested in jupyter kernels, what about my [last article](https://ericmiguel.github.io/using-conda-environments-from-jupyterlab/) on conda envs and Jupyter?