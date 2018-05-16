# Earthchem & PyData

[![PyPI](https://img.shields.io/pypi/v/earthchem.svg)](https://pypi.python.org/pypi/earthchem/)
[![GitHub license](https://img.shields.io/github/license/jesserobertson/earthchem-pyclient.svg)](https://github.com/jesserobertson/earthchem-pyclient/blob/master/LICENSE.txt)

This project wraps the Earthchem web services to provide easy access to geochemical data from [IEDA](https://www.iedadata.org/) in ready-to-use format in your favourite PyData environment.

Maintainer: Jess Robertson (jesse.robertson _at_ csiro.au)

| **Service** | **master** | **develop** |
| ----------- |:----------:|:-----------:|
| Test status | [![Build Status](https://travis-ci.org/jesserobertson/earthchem-pyclient.svg?branch=master)](https://travis-ci.org/jesserobertson/earthchem-pyclient) | [![Build Status](https://travis-ci.org/jesserobertson/earthchem-pyclient.svg?branch=develop)](https://travis-ci.org/jesserobertson/earthchem-pyclient) |
| Test coverage | [![Coverage Status](https://coveralls.io/repos/github/jesserobertson/earthchem-pyclient/badge.svg?branch=master)](https://coveralls.io/github/jesserobertson/earthchem-pyclient?branch=master) | [![Coverage Status](https://coveralls.io/repos/github/jesserobertson/earthchem-pyclient/badge.svg?branch=develop)](https://coveralls.io/github/jesserobertson/earthchem-pyclient?branch=develop) |

### So why would I want to use this?

Say you wanted to know how many samples have been submitted to IEDA by your colleague named Dr Barnes:

```python
>>> from earthchem.query import RESTClientQuery
>>> q = RESTClientQuery(author='barnes')
>>> q.count()

4902
```

That's a lot of samples. Can we see the compositions of the first 50 say?

```python
>>> df = q.dataframe()
>>> df.head()
```

![Table output](https://github.com/jesserobertson/earthchem-pyclient/raw/develop/docs/resources/table_output.png)


Great, so now I can make some little plots right?

```python
>>> df.plot('al2o3', 'sio2', 'scatter')
```

![Plot output](https://github.com/jesserobertson/earthchem-pyclient/raw/develop/docs/resources/plot_output.png)

### Great, I'm sold. How do I get it?

Provided you have python installed, this library is just a `pip install earthchem` away. 

If you don't have Python we recommend taking a look at the marvellous [Anaconda distribution](https://www.anaconda.com/) - just pick your relevant platform download [from here](https://www.anaconda.com/download/).