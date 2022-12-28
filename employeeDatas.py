import mysql.connector


cnx = mysql.connector.connect(user='root', password='@lexander8891',
                              host='127.0.0.1',
                              database='infoDB')
#print("connected to DB")

cursor = cnx.cursor(buffered=True)

cursor.execute("SELECT * From employee ORDER BY Height DESC, Weight;")

cnx.commit()

results = cursor.fetchall()

for row in results:
  print(f"{row[0]} {row[2]} {row[1]}")

cnx.close()
