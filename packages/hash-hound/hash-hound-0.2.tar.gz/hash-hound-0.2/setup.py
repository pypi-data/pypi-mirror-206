from setuptools import setup

setup(
    name='hash-hound',
    version='0.2',
    description='This program identifies the algorithm used for a given hash value and provides the corresponding hashcat mode number, which can be used for password cracking. It uses a dictionary mapping hash lengths to algorithms and their respective hashcat mode numbers. The user inputs a hash value, and the program returns the algorithm and mode number if available, or "Unknown algorithm" otherwise.',
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
