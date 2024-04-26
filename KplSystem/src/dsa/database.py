import cx_Oracle
#数据库操作封装成类
class OracleDB:
    def __init__(self):
        self.username='scott'
        self.password='123456'
        self.hps='localhost:1521/orcl'
        self.conn=None
        self.cursor=None
    #1.连接数据库
    def connect(self):
        self.conn = cx_Oracle.connect(self.username, self.password,self.hps)
        self.cursor = self.conn.cursor()
        # print('数据库连接成功！')
    #2.执行sql语句
    #execute执行单条sql(创建、插入、更新)
    def execute(self,sql,*args):
        self.cursor.execute(sql,*args)
        self.conn.commit()
    #executemany执行多条sql(创建、插入、更新)
    def executemany(self, sql, param:list):
        self.cursor.executemany(sql, param)
        self.conn.commit()
    #查询
    def query(self, sql, *args):
        self.cursor.execute(sql,*args)
        result = self.cursor.fetchall()
        return result

    #3.关闭连接
    def close(self):
        self.cursor.close()
        self.conn.close()




