from setuptools import setup
setup(
    name='cvcli',
    version='1.0.0',
    include_package_data=True,
    py_modules=['cvcli'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'cvcli = app.cvcli:cli',
        ],
    },
)