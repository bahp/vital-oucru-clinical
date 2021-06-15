"""
dengue_interpretation
=====================

.. todo:: Full explanation

.. todo:: Would it be worth it to include
          all this information into a datatable
          so that we can reorder, search, ...?

.. todo:: Review body mass index (BMI)

"""

######################################################################################
# .. raw:: html
#     :file: ../../../../_static/datasets/html-tables/plot_table_base_dengue.html
#
# |
# |

# Libraries
import os
import sys
import warnings
import numpy as np
import pandas as pd

# Import TableOne
from tableone import TableOne

# Import DataBlend
from datablend.core.repair.correctors import day_from_day_values
from datablend.core.repair.correctors import oucru_correction
from datablend.core.repair.correctors import oucru_dengue_interpretation_feature
from datablend.core.repair.correctors import oucru_ns1_interpretation_feature

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

# ---------------------------------
# Constants
# ---------------------------------
# The data filepath
path = '../../../../resources/data/20210313-v0.0.8/'
path+= 'combined/combined_tidy.csv'

# TableOne
# --------
# Columns
columns = ['age',  'day_from_illness',
           'plt', 'wbc', 'haematocrit_percent',
           'albumin', 'ast', 'alt',
           'fluid_accumulation',
           'pcr_dengue_serotype',
           'abdominal_pain',
           'abdominal_tenderness',
           'bleeding',
           'bleeding_mucosal',
           'bleeding_skin',
           'oedema',
           'vomiting',
           'shock_multiple',
           'bmi',
           'sbp',
           'dbp',
           'pulse',
           'pulse_pressure',
           'body_temperature',
           'ns1_interpretation',
           'serology_interpretation']

# Groupby
groupby = ['dengue_interpretation']

# Rename
rename = {
    'day_from_illness': 'day',
    'haematocrit_percent': 'hct',
    'albumin': 'alb',
    'fluid_accumulation': 'Fluid acumm.'
}

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

# Oucru correction
#data = oucru_correction(data)

# Add bmi
data['bmi'] = data.weight / (data.height * 0.01)**2

# Add dengue interpretation
data['dengue_interpretation'] = \
    oucru_dengue_interpretation_feature(data,
        pcr=True, ns1=True, igm=True, serology=True,
        single_igm_igg=True, paired_igm_igg=True,
        default=False)

data['ns1_interpretation'] = \
    oucru_ns1_interpretation_feature(data)

# Add fluid accumulation
data['fluid_accumulation'] = \
    data.pleural_effusion | data.ascites

# Keep only baseline data
data = data[data.event_enrolment.fillna(False)]


HTML = ""

# -------
# Overall
# -------
# Define categorical
nonnormal = list(data[columns].select_dtypes(include='number').columns)
categorical = list(set(columns).difference(set(nonnormal)))
columns = sorted(categorical) + sorted(nonnormal)
order = {k: sorted(data[k].astype(str).unique()) for k in categorical}


# Create table
mytable = TableOne(data,
    columns=columns, categorical=categorical,
    groupby=groupby, nonnormal=nonnormal, pval=True,
    rename=rename, order=order, sort=False, missing=False,
    htest_name=False, min_max=None, label_suffix=True, limit=5,
    dip_test=True, normal_test=True, tukey_test=True)


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
    df_cols = [c for c in columns if c in df.columns] # Keeps order
    df_cate = list(set(categorical).intersection(df.columns))
    df_gpby = list(set(groupby).intersection(df.columns))
    df_nonn = list(set(nonnormal).intersection(df.columns))
    df_rnme = {k:v for k,v in rename.items() if k in df.columns}


    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")

            # Create table
            mytable = TableOne(df, columns=df_cols,
                categorical=df_cate, groupby=df_gpby,
                nonnormal=df_nonn, pval=True, rename=rename,
                order=order, sort=False, missing=False, htest_name=False,
                min_max=None, label_suffix=True, limit=5,
                dip_test=True, normal_test=True, tukey_test=True)

            # Append mytable in HTML
            HTML+= build_html_tableone(mytable, i)
    except Exception as e:
        HTML+= "<br><br>&#9726;Dataset <b>{0}</b>:<br>{1}<br>"\
            .format(i, e)


# Save the result (so that it is loaded in .rst)
PATH = '../../../../docs/source/_static/'
PATH+= 'datasets/html-tables/{0}.html'

# Write file (so that it is loaded in .rst)
f = open(PATH.format(filename()), "w+", encoding='utf8')
f.write(HTML)
f.close()




"""
def keep_nunique_ge(data, th=1000):
    return data.loc[:, data.nunique() >= th].columns


def keep_pmissing_le(data, th=50):
    # Compute missing percentages
    mp = data.isnull().sum() * 100 / len(data)
    # Filter by missing percentages
    return data.loc[:, mp < th].columns


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
"""

a = 10