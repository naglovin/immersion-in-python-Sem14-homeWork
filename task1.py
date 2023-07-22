# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.


import pytest
from  task3 import User
from  task4 import project
from exceptin import AccessException, LevelException
@pytest.fixture()
def set_up():
    return project()   # данные для теста


def test_access_fail_1(set_up):                               # тест на проверку того, что  будет выброс исключения AccesErorr при вводе невалидных данных, AccesErorr  прописан в Exceptions.py

    with pytest.raises(AccessException, match='Access denied'):
        set_up.login('Санин', '1')                      # передаются невалидные данные


def test_access(set_up):                                    # тест на проверку валидных данных, то что должна вернуться
    assert set_up.login('Nesterov', '1') == '5'             # вводятся валидные двнные и проверяем на совпадение с результатом


def test_access_fail_2(set_up):                                    # тест на проверку того, что  будет выброс исключения AccesErorr при вводе невалидных данных, AccesErorr  прописан в Exceptions.py
    with pytest.raises(LevelException):
        set_up.login('павело', '2')
        set_up.create_user('New_user', '1', '3')



if __name__ == '__main__':
    pytest.main(['Main'])


