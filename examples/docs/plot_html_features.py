"""
Datasets Description
====================

"""

# Libraries
import yaml
import pandas as pd

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
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/v/dt/dt-1.10.23/datatables.min.js"></script>

    </head>
    <body>

    %s

    <script>
    
    /* Formatting function for row details - modify as you need */
    function format ( d ) {
        
        // Description
        html_description = ''
        if (d.description != '-') {
            html_description += '<tr>'
            html_description += '<td> Description: </td>'
            html_description += '<td>' + d.description + '</td>'
        }
        
        // Categories
        html_categories = ''
        if (d.categories != '-') {
            html_categories += '<tr>'
            html_categories += '<td> Categories: </td>'
            html_categories += '<td>' + d.categories + '</td>'
        }
        
        
        // Transformations
        html_transformations = ''
        
        // Extra information
        html_extra = ''
    
        // `d` is the original data object for the row
        return '<table cellpadding="5" cellspacing="0" border="0" style="padding-left:50px;">' +
                html_description +
                html_categories +
                html_transformations +
                html_extra +
        '</table>';
    }
    
      $(document).ready(function() {
      
            /* Create table */
            var table = $('#example').DataTable({
                "scrollY": "600px",
                "scrollCollapse": true,
                "paging": false,
                "autoWidth": true,
                 "columns": [
                    {
                        "className": 'details-control',
                        "orderable": false,
                        "data": null,
                        "defaultContent": ''
                    },
                    { "data": "name" },
                    { "data": "dtype" },
                    { "data": "unit" },
                    { "data": "code" },
                    { "data": "type"},
                    { "data": "categories",
                      "visible": false},
                    { "data": "description",
                      "visible": false},    
                ],
                "order": [[1, 'asc']]
            });
          
          
            // Add event listener for opening and closing details
            $('#example tbody .details-control').on('click', function () {
                var tr = $(this).closest('tr');
                var row = table.row( tr );
         
                if ( row.child.isShown() ) {
                    // This row is already open - close it
                    row.child.hide();
                    tr.removeClass('shown');
                }
                else {
                    // Open this row
                    row.child( format(row.data()) ).show();
                    tr.addClass('shown');
                }
            });
      });
    </script>

    </body>"""


# Path where data is
filepath = './corrector.yaml'

# Path where output HTML file should be stored.
outpath = '../../docs/source/_static/corrector.html'

# Columns
columns = ['name',
           'dtype',
           'unit',
           'code',
           'ctype',
           'categories',
           'description']

# ---------------------------------
# Main
# ---------------------------------
# Read yaml configuration
y = yaml.load(open(filepath, 'r'),
    Loader=yaml.FullLoader)

# Load features in pandas DataFrame.
features = pd.DataFrame(y['features'])

# Fill some information

print(features.transformations)

def f(x):
    print(x)
    #if pd.isnull(x):
    #    return x
    #print(pd.DataFrame(x))
    return x

#features.transformations = features.transformation.apply(lambda x: f(x))

features = features.fillna('-')
features = features.applymap(str)


# Create HTML for table
html_table = features.to_html(columns=columns,
                              table_id='example',
                              classes='display',
                              border=0)

print(features)

# Write text to file
f = open(outpath, "w")
f.write(HTML % html_table)
f.close()