import adodbapi
# Proof of concept: connection to Microvellum work order database

database = "MicrovellumWorkOrder"
connstr = """Provider=Microsoft.SQLSERVER.CE.OLEDB.4.0;Data Source={}.sdf""".format(database)

conn = adodbapi.connect(connstr)
curs = conn.cursor()

# Wont work without this for some reason...
conn.connector.CursorLocation = 2

print(conn.get_table_names())

curs.execute("select * from Parts")
parts = curs.fetchall()

for i in parts:
    for x in i:
        print(x.name)


curs.execute("select * from Products")
products = curs.fetchall()

for i in products:
    print(i.name)


curs.execute("select * from Sheets")
sheets = curs.fetchall()

for i in sheets:
    print(i.name, i.thickness)


conn.close()

