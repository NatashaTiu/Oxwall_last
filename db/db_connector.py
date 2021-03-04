import pymysql.cursors

from value_objects.user import User


def _our_hash(password):
    d = {
        "pass": "3b20a0de2500a291d0681bc075f0a761c29b362a2246cde4ed6cbe7bb82d26fa",
        "test": "a2b84e6c176c01e1aacd3312469e5ac732978f6534af33290882f5aa32be572c",
        "secret": "74210d690a28b4372ca86ff249c472975d860a537d19f0f551cd2c7d908222ea"
    }
    return d[password]


param = {"host":'localhost',
        "user": 'root',
        "password":'mysql',
        "database":'oxwa311',
}


class OxwallDB:
    def __init__(self, **param):
        self.connection = pymysql.connect(**param,
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)
        self.connection.autocommit(True)

    def close(self):
        self.connection.close()

    def create_user(self, user):
        with self.connection.cursor() as cursor:
            # Create a new record
            sql = """INSERT INTO `ow_base_user` (`username`, `email`, `password`, `emailVerify`, `joinIp`) 
                     VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(sql, (user.username, user.email, _our_hash(user.password), 0, "2130706433"))
        with self.connection.cursor() as cursor:
            sql1 = f"SELECT * FROM `ow_base_user` WHERE ow_base_user.username = '{user.username}'"
            cursor.execute(sql1)
            user_id = cursor.fetchone()['id']
            sql = f"""INSERT `ow_base_question_data` (`userId`, `textValue`, `questionName`)
                      VALUES ("{user_id}", "{user.real_name}", "realname")"""
            cursor.execute(sql)
            sql = f"""INSERT `ow_base_question_data`(`userId`, `intValue`, `questionName`)
                      VALUES("{user_id}", {user.gender}, "sex")"""
            cursor.execute(sql)
            sql = f"""INSERT `ow_base_question_data`(`userId`, `dateValue`, `questionName`)
                      VALUES("{user_id}", "1982-02-10 00:00:00", "birthdate")"""
            cursor.execute(sql)

    def get_users(self):
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = """SELECT `id`, `username`, `password`, `email` FROM `ow_base_user`"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return(User(**user) for user in result)

    def delete_user(self, user):
        with self.connection.cursor() as cursor:
            sql1 = f"SELECT * FROM ow_base_user WHERE ow_base_user.username = '{user.username}'"
            cursor.execute(sql1)
            user_id = cursor.fetchone()['id']
        #     sql = f"""DELETE FROM `ow_base_question_data`
        #                WHERE `ow_base_question_data`.`userId` = {user_id};"""
        #     cursor.execute(sql)
        # with self.connection.cursor() as cursor:
        #     sql = f'''DELETE FROM `ow_base_user`
        #               WHERE `ow_base_user`.`username` = "{user.username}"'''
        #     cursor.execute(sql)


if __name__ == 'main':
    db_obj = OxwallDB(host='localhost', user="root", password="mysql", database="oxwa311")







