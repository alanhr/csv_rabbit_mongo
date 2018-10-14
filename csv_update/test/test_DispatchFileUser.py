import pytest
import io
from werkzeug.datastructures import FileStorage
from unittest.mock import patch

from csv_update.DispatchFileUser import DispatchFileUser


@patch('csv_update.DispatchFileUser.Queue')
def test_successded(Queue):
    stream = io.BytesIO(
        b"'name,email,age\nJorge,jorge@test.com,30\nAlan,alan@test.com,303'")

    data = {'file': FileStorage(stream=stream,filename='test.csv', content_type='text/csv')}

    expected_result = True

    dispatch = DispatchFileUser(data)
    dispatch.send()

    assert dispatch.successded() == expected_result


@patch('csv_update.DispatchFileUser.Queue')
def test_fail(Queue):
    data = {'file': ''}

    expected_result = False

    dispatch = DispatchFileUser(data)
    dispatch.send()

    assert dispatch.successded() == expected_result
