
# 在Windows上，安装时请选择UTF-8编码，以便正确地处理中文。

# 在Mac或Linux上，需要编辑MySQL的配置文件，把数据库默认的编码全部改为UTF-8。MySQL的配置文件默认存放在/etc/my.cnf或者/etc/mysql/my.cnf


import mysql.connector




conn = mysql.connector.connect( host= "192.168.163.128", user ='root',password = 'berlinhuang', database ="test")
cursor = conn.cursor()
SQL = "select * from auth_group"
r = cursor.execute(SQL)
r = cursor.fetchall()

