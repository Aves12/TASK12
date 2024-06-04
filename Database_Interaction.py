import psycopg2

def store_items(items):
    conn = psycopg2.connect("dbname=restaurant user=postgres password=secret")
    cur = conn.cursor()
    for item, price in items:
        cur.execute("INSERT INTO menu (item, price) VALUES (%s, %s)", (item, price))
    conn.commit()
    cur.close()
    conn.close()
