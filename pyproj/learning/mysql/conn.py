# -*- coding: utf-8 -*-

# mysql.connector
# sqlalchemy
# MySQLdb




# 在Windows上，安装时请选择UTF-8编码，以便正确地处理中文。

# 在Mac或Linux上，需要编辑MySQL的配置文件，把数据库默认的编码全部改为UTF-8。MySQL的配置文件默认存放在/etc/my.cnf或者/etc/mysql/my.cnf


import mysql.connector

from mysql.connector import errorcode
import configparser #sudo pip install configparser
import sys

class Conn:
    def __init__(self, init_file):
        config = configparser.ConfigParser()
        config.read(init_file)
        self.host       = config.get('DATABASE','host')
        self.port       = config['DATABASE']['port']
        self.user       = config['DATABASE']['user']
        self.passwd     = config['DATABASE']['passwd']
        self.db         = config['DATABASE']['db']
        self.charset    = config['DATABASE']['charset']

    def get_conn(self):
        try:
            conn =  mysql.connector.connect( host= self.host, user =self.user,password = self.passwd, database =self.db, charset = self.charset)
            return conn
        except Exception as e:
            print('%s',e)
            sys.exit()

    def create_database(self, cursor, db_name):
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARSET 'utf8'".format(db_name))
        except mysql.connector.Error as err:
            print('Failed creating database: {}'.format(err))
            exit(1)

    def use_database(self, cursor, db_name):
            try:
                cursor.execute('USE {}'.format(db_name))
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_BAD_DB_ERROR: # ER_BAD_DB_ERROR 未知数据库
                    self.create_database(cursor, db_name)
                    cursor.execute('USE {}'.format(db_name))
                else:
                    print(err)
                    exit(1)

    def query_data(self, cursor, query_ddl, query_data=None):
        try:
            if query_data:
                cursor.execute(query_ddl, query_data)
            else:
                cursor.execute(query_ddl)
            for row in cursor:
                print(row)
        except mysql.connector.Error as err:
            print(err)

