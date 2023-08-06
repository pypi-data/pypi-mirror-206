# -*- coding: utf-8 -*-
# author: 长风
import json
import os
import sqlite3
import pymysql
import site
import os
os.chdir(f'{site.getsitepackages()[-1]}/hctest_basic_platform')

class SQLite3Helper:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        """
        创建一个新表，其中包含给定名称和列。
        列应该是一个元组列表，其中每个元组包含列名和数据类型。
        """
        column_str = ', '.join([f'{name} {data_type}' for name, data_type in columns])
        self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({column_str})')
        self.conn.commit()

    def insert_data(self, table_name, data):
        """
        将新数据行插入到给定表中。
        数据应该是一个字典，其中键是列名，值是要插入的数据。
        """
        column_str = ', '.join(data.keys())
        value_str = ', '.join(['?' for _ in data.values()])
        self.cursor.execute(f'INSERT INTO {table_name} ({column_str}) VALUES ({value_str})', tuple(data.values()))
        self.conn.commit()

    def update_data(self, table_name, data, condition):
        """
        更新与给定条件匹配的给定表中的行。
        数据应该是一个字典，其中键是列名，值是要设置的新数据。
        条件应该是一个表示SQL查询的WHERE子句的字符串。
        """
        set_str = ', '.join([f'{name} = ?' for name in data.keys()])
        self.cursor.execute(f'UPDATE {table_name} SET {set_str} WHERE {condition}', tuple(data.values()))
        self.conn.commit()

    def delete_data(self, table_name, condition):
        """
        删除与给定条件匹配的给定表中的行。
        条件应该是一个表示SQL查询的WHERE子句的字符串。
        """
        self.cursor.execute(f'DELETE FROM {table_name} WHERE {condition}')
        self.conn.commit()

    def select_data(self, table_name, columns=None, condition=None):
        """
        选择与给定条件匹配的给定表中的行。
        列应该是要选择的列名的列表，或者为None以选择所有列。
        条件应该是一个表示SQL查询的WHERE子句的字符串，或者为None以选择所有行。
        返回一个字典列表，其中每个字典表示一行数据。
        """
        column_str = '*' if columns is None else ', '.join(columns)
        where_str = '' if condition is None else f'WHERE {condition}'
        self.cursor.execute(f'SELECT {column_str} FROM {table_name} {where_str}')
        rows = self.cursor.fetchall()
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in rows]


class PyMySQLHelper:
    def __init__(self, host, port, user, password, db):
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            db=db,
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        """
        创建一个新表，其中包含给定名称和列。
        列应该是一个元组列表，其中每个元组包含列名和数据类型。
        """
        column_str = ', '.join([f'{name} {data_type}' for name, data_type in columns])
        self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({column_str})')
        self.conn.commit()

    def insert_data(self, table_name, data):
        """
        将新数据行插入到给定表中。
        数据应该是一个字典，其中键是列名，值是要插入的数据。
        """
        column_str = ', '.join(data.keys())
        value_str = ', '.join(['%s' for _ in data.values()])
        self.cursor.execute(f'INSERT INTO {table_name} ({column_str}) VALUES ({value_str})', tuple(data.values()))
        self.conn.commit()

    def update_data(self, table_name, data, condition):
        """
        更新与给定条件匹配的给定表中的行。
        数据应该是一个字典，其中键是列名，值是要设置的新数据。
        条件应该是一个表示SQL查询的WHERE子句的字符串。
        """
        set_str = ', '.join([f'{name} = %s' for name in data.keys()])
        self.cursor.execute(f'UPDATE {table_name} SET {set_str} WHERE {condition}', tuple(data.values()))
        self.conn.commit()

    def delete_data(self, table_name, condition):
        """
        删除与给定条件匹配的给定表中的行。
        条件应该是一个表示SQL查询的WHERE子句的字符串。
        """
        self.cursor.execute(f'DELETE FROM {table_name} WHERE {condition}')
        self.conn.commit()

    def select_data(self, table_name, columns=None, condition=None):
        """
        选择与给定条件匹配的给定表中的行。
        列应该是要选择的列名的列表，或者为None以选择所有列。
        条件应该是一个表示SQL查询的WHERE子句的字符串，或者为None以选择所有行。
        返回一个字典列表，其中每个字典表示一行数据。
        """
        column_str = '*' if columns is None else ', '.join(columns)
        where_str = '' if condition is None else f'WHERE {condition}'
        self.cursor.execute(f'SELECT {column_str} FROM {table_name} {where_str}')
        rows = self.cursor.fetchall()
        return rows


if __name__ == '__main__':
    if not os.path.exists("db_config"):
        db_type = input("你是否需要使用MySQL作为你的数据库\n默认使用文件数据库sqlite3\n请输入['Yes' or 'No']:")
        if db_type.upper() in ["YES", "NO"]:
            if db_type.upper() == "YES":
                HOST = input("请输入数据库 HOST:")
                PORT = int(input("请输入数据库 PORT:"))
                USER = input("请输入数据库连接用户名:")
                password = input("请输入数据库连接密码:")
                db = input("请输入你要连接的数据库库名:")
                con = dict(zip(("host", "port", "user", "password", "db"), (HOST, PORT, USER, password, db)))
                os.makedirs("db_config")
                with open("./db_config/conf.json", encoding="utf-8", mode="w") as f:
                    f.write(json.dumps(con))
                PyMySQLHelper(**con).cursor.execute("""
                CREATE TABLE TestCase (
                    id         INT auto_increment PRIMARY KEY,
                    number     VARCHAR(50) NOT NULL,
                    title      VARCHAR(255) NOT NULL,
                    method     VARCHAR(10) NOT NULL,
                    path       VARCHAR(255) NOT NULL,
                    headers    TEXT,
                    params     TEXT,
                    json       TEXT,
                    data       TEXT,
                    created_at TIMESTAMP default CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP default CURRENT_TIMESTAMP
                );

                """)
            else:
                os.makedirs("db_config")
                with open("./db_config/conf.json", encoding="utf-8", mode="w") as f:
                    f.write(json.dumps({"db_file": "identifier.sqlite"}))
                SQLite3Helper("identifier.sqlite").cursor.execute("""
                create table TestCase
                (
                    id         INTEGER
                        primary key autoincrement,
                    number     VARCHAR(50)  not null,
                    title      VARCHAR(255) not null,
                    method     VARCHAR(10)  not null,
                    path       VARCHAR(255) not null,
                    headers    TEXT,
                    params     TEXT,
                    json       TEXT,
                    data       TEXT,
                    created_at TIMESTAMP default CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP default CURRENT_TIMESTAMP
                );
                """)
