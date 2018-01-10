import sqlite3

conn = sqlite3.connect('AutomationPro.db')
print "Opened database successfully";

conn.execute('''CREATE TABLE tboutputdvc
         (DID INTEGER PRIMARY KEY   AUTOINCREMENT,
         DVC_NAME           TEXT    NOT NULL,
         DVC_IPADDR         TEXT     NOT NULL UNIQUE,
         RELAY_SIZE        TEXT NOT NULL,
         SOCKET_STATUS         INT);''')
print "Table created successfully";

conn.close()
