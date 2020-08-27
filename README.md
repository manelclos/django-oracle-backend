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
