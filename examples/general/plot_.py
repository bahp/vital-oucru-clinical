"""
Overall prevalence
==================

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


def dengue_interpretation(data):
    """Defines dengue interpretation.

    .. note: It is a case of dengue if there is a pcr_dengue_serotype.

    .. warning: Assumming that if no pcr_dengue_serotype then a case
                of no dengue, but might be that the datasets do not
                have such column!
    """

    # Define map
    serotype_map = {
        pd.NA: 'Negative',
        '<LOD': 'Negative'
    }

    # Create binary variable dengue
    data['dengue'] = data.pcr_dengue_serotype
    data.dengue = data.dengue.fillna('0')
    data.dengue = data.dengue.replace({'<LOD': '0'})
    data.loc[~(data.dengue == '0'), 'dengue'] = '1'
    data.dengue = data.dengue.astype(int)

    # Return
    return data


# ---------------------------------
# Constants
# ---------------------------------
# The data filepath
path = '../../resources/data/20212002-v0.2/combined/combined_tidy.csv'

# Features
features = ['study_no',
            'date',
            'dsource',
            'pcr_dengue_serotype']

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
data = dengue_interpretation(data)

# Overall outcome for patient
patients = data.groupby('study_no').max()
patients['month'] = patients.date.dt.month
patients['year'] = patients.date.dt.year

# PCR serotypes count per dataset
serotypes = add_totals(pd.crosstab(
    patients.pcr_dengue_serotype, patients.dsource))

# Dengue interpretation count per dataset
dengue = add_totals(pd.crosstab(
    patients.dengue, patients.dsource))

# Show
print("\nPatients:")
print(patients)
print("\nSerotypes:")
print(serotypes)
print("\nDengue:")
print(dengue)

# ------------------------------------------------
# Example I: Plot the overall prevalence per month
# ------------------------------------------------
# Datasets where serotype has non-null values.
idxs = patients.dsource.isin(serotypes.columns)

# Compute prevalence
overall_prevalence = patients[idxs].groupby('month') \
    .dengue.apply(lambda x: (np.sum(x) / len(x)) * 100)

# Add legible labels
overall_prevalence.index = \
    [calendar.month_abbr[x] for x in overall_prevalence.index]

# Initialize the figure
f, ax = plt.subplots(figsize=(6, 3))

# Plot
sns.set_color_codes("muted")
sns.despine(left=True, bottom=True)
sns.barplot(x=overall_prevalence.index,
            y=overall_prevalence.values,
            label="Dengue prevalence",
            color="b",
            linewidth=0.75)

# Add a legend and informative axis label
ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(xlabel="", ylabel="Prevalence (%)",
       title="Overall dengue prevalence in HTD")