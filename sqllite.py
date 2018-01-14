import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")


def data_entry(field="keyword", search_string="p"):
    c.execute("INSERT INTO stuffToPlot VALUES(1452549219,'2016-01-11 13:53:39','p',6)")
    pyhton = "p"
    sql = c.execute("SELECT datestamp FROM stuffToPlot WHERE %s=?" % field, (search_string,))
    print(c.fetchone())

create_table()
data_entry()