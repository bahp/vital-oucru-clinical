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
import pandas as pd

# Import TableOne
from tableone import TableOne

# Import DataBlend
from datablend.core.repair.correctors import oucru_dengue_interpretation_feature

# ---------------------------------
# Methods
# ---------------------------------

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
    low_memory=False,
    parse_dates=['date'])

# Remove columns with all NaN
data = data.dropna(how='all', axis=1)

# Add dengue interpretation
data['dengue_interpretation'] = \
    oucru_dengue_interpretation_feature(data,
        pcr=True, ns1=True, igm=True, serology=True,
        single_igm_igg=True, paired_igm_igg=True,
        default=False)

# Add fluid accumulation
data['fluid_accumulation'] = \
    data.pleural_effusion | data.ascites


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
    sort=False, missing=False, htest_name=False,
    min_max=None)

# Uncomment to see terminal output
# print(mytable.tabulate(tablefmt="fancy_grid"))

# Save the result (so that it is loaded in .rst)
PATH = '../../../docs/source/_static/'
PATH+= 'datasets/html-tables/{0}.html'
NAME = 'tableone_dengue_interpretation'
mytable.to_html(PATH.format(NAME))

