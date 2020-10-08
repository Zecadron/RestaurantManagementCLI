import sqlite3

class SQLiteDBHelper:

    def __init__(self, dbName, table_create_dict):
        self.conn = sqlite3.connect(dbName)
        for tableName in table_create_dict:
            if not self.tableExists(tableName):
                self.createTable(tableName, table_create_dict)

    def __del__(self):
        self.conn.close()

    def tableExists(self, tableName):
        cur = self.conn.execute("select name from sqlite_master \
                where type='table' and name='{}'".format(tableName))
        data = cur.fetchall()
        if len(data) == 0:
            return False
        else:
            return True

    def createTable(self, tableName, table_create_dict):
        self.conn.execute(table_create_dict[tableName])

    def select(self, tableName, selColumn, whereColumn, whereVal=None):
        sel_dict = dict()
        cur = None
        if whereVal is None:
            cur = self.conn.execute("select * from ?", tableName)
        else:
            cur = self.conn.execute("select * from ? where ?=?",
                    (tableName, whereColumn, whereVal))
        for row in cur:
            sel_dict[row[whereColumn]] = row[selColumn]
        return sel_dict

    def insert(self, tableName, values):
        cmd = "insert into " + tableName + \
                "values (null" + ",?"*len(values) + ");"
        self.conn.execute(cmd, values)
        self.conn.commit()
