#!/usr/bin/env python3
import io
import re
from setuptools import setup, find_packages

with io.open('./voc/__init__.py', encoding='utf8') as version_file:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")


with io.open('README.rst', encoding='utf8') as readme:
    long_description = readme.read()


setup(
    name='voc',
    version=version,
    description='Tools to convert Python code into Java bytecode.',
    long_description=long_description,
    author='Russell Keith-Magee',
    author_email='russell@keith-magee.com',
    url='https://beeware.org/voc',
    packages=find_packages(exclude=['docs', 'tests']),
    python_requires='>=3.4',
    entry_points={
        'console_scripts': [
            'voc = voc.__main__:main',
            'vod = voc.java.__main__:main',
        ]
    },
    license='New BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
    test_suite='tests',
    project_urls={
        'Funding': 'https://beeware.org/contributing/membership/',
        'Documentation': 'https://voc.readthedocs.io/en/latest/',
        'Tracker': 'https://github.com/beeware/voc/issues',
        'Source': 'https://github.com/beeware/voc',
    },
)
