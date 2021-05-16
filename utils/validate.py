import re

from curd.user import user


class Validate:
    def regex_phone(self, phone):
        result = re.match(r"^1[35678]\d{9}$", phone)
        if result:
            return True
        else:
            return False

    def check_phone(self, db, phone):
        if self.regex_phone(phone):
            db_user = user.get_user_by_phone(db, phone)
            if db_user:
                return '手机号已存在'
        else:
            return '手机号错误'

    def regex_email(self, email):
        result = re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', email)
        if result:
            return True
        else:
            return False

    def check_email(self, db, email):
        if self.regex_email(email):
            if user.get_user_by_email(db, email):
                return '邮箱已存在已存在'

    def check_username(self, db, username):
        if user.get_user_by_username(db, username):
            return '用户名已存在'

    def check(self, db, username, phone=None, email=None):
        if phone:
            error = self.check_phone(db, phone)
            if error:
                return error

        if email:
            error = self.check_email(db, email)
            if error:
                return error

        error = self.check_username(db, username)
        if error:
            return error
