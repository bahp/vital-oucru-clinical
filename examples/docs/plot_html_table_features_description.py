"""
Datasets Description
====================

"""

# Libraries
import yaml
import json
import pandas as pd

# ---------------------------------
# Methods
# ---------------------------------
def create_dataframe(data, features):
    """Creates the DataFrame.

    Parameters
    ----------
    data: pd.DataFrame
        The data in tidy format.
    features: pd.DataFrame
        Additional feature information.

    Returns
    -------
    pd.DataFrame
        Combined description.
    """

    # Copy just in case
    aux = data.copy(deep=True)

    # Drop empty columns
    aux = aux.dropna(axis=1, how='all')

    # Modify
    aux = aux.convert_dtypes()

    # Create describe table
    describe = aux.describe(include='all',
        datetime_is_numeric=True).T

    # Add interesting information (before merge)
    describe['dtype'] = aux.dtypes
    describe['nunique'] = aux.agg('nunique', dropna=False)
    describe['unique'] = aux.applymap(str) \
        .agg(lambda x: sorted(list(x.unique())))


    # Sort without nan? convert nan to something??

    # Remove those with too much information
    describe.loc[describe['nunique'] > 1000, 'unique'] = None

    # Show also nunique (otherwise we might think they do not have values!)

    # Merge with yaml information
    describe = describe.merge(features,
        how='left', left_index=True, right_on='name')

    # Format
    #describe.range = describe.range.apply(f)
    #describe.range = describe.range.apply(json.dumps)
    describe = describe.fillna('-')
    describe = describe.applymap(str)
    describe = describe.reset_index()

    # Return
    return describe


# ---------------------------------
# Constants
# ---------------------------------
# Path with data
path_data = '../../resources/data/20210313-v0.8/'
path_data+= 'combined/combined_tidy.csv'

# Path with yaml configuration
path_yaml =  './corrector.yaml'

# Path to load the HTML table template
path_html_template = './template_features_description.html'

# Path to save the HTML file
path_html_tables = '../../docs/source/_static/datasets/html-tables/'

# File name
filename = 'features_description_%s.html'

# Columns to include
columns = ['name',
           'dtype',
           'unit',
           'code',
           'ctype',
           'categories',
           'description',
           'unique',
           'nunique',
           'transformations',
           'range',
           'warning']

# ---------------------------------
# Main
# ---------------------------------
# Read data
data = pd.read_csv(path_data,
    low_memory=False, parse_dates=['date'])

# Read yaml configuration
features = pd.DataFrame( \
    yaml.load(open(path_yaml, 'r', encoding='utf8'),
        Loader=yaml.FullLoader)['features'])

# Create describe
describe = create_dataframe(data, features)

# Create HTML for table
html_table = describe.to_html(columns=columns,
                              table_id='example',
                              classes='display',
                              border=0)

describe.to_csv('test.csv')

# Create full HTML path
path_html_output = path_html_tables + filename % 'combined'

# Load template and save HTML table file
with open(path_html_template, 'r', encoding='utf8') as template, \
     open(path_html_output, "w+", encoding='utf8') as table:

    # Create html
    html = template.read() % html_table

    # Save HTML table file
    table.write(html)
    table.close()
    template.close()



COMPUTE = True

if COMPUTE:

    # -----------------------------
    # For each dataset individually
    # -----------------------------
    for i, df in data.groupby('dsource'):

        # Name
        path_html_output = path_html_tables + filename % i

        # Create describe
        describe = create_dataframe(df, features)

        # Create HTML for table
        html_table = describe.to_html(columns=columns,
                                      table_id='example',
                                      classes='display',
                                      border=0)

        # Load template and save HTML table file
        with open(path_html_template, 'r', encoding='utf8') as template, \
             open(path_html_output, "w+", encoding='utf8') as table:

            # Save HTML table file
            table.write(template.read() % html_table)
            table.close()
            template.close()

a = 8