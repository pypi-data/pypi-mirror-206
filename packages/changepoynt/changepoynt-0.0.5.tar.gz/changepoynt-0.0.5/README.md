# Python Changepoint Detection (changepoynt)

 

This is the repository hosting the **pip-installable** python package changepoynt. It implements several different change point detection techniques, while focusing mostly on "localized" algorithms, that could be run in an online fashion.

 

Current algorithms come from the field of:

* Statistics (Detection of Change in the statistical properties)

* Time Series Segmentation (Algorithms focused on comparing time series shap)

 

The package is aimed at execution performance (using JIT compilation and standing on the shoulders of giants like numpy and scipy) while also keeping code readable and maintainable. This includes comments as well as architectural choices. This might not be perfect, but we are trying!

 

All of our algorithms are implementations of a base changepoint detection interface and therefore are interchangeable. Currently, we are focused on shifting to the very common and existing sklearn interface of fit and predict. This enables our algorithms to be part of the standard sklearn pipeline for preprocessing.

 

# Installation

You can install `changepoynt` from the common package index [PyPi](https://pypi.org/project/changepoynt/) using the following line with pip:

 

    pip install changepoynt

 

Please be aware, that we are currently in an alpha development phase, as this is part of a research project at the FAU Erlangen together with SIEMENS Energy developed by [me](https://www.cs6.tf.fau.eu/person/lucas-weber/). Nevertheless, we aim to be open-source and try our best to guarantee that all the code we use has very permissive licenses.

# Participating

We always love to get feedback or new ideas. If you have any of those, feel free to open an issue. We try to get back to you as soon as we can.

 

If you are an author of a paper in the field or have another algorithmic idea: Feel free to open a pull request. Currently, we are still working on the contribution guides. But if somebody already comes along and has an idea, we do not want to be in the way!