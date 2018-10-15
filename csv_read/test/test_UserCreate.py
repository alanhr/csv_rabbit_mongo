from mongoengine import connect
import pytest

from csv_read.model.User import User
from csv_read.UserCreate import create


@pytest.fixture
def conn():
    conn = connect('mongoenginetest', host='mongomock://localhost')

    yield conn


def test_create_user_with_success(conn):
    user_mock = {'name': 'Teste 01', 'email': 'teste01@gg.com', 'age': 100}

    user = create(user_mock)

    assert user_mock.get('email') == user.email


def test_create_return_expection_when_user_exists(conn):
    user_mock = {'name': 'Teste 01', 'email': 'teste02@gg.com', 'age': 100}

    expected_result = 'this email teste02@gg.com was already registered'

    User.objects.create(**user_mock)

    with pytest.raises(Exception) as excinfo:
        create(user_mock)

    assert expected_result in str(excinfo.value)


def test_create_return_expection_when_user_is_invalid(conn):
    user_mock = {'name': 'Te', 'email': 'teste03@gg.com', 'age': 0}

    expected_result = ("ValidationError (User:None) (String value is too"
                       " short: ['name'] Integer value is too small: ['age'])")

    with pytest.raises(Exception) as excinfo:
        create(user_mock)

    print('aqioidfd', excinfo.value)
    assert expected_result in str(excinfo.value)
