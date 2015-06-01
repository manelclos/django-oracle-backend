from django.db.backends.oracle.base import DatabaseWrapper as OracleDatabaseWrapper
from django_oracle_backend.contrib.gis.db.backends.oracle.creation import OracleCreation
from django.contrib.gis.db.backends.oracle.introspection import OracleIntrospection
from django.contrib.gis.db.backends.oracle.operations import OracleOperations


class DatabaseWrapper(OracleDatabaseWrapper):

    # Django 1.8 moves data_types to DatabaseWrapper
    if hasattr(OracleDatabaseWrapper, 'data_types'):
        data_types = OracleDatabaseWrapper.data_types.copy()
        data_types.update({
                'AutoField': 'NUMBER(38)',
                'CharField': 'VARCHAR2(%(max_length)s)',
                'CommaSeparatedIntegerField': 'VARCHAR2(%(max_length)s)',
                'FileField': 'VARCHAR2(%(max_length)s)',
                'FilePathField': 'VARCHAR2(%(max_length)s)',
                'IPAddressField': 'VARCHAR2(15)',
                'GenericIPAddressField': 'VARCHAR2(39)',
                'SlugField': 'VARCHAR2(%(max_length)s)',
                'TextField': 'CLOB',
                'URLField': 'VARCHAR2(%(max_length)s)',
                'UUIDField': 'VARCHAR2(32)',
            })

    def __init__(self, *args, **kwargs):
        super(DatabaseWrapper, self).__init__(*args, **kwargs)
        self.ops = OracleOperations(self)
        self.creation = OracleCreation(self)
        self.introspection = OracleIntrospection(self)

