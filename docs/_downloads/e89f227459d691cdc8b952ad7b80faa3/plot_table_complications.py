"""
by complications
================

.. todo:: Full explanation

"""

########################################
# .. raw:: html
#     :file: ../../../_static/datasets/html-tables/tableone_complications.html
#
# |
# |

# Libraries
import pandas as pd

# Import TableOne
from tableone import TableOne


# ---------------------------------
# Methods
# ---------------------------------
def complications_feature(tidy,
        ascites=True, pleural_effusion=True,
        jaundice=True, default=False):
    """Creates the complications column

    Parameters
    ----------

    Returns
    -------

    """
    # Create series
    complications = \
        pd.Series(index=tidy.index, data=default, dtype='boolean')

    # Fill.
    complications[tidy.ascites.fillna(False)] = True
    complications[tidy.pleural_effusion.fillna(False)] = True
    complications[tidy.jaundice.fillna(False)] = True
    complications[tidy.shock.fillna(False)] = True

    # Return
    return complications


# ---------------------------------
# Constants
# ---------------------------------
# The data filepath
path = '../../../resources/data/20210309-v0.7/combined/combined_tidy.csv'

# ---------------------------------
# Main
# ---------------------------------
# .. note :: In manuscript 32dx, 2017 the variable fluid accumulation
#            defined pleural effusion and/or ascites. Also important,
#            they present lactate but it is not available on our data.

# .. todo :: Do the renaming by loading the .yaml file?

# Read data
data = pd.read_csv(path,
    low_memory=False,
    #nrows=10000,
    parse_dates=['date'])

# Remove columns with all NaN
data = data.dropna(how='all', axis=1)

# Add fluid accumulation
data['fluid_accumulation'] = \
    data.pleural_effusion | data.ascites

# Add shock type categories
data['complications'] = \
    complications_feature(data)

# --------
# TableOne
# --------
# Columns
columns = ['age', 'gender', 'day_from_illness',
           'plt', 'wbc', 'haematocrit_percent',
           'albumin', 'ast', 'alt',
           'fluid_accumulation']

# Categorical
categorical = ['gender', 'fluid_accumulation']

# order = {'gender': ['Female', 'Male', None]}
# limit = {'gender': 1}



# Groupby
groupby = ['complications']

# Non normal
nonnormal = ['age', 'plt', 'wbc', 'albumin',
             'ast', 'haematocrit_percent',
             'alt', 'day_from_illness']

# Rename labels.
rename = {
    'day_from_illness': 'day',
    'haematocrit_percent': 'hct',
    'albumin': 'alb',
    'fluid_accumulation': 'Fluid acumm.'
}

# Create table
mytable = TableOne(data, columns=columns,
    categorical=categorical, groupby=groupby,
    nonnormal=nonnormal, pval=True, rename=rename,
    sort=False, missing=False, htest_name=True,
    min_max=None, label_suffix=False, limit=5)

# Uncomment to see terminal output
# print(mytable.tabulate(tablefmt="fancy_grid"))

# Save the result (so that it is loaded in .rst)
PATH = '../../../docs/source/_static/'
PATH+= 'datasets/html-tables/{0}.html'
NAME = 'tableone_complications'
mytable.to_html(PATH.format(NAME))

