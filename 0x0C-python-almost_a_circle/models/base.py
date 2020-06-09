#!/usr/bin/python3
"""base model module"""
import json


class Base():
    """base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to json"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """to str"""
        if json_string is None or json_string == "" or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """to file"""
        if list_objs is None:
            lst = []
        else:
            lst = [ele.to_dictionary() for ele in list_objs]

        with open("{}.json".format(cls.__name__), "w") as file:
            file.write(Base.to_json_string(lst))

    @classmethod
    def create(cls, **dic):
        """create"""
        if cls.__name__ == "Square":
            new = cls(1)
        else:
            new = cls(1, 1)
        new.update(**dic)
        return new

    @classmethod
    def load_from_file(cls):
        """load lst"""
        lst = []
        try:
            with open(cls.__name__ + ".json", "r") as file:
                lst_item = file.read()
        except:
            return lst
        lst_dic = cls.from_json_string(lst_item)
        for ele in lst_dic:
            lst.append(cls.create(**ele))
        return lst
