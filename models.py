import pyodbc
import itertools 

conn = pyodbc.connect('DSN=test; database= NOID; Warehouse= ETL01_WH; Schema=DBO; pwd=Hamoudizizo1')
cursor= conn.cursor()
cursor.execute('''SELECT  COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS t1
        WHERE TABLE_NAME = 'WRF_NOID_AMFN_FCO_ALTAIR_EX_ALL' AND TABLE_SCHEMA = 'DBO'
            AND COLUMN_NAME LIKE 'WRFD_%' ''')
row= cursor.fetchall()

for i in row:
    print(i)

l = [my.COLUMN_NAME for my in row]
X = 'WRFD_ZINC'
if X in l:
    print(X)
else:
    print('not in here')