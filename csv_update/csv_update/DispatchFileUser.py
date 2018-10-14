from csv_update.CsvToList import CsvToList
from csv_update.Queue import Queue
from csv_update.utils.file import save_tmp_file, allowed_file


class DispatchFileUser:
    def __init__(self, files):
        self.__files = files
        self.__error = {}

    def __send_to_queue(self, users):
        queue = Queue()

        queue.send_batch('user', users)

        queue.close()

    def __convert_file(self, file, users):
        full_path_file = save_tmp_file(file)

        csvToList = CsvToList(
            open(full_path_file))

        users = csvToList.get_list()
        return users

    def get_error(self):
        return self.__error

    def successded(self):
        return True if not self.__error else False

    def send(self):
        file = self.__files.get('file')
        users = []
        print(file)
        if file and allowed_file(file.filename, ['csv']):
            users = self.__convert_file(file, users)

            self.__send_to_queue(users)
        else:
            self.__error = {'error': 'Invalid file'}

        return users
