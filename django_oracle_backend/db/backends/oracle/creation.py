import django

from django.db.backends.oracle.creation import DatabaseCreation as DjangoDatabaseCreation
from django.db.backends.oracle.base import DatabaseWrapper as DjangoDatabaseWrapper


if django.VERSION >= (1, 8, 0):
    class DatabaseWrapper(DjangoDatabaseWrapper):
        data_types = DjangoDatabaseWrapper.data_types.copy()
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
else:
    class DatabaseCreation(DjangoDatabaseCreation):
        data_types = DjangoDatabaseCreation.data_types.copy()
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
