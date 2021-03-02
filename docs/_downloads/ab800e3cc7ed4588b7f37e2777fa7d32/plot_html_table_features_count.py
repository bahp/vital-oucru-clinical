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
#c = pd.io.json.json_normalize(b, 'transformations', 'name')
#print(c)

# ---------------------------------
# Constants
# ---------------------------------
# HTML
HTML = """
    <html>
    <head>
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.23/css/jquery.dataTables.min.css"/>
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/buttons/1.6.5/css/buttons.dataTables.min.css"/>
     <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/fixedcolumns/3.3.2/css/fixedColumns.dataTables.min.css"/>
    
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/v/dt/dt-1.10.23/datatables.min.js"></script>
    
    
    <script type="text/javascript" src="https://code.jquery.com/jquery-3.5.1.js"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/1.10.23/js/jquery.dataTables.min.js"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/buttons/1.6.5/js/dataTables.buttons.min.js"></script>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.1.3/jszip.min.js"></script>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/pdfmake.min.js"></script>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/vfs_fonts.js"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/buttons/1.6.5/js/buttons.html5.min.js"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/buttons/1.6.5/js/buttons.print.min.js"></script>
   <script type="text/javascript" src="https://cdn.datatables.net/fixedcolumns/3.3.2/js/dataTables.fixedColumns.min.js"></script>
    
    <style>
    
        td.details-control {
        background: url('./arrow_right.jpg') no-repeat center center;
            cursor: pointer;
        }
        tr.shown td.details-control {
            background: url('./arrow_down.jpg') no-repeat center center;
        }
        
    </style>



    </head>
    <body>

    %s

    <script>
    
        $(document).ready(function() {
      
            /* Create table */
            var table = $('#example').DataTable({
                 dom: 'Bfrtip',
                 buttons: [
                    'copy', 'csv', 'excel', 'pdf', 'print'
                ],
                "scrollY": "600px",
                "scrollX": true,
                "scrollCollapse": true,
                "paging": false,
                "autoWidth": true,
                "fixedColumns": {
                    leftColumns: 1,
                    rightColumns: 1
                }
            });
        });
      
    </script>

    </body>"""


a = 1
# Path where the corrector is
filepath = './corrector.yaml'

# Path where output HTML file should be stored.
outpath = '../../docs/source/_static/feature_count.html'

# Path where data is
path = '../../resources/data/20212002-v0.2/combined/combined_tidy.csv'


# Load
tidy = pd.read_csv(path,
                   index_col=0,
                   parse_dates=['date'],
                   low_memory=False)


"""
# Create report
report = {
    'corrections':      corrections_summary(tidy),
    'counts':           report_tidy_feature_count_per_dataset(tidy),
    'dtypes':           report_tidy_dtypes_per_dataset(tidy),
    'units':            report_stack_units_per_dataset(stack),
    'units_undefined':  report_undefined_units(stack.unit.unique(), ureg),
    'units_duplicated': report_stack_duplicated_units(stack),
    'count_feature':    report_stack_feature_count(stack, cpid='study_no'),
    'count_date':       report_stack_date_count(stack, cpid='study_no'),
    'stay':             report_stack_stay(stack, cpid='study_no')
}
"""

# Feature count
count = report_tidy_feature_count_per_dataset(tidy)

# Format
count = count.fillna('-')
count = count.applymap(str)
count = count.reset_index()

print(count)

count.columns = count.columns.droplevel(1)
count = count.rename(columns={'index': 'name'})
count = count.set_index('name')
count = count.reset_index()
count.columns.name = None

# Create HTML for table
html_table = count.to_html(table_id='example',
                           classes='display',
                           border=0,
                           index=False)

print(count)
print(count.index)
print(count.columns)

# Write text to file
f = open(outpath, "w")
f.write(HTML % html_table)
f.close()