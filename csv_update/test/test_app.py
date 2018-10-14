import pytest
import io
from unittest.mock import patch

from csv_update.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client


@patch('csv_update.DispatchFileUser.Queue')
def test_upload_status_equal_200(Queue, client):
    exptected_result = 200

    data = {}
    data['file'] = (io.BytesIO(
        b"'name,email,age\nJorge,jorge@test.com,30\nAlan,alan@test.com,303'"), 'test.csv')

    response = client.post(
        "/users/upload",
        content_type='multipart/form-data',
        data=data
    )

    assert response.status_code == exptected_result


@patch('csv_update.DispatchFileUser.Queue')
def test_upload_status_equal_400(Queue, client):
    exptected_result = 400

    data = {}
    data['file'] = ''

    response = client.post(
        "/users/upload",
        content_type='multipart/form-data',
        data=data
    )

    assert response.status_code == exptected_result
