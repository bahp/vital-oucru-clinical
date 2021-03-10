"""
by dsource and shock_type
=========================

.. todo:: Full explanation

"""

########################################
# .. raw:: html
#     :file: ../../../_static/datasets/html-tables/tableone_dsource_shock_type.html
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
def shock_type_faeture(tidy, default='No Shock'):
    """Creates the shock type.

    .. note: Order is important because the column data.shock
             represents patients with either single or multiple
             shocks.

    .. todo: Move this method to library.

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
    shock_type[data.shock_multiple.fillna(False)] = 'Shock Recurrent'

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

# Add fluid accumulation
data['fluid_accumulation'] = \
    data.pleural_effusion | data.ascites

# Add shock type categories
data['shock_type'] = \
    shock_type_faeture(data)

HTML = ""

for i, df in data.groupby('dsource'):

    # Remove columns with all NaN
    df = df.dropna(how='all', axis=1)

    # --------
    # TableOne
    # --------
    # Columns
    columns = ['age', 'gender', 'day_from_illness',
               'plt', 'wbc', 'haematocrit_percent',
               'albumin', 'ast', 'alt',
               'fluid_accumulation']

    columns = list(set(columns).intersection(df.columns))

    # Categorical
    categorical = ['gender', 'fluid_accumulation']

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
    mytable = TableOne(df, columns=columns,
        categorical=categorical, groupby=groupby,
        nonnormal=nonnormal, pval=True, rename=rename,
        sort=True, missing=False, htest_name=False,
        min_max=None, label_suffix=False, limit=5)

    # Partial HTML
    html_aux = mytable.tabulate(tablefmt="html")

    # In contrast to to_html, the tablefmt does not add style
    # to te table. Thus, we will set the border and class
    # manually.
    html_aux = html_aux.replace('<table>', \
        '<table border="1" class="dataframe">')

    # Store all tables in HTML
    HTML += "<br><br>&#9726;Dataset <b>{0}</b>:<br>{1}<br>".format(i, html_aux)


# Configuration
PATH = '../../../docs/source/_static/'
PATH+= 'datasets/html-tables/{0}.html'
NAME = 'tableone_dsource_shock_type'

# Write file (so that it is loaded in .rst)
f = open(PATH.format(NAME), "w+", encoding='utf8')
f.write(HTML)
f.close()