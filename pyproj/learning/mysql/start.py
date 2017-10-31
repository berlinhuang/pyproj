# -*- coding: utf-8 -*-

from pyproj.learning.mysql import conn

import  os

def operate():
    print os.getcwd() #/home/berlin/code/github/pyproj/pyproj
    db = conn.Conn('./base/mysql/dbconfig.conf')
    dbconn = db.get_conn()
    cursor = dbconn.cursor()
    DB_NAME = 'employees'
    TABLES = {}
    TABLES['employees'] = (
        "CREATE TABLE `employees` ("
        "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
        "  `birth_date` date NOT NULL,"
        "  `member_name` varchar(14) NOT NULL,"
        "  `gender` enum('M','F') NOT NULL,"
        "  `hire_date` date NOT NULL,"
        "  PRIMARY KEY (`emp_no`)"
        ") ENGINE=InnoDB")

    TABLES['departments'] = (
        "CREATE TABLE `departments` ("
        "  `dept_no` int(11) NOT NULL,"
        "  `dept_name` varchar(40) NOT NULL,"
        "  PRIMARY KEY (`dept_no`), UNIQUE KEY `dept_name`(`dept_name`)"
        ") ENGINE=InnoDB")

    db.create_database(cursor,'testdb')

    db.use_database(cursor,DB_NAME)

    print('creating table employees')
    db.create_table(cursor, TABLES['employees'])

    print('creating table departments')
    db.create_table(cursor, TABLES['departments'])
