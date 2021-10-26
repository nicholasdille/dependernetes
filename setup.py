from setuptools import setup

setup(
    name='dependernetes',
    version='0.0.1',
    py_modules=['dependernetes'],
    install_requires=[
        'Click',
        'kubernetes',
        'pydot'
    ],
    entry_points={
        'console_scripts': [
            'dependernetes = dependernetes:cli'
        ],
    },
)