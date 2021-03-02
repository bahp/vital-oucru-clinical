"""
Overall monthly prevalence
==========================

Example using your package

.. warning:: At the moment a the assumption is that if the pcr_dengue_serotype
             is present then the patient had dengue. Otherwise, the patient did
             not suffer dengue. However, the following things should be considered:

               - Not all datasets had pcr_dengue_serotype variable
               - The serology results and/or clinical notes need to be incorporated.
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
path = '../../resources/data/20212002-v0.2/combined/combined_tidy.csv'

# Features
features = ['study_no',
            'date',
            'dsource',
            'pcr_dengue_serotype',
            'ns1_interpretation',
            'igm_interpretation',
            'igg_interpretation']

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

# Dengue interpretation count per dataset
dengue = add_totals(pd.crosstab(
    patients.dengue_interpretation, patients.dsource))

# Show
print("\nPatients:")
print(patients)
print("\nSerotypes:")
print(serotypes)
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
print("\n:")
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