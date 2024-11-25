from io import TextIOWrapper
import json


class JsonFileManager:
    __instance = None

    def __new__(cls, *args, **kwargs) -> "JsonFileManager":
        if cls.__instance is None:
            cls.__instance = super(JsonFileManager, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def read(self, data: TextIOWrapper):
        jsonified = json.load(data)
        return jsonified

    def write(self):
        pass