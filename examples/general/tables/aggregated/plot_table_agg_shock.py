"""
shock_type
==========

.. todo:: Full explanation

"""

#######################################################################################
# .. raw:: html
#     :file: ../../../../_static/datasets/html-tables/plot_table_agg_shock.html
#
# |
# |

# Libraries
import os
import sys
import pandas as pd

# Import TableOne
from tableone import TableOne


# ---------------------------------
# Methods
# ---------------------------------
def filename():
    """Get filename"""
    try:
        return os.path.basename(__file__)[:-3]
    except:
        return os.path.basename(sys.argv[0])[:-3]

def build_html_tableone(table, tag):
    """This methods appends the table in HTML.

    Parameters
    ----------
    HTLM: str
        The HTML output.
    table: TableOne
        The table to append
    tag: str
        The tag for the bulletpoint.

    Return
    ------
    str
        HTML with appended table.
    """

    # Partial HTML
    html_aux = table.tabulate(tablefmt="html")

    # In contrast to to_html, the tablefmt does not add style
    # to te table. Thus, we will set the border and class
    # manually.
    html_aux = html_aux.replace('<table>', \
        '<table border="1" class="dataframe">')

    # Store all tables in HTML
    html_aux = "<br><br>&#9726;Dataset <b>{0}</b>:<br>{1}<br>" \
        .format(tag, html_aux)

    # Return
    return html_aux

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
path = '../../../../resources/data/20210313-v0.0.8/'
path+= 'combined/combined_tidy.csv'

# TableOne
# --------
# Selected columns
columns = ['age', 'gender', 'day_from_illness',
           'plt', 'wbc', 'haematocrit_percent',
           'albumin', 'ast', 'alt',
           'fluid_accumulation']

# Categorical features
categorical = ['gender',
               'fluid_accumulation']

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

# ---------------------------------
# Main
# ---------------------------------

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


# -------
# Overall
# -------
# Create table
mytable = TableOne(data, columns=columns,
    categorical=categorical, groupby=groupby,
    nonnormal=nonnormal, pval=True, rename=rename,
    sort=True, missing=False, htest_name=False,
    min_max=None, label_suffix=True, limit=5)

# Append mytable in HTML
HTML+= build_html_tableone(mytable, 'Aggregated')


# ----------------
# For each dataset
# ----------------
for i, df in data.groupby('dsource'):

    # Remove columns with all NaN
    df = df.dropna(how='all', axis=1)

    # --------
    # TableOne
    # --------
    # Ensure they are in the df
    df_cols = list(set(columns).intersection(df.columns))
    df_cate = list(set(categorical).intersection(df.columns))
    df_gpby = list(set(groupby).intersection(df.columns))
    df_nonn = list(set(nonnormal).intersection(df.columns))
    df_rnme = {k:v for k,v in rename.items() if k in df.columns}

    # Create table
    mytable = TableOne(df, columns=df_cols,
        categorical=df_cate, groupby=df_gpby,
        nonnormal=df_nonn, pval=True, rename=df_rnme,
        sort=True, missing=False, htest_name=False,
        min_max=None, label_suffix=True, limit=5)

    # Append mytable in HTML
    HTML+= build_html_tableone(mytable, i)


# Configuration
# Save the result (so that it is loaded in .rst)
PATH = '../../../../docs/source/_static/'
PATH+= 'datasets/html-tables/{0}.html'

# Write file (so that it is loaded in .rst)
f = open(PATH.format(filename()), "w+", encoding='utf8')
f.write(HTML)
f.close()

a = 10