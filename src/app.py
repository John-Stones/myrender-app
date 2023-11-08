# -*- coding: utf-8 -*-
"""
Created on Sun May 14 16:40:06 2023

@author: SHC4WX
"""

# import dash
from dash import Dash,dcc,html
# import plotly
# import plotly.graph_objs as go
# from collections import deque
import pandas as pd
import pyodbc

# sql_conn=pyodbc.connect('Driver={SQL Server};'
#                     'Server=SZHVSQL16.apac.bosch.com,1433;'
#                     'Database=DB_CCU_Analysis_Projects_Data_SQL;'
#                     'Trusted_connection=yes;'
#         )

# cursor=sql_conn.cursor()
# sql="""
# select top (1000) * from self_humidity
# """
# data=pd.read_sql_query(sql, sql_conn)

# print(data)


app = Dash(__name__)
server = app.server
app.layout = html.Div(

    children=[

        html.H1(children="Avocado Analytics"),

        html.P(

            children=(

                "Analyze the behavior of avocado prices and the number"

                " of avocados sold in the US between 2015 and 2018"

            ),

        ),

        dcc.Graph(

            figure={

                "data": [

                    {

                        "x": [1,2,3,4],

                        "y": [1,2,3,4],#rate

                        "type": "ss",

                    },

                ],

                "layout": {"title": "cathode pressure increase rate"},

            },

        ),

        dcc.Graph(

            figure={

                "data": [

                    {

                        "x": [1,2,3,4],

                        "y": [1,2,3,4],#PAndeDs_p_f_max

                        "type": "ss",

                    },

                ],

                "layout": {"title": "anode pressure downsteam"},

            },

        ),

    ]

)

# from waitress import serve

if __name__ == "__main__":
    # serve(
    #     app.server,
    #     port=8888
    #     )
    app.run_server(debug=True
                    )#host='0.0.0.0' ,port=8050
    
    
    

# # data = (

# #     df
# # )

# app = Dash(__name__)

# # app.py


# # ...


# app.layout = html.Div(

#     children=[

#         html.H1(children="Avocado Analytics"),

#         html.P(

#             children=(

#                 "Analyze the behavior of avocado prices and the number"

#                 " of avocados sold in the US between 2015 and 2018"

#             ),

#         ),

#         dcc.Graph(

#             figure={

#                 "data": [

#                     {

#                         "x": data["index"],

#                         "y": data["current"],

#                         "type": "ss",

#                     },

#                 ],

#                 "layout": {"title": "cathode pressure increase rate"},

#             },

#         ),

#         dcc.Graph(

#             figure={

#                 "data": [

#                     {

#                         "x": data["index"],

#                         "y": data["voltage"],

#                         "type": "ss",

#                     },

#                 ],

#                 "layout": {"title": "anode pressure downsteam"},

#             },

#         ),

#     ]

# )


# if __name__ == "__main__":
#     app.run_server(debug=True)
