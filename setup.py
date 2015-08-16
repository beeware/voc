#/usr/bin/env python
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
    description='Tools to convert Python bytecode into Java bytecode.',
    long_description=long_description,
    author='Russell Keith-Magee',
    author_email='russell@keith-magee.com',
    url='http://pybee.org/voc',
    packages=find_packages(exclude=['docs', 'tests']),
    entry_points={
        'console_scripts': [
            'voc = voc.__main__:main',
        ]
    },
    license='New BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
    test_suite='tests'
)
