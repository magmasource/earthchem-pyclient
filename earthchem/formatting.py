#from pyrolite.geochem import tochem, common_elements, common_oxides
import pyrolite.geochem
from pyrolite.geochem.parse import tochem
from pyrolite.util.text import titlecase
#from pyrolite.normalisation import ReferenceCompositions
from pyrolite.geochem.norm import get_reference_composition

def cleanup_dataframe(df, normalize_to=None):
    """
    Simple dataframe cleanup: reformats and reorders columns.
    Normalises to a reference composition as necessary
    (e.g. try 'Chondrite_PON' or 'PM_PON').

    Parameters
    ----------
    df: pandas DataFrame
        Dataframe to clean up.
    normalize_to: pandas DataFrame
        Dataframe to clean up.
    """
    df.columns = df.columns.map(lambda x: titlecase(x, abbrv=['ID', 'IGSN']))
    df.columns = tochem(df.columns)
    #majors = [i for i in common_oxides(output='str')
    #          if i in df.columns.values]
    #traces = [i for i in common_elements(output='str')
    #          if i in df.columns.values]
    majors = df.pyrochem.list_oxides
    traces = df.pyrochem.list_elements

    # Everything else, then majors, then traces
    df = df.loc[:, [i for i in df.columns if i not in majors+traces] + \
                   majors + traces]
    if normalize_to is not None:
        #df = ReferenceCompositions()[normalize_to].normalize(df)
        df = df.pyrochem.normalize_to(get_reference_composition(normalize_to))
    return df
