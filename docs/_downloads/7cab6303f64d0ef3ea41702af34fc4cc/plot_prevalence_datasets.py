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

# DataBlend library
from datablend.core.repair.correctors import oucru_dengue_interpretation_feature

# Seaborn
sns.set_theme(style="whitegrid")


# ---------------------------------
# Methods
# ---------------------------------
def prevalence(x):
    return (np.sum(x) / len(x)) * 100

def label(x, color, label):
    ax = plt.gca()
    ax.text(0, .2, label, fontweight="bold",
        color=color, ha="left", va="center",
        transform=ax.transAxes)


# ---------------------------------
# Constants
# ---------------------------------
# The data filepath
# The data filepath
path = '../../resources/data/20210106-v0.1/combined/combined_tidy.csv'

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

# Add dengue interpretation
data['dengue_interpretation'] = \
    oucru_dengue_interpretation_feature(data,
        pcr=True, ns1=True, igm=True,
        paired_igm_igg=True, default=False)

# Overall outcome for patient
patients = data.groupby('study_no').max()
patients['month'] = patients.date.dt.month
patients['year'] = patients.date.dt.year

# Show
print("\nPatients:")
print(patients)

# Compute prevalence
aux = patients.reset_index() \
    .groupby([pd.Grouper(key='date', freq='M'), 'dsource']) \
    .agg(prevalence=('dengue_interpretation', prevalence),
         n_patients=('study_no', 'count')).reset_index()

# Show
print("\nTable")
print(aux)

# Create palette
pal = sns.cubehelix_palette(10, rot=-.25, light=.7)

# ---------------------------
# Plot prevalence
# ---------------------------
# Configure
sns.set_style("whitegrid", {
    "ytick.major.size": 0.1,
    "ytick.minor.size": 0.05,
    'grid.linestyle': '--'
})

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
# Configure
sns.set_style("whitegrid", {
    "ytick.major.size": 0.1,
    "ytick.minor.size": 0.05,
    'grid.linestyle': '--'
})

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