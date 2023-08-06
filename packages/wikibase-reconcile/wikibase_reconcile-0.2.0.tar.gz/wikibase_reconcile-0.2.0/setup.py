from setuptools import setup

setup(
    name='wikibase_reconcile',
    version='0.2.0',
    install_requires=[
        'requests',
        'importlib-metadata; python_version == "3.8"',
    ],
)