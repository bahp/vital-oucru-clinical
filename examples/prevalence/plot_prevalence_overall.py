"""
Monthly prevalence (overall)
============================

.. warning::

    - The features must be static.
    - Would it help to print ns1_interpretation table?
    - Should ns1 be a compound of all the ns1?
    - Would it help to plot the prevalence graph for each dataset?


This example computes the prevalence of dengue in the ``HTD`` as the
proportion of patients which were diagnosed with Dengue based on any
positive result for the ``NS1``, ``PCR`` or ``serology`` tests. The
x-axis represents the month and the y-axis the prevalence in %. In
addition, the number on top of each bar represents the total number
of patients used to compute the proportion.

"""

# Libraries
import calendar
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# DataBlend library
from datablend.core.repair.correctors import oucru_dengue_interpretation_feature

# Seaborn
sns.set_theme(style="whitegrid")


# ---------------------------------
# Methods
# ---------------------------------
def add_totals(df):
    """Adds total sum for rows/cols."""
    # Add columns
    df.loc['Total', :] = df.sum(axis=0)
    df.loc[:, 'Total'] = df.sum(axis=1)
    df = df.astype(int)
    # Return
    return df


def prevalence(x):
    return (np.sum(x) / len(x)) * 100


# ---------------------------------
# Constants
# ---------------------------------
# The data filepath
path = '../../resources/data/20210313-v0.8/combined/combined_tidy.csv'

# Features
features = ['study_no',
            'date',
            'dsource',
            'pcr_dengue_serotype',
            'igm_interpretation',
            'igg_interpretation',
            'ns1_interpretation',
            'ns1_plasma_interpretation',
            'ns1_platelia_interpretation',
            'ns1_urine_interpretation',
            'serology_interpretation',
            'serology_single_interpretation',
            'serology_paired_interpretation']

# ---------------------------------
# Main
# ---------------------------------
# Read data
data = pd.read_csv(path, low_memory=False,
                         parse_dates=['date'],
                         usecols=features)

# Format
data = data.convert_dtypes()
data = data[features]

# Define positive dengue
#data = dengue_interpretation(data)

# Add dengue interpretation
data['dengue_interpretation'] = \
    oucru_dengue_interpretation_feature(data,
        pcr=True, ns1=True, igm=True,
        paired_igm_igg=True, default=False)

# Overall outcome for patient
patients = data.groupby('study_no').max()
patients['month'] = patients.date.dt.month
patients['year'] = patients.date.dt.year

# PCR serotypes count per dataset
serotypes = add_totals(pd.crosstab(
    patients.pcr_dengue_serotype, patients.dsource))

# Serology count per dataset
serology = add_totals(pd.crosstab(
    patients.serology_interpretation, patients.dsource
))

# Dengue interpretation count per dataset
dengue = add_totals(pd.crosstab(
    patients.dengue_interpretation, patients.dsource))

# Show
print("\nColumns:")
print(data.columns)
print("\nPatients:")
print(patients)
print("\nSerotypes:")
print(serotypes)
print("\nSerology:")
print(serology)
print("\nDengue:")
print(dengue)

# Compute prevalence
# ------------------
# Datasets where serotype has non-null values.
idxs = patients.dsource.isin(serotypes.columns)

# Compute prevalence
prevalence = patients.reset_index().groupby('month').agg(
    prevalence=('dengue_interpretation', prevalence),
    n_patients=('study_no', 'count'))

# Add legible labels
prevalence.index = \
    [calendar.month_abbr[x] for x in prevalence.index]

# Show
print("\nPrevalence:")
print(prevalence)


# ------------------------------------------------
# Plot
# ------------------------------------------------
# Initialize the figure
f, ax = plt.subplots(figsize=(6, 3))

# Plot
sns.set_color_codes("muted")
sns.despine(left=True, bottom=True)
sns.barplot(x=prevalence.index,
            y=prevalence.prevalence,
            label="Dengue prevalence",
            color="b",
            linewidth=0.75)

# Add a legend and informative axis label
ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(xlabel="", ylabel="Prevalence (%)",
       title="Overall dengue prevalence in HTD")

# Add number of patients considered
for i, (index, row) in enumerate(prevalence.iterrows()):
    ax.text(i, row.prevalence, int(row.n_patients),
            color='black', ha="center", fontsize=8)

# Show
plt.show()