from app.data.users import users

class AccountService:
    @staticmethod
    def authenticate(username: str, password: str):
        user = users.get(username)
        if not user:
            return None
        if user["password"] != password:
            return None
        return user
