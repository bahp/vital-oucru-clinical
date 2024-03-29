"""
Monthly prevalence (yearly)
===========================

This example computes the prevalence of dengue in the ``HTD`` as the
proportion of patients which were diagnosed with Dengue based on any
positive result for the ``NS1``, ``PCR`` or ``serology`` tests for
each year from 1999 to 2021.

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
def prevalence(x):
    return (np.sum(x) / len(x)) * 100


# ---------------------------------
# Constants
# ---------------------------------
# The data filepath
path = '../../resources/data/20210313-v0.0.8/combined/combined_tidy.csv'

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

# These datasets do not have pcr_dengue_serotype.
data = data[~data.dsource.isin(['01nva', '42dx'])]

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
# ------------------
# Compute prevalence
prevalence = patients.reset_index() \
    .groupby(by=['month', 'year']).agg( \
        prevalence=('dengue_interpretation', prevalence),
        n_patients=('study_no', 'count'))

# Drop extremes
#idxs = prevalence.prevalence.between(0.01, 99.9)

# Clean for plotting
prevalence = prevalence.reset_index()
#prevalence = prevalence[idxs]

# Format month
#prevalence.month = prevalence.month.apply(
#    lambda x: calendar.month_abbr[x])

# Create tables
table_prevalence = pd.pivot_table(prevalence,
    index=['year'], values='prevalence', columns=['month'])
table_npatients = pd.pivot_table(prevalence,
    index=['year'], values='n_patients', columns=['month'])

# Month numbers to abbr
def month_abbr(v):
    return [calendar.month_abbr[x] for x in v]

table_prevalence.columns = month_abbr(table_prevalence.columns)
table_npatients.columns = month_abbr(table_npatients.columns)
prevalence.month = month_abbr(prevalence.month)

# Show
print("\n")
print(prevalence)
print("\nPrevalence table:")
print(table_prevalence.round(2))
print("\n#Patients table:")
print(table_npatients.round(0))


###############################################################
# Lets plot the ``boxplot`` with the monthly dengue prevalence per
# year. The x-axis represents the month and the y-axis the prevalence
# in %. In addition, to the distribution (boxplot) the single markers
# have been displayed.

# --------------------------
# Plot boxplot
# --------------------------
# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(6, 3))

# Draw boxplot
sns.boxplot(x="month", y="prevalence",
    data=prevalence, whis=[0, 100], width=.6,
    linewidth=0.75, palette="vlag")

# Draw each observation
sns.stripplot(x="month", y="prevalence",
    data=prevalence, dodge=True,
    linewidth=0.2, palette='vlag')

# Sns plot config
sns.despine(left=True, bottom=True)

# Add a legend and informative axis label
ax.set(xlabel="", ylabel="Prevalence (%)",
       title="Monthly dengue prevalence in HTD")

###############################################################
# Let's create the same figure but adding the prevalence values
# in a ``table`` below.

# ----------------------
# Plot boxplot and table
# ----------------------
# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(6, 6))

# Draw boxplot
sns.boxplot(x="month", y="prevalence",
    data=prevalence, whis=[0, 100], width=.6,
    linewidth=0.75, palette="vlag")

# Draw each observation
sns.stripplot(x="month", y="prevalence",
    data=prevalence, dodge=True,
    linewidth=0.2, palette='vlag')

# Sns plot config
sns.despine(left=True, bottom=True)

# Create aux table for visualization
aux = table_prevalence.round(2)\
    .astype(str).replace({'nan': '-'})

# Draw table
table = plt.table(cellText=aux.to_numpy(),
                  rowLabels=aux.index,
                  colLabels=aux.columns,
                  cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(7.5)
table.scale(1, 3.2)

# Sns config
sns.despine(left=True, bottom=True)

# Add a legend and informative axis label
ax.set(xlabel='', ylabel='Prevalence (%)', xticks=[],
       title="Monthly dengue prevalence in HTD")

# Adjust subplots
plt.subplots_adjust(left=0.2, bottom=0.65)

###################################################################
# Lets plot the ``heatmaps`` with (i) the monthly dengue prevalence
# per year and (ii) the number of patients with/without dengue used
# to compute such prevalence. It is important to highlight that
# in previous plots some extreme prevalence values (either 0% or
# 100%) where found. As shown in the figure below, these correspond
# to months in which there are not enough patients (<4) to
# accurately describe the prevalence.
#
#

# -----------------------
# Plot heatmaps
# ----------------------
# Create figure
f, ax = plt.subplots(1, 2, figsize=(14, 6))
ax = ax.flatten()

# Draw a heatmap with the numeric values in each cell
sns.heatmap(table_prevalence, annot=True, fmt='.2f',
    annot_kws={'fontsize': 8}, linewidths=.5, ax=ax[0],
    cmap=sns.cm.rocket_r)

# Configure axes
ax[0].set(title="Monthly dengue prevelence (%) in HTD")

# Draw a heatmap with the numeric values in each cell
sns.heatmap(table_npatients, annot=True, fmt='.0f',
    annot_kws={'fontsize': 10}, linewidths=.5, ax=ax[1],
    cmap=sns.cm.rocket_r)

# Configure axes
ax[1].set(title="Number of patients (study) in HTD")

# Adjust layout
plt.tight_layout()


###############################################################
# If we want to check whether the number of patients is directly
# affecting the prevalence seen in the HTD hospital we can plot
# their correlation (e.g.) as shown in the picture there is no
# strong linear correlation between the number of patients and
# the prevalence.

# ----------------
# Plot correlation
# ----------------
# Create figure
f, ax = plt.subplots(1, 1, figsize=(4, 4))

# Palette
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Mask
mask = np.triu(np.ones_like(prevalence.corr(), dtype=np.bool))

# Draw heatmap
sns.heatmap(prevalence.corr()*100, cmap=cmap, center=0,
    mask=mask, vmax=100, vmin=-100, square=True, linewidths=0.5,
    cbar_kws={'shrink':.5}, annot=True, fmt=".0f",
            annot_kws={"size": 10})

# Configure axes
ax.set(title="Correlation")

# Show
plt.show()