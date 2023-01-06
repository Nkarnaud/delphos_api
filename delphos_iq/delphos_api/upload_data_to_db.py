import psycopg2

conn = psycopg2.connect(
    database="delphos_iq",
    user='ubuntu', password='ubuntu',
    host='psql', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

sql2 = '''COPY delphos_api_loans(title,country,sector,amount)
FROM  '/app/delphos_api/result.csv'
DELIMITER ';'
CSV HEADER;'''

cursor.execute(sql2)

conn.commit()
conn.close()
