django-oracle-backend
=====================

It is not easy to override django so that the Oracle driver does not use NVARCHAR2. So here is a very simple package to force usage of VARCHAR2 when creating the database fields.

Installation
------------
```
pip install git+https://github.com/manelclos/django-oracle-backend.git#egg=django-oracle-backend
```

Usage
-----

As reported in [issue #1](https://github.com/manelclos/django-oracle-backend/issues/1) this seems to still be usable.

Add it to your DATABASES configuration, Django will init the classes, see how to use it in the Django documentation: 
https://docs.djangoproject.com/en/3.1/ref/databases/#subclassing-the-built-in-database-backends


# Simple Example Setup

```
mysite/
    ...
    custom_oracle_engine/
        __init__.py
        base.py
```

## base.py
```python
from django.db.backends.oracle import base

class DatabaseWrapper(base.DatabaseWrapper):
    data_types = base.DatabaseWrapper.data_types.copy()
    data_types.update({
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

```

## settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'custom_oracle_engine',
        'NAME': 'XXX',
        'USER': 'XXX',
        'PASSWORD': 'XXX',
        'HOST': 'XXX',
        'PORT': '1521',
    }
}
```

More documentation can be found [here](https://docs.djangoproject.com/en/3.1/ref/databases/#subclassing-the-built-in-database-backends)
