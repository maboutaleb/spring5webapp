#!/usr/bin/env python3
import os
import snowflake.connector
import pandas as pd 
import dash
import pyodbc
import dash_html_components as html
import dash_table
import dash_core_components as dcc
from dash.dependencies import Input, Output
from datetime import datetime as dt
import flask
from flask import send_file
from waitress import serve
from flask import Flask

external_stylesheets =['https://codepen.io/aboutaleb95/pen/gOPJagZ.css']
server = Flask(__name__)
app = dash.Dash(__name__,server=server,external_stylesheets=external_stylesheets)
app.title = 'Dash-[Mailers]'

tabs_styles = {
    'height': '44px','color': '#28334AFF', 'fontSize': 26,'font-family': 'Calibri'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'backgroundColor':'#f2f2f2',
    'color': '#C7D3D4FF',

    
}

tab_selected_style = {
    'borderTop': '1px solid #d9dddc',
    'borderBottom': '1px solid #d9dddc',
    'backgroundColor': '#d9dddc',
    'color': 'black',
    'padding': '6px'
    #'fontWeight': 'bold'
}

#cnx = pyodbc.connect('dsn=snowflake_noid;Encrypt=yes;')
#from connection import cnx
import queries
import dropdpwn
import mindah
ranges={}
for x in range(100):
    ranges[x] = str(x)
    #ranges.append({'key': x, 'label': str(x)})

#df = pd.read_sql(query,conn)
#df1 = df.groupby(["MarketingDate"])
#df2= df1.apply(lambda x: x.sort_values(["DropNumber"]))


##x = pd.read_sql(query2,conn)
#x['bb'] = x['bb'] *2
#x = x.groupby(['MarketingDate','bb' ,'record' ,'Office']).count()
#x['cost'] = x['state'] * 2

PLOTLY_LOGO = "C:\\Users\\Mahmoud\\Pictures\\directmailers.png"

all_options = {
    'countsperdrop': ['American Financial', 'Essex', 'Direct Access','Spring EQ','Veteran United','Bank of England','Magnolia','Tam Lending','Advisor'],
    'notyet': ['American Financial', 'Direct Access', 'Essex','Spring EQ','Veteran United','Bank of England','Magnolia','Tam Lending','Advisor']
}

Deci = {
    'Essex': dropdpwn.Decile,
    'American Financial': dropdpwn.Decile,
    'Direct Access' : dropdpwn.Decile,
    'Spring EQ' : dropdpwn.Decile,
    'Veteran United' : dropdpwn.Decile,
    'Bank of England' : dropdpwn.Decile,
    'Magnolia': dropdpwn.Decile,
    'Tam Lending': dropdpwn.Decile,
    'Advisor':dropdpwn.Decile,
}
db = {
    'Essex': 'EXMT_REPORTING',
    'American Financial': 'AMFN_REPORTING',
    'Direct Access' : 'DCXF_REPORTING',
    'Spring EQ' : 'SPEQ_REPORTING',
    'Veteran United' : 'VUHL_REPORTING',
    'Bank of England' : 'ENGB_REPORTING',
    'Magnolia': 'MGBK_REPORTING',
    'Tam Lending':'TAML_REPORTING',
    'Advisor':'ADVR_REPORTING'
}

app.layout = html.Div([

     html.Nav(children='Dash-[Mailers]',style={'color': 'Black', 'font-family': 'Impact','backgroundColor': 'yellow','font-weight':'bold','padding': '14px 16px','fontSize': 26 }),
        dcc.Tabs(id="tabs-dropdown",  children=[
        dcc.Tab(label='Counts Per Drop', value='countsperdrop', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Custom Query', value='notyet', style=tab_style, selected_style=tab_selected_style),

    ],style=tabs_styles#,style={'color': 'Black', 'fontSize': 23,'font-family': 'Calibri','font-weight':'bold'}
    ),


    html.Div(id='Khara'),
    
    
    #html.Div(id='dd-output-container'),



])

@app.callback(

    dash.dependencies.Output('Khara', 'children'),
    [dash.dependencies.Input('tabs-dropdown', 'value')])
def set_cities_options(Tab):
    if Tab == "countsperdrop":
        from connection import cnx
        return html.Div([
                dcc.Dropdown(id='clients-dropdown',style={'color': 'Black', 'fontSize': 20,'font-family': 'Calibri','font-weight':'bold'},placeholder="Select Client"),

           dcc.Dropdown(
        id='demo-dropdown',
        multi=True,
        placeholder="Group by Model",
        style={'color': 'Black', 'fontSize': 20,'font-family': 'Calibri'},
        value=[],
        #options=' '

    ),
        dcc.Dropdown(
        id='cra-dropdown',
        multi=True,
        placeholder="Group by Bureau",
        style={'color': 'Black', 'fontSize': 20,'font-family': 'Calibri'},
        value=[],
        #options=' '


    ),
            dcc.Dropdown(
        id='class-dropdown',
        multi=True,
        placeholder="Group by Class",
        style={'color': 'Black', 'fontSize': 20,'font-family': 'Calibri'},
        value=[],
        #options=' '


    ),
    html.Div(id='display-selected-values'),
        ])
    if Tab == "notyet":
        from connection import cnx
        return html.Div([
           dcc.Dropdown(id='clients-dropdown',style={'color': 'Black', 'fontSize': 20,'font-family': 'Calibri','font-weight':'bold'},placeholder="Select Client"),
        html.Div(
           dcc.Dropdown(
        id='demo-dropdown',
        multi=True,
        placeholder="From Date",
        style={'color': 'Black', 'fontSize': 20,'font-family': 'Calibri'},
        value=[],
        #options=' '

    ),style={'width': '50%', 'display': 'inline-block'}),

       html.Div(
           dcc.Dropdown(
        id='To-dropdown',
        multi=True,
        placeholder="To Date",
        style={'color': 'Black', 'fontSize': 20,'font-family': 'Calibri'},
        value=[],
        #options=' '

    ),style={'width': '50%', 'display': 'inline-block'}),

    dcc.Dropdown(
        id='fields-dropdown',
        multi=True,
        placeholder="group by fields",
        style={'color': 'Black', 'fontSize': 20,'font-family': 'Calibri'},
        value=[],
        #options=' '
    ),

    dcc.Dropdown(
        id='decile-dropdown',
        multi=True,
        placeholder="group by model",
        style={'color': 'Black', 'fontSize': 20,'font-family': 'Calibri'},
        value=[],
        #options=' '
    ),
        
        html.Div(
        dcc.RangeSlider(
        id='my-slider',
        min=0,
        max=100,
        step=1,
        value=[0,0],
        marks=ranges
    ),style={'height':'100%' ,'vertical-align': 'middle','padding': '10px 0'}#,style={'width': '80%','height':'50%' ,'display': 'inline-block','vertical-align': 'middle'}
    ),
    #html.Div(id='slider-output-container',style={'float':'right','width': '49%','color': 'Black', 'fontSize': 15,'font-family': 'Calibri','padding': '0px 0'}),
    html.Div(id='display-selected-values1'),
        ])

@app.callback(
    dash.dependencies.Output('slider-output-container', 'children'),
    [dash.dependencies.Input('my-slider', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value[0])
@app.callback(

    dash.dependencies.Output('clients-dropdown', 'options'),
    [dash.dependencies.Input('tabs-dropdown', 'value')])
def set_clients_options(Tab):
    return [{'label': i, 'value': i} for i in all_options[Tab]]

@app.callback(

    dash.dependencies.Output('demo-dropdown', 'options'),
    [dash.dependencies.Input('clients-dropdown', 'value')])
def set_model_options(Tab):
    if Tab is None:
        return []
    return [{'label': i, 'value': i} for i in dropdpwn.eshta(Tab)]

@app.callback(

    dash.dependencies.Output('To-dropdown', 'options'),
    [dash.dependencies.Input('clients-dropdown', 'value')])
def set_modell_options(Tab):
    if Tab is None:
        return dropdpwn.mylist
    return [{'label': i, 'value': i} for i in dropdpwn.eshta(Tab)]

@app.callback(

    dash.dependencies.Output('cra-dropdown', 'options'),
    [dash.dependencies.Input('clients-dropdown', 'value')])
def set_cra_options(Tab):
    if Tab is None:
        return dropdpwn.mylist1
    return [{'label': i, 'value': i} for i in dropdpwn.eshta(Tab)]

@app.callback(

    dash.dependencies.Output('decile-dropdown', 'options'),
    [dash.dependencies.Input('clients-dropdown', 'value')])
def set_decile_options(Tab):
    return dropdpwn.Decile

@app.callback(

    dash.dependencies.Output('fields-dropdown', 'options'),
    [dash.dependencies.Input('clients-dropdown', 'value')])
def set_field_options(Tab):
    return dropdpwn.Fields

@app.callback(

    dash.dependencies.Output('class-dropdown', 'options'),
    [dash.dependencies.Input('clients-dropdown', 'value')])
def set_class_options(Tab):
    if Tab is None:
        return dropdpwn.mylist1
    return [{'label': i, 'value': i} for i in dropdpwn.eshta(Tab)]

@app.callback(

    dash.dependencies.Output('display-selected-values', 'children'),
    [dash.dependencies.Input('cra-dropdown', 'value'),
    dash.dependencies.Input('demo-dropdown', 'value'),
     dash.dependencies.Input('tabs-dropdown', 'value'),
     dash.dependencies.Input('clients-dropdown', 'value'),
     dash.dependencies.Input('class-dropdown', 'value'),

     ])


def set_display_children(mahmoud,value,Tab, client,model):
    from connection import cnx
    if Tab == "countsperdrop":
        if client is None:
            cnx.cursor().execute("USE database NOID;")
            cnx.cursor().execute("USE schema DBO;")
            MAIN = pd.read_sql(queries.query,cnx)
            return dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in MAIN.columns],
            data=MAIN.to_dict('records'),
            sort_action="native",
            sort_mode="multi",
            #page_current = 0,
            page_size =20,
            #row_selectable='multi',
            #page_action='custom',
            filter_action='native',
            export_format='csv',
            #selected_rows=[],
            style_table={
            'maxHeight': '100ex',
            'overflowY': 'scroll',
            'width': '100%',
            'minWidth': '100%',
            'flex-wrap': 'nowrap',
            'text_align': 'center'
        },
        style_cell={
                'max-width': '5px',
                'font-family': 'Calibri',
                'text_align': 'left'
            },
            style_header={
        'backgroundColor': 'white',
        'fontWeight': 'bold',
        'font-family': 'Calibri',
    },

            )
        if  client is not None and (value is None or  len(value) ==0) and (mahmoud is None or  len(mahmoud) == 0) and (model is None or  len(model) == 0) :
            
            cnx.cursor().execute("USE database " + db[client] + " ;")
            cnx.cursor().execute("USE schema DBO;")
            r = pd.read_sql(queries.query1,cnx)
            #r = r.groupby(['MarketingDate','total','responses','perc']).count().reset_index()
            return dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in r.columns],
            data=r.to_dict('records'),
            sort_action="native",
            sort_mode="multi",
            #page_current = 0,
            page_size =20,
            #row_selectable='multi',
            #page_action='custom',
            filter_action='native',
            export_format='csv',
            #selected_rows=[],
            style_table={
            'maxHeight': '100ex',
            'overflowY': 'scroll',
            'width': '100%',
            'minWidth': '100%',
            'flex-wrap': 'nowrap',
            'text_align': 'center'
        },
        style_cell={
                'max-width': '5px',
                'font-family': 'Calibri',
                'text_align': 'left'
            },
        style_header={
        'backgroundColor': 'white',
        'fontWeight': 'bold',
        'font-family': 'Calibri',
    },

            )

        if client is not None and len(value) >0  and (mahmoud is None or  len(mahmoud) == 0) and (model is None or  len(model) == 0):
            paramss =""
            for i in value:
                paramss += "'" + i + "',"
            paramss= paramss[:-1]
            query3="""select right(OFFER_SEGMENT,CHARINDEX('.',REVERSE(OFFER_SEGMENT))-1) as Model, to_varchar(count( *),'999,999,999') as Total ,to_varchar(count (case when RESP_RESPONSEFLAG = 1 then 1 end),'999,999,999') as Responses,
    cast(round(cast(count (case when RESP_RESPONSEFLAG=1 then 1 end) as float)/cast(count( *) as float)*100,2) as varchar(32)) as Perc
    from PRO_TABLEAU
    where  OFFER_SEGMENT not like '%Trig%' and OFFER_SEGMENT not like 'seed%' and OFFER_SEGMENT not like '%TRIG%' and SRC_RECORDTYPE =1 and SRC_MARKETINGDATE in (""" + paramss + """) group by right(OFFER_SEGMENT,CHARINDEX('.',REVERSE(OFFER_SEGMENT))-1) order by perc desc
    """
            cnx.cursor().execute("USE database " + db[client] + " ;")
            cnx.cursor().execute("USE schema DBO;")
            x = pd.read_sql(query3,cnx)
            return dash_table.DataTable(
            id='table1',
            columns=[{"name": i, "id": i} for i in x.columns],
            data=x.to_dict('records'),
            sort_action="native",
            sort_mode="multi",
            #page_current = 0,
            page_size =20,
            #row_selectable='multi',
            #page_action='custom',
            filter_action='native',
            export_format='csv',
            #selected_rows=[],
            style_table={
            'maxHeight': '200ex',
            'overflowY': 'scroll',
            'width': '100%',
            'minWidth': '100%',
            'flex-wrap': 'nowrap',
            'text_align': 'center'
        },
        style_cell={
                'max-width': '20px',
                'font-family': 'Calibri',
                'text_align': 'left'
            },
            style_header={
        'backgroundColor': 'white',
        'fontWeight': 'bold',
        'font-family': 'Calibri',
    },
            )

        if client is not None and len(mahmoud) >0 and (model is None or  len(model) == 0):
            eshta =""
            for i in mahmoud:
                eshta += "'" + i + "',"
            eshta= eshta[:-1]
            query4="""select CREDIT_CRA as Bureau,right(OFFER_SEGMENT,CHARINDEX('.',REVERSE(OFFER_SEGMENT))-1) as Model, to_varchar(count( *),'999,999,999') as Total ,to_varchar(count (case when RESP_RESPONSEFLAG = 1 then 1 end),'999,999,999') as Responses,
    cast(round(cast(count (case when RESP_RESPONSEFLAG=1 then 1 end) as float)/cast(count( *) as float)*100,2) as varchar(32)) as Perc
    from PRO_TABLEAU
    where    OFFER_SEGMENT not like '%Trig%' and OFFER_SEGMENT not like 'seed%' and OFFER_SEGMENT not like '%TRIG%' and SRC_RECORDTYPE =1 and SRC_MARKETINGDATE in (""" + eshta + """)
    group by Bureau,MODEL order by Bureau desc"""
            cnx.cursor().execute("USE database " + db[client] + " ;")
            cnx.cursor().execute("USE schema DBO;")
            xp = pd.read_sql(query4,cnx)
            return dash_table.DataTable(
            id='table1',
            columns=[{"name": i, "id": i} for i in xp.columns],
            data=xp.to_dict('records'),
            sort_action="native",
            sort_mode="multi",
            #page_current = 0,
            page_size =20,
            #row_selectable='multi',
            #page_action='custom',
            filter_action='native',
            export_format='csv',
            #selected_rows=[],
            style_table={
            'maxHeight': '200ex',
            'overflowY': 'scroll',
            'width': '100%',
            'minWidth': '100%',
            'flex-wrap': 'nowrap',
            'text_align': 'center'
        },
        style_cell={
                'max-width': '20px',
                'font-family': 'Calibri',
                'text_align': 'left'
            },
            style_header={
        'backgroundColor': 'white',
        'fontWeight': 'bold',
        'font-family': 'Calibri',
    },
            )
        if client is not None and len(model) >0  :
            eshta =""
            for i in model:
                eshta += "'" + i + "',"
            eshta= eshta[:-1]
            decile_query="""select case when left(OFFER_SEGMENT,3) = 'CLP' AND OFFER_SEGMENT LIKE '%ST%' THEN 'CLP_ST' WHEN left(OFFER_SEGMENT,3) = 'CLP' AND (OFFER_SEGMENT LIKE '%360%' OR OFFER_SEGMENT LIKE '%180%') THEN 'CLP_FIXED'
ELSE left(OFFER_SEGMENT,3) END AS Class,  to_varchar(count( *),'999,999,999') as Total ,to_varchar(count (case when RESP_RESPONSEFLAG = 1 then 1 end),'999,999,999') as Responses,
    cast(round(cast(count (case when RESP_RESPONSEFLAG=1 then 1 end) as float)/cast(count( *) as float)*100,2) as varchar(32)) as Perc
from  PRO_TABLEAU where  SRC_MARKETINGDATE in (""" + eshta + """)
GROUP BY case when left(OFFER_SEGMENT,3) = 'CLP' AND OFFER_SEGMENT LIKE '%ST%' THEN 'CLP_ST' WHEN left(OFFER_SEGMENT,3) = 'CLP' AND (OFFER_SEGMENT LIKE '%360%' OR OFFER_SEGMENT LIKE '%180%') THEN 'CLP_FIXED'
ELSE left(OFFER_SEGMENT,3) END"""
            cnx.cursor().execute("USE database " + db[client] + " ;")
            cnx.cursor().execute("USE schema DBO;")
            xyz = pd.read_sql(decile_query,cnx)
            return dash_table.DataTable(
            id='table1',
            columns=[{"name": i, "id": i} for i in xyz.columns],
            data=xyz.to_dict('records'),
            sort_action="native",
            sort_mode="multi",
            #page_current = 0,
            page_size =20,
            #row_selectable='multi',
            #page_action='custom',
            filter_action='native',
            export_format='csv',
            #selected_rows=[],
            style_table={
            'maxHeight': '200ex',
            'overflowY': 'scroll',
            'width': '100%',
            'minWidth': '100%',
            'flex-wrap': 'nowrap',
            'text_align': 'center'
        },
        style_cell={
                'max-width': '20px',
                'font-family': 'Calibri',
                'text_align': 'left'
            },
            style_header={
        'backgroundColor': 'white',
        'fontWeight': 'bold',
        'font-family': 'Calibri',
    },
            )
        
  
@app.callback(

    dash.dependencies.Output('display-selected-values1', 'children'),
    [dash.dependencies.Input('demo-dropdown', 'value'),
     dash.dependencies.Input('tabs-dropdown', 'value'),
     dash.dependencies.Input('clients-dropdown', 'value'),
     dash.dependencies.Input('decile-dropdown', 'value'),
     dash.dependencies.Input('fields-dropdown', 'value'),
     dash.dependencies.Input('To-dropdown', 'value'),
     dash.dependencies.Input('my-slider', 'value'),
     ])
def sett_display_children(value,Tab, client,model,properties, to,range_slide):
    from connection import cnx
    if Tab == "notyet":        
        if client is not None and len(value)> 0 and len(properties)> 0  and ( to is None or len(to) ==0) and ( model is None or len(model) == 0) :
            date =""
            for i in value:
                date += "'" + i + "',"
            date= date[:-1]
            mod =""
            for i in properties:
                mod += "" + i + ","
            mod= mod[:-1]
            decile_query1="""select """ + mod + """ , to_varchar(count( *),'999,999,999') as Total ,to_varchar(count (case when RESP_RESPONSEFLAG = 1 then 1 end)) as reponses ,cast(round(cast(count (case when RESP_RESPONSEFLAG=1 then 1 end) as float)/cast(count( *) as float)*100,2) as varchar(32)) as Perc,to_varchar(count (case when APP_FLAG = 1 then 1 end) ) as App
    from DBO.PRO_TABLEAU  where SRC_MARKETINGDATE in (""" + date + """) group  by """ + mod + """"""
            cnx.cursor().execute("USE database " + db[client] + " ;")
            cnx.cursor().execute("USE schema DBO;")
            err = pd.read_sql(decile_query1,cnx)
            return dash_table.DataTable(
            id='table1',
            columns=[{"name": i, "id": i} for i in err.columns],
            data=err.to_dict('records'),
            sort_action="native",
            sort_mode="multi",
            #page_current = 0,
            page_size =20,
            #row_selectable='multi',
            #page_action='custom',
            filter_action='native',
            export_format='csv',
            #selected_rows=[],
            style_table={
            'maxHeight': '200ex',
            'overflowY': 'scroll',
            'width': '100%',
            'minWidth': '100%',
            'flex-wrap': 'nowrap',
            'text_align': 'center'
        },
        style_cell={
                'max-width': '20px',
                'font-family': 'Calibri',
                'text_align': 'left'
            },
            style_header={
        'backgroundColor': 'white',
        'fontWeight': 'bold',
        'font-family': 'Calibri',
    },
            )
        if client is not None and len(value)> 0 and len(properties)> 0 and len(to) > 0   and ( model is None or len(model) == 0) :
            date = "'" + value[0] + "'"
            date2 = "'" + to[0] + "'"
            mod =""
            mod2=""
            for i in properties:
                mod += "" + i + ","
            mod= mod[:-1]
            decile_query1="""select """ + mod + """ , to_varchar(count( *),'999,999,999') as Total ,to_varchar(count (case when RESP_RESPONSEFLAG = 1 then 1 end)) as reponses ,cast(round(cast(count (case when RESP_RESPONSEFLAG=1 then 1 end) as float)/cast(count( *) as float)*100,2) as varchar(32)) as Perc,to_varchar(count (case when APP_FLAG = 1 then 1 end) ) as App
    from PRO_TABLEAU  where SRC_MARKETINGDATE between """ + date + """ and  """ + date2 + """ group  by """ + mod + """"""
            cnx.cursor().execute("USE database " + db[client] + " ;")
            cnx.cursor().execute("USE schema DBO;")
            err = pd.read_sql(decile_query1,cnx)
            return dash_table.DataTable(
            id='table1',
            columns=[{"name": i, "id": i} for i in err.columns],
            data=err.to_dict('records'),
            sort_action="native",
            sort_mode="multi",
            #page_current = 0,
            page_size =20,
            #row_selectable='multi',
            #page_action='custom',
            filter_action='native',
            export_format='csv',
            #selected_rows=[],
            style_table={
            'maxHeight': '200ex',
            'overflowY': 'scroll',
            'width': '100%',
            'minWidth': '100%',
            'flex-wrap': 'nowrap',
            'text_align': 'center'
        },
        style_cell={
                'max-width': '20px',
                'font-family': 'Calibri',
                'text_align': 'left'
            },
            style_header={
        'backgroundColor': 'white',
        'fontWeight': 'bold',
        'font-family': 'Calibri',
    },
            )
        if client is not None and len(value)> 0 and  ( to is None or len(to) ==0) and len(model)> 0 and len(properties) > 0  and range_slide[0] == 0 and range_slide[1]==0:
            date =""
            for i in value:
                date += "'" + i + "',"
            date= date[:-1]
            prop=""
            prop2=""
            for i in properties:
                if i == 'OFFER_SEGMENT':
                    i2 = """ case when left(OFFER_SEGMENT,3) = 'CLP' AND OFFER_SEGMENT LIKE '%ST%' THEN 'CLP_ST' WHEN left(OFFER_SEGMENT,3) = 'CLP' AND (OFFER_SEGMENT LIKE '%360%' OR OFFER_SEGMENT LIKE '%180%') THEN 'CLP_FIXED'
ELSE left(OFFER_SEGMENT,3) END as Class"""
                    prop2 += "" + i2 + ","
                    
                    i = """ case when left(OFFER_SEGMENT,3) = 'CLP' AND OFFER_SEGMENT LIKE '%ST%' THEN 'CLP_ST' WHEN left(OFFER_SEGMENT,3) = 'CLP' AND (OFFER_SEGMENT LIKE '%360%' OR OFFER_SEGMENT LIKE '%180%') THEN 'CLP_FIXED'
ELSE left(OFFER_SEGMENT,3) END """
                    prop += "" + i + ","
                    continue
                prop += "" + i + ","
                prop2 += "" + i + ","
            prop= prop[:-1]
            prop2= prop2[:-1]
            mod =""
            for i in model:
                mod += "CEIL(" + i + ",-1),"
            mod= mod[:-1]
            decile_query1="""select """ + prop2 + """,""" + mod + """ ,  to_varchar(count( *),'999,999,999') as Total ,to_varchar(count (case when RESP_RESPONSEFLAG = 1 then 1 end)) as reponses ,cast(round(cast(count (case when RESP_RESPONSEFLAG=1 then 1 end) as float)/cast(count( *) as float)*100,2) as varchar(32)) as Perc,to_varchar(count (case when APP_FLAG = 1 then 1 end) ) as App
    from PRO_TABLEAU a inner join scores3 b ON A.SRC_CLIENTID = B.CLIENTID where SRC_MARKETINGDATE in (""" + date + """) group  by """ + prop + """,""" + mod + """"""
            decile_query2="""WITH CTE AS (SELECT * from AMFN_REPORTING.dbo.PRO_TABLEAU a inner join MO.DBO.Deciles2 b ON A.SRC_CLIENTID = B.CLIENTID)
select """ + mod + """ as shit, COUNT(*) FROM CTE PIVOT(MAX(Decile) FOR MODEL IN ('ALTAIR_EQ_CASHOUT_2019_20200120','SUPERSCORE_V2')) where SRC_MARKETINGDATE = '2020-07-23' group by """ + mod + """"""
            cnx.cursor().execute("USE database " + db[client] + " ;")
            cnx.cursor().execute("USE schema DBO;")
            err = pd.read_sql(decile_query1,cnx)
            return dash_table.DataTable(
            id='table1',
            columns=[{"name": i, "id": i} for i in err.columns],
            data=err.to_dict('records'),
            sort_action="native",
            sort_mode="multi",
            #page_current = 0,
            page_size =20,
            #row_selectable='multi',
            #page_action='custom',
            filter_action='native',
            export_format='csv',
            #selected_rows=[],
            style_table={
            'maxHeight': '200ex',
            'overflowY': 'scroll',
            'width': '100%',
            'minWidth': '100%',
            'flex-wrap': 'nowrap',
            'text_align': 'center'
        },
        style_cell={
                'max-width': '20px',
                'font-family': 'Calibri',
                'text_align': 'left'
            },
            style_header={
        'backgroundColor': 'white',
        'fontWeight': 'bold',
        'font-family': 'Calibri',
    },
            )
        if client is not None and len(value)> 0 and  len(to) > 0 and len(model)> 0 and len(properties) > 0 and range_slide[0] == 0 and range_slide[1]==0:
            date = "'" + value[0] + "'"
            date2 = "'" + to[0] + "'"
            prop=""
            prop2=""
            for i in properties:
                if i == 'OFFER_SEGMENT':
                    i2 = """ case when left(OFFER_SEGMENT,3) = 'CLP' AND OFFER_SEGMENT LIKE '%ST%' THEN 'CLP_ST' WHEN left(OFFER_SEGMENT,3) = 'CLP' AND (OFFER_SEGMENT LIKE '%360%' OR OFFER_SEGMENT LIKE '%180%') THEN 'CLP_FIXED'
ELSE left(OFFER_SEGMENT,3) END as Class"""
                    prop2 += "" + i2 + ","
                    
                    i = """ case when left(OFFER_SEGMENT,3) = 'CLP' AND OFFER_SEGMENT LIKE '%ST%' THEN 'CLP_ST' WHEN left(OFFER_SEGMENT,3) = 'CLP' AND (OFFER_SEGMENT LIKE '%360%' OR OFFER_SEGMENT LIKE '%180%') THEN 'CLP_FIXED'
ELSE left(OFFER_SEGMENT,3) END """
                    prop += "" + i + ","
                    continue
                prop += "" + i + ","
                prop2 += "" + i + ","
            prop= prop[:-1]
            prop2= prop2[:-1]
            mod =""
            for i in model:
                mod += "CEIL(" + i + ",-1),"
            mod= mod[:-1]
            decile_query1="""select """ + prop2 + """,""" + mod + """ ,  to_varchar(count( *),'999,999,999') as Total ,to_varchar(count (case when RESP_RESPONSEFLAG = 1 then 1 end)) as reponses ,cast(round(cast(count (case when RESP_RESPONSEFLAG=1 then 1 end) as float)/cast(count( *) as float)*100,2) as varchar(32)) as Perc,to_varchar(count (case when APP_FLAG = 1 then 1 end) ) as App
    from PRO_TABLEAU a inner join scores3 b ON A.SRC_CLIENTID = B.CLIENTID where SRC_MARKETINGDATE between """ + date + """ and  """ + date2 + """ group  by """ + prop + """,""" + mod + """"""
            cnx.cursor().execute("USE database " + db[client] + " ;")
            cnx.cursor().execute("USE schema DBO;")
            err = pd.read_sql(decile_query1,cnx)
            return dash_table.DataTable(
            id='table1',
            columns=[{"name": i, "id": i} for i in err.columns],
            data=err.to_dict('records'),
            sort_action="native",
            sort_mode="multi",
            #page_current = 0,
            page_size =20,
            #row_selectable='multi',
            #page_action='custom',
            filter_action='native',
            export_format='csv',
            #selected_rows=[],
            style_table={
            'maxHeight': '200ex',
            'overflowY': 'scroll',
            'width': '100%',
            'minWidth': '100%',
            'flex-wrap': 'nowrap',
            'text_align': 'center'
        },
        style_cell={
                'max-width': '20px',
                'font-family': 'Calibri',
                'text_align': 'left'
            },
        style_header={
        'backgroundColor': 'white',
        'fontWeight': 'bold',
        'font-family': 'Calibri',
    },
            )
        if client is not None and len(value)> 0 and  ( to is None or len(to) ==0) and len(model)> 0 and range_slide[0] == 0 and range_slide[1]==0:
            date =""
            for i in value:
                date += "'" + i + "',"
            date= date[:-1]
            mod =""
            for i in model:
                mod += "CEIL(" + i + ",-1),"
            mod= mod[:-1]
            decile_query1="""select """ + mod + """ ,  to_varchar(count( *),'999,999,999') as Total ,to_varchar(count (case when RESP_RESPONSEFLAG = 1 then 1 end)) as reponses ,cast(round(cast(count (case when RESP_RESPONSEFLAG=1 then 1 end) as float)/cast(count( *) as float)*100,2) as varchar(32)) as Perc,to_varchar(count (case when APP_FLAG = 1 then 1 end) ) as App
    from PRO_TABLEAU a inner join scores3 b ON A.SRC_CLIENTID = B.CLIENTID where SRC_MARKETINGDATE in (""" + date + """) group  by """ + mod + """"""
            decile_query2="""WITH CTE AS (SELECT * from AMFN_REPORTING.dbo.PRO_TABLEAU a inner join MO.DBO.Deciles2 b ON A.SRC_CLIENTID = B.CLIENTID)
select """ + mod + """ as shit, COUNT(*) FROM CTE PIVOT(MAX(Decile) FOR MODEL IN ('ALTAIR_EQ_CASHOUT_2019_20200120','SUPERSCORE_V2')) where SRC_MARKETINGDATE = '2020-07-23' group by """ + mod + """"""
            cnx.cursor().execute("USE database " + db[client] + " ;")
            cnx.cursor().execute("USE schema DBO;")
            err = pd.read_sql(decile_query1,cnx)
            return dash_table.DataTable(
            id='table1',
            columns=[{"name": i, "id": i} for i in err.columns],
            data=err.to_dict('records'),
            sort_action="native",
            sort_mode="multi",
            #page_current = 0,
            page_size =20,
            #row_selectable='multi',
            #page_action='custom',
            filter_action='native',
            export_format='csv',
            #selected_rows=[],
            style_table={
            'maxHeight': '200ex',
            'overflowY': 'scroll',
            'width': '100%',
            'minWidth': '100%',
            'flex-wrap': 'nowrap',
            'text_align': 'center'
        },
        style_cell={
                'max-width': '20px',
                'font-family': 'Calibri',
                'text_align': 'left'
            },
            style_header={
        'backgroundColor': 'white',
        'fontWeight': 'bold',
        'font-family': 'Calibri',
    },
            )
        if client is not None and len(value)> 0 and  len(to) > 0 and len(model)> 0 and range_slide[0] == 0 and range_slide[1]==0:
            date = "'" + value[0] + "'"
            date2 = "'" + to[0] + "'"
            mod =""
            for i in model:
                mod += "CEIL(" + i + ",-1),"
            mod= mod[:-1]
            decile_query1="""select """ + mod + """ ,  to_varchar(count( *),'999,999,999') as Total ,to_varchar(count (case when RESP_RESPONSEFLAG = 1 then 1 end)) as reponses ,cast(round(cast(count (case when RESP_RESPONSEFLAG=1 then 1 end) as float)/cast(count( *) as float)*100,2) as varchar(32)) as Perc,to_varchar(count (case when APP_FLAG = 1 then 1 end) ) as App
    from PRO_TABLEAU a inner join scores3 b ON A.SRC_CLIENTID = B.CLIENTID where SRC_MARKETINGDATE between """ + date + """ and  """ + date2 + """ group  by """ + mod + """"""
            cnx.cursor().execute("USE database " + db[client] + " ;")
            cnx.cursor().execute("USE schema DBO;")
            err = pd.read_sql(decile_query1,cnx)
            return dash_table.DataTable(
            id='table1',
            columns=[{"name": i, "id": i} for i in err.columns],
            data=err.to_dict('records'),
            sort_action="native",
            sort_mode="multi",
            export_format='csv',
            #page_current = 0,
            page_size =20,
            #row_selectable='multi',
            #page_action='custom',
            filter_action='native',
            #selected_rows=[],
            style_table={
            'maxHeight': '200ex',
            'overflowY': 'scroll',
            'width': '100%',
            'minWidth': '100%',
            'flex-wrap': 'nowrap',
            'text_align': 'center'
        },
        style_cell={
                'max-width': '20px',
                'font-family': 'Calibri',
                'text_align': 'left'
            },
            style_header={
        'backgroundColor': 'white',
        'fontWeight': 'bold',
        'font-family': 'Calibri',
    },
            )
        if client is not None and len(value)> 0 and  ( to is None or len(to) ==0) and len(properties) > 0 and len(model)> 0:
            date =""
            for i in value:
                date += "'" + i + "',"
            date= date[:-1]
            prop=""
            prop2=""
            for i in properties:
                if i == 'OFFER_SEGMENT':
                    i2 = """ case when left(OFFER_SEGMENT,3) = 'CLP' AND OFFER_SEGMENT LIKE '%ST%' THEN 'CLP_ST' WHEN left(OFFER_SEGMENT,3) = 'CLP' AND (OFFER_SEGMENT LIKE '%360%' OR OFFER_SEGMENT LIKE '%180%') THEN 'CLP_FIXED'
ELSE left(OFFER_SEGMENT,3) END as Class"""
                    prop2 += "" + i2 + ","
                    
                    i = """ case when left(OFFER_SEGMENT,3) = 'CLP' AND OFFER_SEGMENT LIKE '%ST%' THEN 'CLP_ST' WHEN left(OFFER_SEGMENT,3) = 'CLP' AND (OFFER_SEGMENT LIKE '%360%' OR OFFER_SEGMENT LIKE '%180%') THEN 'CLP_FIXED'
ELSE left(OFFER_SEGMENT,3) END """
                    prop += "" + i + ","
                    continue
                prop += "" + i + ","
                prop2 += "" + i + ","
            prop= prop[:-1]
            prop2= prop2[:-1]
            mod =""
            for i in model:
                mod += "" + i + ","
            mod= mod[:-1]
            decile_query1="""WITH CTE AS (SELECT * from PRO_TABLEAU a inner join scores3 b ON A.SRC_CLIENTID = B.CLIENTID)
SELECT """ + prop2 + """, MODEL,  to_varchar(count( *),'999,999,999') as Total ,to_varchar(count (case when RESP_RESPONSEFLAG = 1 then 1 end),'999,999,999') as Responses,cast(round(cast(count (case when RESP_RESPONSEFLAG=1 then 1 end) as float)/cast(count( *) as float)*100,2) as varchar(32)) as Perc FROM CTE UNPIVOT(DECILE FOR MODEL IN (""" + mod + """) ) WHERE SRC_MARKETINGDATE in (""" + date + """) and DECILE BETWEEN """ + str(range_slide[0]) + """ AND """ + str(range_slide[1]) + """ GROUP BY """ + prop + """, MODEL """
            cnx.cursor().execute("USE database " + db[client] + " ;")
            cnx.cursor().execute("USE schema DBO;")
            err = pd.read_sql(decile_query1,cnx)
            return dash_table.DataTable(
            id='table1',
            columns=[{"name": i, "id": i} for i in err.columns],
            data=err.to_dict('records'),
            sort_action="native",
            sort_mode="multi",
            #page_current = 0,
            page_size =20,
            #row_selectable='multi',
            #page_action='custom',
            filter_action='native',
            export_format='csv',
            #selected_rows=[],
            style_table={
            'maxHeight': '200ex',
            'overflowY': 'scroll',
            'width': '100%',
            'minWidth': '100%',
            'flex-wrap': 'nowrap',
            'text_align': 'center'
        },
        style_cell={
                'max-width': '20px',
                'font-family': 'Calibri',
                'text_align': 'left'
            },
            style_header={
        'backgroundColor': 'white',
        'fontWeight': 'bold',
        'font-family': 'Calibri',
    },
            )
        if client is not None and len(value)> 0 and  ( to is None or len(to) ==0) and len(model)> 0:
            date =""
            for i in value:
                date += "'" + i + "',"
            date= date[:-1]
            mod =""
            for i in model:
                mod += "" + i + ","
            mod= mod[:-1]
            decile_query1="""WITH CTE AS (SELECT * from PRO_TABLEAU a inner join scores3 b ON A.SRC_CLIENTID = B.CLIENTID)
SELECT MODEL,  to_varchar(count( *),'999,999,999') as Total ,to_varchar(count (case when RESP_RESPONSEFLAG = 1 then 1 end),'999,999,999') as Responses,cast(round(cast(count (case when RESP_RESPONSEFLAG=1 then 1 end) as float)/cast(count( *) as float)*100,2) as varchar(32)) as Perc FROM CTE UNPIVOT(DECILE FOR MODEL IN (""" + mod + """) ) WHERE SRC_MARKETINGDATE in (""" + date + """) and DECILE BETWEEN """ + str(range_slide[0]) + """ AND """ + str(range_slide[1]) + """ GROUP BY MODEL"""
            cnx.cursor().execute("USE database " + db[client] + " ;")
            cnx.cursor().execute("USE schema DBO;")
            err = pd.read_sql(decile_query1,cnx)
            return dash_table.DataTable(
            id='table1',
            columns=[{"name": i, "id": i} for i in err.columns],
            data=err.to_dict('records'),
            sort_action="native",
            sort_mode="multi",
            #page_current = 0,
            page_size =20,
            #row_selectable='multi',
            #page_action='custom',
            filter_action='native',
            export_format='csv',
            #selected_rows=[],
            style_table={
            'maxHeight': '200ex',
            'overflowY': 'scroll',
            'width': '100%',
            'minWidth': '100%',
            'flex-wrap': 'nowrap',
            'text_align': 'center'
        },
        style_cell={
                'max-width': '20px',
                'font-family': 'Calibri',
                'text_align': 'left'
            },
            style_header={
        'backgroundColor': 'white',
        'fontWeight': 'bold',
        'font-family': 'Calibri',
    },
            )
        if client is not None and len(value)> 0 and len(properties) > 0 and  len(to) > 0 and len(model)> 0:
            date = "'" + value[0] + "'"
            date2 = "'" + to[0] + "'"
            prop=""
            prop2=""
            for i in properties:
                if i == 'OFFER_SEGMENT':
                    i2 = """ case when left(OFFER_SEGMENT,3) = 'CLP' AND OFFER_SEGMENT LIKE '%ST%' THEN 'CLP_ST' WHEN left(OFFER_SEGMENT,3) = 'CLP' AND (OFFER_SEGMENT LIKE '%360%' OR OFFER_SEGMENT LIKE '%180%') THEN 'CLP_FIXED'
ELSE left(OFFER_SEGMENT,3) END as Class"""
                    prop2 += "" + i2 + ","
                    
                    i = """ case when left(OFFER_SEGMENT,3) = 'CLP' AND OFFER_SEGMENT LIKE '%ST%' THEN 'CLP_ST' WHEN left(OFFER_SEGMENT,3) = 'CLP' AND (OFFER_SEGMENT LIKE '%360%' OR OFFER_SEGMENT LIKE '%180%') THEN 'CLP_FIXED'
ELSE left(OFFER_SEGMENT,3) END """
                    prop += "" + i + ","
                    continue
                prop += "" + i + ","
                prop2 += "" + i + ","
            prop= prop[:-1]
            prop2= prop2[:-1]
            mod =""
            for i in model:
                mod += "" + i + ","
            mod= mod[:-1]
            decile_query1="""WITH CTE AS (SELECT * from PRO_TABLEAU a inner join scores3 b ON A.SRC_CLIENTID = B.CLIENTID)
SELECT """ + prop2 + """ , MODEL,  to_varchar(count( *),'999,999,999') as Total ,to_varchar(count (case when RESP_RESPONSEFLAG = 1 then 1 end),'999,999,999') as Responses,cast(round(cast(count (case when RESP_RESPONSEFLAG=1 then 1 end) as float)/cast(count( *) as float)*100,2) as varchar(32)) as Perc FROM CTE UNPIVOT(DECILE FOR MODEL IN (""" + mod + """) ) WHERE SRC_MARKETINGDATE  between """ + date + """ and """ + date2 + """and DECILE BETWEEN """ + str(range_slide[0]) + """ AND """ + str(range_slide[1]) + """ GROUP BY """ + prop + """ , MODEL"""
            cnx.cursor().execute("USE database " + db[client] + " ;")
            cnx.cursor().execute("USE schema DBO;")
            err = pd.read_sql(decile_query1,cnx)
            return dash_table.DataTable(
            id='table1',
            columns=[{"name": i, "id": i} for i in err.columns],
            data=err.to_dict('records'),
            sort_action="native",
            sort_mode="multi",
            #page_current = 0,
            page_size =20,
            #row_selectable='multi',
            #page_action='custom',
            filter_action='native',
            export_format='csv',
            #selected_rows=[],
            style_table={
            'maxHeight': '200ex',
            'overflowY': 'scroll',
            'width': '100%',
            'minWidth': '100%',
            'flex-wrap': 'nowrap',
            'text_align': 'center'
        },
        style_cell={
                'max-width': '20px',
                'font-family': 'Calibri',
                'text_align': 'left'
            },
            style_header={
        'backgroundColor': 'white',
        'fontWeight': 'bold',
        'font-family': 'Calibri',
    },
            )
        if client is not None and len(value)> 0 and   len(to) > 0 and len(model)> 0:
            date = "'" + value[0] + "'"
            date2 = "'" + to[0] + "'"
            mod =""
            for i in model:
                mod += "" + i + ","
            mod= mod[:-1]
            decile_query1="""WITH CTE AS (SELECT * from PRO_TABLEAU a inner join scores3 b ON A.SRC_CLIENTID = B.CLIENTID)
SELECT MODEL,  to_varchar(count( *),'999,999,999') as Total ,to_varchar(count (case when RESP_RESPONSEFLAG = 1 then 1 end),'999,999,999') as Responses,cast(round(cast(count (case when RESP_RESPONSEFLAG=1 then 1 end) as float)/cast(count( *) as float)*100,2) as varchar(32)) as Perc FROM CTE UNPIVOT(DECILE FOR MODEL IN (""" + mod + """) ) WHERE SRC_MARKETINGDATE  between """ + date + """ and """ + date2 + """and DECILE BETWEEN """ + str(range_slide[0]) + """ AND """ + str(range_slide[1]) + """ GROUP BY MODEL"""
            cnx.cursor().execute("USE database " + db[client] + " ;")
            cnx.cursor().execute("USE schema DBO;")
            err = pd.read_sql(decile_query1,cnx)
            return dash_table.DataTable(
            id='table1',
            columns=[{"name": i, "id": i} for i in err.columns],
            data=err.to_dict('records'),
            sort_action="native",
            sort_mode="multi",
            #page_current = 0,
            page_size =20,
            #row_selectable='multi',
            #page_action='custom',
            filter_action='native',
            export_format='csv',
            #selected_rows=[],
            style_table={
            'maxHeight': '200ex',
            'overflowY': 'scroll',
            'width': '100%',
            'minWidth': '100%',
            'flex-wrap': 'nowrap',
            'text_align': 'center'
        },
        style_cell={
                'max-width': '20px',
                'font-family': 'Calibri',
                'text_align': 'left'
            },
            style_header={
        'backgroundColor': 'white',
        'fontWeight': 'bold',
        'font-family': 'Calibri',
    },
            )
        if client is not None and len(properties)> 0:
            mod =""
            for i in properties:
                mod += "" + i + ","
            mod= mod[:-1]
            decile_query1="""select """ + mod + """ , to_varchar(count( *),'999,999,999') as Total ,to_varchar(count (case when RESP_RESPONSEFLAG = 1 then 1 end)) as reponses ,to_varchar(count (case when APP_FLAG = 1 then 1 end) ) as App
    from PRO_TABLEAU a inner join scores3 b ON A.SRC_CLIENTID = B.CLIENTID  group  by """ + mod + """"""
            cnx.cursor().execute("USE database " + db[client] + " ;")
            cnx.cursor().execute("USE schema DBO;")
            err = pd.read_sql(decile_query1,cnx)
            return dash_table.DataTable(
            id='table1',
            columns=[{"name": i, "id": i} for i in err.columns],
            data=err.to_dict('records'),
            sort_action="native",
            sort_mode="multi",
            #page_current = 0,
            page_size =20,
            #row_selectable='multi',
            #page_action='custom',
            filter_action='native',
            export_format='csv',
            #selected_rows=[],
            style_table={
            'maxHeight': '200ex',
            'overflowY': 'scroll',
            'width': '100%',
            'minWidth': '100%',
            'flex-wrap': 'nowrap',
            'text_align': 'center'
        },
        style_cell={
                'max-width': '20px',
                'font-family': 'Calibri',
                'text_align': 'left'
            },
            style_header={
        'backgroundColor': 'white',
        'fontWeight': 'bold',
        'font-family': 'Calibri',
    },
            )





if __name__ == '__main__':
    serve(server)
    #app.run_server(debug=True)
