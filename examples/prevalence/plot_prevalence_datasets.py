"""
Prevalence per dataset
======================

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
import matplotlib.dates as mdates

# Configure
sns.set_style("whitegrid", {
    "ytick.major.size": 0.1,
    "ytick.minor.size": 0.05,
    'grid.linestyle': '--'
})

# Seaborn
sns.set_theme(style="whitegrid")


# ---------------------------------
# Methods
# ---------------------------------
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
# The data filepath
path = '../../resources/data/20210601-v0.1/combined/combined_tidy.csv'

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

# These datasets do not have pcr_dengue_serotype.
data = data[~data.dsource.isin(['01nva', '42dx'])]

# Define positive dengue
data = dengue_interpretation(data)

# Overall outcome for patient
patients = data.groupby('study_no').max()
patients['month'] = patients.date.dt.month
patients['year'] = patients.date.dt.year

# Show
print("\nPatients:")
print(patients)


def prevalence(x):
    return (np.sum(x) / len(x)) * 100


aux = patients.reset_index() \
    .groupby([pd.Grouper(key='date', freq='M'), 'dsource']) \
    .agg(prevalence=('dengue', prevalence),
         n_patients=('study_no', 'count')).reset_index()

# Show
print("\nTable")
print(aux)


def label(x, color, label):
    ax = plt.gca()
    ax.text(0, .2, label, fontweight="bold",
        color=color, ha="left", va="center",
        transform=ax.transAxes)

# Create palette
pal = sns.cubehelix_palette(10, rot=-.25, light=.7)


# ---------------------------
# Plot prevalence
# ---------------------------
# Create facetgrid
g1 = sns.FacetGrid(aux, row='dsource', hue='dsource',
    height=1, sharex=True, aspect=15, palette=pal)

# Plot lines
g1.map(sns.lineplot, "date", "prevalence")

# Configure axes
g1.map(plt.axhline, y=0, lw=2, clip_on=False)
g1.map(label, "dsource")
g1.map(plt.fill_between, "date", "prevalence")

# Configure axes
g1.set_titles("")
g1.set(yticks=[25, 50, 75, 100], ylabel='', xlabel='')
g1.despine(bottom=True, left=True)
g1.fig.subplots_adjust(hspace=0.02)

# Configure ticks
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
ax.xaxis.set_minor_formatter(mdates.DateFormatter("%Y"))

# Suptitle
plt.suptitle('Monthly prevalence (%) by dataset')


# ---------------------------
# Plot n_patients
# ---------------------------
# Create facetgrid
g2 = sns.FacetGrid(aux, row='dsource', hue='dsource',
    height=1, sharex=True, aspect=15, palette=pal)

# Plot lines
g2.map(sns.lineplot, "date", "n_patients")

# Plot extra
g2.map(plt.axhline, y=0, lw=2, clip_on=False)
g2.map(label, "dsource")
g2.map(plt.fill_between, "date", "n_patients")

# Configure axes
g2.set_titles("")
g2.set(yticks=[100, 200, 300, 400], ylabel='', xlabel='')
g2.despine(bottom=True, left=True)
g2.fig.subplots_adjust(hspace=0.02)

# Configure ticks
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
ax.xaxis.set_minor_formatter(mdates.DateFormatter("%Y"))

# Sup title
plt.suptitle('Monthly #Patients by dataset')

# Show
plt.show()