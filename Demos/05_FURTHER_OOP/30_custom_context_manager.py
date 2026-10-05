import json

# Our JSON handling file-based context manager! requires magic methods
class MyJsonFile():
    ...
    def __init__(self, filename, access_mode):
        """initialisation"""
        self.__filename = filename
        self.__access_mode = access_mode
    ...
    def __enter__(self):
        """open file and deserialize"""
        self.__open_file = open(self.__filename, self.__access_mode)
        self.__deserialize()
        return self.__myJsonData
    ...
    def __deserialize(self):
        """deserialize the json file into an object"""
        self.__myJsonData = json.load(self.__open_file)
    ...
    def __exit__(self, *args):
        """ensure file is safely closed"""
        self.__open_file.close()

import os
data_path = os.path.join(os.path.dirname(__file__), 'mydata.json')
with MyJsonFile(data_path, 'r') as mydata:
    """what do we have?"""
    print(mydata)


