"""
by dengue_interpretation
========================

.. todo:: Full explanation

"""

########################################
# .. raw:: html
#     :file: ../../../_static/datasets/html-tables/tableone_dengue_interpretation.html
#
# |
# |

# Libraries
import numpy as np
import pandas as pd

# Import TableOne
from tableone import TableOne

# Import DataBlend
from datablend.core.repair.correctors import oucru_dengue_interpretation_feature

# ---------------------------------
# Methods
# ---------------------------------
def keep_nunique_ge(data, th=1000):
    """Keep columns with more than nunique values."""
    return data.loc[:, data.nunique() >= th].columns

def keep_pmissing_le(data, th=50):
    """Keep columns with less than percent missing.

    Parameters
    ----------

    Returns
    -------
    """
    # Compute missing percentages
    mp = data.isnull().sum() * 100 / len(data)
    # Filter by missing percentages
    return data.loc[:, mp < th].columns


# ---------------------------------
# Constants
# ---------------------------------
# The data filepath
path = '../../../resources/data/20210309-v0.7/combined/combined_tidy.csv'

# ---------------------------------
# Main
# ---------------------------------
# ..note :: In manuscript 32dx, 2017 the variable fluid accumulation
#           defined pleural effusion and/or ascites. Also important,
#           they present lactate but it is not available on our data.

# Read data
data = pd.read_csv(path,
    #nrows=1000,
    #index_col=0,
    low_memory=False,
    parse_dates=['date'])

# Add dengue interpretation
data['dengue_interpretation'] = \
    oucru_dengue_interpretation_feature(data,
        pcr=True, ns1=True, igm=True, serology=True,
        single_igm_igg=True, paired_igm_igg=True,
        default=False)

# Add fluid accumulation
data['fluid_accumulation'] = \
    data.pleural_effusion | data.ascites

# Columns to keep
keep1 = keep_nunique_ge(data, th=1000)
keep2 = keep_pmissing_le(data, th=50)

# Copy dataset
keep = data.copy(deep=True)
keep = keep[keep_pmissing_le(data, th=75)]
keep = keep.drop(columns=['Unnamed: 0',
                          'date',
                          'study_no',
                          'parental_fluid'])

# Categorical
categorical = keep.convert_dtypes() \
    .select_dtypes(include=['boolean', 'object']) \
    .columns.tolist()

# Non-normal
nonnormal = keep.convert_dtypes() \
    .select_dtypes(include=['Int64', 'Float64']) \
    .columns.tolist()

# Columns
columns = categorical + nonnormal

groupby = ['dengue_interpretation']

# One table for labs and one table for examination!

# Compute table
mytable = TableOne(data, columns=columns,
    categorical=categorical, nonnormal=nonnormal,
    groupby=groupby,
    pval=False, rename={}, sort=True, missing=True,
    htest_name=True, min_max=None, label_suffix=False,
    limit=5)

print(mytable.tabulate(tablefmt="fancy_grid"))

import sys
sys.exit()


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

# Groupby
groupby = ['dengue_interpretation']

# Non normal
nonnormal = ['age', 'plt', 'wbc', 'albumin',
             'ast', 'haematocrit_percent',
             'alt', 'day_from_illness']

# Rename
rename = {
    'day_from_illness': 'day',
    'haematocrit_percent': 'hct',
    'albumin': 'alb',
    'fluid_accumulation': 'Fluid acumm.'
}

mytable = TableOne(data, columns=columns,
    categorical=categorical, groupby=groupby,
    nonnormal=nonnormal, pval=True, rename=rename,
    sort=False, missing=False, htest_name=True,
    min_max=None)


# Uncomment to see terminal output
# print(mytable.tabulate(tablefmt="fancy_grid"))

# Save the result (so that it is loaded in .rst)
PATH = '../../../docs/source/_static/'
PATH+= 'datasets/html-tables/{0}.html'
NAME = 'tableone_dengue_interpretation'
mytable.to_html(PATH.format(NAME))

