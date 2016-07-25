# ReGraph

Graph Rewriting Library

## About project

The **ReGraph** Python library is a generic framework for modelling graph-centric systems. In this context models are viewed as graphs and graph transformations - as a tool to describe both the system evolution and the model evolution [read more about the approach] (http://link.springer.com/chapter/10.1007%2F978-3-540-30203-2_30). 

**ReGraph** includes data structures for representation of typed graphs, both directed (`TypedDiGraph`) and undirected (`TypedGraph`). They are inherited from [NetworkX] (https://networkx.github.io/) graphs, therefore can be operated as any graph in the context of the reach functionality available in NetworkX.

Graph rewriting is performed by an object of the class `Rewriter` which is initialised with the target graph for rewriting. Rewriting is performed in-place, so the initial graph is modified in course of rewriting. Two graph rewriting modes are available: declarative (implementing [sesqui-pushout rewriting](http://link.springer.com/chapter/10.1007%2F11841883_4)) and declarative (sequence of primitive operations on the graph).

Every graph can have a meta-model, so it is possible to construct a cascade of graphs, where the graph on each level would type the the graph immediately above. In addition to simple graph rewriting, the **ReGraph** library provides the class `GraphModeler`, which implements a way to propagate specific changes (stable for cloning and deletion) in the graph at any level to the upper levels automatically.


## Environment configs 

### Requirement

The following `Python 3` packages are required

```
cycler==0.10.0
decorator==4.0.9
matplotlib==1.5.1
networkx==1.11
numpy==1.11.0
pyparsing==2.1.4
python-dateutil==2.5.3
pytz==2016.4
six==1.10.0
wheel==0.24.0
```

To avoid manual installation and to easily set up development environment you may consider following the instructions below:

### Create virtual environment

```
virtualenv venv -p path/to/your/python3
```

### Setup environment

To activate the virtual environment
```
source venv/bin/activate
```

To install required dependencies
```
pip install -r requirement.txt
```

## Installation

In order to install the **ReGraph** library you have to clone this repository using SSH
```
git clone git@github.com:eugeniashurko/ReGraph.git
```
or using HTTPS
```
https://github.com/eugeniashurko/ReGraph.git
```
Install the library with
```
python setup.py install
```

## Run tests

```
python tests/test.py
```
