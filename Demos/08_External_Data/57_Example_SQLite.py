import sqlite3

db = sqlite3.connect('whisky')

cur = db.cursor()
cur.execute('SELECT BRANDS.BNAME, REGION.RNAME         \
             FROM BRANDS,REGION                        \
             WHERE REGION.REGION_ID = BRANDS.REGION_ID \
             ORDER BY BRANDS.BNAME;')

for row in cur.fetchall():
   print("{0[0]:<30s} {0[1]:<30s}".format(row))

db.close()
