from django.contrib.gis.db.backends.oracle.creation import OracleCreation as DjangoOracleCreation


class OracleCreation(DjangoOracleCreation):

    # Django 1.8 moves data_types to DatabaseWrapper
    if hasattr(DjangoOracleCreation, 'data_types'):
        data_types = DjangoOracleCreation.data_types.copy()
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
