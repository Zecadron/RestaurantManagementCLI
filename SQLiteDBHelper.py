import sqlite3

class SQLiteDBHelper:

    def __init__(self, dbName, table_create_dict):
        self.conn = sqlite3.connect(dbName)
        self.conn.row_factory = sqlite3.Row
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

    def select(self, tableName, selColumn, whereCols, whereVals=None):
        sel_dict = dict()
        cur = None

        if whereVals is None:
            cur = self.conn.execute("select * from " + tableName)
        else:
            cmd = "select * from {} where {}=?" + " and {}=?"*(len(whereCols)-1)
            cmd = cmd.format(*((tableName,) + whereCols))
            cur = self.conn.execute(cmd, whereVals)

        for row in cur:
            if not row[whereCols[0]] in sel_dict:
                sel_dict[row[whereCols[0]]] = row[selColumn]
            elif type(sel_dict[row[whereCols[0]]]) is not list:
                temp = sel_dict[row[whereCols[0]]]
                sel_dict[row[whereCols[0]]] = [temp, row[selColumn]]
            else:
                sel_dict[row[whereCols[0]]].append(row[selColumn])

        return sel_dict

    def insert(self, tableName, values):
        if values[0] == "auto":
            cmd = "insert into " + tableName + \
                    " values (null" + ",?"*(len(values)-1) + ");"
            values = values[1:]
        else:
            cmd = "insert into " + tableName + \
                    " values (?" + ",?"*(len(values)-1) + ");"
        print(cmd)
        print(values)
        self.conn.execute(cmd, values)
        self.conn.commit()

    def update(self, tableName, selColumn, value, whereColumn, whereVal):
        cmd = "update " + tableName + " set {}=? where {}=?;" 
        cmd = cmd.format(selColumn, whereColumn)
        self.conn.execute(cmd, (value, whereVal))
        self.conn.commit()

    def delete(self, tableName, whereColumn, whereVal):
        cmd = "delete from " + tableName + " where {}=?;"
        cmd = cmd.format(whereColumn)
        self.conn.execute(cmd, (whereVal,))
        self.conn.commit()
