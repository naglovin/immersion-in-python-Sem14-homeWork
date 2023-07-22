
class BaseException(Exception):
    pass

class LevelException(BaseException):
    def __init__(self, level):
        self.level = level
    def __str__(self):
        return f'Level {self.level} incorrect'

class AccessException(BaseException):
    def __init__(self, user_id):
        self.user_id = user_id
    def __str__(self):
        return f'Acces for {self.user_id} denied'
