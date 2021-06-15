# Libraries
import pandas as pd

# Library DataBlend
#from datablend.core.repair.correctors import oucru_dengue_interpretation_feature

# ---------------------------------
# Constants
# ---------------------------------
# The data filepath
path = '../../resources/data/20210313-v0.0.8/'
path+= 'combined/combined_tidy.csv'

# Features
features = sorted(['age',
                   'gender',
                   'plt',
                   'haematocrit_percent'])

# Usecols
usecols = ['date', 'study_no', 'dsource',
    'day_from_admission', 'pcr_dengue_serotype',
    'pcr_dengue_load', 'ns1_interpretation',
    'igm_interpretation', 'igg_interpretation',
    'serology_single_interpretation',
    'serology_paired_interpretation',
    'bleeding']
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
    #nrows=50000,
    usecols=usecols,
    parse_dates=['date'])

# Reset index
data = data.reset_index()

# Remove columns with all NaN
data = data.dropna(how='all', axis=1)
data = data.dropna(how='any', subset=features)

# Add dengue interpretation
#data['dengue_interpretation'] = \
#    oucru_dengue_interpretation_feature(data,
#        pcr=True, ns1=False, igm=False, serology=False,
#        single_igm_igg=False, paired_igm_igg=False,
#        default=False)

# Create outcome
#data['outcome'] = \
#    data.dengue_interpretation.astype(int)

data['outcome'] = data.bleeding.fillna(False).astype(int)

# Add month
data['month'] = data.date.dt.month

# -----------
# Format data
# -----------

# Keep only day_from_admission == 0 data
data = data[data.day_from_admission == 0]

# Keep only certain months
#data = data[data.month.isin([2, 3, 4])]

# Drop any without interpretation
#data = data[~data.dengue_interpretation.isna()]

# Do this with sklearn column transformer
data.gender = data.gender.replace({'Male': 0, 'Female': 1})

# ----------------
#
# ----------------
#
import lazypredict

from lazypredict.Supervised import LazyClassifier

from sklearn.model_selection import train_test_split

# Define
features = features
target = 'outcome'

# Get data
X = data[features]
y = data[target]

# Get splits
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=.25)

# Create classifier
clf = LazyClassifier(ignore_warnings=True,
    custom_metric=None, verbose=0)

# Get models and predictions
models, predictions = clf.fit(X_train, X_test, y_train, y_test)

print(data)
print(models)