import psycopg2

conn = psycopg2.connect("dbname=postgres user=postgres host=localhost password=2345")

cur = conn.cursor()

# cur.execute("CREATE TABLE weather2 (city varchar(80), temp int, daydate date);")

# cur.execute("INSERT INTO weather2 (city, temp, daydate) VALUES ('Minsk', 16, '2022-09-06')")
# cur.execute("INSERT INTO weather2 (city, temp, daydate) VALUES ('Minsk', 13, '2022-09-07')")
# cur.execute("INSERT INTO weather2 (city, temp, daydate) VALUES ('Gomel', 20, '2022-09-06')")
# cur.execute("INSERT INTO weather2 (city, temp, daydate) VALUES ('Gomel', 22, '2022-09-07')")

cur.execute("SELECT * FROM weather2;")

# print(cur.fetchone())
# print('-------------------------------------------------------------------------------------------')
for ln in cur.fetchall():
    print(ln)
# print(cur.fetchall())

conn.commit()
cur.close()
conn.close()
