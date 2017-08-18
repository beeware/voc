# -*- coding: utf-8 -*-
"""Check modules from Ouroboros that compile with voc."""

# Standard library imports
import argparse
from datetime import datetime
import subprocess
import multiprocessing
import os
import sys


REPO_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
KNOWN_PROBLEM_MODULES = set([
    '_collections_abc',
    '_markupbase',
    '_pyio',
    '_sitebuiltins',
    '_strptime',
    '_threading_local',
    '_weakrefset',
    'abc',
    'aifc',
    'argparse',
    'asyncio',
    'base64',
    'binhex',
    'bz2',
    'chunk',
    'codecs',
    'collections',
    'compileall',
    'concurrent',
    'contextlib',
    'ctypes',
    'curses',
    'datetime',
    'dbm',
    'decimal',
    'difflib',
    'distutils',
    'doctest',
    'email',
    'encodings',
    'enum',
    'filecmp',
    'ftplib',
    'functools',
    'getpass',
    'gettext',
    'glob',
    'heapq',
    'http',
    'idlelib',
    'imaplib',
    'importlib',
    'inspect',
    'io',
    'ipaddress',
    'itertools',
    'json',
    'lib2to3',
    'logging',
    'lzma',
    'macpath',
    'mailbox',
    'mimetypes',
    'modulefinder',
    'msilib',
    'multiprocessing',
    'netrc',
    'numbers',
    'operator',
    'optparse',
    'os',
    'pathlib',
    'pickle',
    'pkgutil',
    'platform',
    'plistlib',
    'profile',
    'pstats',
    'pty',
    'pydoc',
    'quopri',
    'selectors',
    'shutil',
    'smtpd',
    'smtplib',
    'sndhdr',
    'socketserver',
    'sqlite3',
    'sre_compile',
    'string',
    'tabnanny',
    'tarfile',
    'test',
    'timeit',
    'trace',
    'traceback',
    'unittest',
    'urllib',
    'uu',
    'uuid',
    'weakref',
    'webbrowser',
    'wsgiref',
    'xdrlib',
    'xml',
    'xmlrpc',
    'zipfile',
])

IGNORE_MODULES = set([
    '__builtins__',
    '__init__',
    'plat-aix4',
    'plat-darwin',
    'plat-freebsd4',
    'plat-freebsd5',
    'plat-freebsd6',
    'plat-freebsd7',
    'plat-freebsd8',
    'plat-generic',
    'plat-linux',
    'plat-netbsd1',
    'plat-next3',
    'plat-sunos5',
    'plat-unixware7',
    'site-packages',
    'tkinter',
    'turtle',
    'turtledemo',
])


def ouroboros_repo_folder():
    """Return the folder where the ouroboros repo was cloned.

    If the repo doesn't exist, clone it.
    """
    path = os.path.join(os.path.dirname(os.path.dirname(REPO_ROOT)), 'ouroboros')
    if os.path.isdir(os.path.join(path, '.git')):
        return path

    path = os.path.join(os.path.dirname(REPO_ROOT), 'ouroboros')
    if not os.path.isdir(os.path.join(path, '.git')):
        return path


def native_modules(target):
    """Find stdlib modules already implemented in java."""
    modules = []
    for folder in ['common', target]:
        basedir = os.path.join(REPO_ROOT, 'python', folder, 'python')
        for name in os.listdir(basedir):
            module_name, ext = os.path.splitext(name)
            if (ext == '.java' or
                ext == '' and os.path.isdir(os.path.join(basedir, name))):
                modules.append(module_name)

    return set(modules)


def module_list(target, fast):
    """Find the list of modules to be compiled"""
    modules = []
    native = native_modules(target)
    basedir = os.path.join(ouroboros_repo_folder(), 'ouroboros')
    for name in os.listdir(basedir):
        module_name, ext = os.path.splitext(name)
        if (ext == '.py' or
            ext == '' and os.path.isdir(os.path.join(basedir, name))):
            if (module_name not in IGNORE_MODULES
                and module_name not in native):
                if not (fast and module_name in KNOWN_PROBLEM_MODULES):
                    modules.append(module_name)

    return set(modules)

def update_repo():
    """Update the ouroboros repository inside the voc folder."""
    repo_folder = ouroboros_repo_folder()
    if repo_folder is None  :
        print('Cloning Ouroboros...')
        subprocess.Popen(
            ['git', 'clone', 'https://github.com/pybee/ouroboros.git'],
            cwd=os.path.dirname(REPO_ROOT)
        ).wait()
    else:
        print('Updating Ouroboros...')
        subprocess.Popen(
            ['git', 'pull', 'origin', 'master'],
            cwd=repo_folder
        ).wait()


def compile_module(args):
    """
    Compile the given (name, target, passed, failed) with voc.

    Save results in the queues passed by pool.map.
    """
    name, target, passed, failed = args

    module_path = os.path.join(ouroboros_repo_folder(), 'ouroboros', name)
    output_path = os.path.join(REPO_ROOT, 'build', target, 'python', name)

    if os.path.isdir(module_path):
        output_path = os.path.join(output_path, '__init__.class')
    else:
        module_path += '.py'
        output_path += '.class'

    try:
        last_output_timestamp = os.path.getmtime(output_path)
        last_input_timestamp = os.path.getmtime(module_path)

        if last_input_timestamp <= last_output_timestamp:
            # The file hasn't been modified; don't rebuild.
            return

    except FileNotFoundError:
        pass

    p = subprocess.Popen(
        [
            'voc',
            '-v',
            '-o', os.path.join(REPO_ROOT, 'build', target),
            '-p', os.path.join(ouroboros_repo_folder(), 'ouroboros'),
            module_path,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=REPO_ROOT
    )
    stdout, stderr = p.communicate()
    stdout = stdout.decode()
    stderr = stderr.decode()

    # print('=====' * 10)
    # print("OUT", stdout)
    # print('-----' * 10)
    # print("ERR", stderr)
    # print('-----' * 10)
    if stderr:
        if name in KNOWN_PROBLEM_MODULES:
            print('x', end='', flush=True)
        else:
            print('F', end='', flush=True)
            failed.append(name)
    else:
        print('.', end='', flush=True)
        passed.append(name)

def compile(modules, target):
    """Run main compilation process on all modules found."""
    pool = multiprocessing.Pool(multiprocessing.cpu_count())

    m = multiprocessing.Manager()
    passed = m.list()
    failed = m.list()

    args = [
        (name, target, passed, failed)
        for name in modules
    ]

    pool.map(compile_module, args)
    pool.close()
    pool.join()

    return passed, failed


def main(target, fast):
    """Run main compilation process."""
    start = datetime.now()
    update_repo()

    # List valid files to try to compile
    modules = module_list(target, fast)
    print('Compiling %s python modules...' % len(modules))

    # Run compilation process
    passed, failed = compile(modules, target)

    print()
    print("Built %s modules" % len(passed))
    if failed:
        print("%s modules failed to build" % len(failed))
        for name in sorted(failed):
            print(name)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Compile the Python standard library.'
    )
    parser.add_argument(
        'target',
        help='The platform target (java/android)'
    )
    parser.add_argument(
        '--fast',
        action='store_true',
        help='Fast compile; ignore any known-bad modules'
    )

    args = parser.parse_args()
    main(target=args.target, fast=args.fast)
