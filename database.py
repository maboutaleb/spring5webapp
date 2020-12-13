import pyodbc
import itertools 

conn = pyodbc.connect('DSN=test; database= AMFN_REPORTING; Warehouse= ETL01_WH; Schema=DBO; pwd=Hamoudizizo1')
cursor= conn.cursor()
cursor.execute('''SELECT * from PRO_TABLEAU a inner join scores3 b ON A.SRC_CLIENTID = B.CLIENTID  where SRC_MARKETINGDATE between '2020-09-01' and '2020-09-30' limit 50''')
row= cursor.fetchall()
#print(row.__getattribute__('OFFER_SEGMENT'))
mylist ={}
for i in row:
    newlist=[]
    if str(i.TD100_ALTAIR_EQ_CASHOUT_HF_2019_OCT_2020_MAR_LESSCOLS_FOLD) != 'None'  and int(str(i.TD100_ALTAIR_EQ_CASHOUT_HF_2019_OCT_2020_MAR_LESSCOLS_FOLD)) < 20:
        #mylist.append({i.SRC_CLIENTID,i.SRC_RESNUM})
        newlist.append(i.SRC_CLIENTID)
        newlist.append(i.SRC_RESNUM)
        newlist.append(i.SRC_CITY)
        mylist[i.SRC_CLIENTID] = newlist
        print(i.SRC_CLIENTID)
for i in mylist:
    #print(i, mylist[i] , len(mylist[i]))
    for x in range(len(mylist[i])):
        for y in list(itertools.combinations(mylist[i],x+1)):
            eshta=""
            for z in sorted(y):
                eshta += z + ',' 
            eshta +=  'Clientid-->' + i
            print(eshta)
            #print(y) 
        #print(list(itertools.combinations(mylist[i],x+1)))


