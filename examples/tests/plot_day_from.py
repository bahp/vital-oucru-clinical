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
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Import datablend
from datablend.core.repair.correctors import oucru_correction
from datablend.core.repair.correctors import day_from_first_true
from datablend.core.repair.correctors import date_outliers_correction

# ---------------------------------
# Methods
# ---------------------------------
def script_00(data, threshold=10):
    """This method..."""

    for i, df in data.groupby('dsource'):

        # Compute the counts
        count = df.day_from_illness.value_counts()

        # Indexes
        idxs = count.index.values > 10

        # Count the number of occurrences
        print("Total outliers for %8s: %s" %
              (i, np.sum(count[idxs])))
        print(count)
        print("\n\n")
        #print(count[idxs].sort_index())


    #print("\nShow count:")
    #counts = data.day_from_admission \
    #          .value_counts() \
    #          .sort_index()
    #counts.to_csv('day_from_admission_count.csv')


def script_01(data, data32):
    """This method..."""

    # Filter 32dx in whole data
    data = data[data.dsource.isin(['32dx'])]

    # ---------
    # Compare
    # ---------
    # .. note:: DataFrames can't be equal because we have added the
    #           dsource column and also we have included such info
    #           in the study_no column.

    # .. note:: The dates corrected (from 20210305-v0.5) seem that
    #           are coherent corrections. It is possible to double
    #           check from DataFrame below.

    # Reset indexes
    data = data.reset_index()
    data32 = data32.reset_index()

    # Compare dates
    compare_dates = data32.date.compare(data.date)

    # Compare days_from_admission
    compare_dfa = \
        data32.day_from_admission.compare( \
              data.day_from_admission)

    # Patients with dates corrected
    patients = data32.loc[compare_dates.index, 'study_no'].unique()

    # Show
    print("\nAre they Equal? \n%s" % compare_dates)
    print("\nWhat about the day_from_admission? \n%s" % compare_dfa)
    print("\nPatients with dates modified: \n %s" % \
        data32[data32.study_no.isin(patients)]\
            .sort_values(by=['study_no', 'date']) \
                .to_string())

    # Days from admission
    data = \
        data.groupby('study_no') \
            .apply(day_from_first_true,
                   event='event_admission',
                   tag='admission_recomputed')

    # Show data
    print("\n\nData:")
    print(data)

    # Check differences
    print("\nComparison:")
    print(data.day_from_admission.compare( \
        data.day_from_admission_recomputed))

    print("\nShow count:")
    print(data.day_from_admission \
              .value_counts()
              .sort_index())


# ---------------------------------
# Constants
# ---------------------------------
# The data filepath
path = '../../resources/data/20210309-v0.7/combined/combined_tidy.csv'

# Path
path2 = '../../../../datablend/main/examples/oucru/oucru-full/'
path2+= 'resources/datasets/tidy/32dx_data_tidy_corrected.csv'

# Columns
columns = ['day_from_admission',
           'day_from_enrolment',
           'day_from_onset',
           'study_no',
           'date',
           'event_admission',
           'day_from_illness']

# ---------------------------------
# Main
# ---------------------------------
# Information
print("Executing...")


# ------------
# Read COMBINED
# -------------
# Read data
data = pd.read_csv(path,
    usecols=['date',
             'dsource',
             'study_no',
             'event_admission',
             'day_from_illness'],
    low_memory=False,
    parse_dates=['date'])

# ---------
# Read 32DX
# ---------
"""
# Read data
data32 = pd.read_csv(path2,
    usecols=['date',
             'study_no',
             'event_admission',
             'day_from_illness'],
    parse_dates=['date'],
    low_memory=False)
"""

# Run scripts
script_00(data)
#script_01(data, data32)

import sys
sys.exit()





"""
# Groupby
for i, df in data.groupby(by='dsource'):
    print("\n\n%s" % i)
    print(df.day_from_admission
              .value_counts()
              .sort_index()
              .to_string())
"""


# Indexes with large admission day
idxs = aux.day_from_admission.abs() > 100

# Show
print("Large admission day:")
print(aux[idxs])

import sys
sys.exit()

# Select those patients
patients = aux[idxs].study_no.unique()

# Show these patients
outliers = aux[aux.study_no.isin(patients)]

# Show
for i, df in outliers.groupby('study_no'):
    print("\nPatient %s:" % i)
    print(df)

# ------------
# PER PATIENT
# ------------
# For each patient
for i, df in aux.groupby(['study_no']):

    # Correct date
    date_corrected = \
        date_outliers_correction(df.date,
            max_days_to_median=100,
            outliers_as_nat=False)

    # Compare
    compare = df.date.compare(date_corrected)

    # Show information
    if compare.shape[0] > 0:
        print("-"*50)
        print("\n\nPatient '%s'" % i)
        print("\nRaw data:")
        print(df.date)
        print("\nCorrected:")
        print(compare)
        print("-"*50)