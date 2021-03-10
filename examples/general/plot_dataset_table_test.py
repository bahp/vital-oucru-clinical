"""
Dataset TableOne - Shock
========================

.. todo:: Full explanation

"""

########################################
# .. raw:: html
#     :file: ../../../_static/datasets/html-tables/shock.html

########################################
# |
# |
#

# Libraries
import pandas as pd

# Import TableOne
# .. note:: https://github.com/tompollard/tableone
from tableone import TableOne

# Import DataBlend
from datablend.core.repair.correctors import oucru_dengue_interpretation_feature


# ---------------------------------
# Methods
# ---------------------------------
def shock_type_faeture(tidy, default='No Shock'):
    """Creates the shock type.

    .. note: Order is important because the column data.shock
             represents patients with either single or multiple
             shocks.

    Parameters
    ----------

    Returns
    -------

    """
    # Create series
    shock_type = \
        pd.Series(index=tidy.index, data=default, dtype='object')

    # Set single shocks
    shock_type[data.shock.fillna(False)] = 'Shock'

    # Set multiple shocks
    shock_type[data.shock_multiple.fillna(False)] = 'Recurrent Shock'

    # Return
    return shock_type


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
data['shock_type'] = \
    shock_type_faeture(data)

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
groupby = ['shock_type']

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
    sort=False, missing=False, htest_name=False,
    min_max=None)

# Show
#print(mytable.tabulate(tablefmt="fancy_grid"))

# Other export formats
#print(mytable.tabulate(tablefmt="github"))
#print(mytable.tabulate(tablefmt="rst"))
#print(mytable.tabulate(tablefmt="html"))
#print(mytable.tabulate(tablefmt="latex"))

# Show
#print(data.groupby('dsource').study_no.nunique())

# Save the result (so that it is loaded in .rst)
path = '../../../docs/source/_static/'
path+= 'datasets/html-tables/shock.html'
mytable.to_html(path)

