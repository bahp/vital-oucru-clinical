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

# DataBlend library
from datablend.core.validation.reports import report_tidy_feature_count_per_dataset


# ---------------------------------
# Methods
# ---------------------------------

# ---------------------------------
# Constants
# ---------------------------------


# The data filepath
path = '../../resources/data/20212002-v0.2/combined/combined_tidy.csv'

# ---------------------------------
# Main
# ---------------------------------
# Read data
data = pd.read_csv(path,
    low_memory=False, parse_dates=['date'])

# Format
data = data.convert_dtypes()

# Counts (profiles)
counts = report_tidy_feature_count_per_dataset(data)

# Show
print("\nData:")
print(data)
print("\nCounts:")
print(counts)

# Save
counts.to_csv("../../resources/outputs/feature_count_per_dataset.csv")