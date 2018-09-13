# -*- coding:utf-8 -*-

# add the model path to sys.path
import sys
import os

current_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_PATH = os.path.join(current_path, '..')
sys.path.append(ROOT_PATH)

from chatterbot_re.storage import StorageAdapter

class Query(object):

    def __init__(self, query={}):
        self.query = query

    def raw(self, data):
        query = self.query.copy()

        query.update(data) # query是字典，为什么可以query方法？

        return Query(query)

    def statement_text_equals(self, statement_text):
        query = self.query.copy()

        query['text'] = statement_text

        return Query(query)

    def statement_text_not_in(self, statements):
        query = self.query.copy()

        if 'text' not in query:
            query['text'] = {}

        if '$nin' not in query['text']:
            query['text']['$nin'] = []

        query['text']['$nin'].extend(statements)

        return Query(query)

    def statement_response_list_contains(self, statement_text):
        query = self.query.copy()

        if 'in_response_to' not in query:
            query['in_response_to'] = {}

        if '$elemMatch' not in query['in_response_to']:
            query['in_response_to']['$elemMatch'] = {}

        query['in_response_to']['$elemMatch']['text'] = statement_text

        return Query(query)

    def statement_response_list_equals(self, response_list):
        query = self.query.copy()

        query['in_response_to'] = response_list

        return Query(query)


class MongoDatabaseAdapter(StorageAdapter):
    """
    The MongoDatabaseAdapter is an interface that allows
    ChatterBot to store statements in a MongoDB database.
    :keyword database_uri: The URI of a remote instance of MongoDB.
                           This can be any valid
                           `MongoDB connection string <https://docs.mongodb.com/manual/reference/connection-string/>`_
    :type database_uri: str
    .. code-block:: python
       database_uri='mongodb://example.com:8100/'
    """

    def __init__(self, **kwargs):
        super(MongoDatabaseAdapter, self).__init__(**kwargs)
        from pymongo import MongoClient
        from pymongo.errors import OperationFailure

        self.database_uri = self.kwargs.get(
            'database_uri', 'mongodb://localhost:27017/chatterbot-database'
        )