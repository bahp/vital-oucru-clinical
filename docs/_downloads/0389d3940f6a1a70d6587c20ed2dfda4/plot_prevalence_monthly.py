"""
Yearly monthly prevalence
=========================

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


# Compute prevalence
# ------------------
# Compute prevalence
prevalence = patients.reset_index() \
    .groupby(by=['month', 'year']).agg( \
        prevalence=('dengue', prevalence),
        n_patients=('study_no', 'count'))

# Drop extremes
#idxs = prevalence.prevalence.between(0.01, 99.9)

# Clean for plotting
prevalence = prevalence.reset_index()
#prevalence = prevalence[idxs]

# Format month
prevalence.month = prevalence.month.apply(
    lambda x: calendar.month_abbr[x])

# Create tables
table_prevalence = pd.pivot_table(prevalence,
    index=['year'], values='prevalence', columns=['month'])
table_npatients = pd.pivot_table(prevalence,
    index=['year'], values='n_patients', columns=['month'])

# Show
print("\n")
print(prevalence)
print("\nPrevalence table:")
print(table_prevalence.round(2))
print("\n#Patients table:")
print(table_npatients.round(0))


###############################################################
# Lets plot the boxplot with the monthly dengue prevalence per
# year. In addition, let's add the prevalence values in a table
# below.

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
table.set_fontsize(8)
table.scale(1, 3.2)

# Sns config
sns.despine(left=True, bottom=True)

# Add a legend and informative axis label
ax.set(xlabel='', ylabel='Prevalence (%)', xticks=[],
       title="Monthly dengue prevalence in HTD")

# Adjust subplots
plt.subplots_adjust(left=0.2, bottom=0.6)

###############################################################
# Lets plot the heatmaps with (i) the monthly dengue prevalence
# per year (ii) the number of patients with/without dengue used
# to compute such prevalence.

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

# Show
plt.show()