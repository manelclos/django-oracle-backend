django-oracle-backend
=====================

It is not easy to override django so that the Oracle driver does not use NVARCHAR2. So here is a very simple package to force usage of VARCHAR2 when creating the database fields.

Installation
------------
```
pip install git+https://github.com/manelclos/django-oracle-backend.git#egg=django-oracle-backend
```
