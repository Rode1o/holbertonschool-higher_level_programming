#!/usr/bin/python3
"""MOdule for the class base"""
import json


class Base:
    """Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor of Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a json string"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save info into a file"""
        json_file = cls.__name__ + ".json"
        empty_list = []

        if list_objs is not None:
            for run in list_objs:
                empty_list.append(run.to_dictionary())

        with open(json_file, "w") as f:
            f.write(cls.to_json_string(empty_list))

    @staticmethod
    def from_json_string(json_string):
        """ returns the JSON string to a list of
        dictionaries."""
        if json_string is None and not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Returns an instance with all attributes
        already set'''

        dummy = cls(1, 1)
        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        '''Returns a list of instances'''
        filename = cls.__name__ + ".json"
        json_string = ""
        list_instances = []

        try:
            with open(filename) as fl:
                json_string = fl.read()
        except FileNotFoundError:
            return list()

        list_from_json = cls.from_json_string(json_string)
        for i in list_from_json:
            list_instances.append(cls.create(**i))

        return list_instances
