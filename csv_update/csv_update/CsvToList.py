from csv import DictReader
import codecs

class CsvToList():

    def __init__(self, file):
        self.file = file
    
    def __get_lines(self):
        lines = (self.file.read()).splitlines()
        return lines 

    def __get_rows(self):
       return DictReader(self.__get_lines(), skipinitialspace=True) 
    
    def get_list(self):
        rows = self.__get_rows()

        return [{k: v for k, v in row.items()} for row in rows]

