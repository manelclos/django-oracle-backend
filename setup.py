from setuptools import setup, find_packages


setup(
    name='django-oracle-backend',
    version='0.1',
    description='Use VARCHAR2 instead of NVARCHAR2 when creating '
                'the database tables',
    long_description=open('README.md').read(),
    author='Manel Clos',
    author_email='manelclos@gmail.com',
    url='http://github.com/manelclos/django-oracle-backend',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
