from io import StringIO
from csv_update.CsvToList import CsvToList

MOCK = StringIO('name,email,age\nJorge,jorge@test.com,30\nAlan,alan@test.com,303')

def test_convert_string():

    expected_result = [{'name': 'Jorge', 'email': 'jorge@test.com', 'age': '30'}, 
    {'name': 'Alan', 'email': 'alan@test.com', 'age': '303'}]

    csvToList = CsvToList(MOCK)

    listDict = csvToList.get_list()

    assert listDict == expected_result
