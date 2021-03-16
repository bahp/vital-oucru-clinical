"""
Daily biomarker per dengue_interpretation (admission)
======================================================

.. todo:: Full explanation

"""

# Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams

# DataBlend library
from datablend.core.repair.correctors import oucru_dengue_interpretation_feature
from datablend.core.repair.correctors import day_from_day_values

# -----------------------------------
# Configuration
# -----------------------------------
# Configure
#sns.set_theme(style="ticks", palette="pastel")

# Seaborn
#sns.set_theme(style="whitegrid")


# Update
rcParams.update(
    {'font.size': 9,
     'axes.labelsize': 'large',
     'ytick.labelsize': 'large',
     'xtick.labelsize': 'large'
     })

# -----------------------------------
# Methods
# -----------------------------------

# -----------------------------------
# Constants
# -----------------------------------
# Path with data
path_data = '../../../resources/data//20210313-v0.8/'
path_data+= 'combined/combined_tidy.csv'


rename = {
    'haematocrit_percent': 'hct',
    'respiratory_rate': 'rr'
}

NRR = {
    'plt': [140, 350],
    'haematocrit_percent': [35, 49],
    'albumin': [35, 55],
    'wbc': [3.5, 9.0]
}

FEATURES = [
    'plt',                   # keep
    'haematocrit_percent',   # keep
    # 'haemoglobin',         # too binary
    'albumin',               # keep
    'alt',                   # keep
    'ast',                   # keep
    'wbc',                   # keep
    # 'creatine_kinase',     # only beginning
    # 'lymphocytes',   # only beginning
    # 'monocytes',     # only beginning
    # 'neutrophils',   # only beginning
    # 'creatinine',    # so so
    # 'crp',           # not much data
    # 'procalcitonin', # not much data
    # 'sbp',           # too binary
    # 'dbp',           # too binary
    # 'pulse',
    # 'pulse_pressure',
    # 'respiratory_rate',
    # 'body_temperature',
    # 'spo2_percent',
]

# The due to separate
HUE = 'dengue_interpretation'

# The day column to use
#   - day_from_onset
#   - day_from_admission
#   - day_from_enrolment
#   - day_from_illness (manually inputed by clinicians)
DAY_COLUMN = 'day_from_admission'

# ------------------------------
# Load data
# ------------------------------
# Load data
original = pd.read_csv(path_data,
    index_col=0,
    low_memory=False,
    #nrows=1000000,
    parse_dates=['date'])

# Copy data
data = original.copy(deep=True)
data = data.convert_dtypes()

# Create dengue interpretation
data['dengue_interpretation'] = \
    oucru_dengue_interpretation_feature(data,
        pcr=True, ns1=True, igm=True, serology=True,
        single_igm_igg=True, paired_igm_igg=True,
        default=False)

# Need to remove outliers earlier on!
idxs = data.plt > 1000
data.loc[idxs, 'plt'] = None


"""
# Correct day from illness
# TOO SLOW!
aux = \
    data.groupby('study_no') \
        .apply(day_from_day_values) \
        .droplevel(level=0, axis=0) \
        .dt.days
"""

# Create day for x-axis.
data['day'] = data[DAY_COLUMN]
data.day = data.day.fillna(-2000).astype(int)
data = data[data.day.between(0, 20)]

# Drop columns with all NaN.
data = data.dropna(how='all', axis=1)

# Show information
print("\nDengue count:")
print(data.dengue_interpretation.value_counts())

# Rename this variables...
a =  data[FEATURES + ['day', 'dengue_interpretation']]
a = a.groupby(by=['day', 'dengue_interpretation']).count().unstack()

b =  data[FEATURES + ['day', 'dsource']]
b = b.groupby(by=['day', 'dsource']).count().unstack()

# --------------------------------
# Plot the biomarker distributions
# --------------------------------
# .. note:: Could this be done nicely without a loop by using
#           some of the seaborn functionality such as the
#           FaceGrid? Note we can also incorporate the hue.

# Loop
for i, c in enumerate(FEATURES):

    # Draw
    print("  Drawing... %s." % c)

    # Create figure
    fig, ax = \
        plt.subplots(1, 1, figsize=(8, 5))

    # Configuration and plot
    sns.set_color_codes("muted")
    sns.boxplot(x=data.day, y=data[c], whis=1.5,
                hue='dengue_interpretation',
                fliersize=0, showfliers=False,
                linewidth=0.75, saturation=0.75,
                palette='Set3', data=data, ax=ax)

    # Draw normal reference range
    if c in NRR:
        ax.fill_between(x=sorted(data.day.values),
             y1=NRR[c][0], y2=NRR[c][1], color='#D3D3D3',
             alpha=0.25, zorder=0)

    # Create aux table for visualization
    aux = a[c].T.astype(str).replace({'nan': '-'})

    # Draw table
    table = plt.table(cellText=aux.to_numpy(),
                      rowLabels=aux.index,
                      colLabels=aux.columns,
                      cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(1, 3.2)

    # Sns plot config
    sns.despine(left=True, bottom=True)

    # Configure axes
    ax.set(xlabel="", xticks=[], xticklabels=[],
        title='<{0}> distribution group by <{1}> for <{2}>' \
            .format(c, HUE, DAY_COLUMN))
    #axes[i].get_legend().remove()

    # Adjust subplots
    #plt.legend(loc='upper left')
    plt.subplots_adjust(left=0.08, bottom=0.4, right=0.95)
    #plt.tight_layout()


##########################################################################
# Lets plot the ``overall`` count of samples for each dataset and day. Note
# that some datasets (13dx and md) have a much larger number of patients
# and therefore the colors are "biased" towards them.
#

# Configuration
n_cols = 2
n_rows = round(len(FEATURES) / n_cols)

# -----------------------
# Plot heatmaps
# ----------------------
# Create figure
f, axes = plt.subplots(n_rows, n_cols,
    figsize=(14, 8), sharex=True, sharey=True)

# Flatten
axes = axes.flatten()

# Loop
for i, f in enumerate(FEATURES):

    # Show
    print("\n\n%s:" % f)
    print(b[f].T)

    # Draw a heatmap with the numeric values in each cell
    sns.heatmap(b[f].T, annot=True, fmt='.0f',
        annot_kws={'fontsize': 8}, linewidths=.5,
        ax=axes[i], cmap=sns.cm.rocket_r)

    # Configure axes
    axes[i].set(xlabel="", title='<%s>' % f)

# Adjust
plt.tight_layout()



##########################################################################
# Lets plot the ``normalized`` count of samples for each individual dataset
# and the corresponding day
#

# -----------------------
# Plot heatmaps
# ----------------------
# Create figure
f, axes = plt.subplots(n_rows, n_cols,
    figsize=(14, 8), sharex=True, sharey=True)

# Flatten
axes = axes.flatten()

# Loop
for i, f in enumerate(FEATURES):

    # Compute normalised
    norm = b[f].divide(b[f].max()).T

    # Print
    print("\n\n%s:" % f)
    print(norm)

    # Draw a heatmap with the numeric values in each cell
    sns.heatmap(norm*100, annot=True, fmt='.0f',
        annot_kws={'fontsize': 8}, linewidths=.5,
        ax=axes[i], cmap=sns.cm.rocket_r)

    # Configure axes
    axes[i].set(xlabel="", title='<%s>' % f)

# Adjust
plt.tight_layout()

# Plot
plt.show()

a = 0