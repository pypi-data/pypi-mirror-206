from setuptools import setup

setup(
    name='SharkBinary',
    version='0.1',
    author='Shark Studios',
    author_email='margetin.michal123@gmail.com',
    description='A Python package for saving and loading data to and from custom binary files',
    py_modules=['sharkbinary'],
    install_requires=[
        'struct'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    project_urls={
        'Documentation': 'https://github.com/Miskoking800/SharkBinary/blob/main/README.md',
        'Source': 'https://github.com/Miskoking800/SharkBinary',
        'Tracker': 'https://github.com/Miskoking800/SharkBinary/issues',
    },
)
