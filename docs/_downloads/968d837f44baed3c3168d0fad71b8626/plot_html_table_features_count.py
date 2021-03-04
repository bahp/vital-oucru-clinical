"""
Datasets Description
====================

"""

# Libraries
import yaml
import pandas as pd

from datablend.core.validation.reports import report_tidy_feature_count_per_dataset


# ---------------------------------
# Methods
# ---------------------------------
def create_dataframe(data):
    """Creates the DataFrame.

    Parameters
    ----------
    data: pd.DataFrame

    Returns
    -------
    pd.DataFrame
        Counts per datasets.
    """

    # Copy just in case
    count = data.copy(deep=True)

    # Feature count
    count = report_tidy_feature_count_per_dataset(count)

    # Format
    count = count.fillna('-')
    count = count.applymap(str)
    count = count.reset_index()
    count.columns = count.columns.droplevel(1)
    count = count.rename(columns={'index': 'name'})
    count = count.set_index('name')
    count = count.reset_index()
    count.columns.name = None

    # Return
    return count


# ---------------------------------
# Constants
# ---------------------------------
# Path with data
path_data = '../../resources/data/20210304-v0.4/'
path_data+= 'combined/combined_tidy.csv'

# Path to load the HTML table template
path_html_template = './template_features_count.html'

# Path to save the HTML file
path_html_tables = '../../docs/source/_static/datasets/html-tables/'

# File name
filename = 'features_count.html'

# Columns to include
columns = ['name',
           'dtype',
           'unit',
           'code',
           'ctype',
           'categories',
           'description',
           'unique',
           'transformations',
           'range']

# ---------------------------------
# Main
# ---------------------------------
# Load
data = pd.read_csv(path_data,
    index_col=0, parse_dates=['date'],
    low_memory=False)


# Create describe
describe = create_dataframe(data)


# Create HTML for table
html_table = describe.to_html(table_id='example',
     classes='display', border=0, index=False)

# Create full HTML path
path_html_output = path_html_tables + filename

# Load template and save HTML table file
with open(path_html_template, 'r') as template, \
     open(path_html_output, "w+") as table:

    # Save HTML table file
    table.write(template.read() % html_table)
    table.close()
    template.close()

a = 1