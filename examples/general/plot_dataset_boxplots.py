# Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Specific libraries
from pathlib import Path

# -----------------------------------
# Configuration
# -----------------------------------
# Configure
#sns.set_theme(style="ticks", palette="pastel")

# Seaborn
sns.set_theme(style="whitegrid")
# Configure
sns.set_theme(style="ticks", palette="pastel")

# Update
rcParams.update(
    {'font.size': 7,
     'axes.labelsize': 'large',
     'ytick.labelsize': 'small',
     'xtick.labelsize': 'small'
     })

# -----------------------------------
# Methods
# -----------------------------------

# -----------------------------------
# Constants
# -----------------------------------
# Path with data
path_data = Path('../../resources/data/20210309-v0.7/combined/combined_tidy.csv')

# Columns
cols = ['plt',
        'alt',
        'age',
        'sbp',
        'dbp',
        'pulse', 'respiratory_rate', 'date', 'dsource']

"""
spo2_percent
body_temperature

albumin
alt
ast
creatine_kinase
haemoglobin
lymphocytes
monocytes
neutrophils
haematocrit_percent
lymphocytes_percent
monocytes_percent
neutrophils_percent
plt
wbc
sodium
creatinine
crp
procalcitonin
"""

# ------------------------------
# Load data
# ------------------------------
# Load data
original = pd.read_csv(path_data,
    index_col=0,
    #usecols=cols,
    parse_dates=['date'])
    #nrows=10000)

# Copy data
data = original.copy(deep=True)
data = data.convert_dtypes()
data = data.select_dtypes(include=['Int64', 'Float64'])
data = data.dropna(how='all', axis=1)

# Count
count = data.count()
count = count[count > 10000]

# Filter
data = data[count.index.values]


# Ignore columns
#data = data

n_cols = 10
n_rows = round(data.shape[1] / n_cols) + 1

"""


# We should pivot with pd.melt to be able to
# keep both the result value and the dsource.
#data['dsource'] = original['dsource']

# Set into stacked format
stacked = data.copy(deep=True)
stacked = stacked.drop(columns=['dsource', 'date'])
stacked = stacked.stack().to_frame()
stacked = stacked.reset_index()
stacked.columns = ['index', 'column', 'result']
"""
# -------------------------------------------
# Compare distributions for numeric variables
# -------------------------------------------

# --------------------------
# Sample I
# --------------------------
# .. note:: Not working, dsource not used as hue.
# Create figure
fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 9))
axes = axes.flatten()

# Loop
for i, c in enumerate(data.columns.unique()):

    if c == 'dsource':
        continue
    if c == 'date':
        continue
    # Sns plot config
    sns.despine(left=True, bottom=True)
    sns.set_color_codes("muted")
    sns.boxplot(y=c, whis=1.5, fliersize=0,
        showfliers=False,
        linewidth=0.75, saturation=0.75,
        data=data, ax=axes[i])
    axes[i].set(xlabel="", xticklabels=[], xticks=[])
"""
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
"""


# Add a legend and informative axis label
#ax.set(xlabel="", ylabel="Prevalence (%)",
#       title="Monthly dengue prevalence in HTD")

# Format
#plt.tight_layout()
plt.subplots_adjust(left=0.06, right=0.94, wspace=10)
plt.show()

import sys
sys.exit()

# --------------------------
# Sample II
# --------------------------
# Create grid
grid = sns.FacetGrid(stacked, col="column",
    hue="column", palette="tab20c", sharex=False,
    sharey=False, col_wrap=6, height=1.5)

# Display strip (boxplot not allowed).
grid.map(sns.stripplot, "result")

# Format
plt.tight_layout()

# --------------------------
# Sample III
# --------------------------

# Create figure
plt.figure()

# Draw a nested boxplot
sns.boxplot(x="column", y="result", whis=1.5,
            data=stacked)
# Format
sns.despine(offset=10, trim=True)

# Format
#plt.title(idx)
plt.tight_layout()


"""
fig, axes = plt.subplots(7, 7)
axes = axes.flatten()

for i, c in enumerate(data.columns.unique()):

    sns.boxenplot(x=c, y="result", whis=1.5,
                data=data, axes=axes[i])
"""

# Show
plt.show()


# ----
sns.pairplot(data[['plt', 'alt', 'age', 'dsource']])