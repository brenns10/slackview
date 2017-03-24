from setuptools import setup, find_packages

setup(
    name='slackview',
    packages=find_packages(include=['slackview*']),
    include_package_data=True,
    install_requires=[
        'flask',
        'sqlalchemy',
        'flask-sqlalchemy',
        'flask-cas',
    ],
)
