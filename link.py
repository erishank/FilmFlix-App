import sqlite3 as sql

dbLink = sql.connect("python project2/filmFlix.db") # connect method
dbCursor = dbLink.cursor()# cursor method to execute the sql queries/statements