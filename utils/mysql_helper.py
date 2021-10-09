"""
数据库连接助手
"""
import pymysql

from news_web.settings import DATABASES


class MySqlDbHelper(object):
    conn = None  # 连接对象
    cursor = None  # 游标对象，用来执行SQL语句
    database = DATABASES["default"].get("NAME")
    host = DATABASES["default"]["HOST"]
    port = int(DATABASES["default"]["PORT"])
    user = DATABASES["default"]["USER"]
    password = DATABASES["default"]["PASSWORD"]

    @classmethod
    def __open_connect(cls):
        '''
        这是私有方法，获取连接
        :return:
        '''

        cls.conn = pymysql.connect(
            host=cls.host,
            port=cls.port,
            database=cls.database,
            user=cls.user,
            password=cls.password,
        )
        return cls.conn


    @classmethod
    def query(cls, *args):
        '''
        执行select查询
        :paramsql:sql语句
        :paramargs:查询参数
        :return:返回的是字典row
        '''


        try:
            cls.__open_connect()
            cls.cursor = cls.conn.cursor(pymysql.cursors.DictCursor)
            sql = args[0]  # 这是查询语句
            params = list(args[1:])  # 后面是参数
            cls.cursor.execute(sql, params)
            rows = cls.cursor.fetchall()
            return rows
        except Exception as e:
            raise e
        finally:
            cls.__closeAll()


    @classmethod
    def execute(cls, *args):
        '''
        用来执行DML语句insert,update,delete
        :paramargs:
        :return:
        '''


        try:
            cls.__open_connect()
            cls.cursor = cls.conn.cursor()
            sql = args[0]  # 这是DML语句
            params = list(args[1:])  # 后面是参数
            ret = cls.cursor.execute(sql, params)
            cls.conn.commit()
            return ret
        except Exception as e:
            cls.conn.rollback()
            raise e
        finally:
            cls.__closeAll()


    @classmethod
    def __closeAll(cls):
        '''
        私有方法，用来关闭连接
        :return:
        '''


        if cls.cursor is not None:
            cls.cursor.close()
        if cls.conn is not None:
            cls.conn.close()
