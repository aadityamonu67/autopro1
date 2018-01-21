import sqlite3

conn = sqlite3.connect('AutomationPro.db')
print "Opened database successfully";

conn.execute('''CREATE TABLE tbtrigger
         (TID INTEGER PRIMARY KEY   AUTOINCREMENT,
         T_NAME         TEXT     NOT NULL,

         T_MSG       TEXT     ,
         T_IPADDR TEXT,
         T_RELAY_NO INT,     ----things to be triggered---
         T_STS INT,         

         T_SID INT,     # sensor id
         T_EXP TEXT,    #exp >,<,== 
         T_VALUE INT,    #value
         FOREIGN KEY(T_SID) REFERENCES tbinputdvc(SID)
        
        );''')
print "Table created successfully";

conn.close()
