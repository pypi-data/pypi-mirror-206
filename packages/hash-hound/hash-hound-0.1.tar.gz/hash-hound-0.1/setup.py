from setuptools import setup

setup(
    name='hash-hound',
    version='0.1',
    description='Identify the algorithm used for a given hash value',
    url='https://github.com/hac10101/Hash-hound',
    author='hac10101',
    author_email='hac1337@tutanota.com',
    license='MIT',
    py_modules=['hash'],
    entry_points={
        'console_scripts': [
            'hash-hound=hash:main'
        ]
    },
    install_requires=[
        'termcolor'
    ],
    zip_safe=False
)
