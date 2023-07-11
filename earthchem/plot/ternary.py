""" file:   ternary.py (earthchem.plot)
    author: Jess Robertson, CSIRO Minerals
    date:   May 2018

    description: Ternary plots
"""

from pyrolite.plot import pyroplot

def ternaryplot(df=None, components=None, **kwargs):
    """
    Plots scatter ternary diagrams, using a wrapper around the
    python-ternary library (gh.com/marcharper/python-ternary).

    Parameters
    ----------
    df: pandas DataFrame
        Dataframe from which to draw data.
    ax: Matplotlib AxesSubplot, None
        The subplot to draw on.
    components: list, None
        Elements or compositional components to plot.
    """
    if components is None:
        return df.pyroplot.scatter(**kwargs)
    else:
        return df.loc[:, components].pyroplot.scatter(**kwargs)
