"""
Dengue - ANN
=============

.. todo:: Full explanation

.. todo:: Use column transformer.

    ctf = ColumnTransformer(
        [('gender', LabelBinarizer())]
    )

    data = ctf.fit_transform(data)

"""


# Libraries
import os
import sys
import calendar
import numpy as np
import pandas as pd
#import modin.pandas as pd

# Libraries imblearn
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE

# Libraries sklearn
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelBinarizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import make_scorer
from sklearn.metrics import confusion_matrix
from sklearn.metrics import recall_score
from sklearn.metrics import roc_auc_score

# Import DataBlend
from datablend.core.repair.correctors import oucru_dengue_interpretation_feature
from datablend.core.repair.correctors import static_correction

# ---------------------------------
# Methods
# ---------------------------------
def cvs_hos_split(data, **kwargs):
    """This method labels the dataframe hos and cvs sets.

    Parameters
    ----------
    data: np.array or pd.DataFrame
        The data to be divided into HOS/CVS.

    Returns
    -------
    np.array:
        The outcome is a numpy array with rows labelled as
        cvs (cross-validation set) and hos (hold-out set).
    """
    # Length
    r, c = data.shape

    # Create indexes to use for splitting
    idxs = np.arange(r).reshape(-1, 1)

    # Split in hos and training sets
    cvs, hos = train_test_split(idxs, **kwargs)

    # Create result
    empty = np.array([None] * data.shape[0])
    empty[cvs] = 'cvs'
    empty[hos] = 'hos'

    # Convert to series
    if isinstance(data, pd.DataFrame):
        empty = pd.Series(index=data.index, data=empty)

    # Return
    return empty

# .. note: This is computationally expensive because it
#          calls the same method (confusion_matrix) four
#          times. But scorer functions need to be created
#          for GridSearchCV.

def tp(y, y_pred, **kwargs):
    """Return the true positives"""
    tn, fp, fn, tp = confusion_matrix(y, y_pred).ravel()
    return tp

def tn(y, y_pred, **kwargs):
    """Return the true negatives"""
    tn, fp, fn, tp = confusion_matrix(y, y_pred).ravel()
    return tn

def fp(y, y_pred, **kwargs):
    """Return the false positives"""
    tn, fp, fn, tp = confusion_matrix(y, y_pred).ravel()
    return fp

def fn(y, y_pred, **kwargs):
    """Return the false negatives"""
    tn, fp, fn, tp = confusion_matrix(y, y_pred).ravel()
    return fn


# ---------------------------------
# Constants
# ---------------------------------
# The data filepath
path = '../../../resources/data/20210313-v0.0.8/'
path+= 'combined/combined_tidy.csv'

# Features
features = sorted([#'age',
                   #'gender',
                   'plt',
                   'haematocrit_percent'])

# Usecols
usecols = ['date', 'study_no', 'dsource',
    'day_from_admission', 'pcr_dengue_serotype',
    'pcr_dengue_load', 'ns1_interpretation',
    'igm_interpretation', 'igg_interpretation',
    'serology_single_interpretation',
    'serology_paired_interpretation',
    'day_from_admission', 'day_from_illness',
    'shock', 'shock_multiple', 'age', 'gender']
usecols+= features

# ---------------------------------
# Main
# ---------------------------------

# ---------
# Load data
# ---------
# Read data
data = pd.read_csv(path,
    low_memory=False,
    #nrows=20000,
    usecols=usecols,
    parse_dates=['date'])

# Reset index
data = data.reset_index()

# Remove columns with all NaN
data = data.dropna(how='all', axis=1)
data = data.dropna(how='any', subset=features)
#data = data[data.dsource.isin(['13dx'])]

# Remove outliers
def quantile_filter(data, column, qlow, qhigh):
    return data[data[column].between(
        data[column].quantile(qlow),
        data[column].quantile(qhigh)
    )]

# Add dengue interpretation
data['dengue_interpretation'] = \
    oucru_dengue_interpretation_feature(data,
        pcr=True, ns1=False, igm=False, serology=False,
        single_igm_igg=False, paired_igm_igg=False,
        default=False)

# Create outcome
data['outcome'] = \
    data.dengue_interpretation.astype(int)

# Add month
data['month'] = data.date.dt.month

# -----------
# Format data
# -----------
# Keep only day_from_admission == 0 data
data = data[data.day_from_admission.isin(range(2))]

# Keep only certain months
#data = data[data.month.isin([2, 3, 4])]

# Drop any without interpretation
data = data[~data.outcome.isna()]

if 'gender' in data:
    # Do this with sklearn column transformer
    data.gender = data.gender.replace({'Male': 0, 'Female': 1})

print(data)


# ----------
# Approach I
# -----------
# Interesting columns
interesting = ['study_no', 'day_from_admission']
interesting+= features

# Pivot
aux = pd.pivot_table(data[interesting],
    index='study_no',
    values=features,
    columns='day_from_admission')

# Data
aux = aux.dropna(how='any')



for f in['haematocrit_percent', 'plt']:
    aux.loc[:, '%s_diff' % f] = \
        aux.loc[:, (f, 1.0)] - aux.loc[:, (f, 0.0)]

# Rename
aux.columns = ['%s%s' % (a, '_%s' % b if b else '') \
    for a, b in aux.columns]


data = aux.merge(data[['study_no',
                       'outcome',
                       'dsource',
                       'age',
                       'gender']].drop_duplicates(),
                on='study_no', how='left')



features = ['age',
            'gender',
            'haematocrit_percent',
            'haematocrit_percent_1.0',
            #'haematocrit_percent_diff',
            'plt',
            'plt_1.0',
            #'plt_diff'
            ]
print(data)


# Data
data = data.dropna(how='any', subset=features)


# -----------
# Add splits
# -----------
data['sets'] = cvs_hos_split(data, stratify=data.outcome)

# Show information
print("\n\nData rows: %s" % data.shape[0])
print("\nby dsource:")
print(data.dsource.value_counts())
print("\nby outcome:")
print(data.outcome.value_counts(dropna='False'))
print("\nby sets:")
print(data.sets.value_counts(dropna='False'))
print("\n")


# ----------
# Train
# ----------
# Estimator
estimator = MLPClassifier()

param_grid = {
    'ann__hidden_layer_sizes': [ (100, 100) ],
    'ann__activation': ['relu'],
    'ann__solver': ['adam'],
    'ann__alpha': [0.001],
    'ann__batch_size': ['auto'],
    'ann__learning_rate': ['constant'],
    'ann__learning_rate_init': [0.001],
    'ann__power_t': [0.5],
    'ann__max_iter': [10000],
    'ann__tol': [1e-4],
    'ann__warm_start': [False],
    'ann__momentum': [0.9],
}

# Scoring
scoring = {
    'aucroc': 'roc_auc',
    'sensitivity': make_scorer(recall_score),
    'specificity': make_scorer(recall_score, pos_label=0),
    #'tp': make_scorer(tp),
    #'tn': make_scorer(tn),
    #'fp': make_scorer(fp),
    #'fn': make_scorer(fn),
}

# Create pipeline
pipe = Pipeline(steps=[('smt', SMOTE(random_state=42)),
                       ('std', StandardScaler()),
                       ('ann', estimator)],
                memory='./outputs',
                verbose=True)

# Create k-folds
kf = StratifiedKFold(n_splits=5, random_state=42, shuffle=True)

# Create grid search
grid = GridSearchCV(pipe, cv=kf, scoring=scoring,
    param_grid=param_grid, return_train_score=True,
    refit='aucroc')

# Define
features = features
target = 'outcome'

# Get train data
train = data[data.sets == 'cvs']
train = train[features + [target]]
#train = train.dropna(how='any') # done already

# Get X and y
X = train[features].to_numpy()
y = train[target].to_numpy()

# Fit
grid.fit(X, y);

# ----------------
# Show scores
# ----------------
# Show results
results = pd.DataFrame(grid.cv_results_)

#print("\nResult columns:")
#print(results.columns.values)
print("\n\nGrid Search ALL scores (CVS):")
print(results.round(decimals=3).T)

# Select columns
columns = [c for c in results.columns if 'param_' in c]
columns+= [c for c in results.columns if 'mean_' in c]
columns = sorted(columns)

# Show
print("\nGrid Search MEAN scores (CVS):")
print(results[columns].round(decimals=3).T)

# -------------------
# Best estimator
# -------------------
# .. note: It is possible to evaluate the estimator
#          only in HOS. In addition, we would like to
#          see how the predictions and metrics vary
#          according to the seasonality.
# Get best estimator
best_estimator = grid.best_estimator_

# -----------------
# Evaluation in HOS
# -----------------
# Evaluate best estimator on HOS
hos = data[data.sets == 'hos']

# Get X and y
X = hos[features].to_numpy()
y = hos[target].to_numpy()

# Do predictions
y_pred = best_estimator.predict(X)
y_score = best_estimator.predict_proba(X)

# Scores
aucroc = roc_auc_score(y, y_score[:, 1])
sensitivity = recall_score(y, y_pred)
specificity = recall_score(y, y_pred, pos_label=0)

# Create series
series = pd.Series(\
    index=['AUCROC', 'Sensitivity', 'Specificity'],
    data=[aucroc, sensitivity, specificity])

# Show
print("\nBest estimator HOS scores:")
print(series.round(decimals=3))

# --------------------------------
# Evaluation of seasonality effect
# --------------------------------
# Get X and y
X = data[features].to_numpy()
y = data[target].to_numpy()

# Add columns to data
data['y_pred'] = best_estimator.predict(X)
data['y_score'] = best_estimator.predict_proba(X)[:, 1]

#
def _aucroc(x):
    try:
        return roc_auc_score(x.outcome, x.y_score)
    except:
        return None

def _sens(x):
    try:
        return recall_score(x.outcome, x.y_pred)
    except:
        return None

def _spec(x):
    try:
        return recall_score(x.outcome, x.y_pred, pos_label=0)
    except:
        return None

def prevalence(x):
    return (np.sum(x) / len(x)) * 100

# Outputs
aucroc = data.groupby('month').apply(_aucroc)
sensitivity = data.groupby('month').apply(_sens)
specificity = data.groupby('month').apply(_spec)
prevalence = data.groupby('month').outcome.apply(prevalence)

# Scores
scores = pd.DataFrame()
scores['aucroc'] = aucroc * 100
scores['sens'] = sensitivity * 100
scores['spec'] = specificity * 100
scores['prevalence'] = prevalence
scores['n'] = data.groupby('month').study_no.count()
#scores['sens_prev_ratio'] = scores.sens / scores.prevalence
#scores['spec_prev_ratio'] = scores.spec / scores.prevalence
#scores['spec_prev_ratio'] = scores.spec / scores.prevalence
#scores['spec_n_ratio'] = scores.spec / scores.n
scores = scores.round(decimals=3)

print(scores)

# Add legible labels
scores.index = \
     [calendar.month_abbr[x] for x in scores.index]

# Create stacked version (seaborn)
scores_stacked = scores.stack().reset_index()
scores_stacked.columns = ['month', 'metric', 'result']

# Show
print("\nMonthly scores:")
print(scores)

print("\nMonthly scores (stacked):")
print(scores_stacked)

print("\nCorrelation with prevalence (pearson):")
print(scores.corr()[['prevalence', 'n']])
print("\nCorrelation with prevalence (spearman):")
print(scores.corr(method='spearman')[['prevalence', 'n']])

# ------------------------------------------------
# Plot
# ------------------------------------------------
# Libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Seaborn
sns.set_theme(style="whitegrid")


# --------------
# Plot FacetGrid
# --------------
"""
sns.set_color_codes("muted")
sns.despine(left=True, bottom=True)

# Create facet grid
g = sns.FacetGrid(scores_stacked,
    col="metric", col_wrap=3, sharey=False,
    aspect=1.5)

# Plot sns plots
g.map_dataframe(sns.barplot, x="month",
    y="result", linewidth=0.76)
"""

# ---------------
# Plot main
# ---------------
# Colors
colors = ['b', 'g', 'r', 'b']

# Initialize the figure
f, axes = plt.subplots(1, 4, figsize=(12, 2.5), sharey=True)
axes = axes.flatten()

# Plot
for i, c in enumerate(['aucroc', 'sens', 'spec', 'prevalence']):

    # Plot barplot
    sns.despine(left=True, bottom=True)
    sns.barplot(x=scores.index,
             y=scores[c],
             label=c,
             color=colors[i],
             ax=axes[i],
             linewidth=0.75)

    # Add a legend and informative axis label
    axes[i].legend(ncol=2, loc="lower right", frameon=True)
    axes[i].set(xlabel="", ylabel="",
        title="%s in HTD by month" % c)

# Tight layout
plt.tight_layout()


# ---------------------------
#
# ---------------------------
aux = data[data.day_from_illness.between(0, 10)]
aux.day_from_illness = aux.day_from_illness.round()

# Outputs
aucroc = aux.groupby('day_from_illness').apply(_aucroc)
sensitivity = aux.groupby('day_from_illness').apply(_sens)
specificity = aux.groupby('day_from_illness').apply(_spec)
#prevalence = data.groupby('day_from_illness').outcome.apply(prevalence)

# Scores
scores = pd.DataFrame()
scores['aucroc'] = aucroc * 100
scores['sens'] = sensitivity * 100
scores['spec'] = specificity * 100
#scores['prevalence'] = prevalence
scores['n'] = data.groupby('day_from_illness').study_no.count()
#scores['sens_prev_ratio'] = scores.sens / scores.prevalence
#scores['spec_prev_ratio'] = scores.spec / scores.prevalence
#scores['spec_prev_ratio'] = scores.spec / scores.prevalence
#scores['spec_n_ratio'] = scores.spec / scores.n
scores = scores.round(decimals=3)
scores = scores.dropna(how='any')
print(scores)


# Create figure
fig, ax = plt.subplots(1, 1, figsize=(6, 7))

# Plot the three main scores
ax = scores[['aucroc', 'sens', 'spec']].plot(ax=ax,
    marker='o', markersize=3, linewidth=0.75)

#  Configure axes
ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(xlabel="", ylabel="", ylim=[0, 100],
    xticklabels=[],
    title="metrics by day_of_illness")
ax.grid(b=True, which='both', axis='both',
        linestyle='dashed', linewidth=0.75, color='gray')

# Create aux table for visualization
aux = scores.round(2) \
    .astype(str).replace({'nan': '-'})

# Draw table
table = plt.table(cellText=aux.T.to_numpy(),
                  rowLabels=aux.T.index,
                  colLabels=aux.T.columns,
                  cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(7.5)
table.scale(1, 1.5)

# Sns config
sns.despine(left=True, bottom=True)

# Adjust subplots
plt.subplots_adjust(left=0.2, bottom=0.25)




"""
# --------------------
# Plot others
# --------------------
# Initialize the figure
f, axes = plt.subplots(1, 4, figsize=(12, 2.5))
axes = axes.flatten()

# Plot
for i, c in enumerate(['aucroc',
                       'sens',
                       'spec']):

    # Plot barplot
    sns.despine(left=True, bottom=True)
    sns.barplot(x=scores.index,
             y=scores[c] / scores.prevalence,
             label=c,
             color='b',
             ax=axes[i],
             linewidth=0.75)

    # Add a legend and informative axis label
    axes[i].legend(ncol=2, loc="lower right", frameon=True)
    axes[i].set(xlabel="", ylabel="",
        title="%s in HTD by month" % c)

plt.tight_layout()
"""

plt.show()
