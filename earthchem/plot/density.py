from pyrolite.plot import pyroplot

def densityplot(df=None, components=None, **kwargs):
    if components is None:
        return df.pyroplot.density(**kwargs)
    else:
        return df.loc[:, components].pyroplot.density(**kwargs)
