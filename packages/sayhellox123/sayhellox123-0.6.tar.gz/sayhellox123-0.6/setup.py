from setuptools import setup, find_packages

setup(name="sayhellox123", version="0.6", description="says hello", long_description="says hello", entry_points={
        'console_scripts': [
            'helloworld=helloworld.a:say_hello',
        ],
    })
