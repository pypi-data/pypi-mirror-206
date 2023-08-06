import psycopg2
import configparser

import re
import inflect


from custom_rails.db import *


class DbStatic:
    
    @classmethod
    def get_model(cls):

        name = cls.__name__
        # Remove "Model" from the end of the string
        name = re.sub("Model$", "", name)
        
        # Lowercase the string
        name = name.lower()
        
        # Pluralize the word
        p = inflect.engine()
        name = p.plural(name)
        return Db(name)
    
    @classmethod
    def execute_query(cls, query, params=None):
        model = cls.get_model()
        model.execute_query(query, params=None)

    @classmethod
    def execute_select(cls, query, params=None):
        model = cls.get_model()
        return model.execute_select(query, params=None)

    @classmethod
    def add(cls, data):
        model = cls.get_model()
        return model.add(data)

    @classmethod
    def get_all(cls):
        model = cls.get_model()
        return model.get_all()

    @classmethod
    def get_by_id(cls, id):
        model = cls.get_model()
        return model.get_by_id(id)

    @classmethod
    def update(cls, id, data):
        model = cls.get_model()
        model.update(id, data)

    @classmethod
    def delete(cls, id):
        model = cls.get_model()
        model.delete(id)

    @classmethod
    def add_column(cls, column_name, data_type):
        model = cls.get_model()
        model.add_column(column_name, data_type)

    @classmethod
    def delete_column(cls, column_name):
        model = cls.get_model()
        model.delete_column(column_name)
