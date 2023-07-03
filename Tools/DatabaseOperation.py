import mysql.connector
import re


class SQL:
    """
    创建示例后记得关闭游标，调用close_SQL实现
    """

    def __init__(self):
        self.cnx = self.__connectSQL__()
        self.cursor = self.cnx.cursor()

    def __connectSQL__(self):
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="100221",
            database="code_audit"
        )
        return cnx

    @staticmethod
    def insert_scan_function(cnx, cursor, data_list):
        """
        读入一条函数信息
        :param cnx: 实例的cnx
        :param cursor: 实例的cursor
        :param data_list: 函数信息
        :return: 是否执行成功,错误返回-1
        """
        try:
            # 使用正则表达式匹配参数
            pattern = r"\b\w+\s\w+\b"
            matches = re.findall(pattern, data_list["parameter"])

            # 将匹配到的参数存储到列表中
            param_list = list(matches)

            insert_query = "INSERT INTO scan_function ( return_type, `function`, parameter, " \
                           "  function_text, belong_file, `start`, `end`," \
                           "  parameters, function_type, risk) VALUES " \
                           "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (data_list['return_type'], data_list['function_name'], ','.join(param_list), data_list['body'],
                    data_list['path'], data_list['start'], data_list['end'], param_list.__len__(), '0', '0')
            cursor.execute(insert_query, data)
            # 提交
            cnx.commit()

            return 0

        except Exception as e:
            print("怎么想都插不进去吧喵（哭泣）")
            return e

    @staticmethod
    def insert_function_tree(cnx, cursor, data_list):
        """
        按照数据库格式插入：list第一项是function的id，第二项是前置的list序列化形式，第三项是后置的list序列化形式
        :param cnx:
        :param cursor:
        :param data_list: list
        :return: 无
        """
        # 插入
        try:
            insert_query = "INSERT INTO function_tree ( function_id, pre_function, sub_function) VALUES " \
                           "(%s, %s, %s)"
            data = (data_list[0], data_list[1], data_list[2])
            cursor.execute(insert_query, data)
            # 提交
            cnx.commit()
        except Exception as e:
            print("怎么想都插不进去吧喵（哭泣）")
            return e

    @staticmethod
    def select_function_tree(cursor):
        """
        返回function_tree的所有信息
        :param cursor:
        :return: 以list形式返回
        """
        try:
            # 执行查询语句
            query = "SELECT DISTINCT * FROM function_tree"
            cursor.execute(query)

            # 获取结果
            return [cursor.fetchall()]
        except Exception as e:
            print("不是主人不可以看得啦喵（气急败坏）")
            return e

    @staticmethod
    def select_scan_function(cursor):
        try:
            # 执行SQL查询
            query = "SELECT * FROM scan_function"
            cursor.execute(query)

            # 获取查询结果
            func_infos = []

            result = cursor.fetchall()

            for ret in result:
                func_info = {
                    'id': ret[0],
                    'function': ret[1],
                    'function_text': ret[2],
                    'return_type': ret[3],
                    'parameter': ret[4],
                    'parameters': ret[5],
                    'function_type': ret[6],
                    'belong_file': ret[7],
                    'start': ret[8],
                    'end': ret[9],
                    'risk': ret[10]
                }
    
                func_infos.append(func_info)
            # 遍历结果并输出
            return func_infos
        except Exception as e:
            print("不是主人不可以看得啦喵（气急败坏）")
            return e

    @staticmethod
    def select_file(cursor):
        try:
            # 执行查询语句
            query = "SELECT DISTINCT belong_file FROM scan_function"
            cursor.execute(query)

            # 获取结果
            return [row[0] for row in cursor.fetchall()]
        except Exception as e:
            print("不是主人不可以看得啦喵（气急败坏）")
            return e

    @staticmethod
    def select_id_by_path(cursor, path):
        try:
            # 执行查询语句
            query = "SELECT id, `end` FROM scan_function WHERE belong_file = %s"
            value = (path,)
            cursor.execute(query, value)

            # 获取查询结果并存入列表
            result = []
            for row in cursor:
                result.append(row)
            return result
        except Exception as e:
            print("不是主人不可以看得啦喵（气急败坏）")
            return e

    @staticmethod
    def select_id_by_end(cursor, end):
        try:
            # 执行查询语句
            query = "SELECT id FROM scan_function WHERE `end` = %s"
            value = (end,)
            cursor.execute(query, value)

            # 获取查询结果并存入列表
            result = []
            for row in cursor:
                result.append(row)
            return result
        except Exception as e:
            print("不是主人不可以看得啦喵（气急败坏）")
            return e

    @staticmethod
    def update_risk_by_id(cnx, cursor, id):
        try:
            # 执行更新操作
            update_query = "UPDATE scan_function SET risk = %s WHERE id = %s"
            update_value = ('-1', id)
            cursor.execute(update_query, update_value)

            # 提交更改
            cnx.commit()
        except Exception as e:
            print("不是主人不可以帮我换的喵（害羞）")
            return e

    @staticmethod
    def update_risk_by_c(cnx, cursor, id, risk):
        try:
            # 执行更新操作
            update_query = "UPDATE scan_function SET risk = %s WHERE id = %s"
            update_value = (risk, id)
            cursor.execute(update_query, update_value)

            # 提交更改
            cnx.commit()
        except Exception as e:
            print("不是主人不可以帮我换的喵（害羞）")
            return e

    @staticmethod
    def read_function_from_s(cursor):
        try:
            # 从表scan中读取列name的信息
            query = "SELECT id, `function` FROM scan_function"
            cursor.execute(query)
            result = []
            for row in cursor:
                result.append(row)
            return result
        except Exception as e:
            print("不是主人不可以看得啦喵（气急败坏）")
            return e

    @staticmethod
    def read_function_from_c(cursor):
        try:
            # 从表scan中读取列name的信息
            query = "SELECT id, `function` FROM c_function"
            cursor.execute(query)
            result = []
            for row in cursor:
                result.append(row)
            return result
        except Exception as e:
            print("不是主人不可以看得啦喵（气急败坏）")
            return e

    def delete_SQL(self, cnx, cursor):
        pass

    def close_SQL(self, cursor, cnx):
        # 关闭游标对象和数据库连接
        cursor.close()
        cnx.close()
