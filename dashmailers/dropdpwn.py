from connection import cnx
import queries
cnx.cursor().execute("USE database AMFN_REPORTING;")
cnx.cursor().execute("USE schema DBO;")
cs = cnx.cursor()

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

decile_results = cs.execute(queries.query_decile).fetchall()
fields_results = cs.execute(queries.query_fields).fetchall()
mylist=[]
mylist1=[]
Decile=[]
Fields =[]
ranges={}
for i in decile_results:
    model = i[0]
    Decile.append({'label': model, 'value': model})
for i in fields_results:
    field = i[0]
    Fields.append({'label': field, 'value': field})

def eshta (x):
    cnx.cursor().execute("USE database " + db[x] + " ;")
    cnx.cursor().execute("USE schema DBO;")
    listy=[]
    query = "select SRC_MARKETINGDATE from DBO.PRO_TABLEAU where SRC_MARKETINGDATE > DATEADD(MONTH,-24,CURRENT_DATE())  and OFFER_SEGMENT not like '%Trig%' and OFFER_SEGMENT not like 'seed%' and OFFER_SEGMENT not like '%TRIG%' group by SRC_MARKETINGDATE order by SRC_MARKETINGDATE desc"
    results = cnx.cursor().execute(query).fetchall()
    for i in results:
        date = i[0].strftime('%Y-%m-%d')
        #x += "{'label' : '" + str(i[0]) + "' , 'value' : '" + str(i[0]) + "'},\n"
        #listy.append({'label': date, 'value': date})
        listy.append(str(date))
    return listy



