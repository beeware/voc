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

    If the repo doesn't exist, return None. It should get cloned by
    update_repo.
    """

    for dirpath in (
        os.path.dirname(os.path.dirname(REPO_ROOT)),
        os.path.dirname(REPO_ROOT),
    ):
        path = os.path.join(dirpath, 'ouroboros')
        if os.path.isdir(os.path.join(path, '.git')):
            return path
    else:
        return None


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


def write_file(path, content):
    dir_path = os.path.dirname(path)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
    with open(path, 'w') as f:
        f.write(content)


def write_result_file(output_path, extension, content):
    result_path = os.path.splitext(output_path)[0] + extension
    write_file(result_path, content)


def run_cmd(cmd):
    pipe = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=REPO_ROOT
    )
    stdout, stderr = pipe.communicate()
    return pipe.returncode, stdout, stderr


def run_smoke_test(mod_name, output_path):
    test_path = os.path.join(REPO_ROOT, 'stdlib_tests', 'test_%s.py' % mod_name)
    if not os.path.exists(test_path):
        write_result_file(output_path, '.test.notest', '')
        return
    test_dir = os.path.join(REPO_ROOT, 'build', 'stdlib_tests')
    _, stdout, stderr = run_cmd([
        'voc',
        '-v',
        '-o', test_dir,
        '-p', 'stdlib_tests',
        test_path,
    ])
    if stderr:
        write_result_file(output_path, '.test.stderr', stderr)
    else:
        _, py_stdout, py_stderr = run_cmd(['python', test_path])
        # XXX: fix this for multiple-levels:
        test_mod_name = 'python.' + os.path.splitext(os.path.basename(test_path))[0]
        _, voc_stdout, voc_stderr = run_cmd([
            'java',
            '-cp', './dist/python-java-support.jar:' + test_dir,
            test_mod_name
        ])
        if py_stdout == voc_stdout and py_stderr == voc_stderr:
            write_result_file(output_path, '.test.works', stdout.decode('utf-8'))
        else:
            write_result_file(output_path, '.test.fails.voc_stdout', voc_stdout.decode('utf-8'))
            write_result_file(output_path, '.test.fails.voc_stderr', voc_stderr.decode('utf-8'))
            write_result_file(output_path, '.test.fails.py_stdout', py_stdout.decode('utf-8'))
            write_result_file(output_path, '.test.fails.py_stderr', py_stderr.decode('utf-8'))


def _compile_module(args):
    """
    Compile the given (name, target, passed, failed) with voc.

    Save results in the queues passed by pool.map.
    """
    name, target, passed, failed, fast = args

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

        if fast and last_input_timestamp <= last_output_timestamp:
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
        if not fast:
            write_result_file(output_path, '.compile.stderr', stderr)
    else:
        print('.', end='', flush=True)
        passed.append(name)
        if not fast:
            run_smoke_test(name, output_path)

def compile_modules(modules, target, fast):
    """Run main compilation process on all modules found."""
    pool = multiprocessing.Pool(multiprocessing.cpu_count())

    m = multiprocessing.Manager()
    passed = m.list()
    failed = m.list()

    args = [
        (name, target, passed, failed, fast)
        for name in modules
    ]

    pool.map(_compile_module, args)
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
    passed, failed = compile_modules(modules, target, fast)

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
        help="Fast compile; ignore any known-bad modules and skip already compiled files"
    )

    args = parser.parse_args()
    main(target=args.target, fast=args.fast)
