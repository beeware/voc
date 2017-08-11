# -*- coding: utf-8 -*-
"""Check modules from Ouroboros that compile with voc."""

# Standard library imports
from datetime import datetime
from subprocess import Popen, PIPE
import multiprocessing
import os


REPO_ROOT = os.path.dirname(os.path.realpath(__file__))
MODULES_NOT_COMPILING = [
    'ouroboros/__init__.py',
    'ouroboros/_collections_abc.py',
    'ouroboros/_markupbase.py',
    'ouroboros/_pyio.py',
    'ouroboros/_sitebuiltins.py',
    'ouroboros/_strptime.py',
    'ouroboros/_threading_local.py',
    'ouroboros/_weakrefset.py',
    'ouroboros/abc.py',
    'ouroboros/aifc.py',
    'ouroboros/argparse.py',
    'ouroboros/asyncio/base_events.py',
    'ouroboros/asyncio/base_subprocess.py',
    'ouroboros/asyncio/coroutines.py',
    'ouroboros/asyncio/events.py',
    'ouroboros/asyncio/futures.py',
    'ouroboros/asyncio/locks.py',
    'ouroboros/asyncio/proactor_events.py',
    'ouroboros/asyncio/queues.py',
    'ouroboros/asyncio/selector_events.py',
    'ouroboros/asyncio/sslproto.py',
    'ouroboros/asyncio/streams.py',
    'ouroboros/asyncio/subprocess.py',
    'ouroboros/asyncio/tasks.py',
    'ouroboros/asyncio/unix_events.py',
    'ouroboros/asyncio/windows_events.py',
    'ouroboros/base64.py',
    'ouroboros/binhex.py',
    'ouroboros/bz2.py',
    'ouroboros/chunk.py',
    'ouroboros/codecs.py',
    'ouroboros/collections/__init__.py',
    'ouroboros/compileall.py',
    'ouroboros/concurrent/futures/_base.py',
    'ouroboros/concurrent/futures/process.py',
    'ouroboros/contextlib.py',
    'ouroboros/ctypes/_endian.py',
    'ouroboros/curses/textpad.py',
    'ouroboros/datetime.py',
    'ouroboros/dbm/__init__.py',
    'ouroboros/decimal.py',
    'ouroboros/difflib.py',
    'ouroboros/distutils/ccompiler.py',
    'ouroboros/distutils/command/build_py.py',
    'ouroboros/distutils/command/register.py',
    'ouroboros/distutils/dist.py',
    'ouroboros/distutils/fancy_getopt.py',
    'ouroboros/doctest.py',
    'ouroboros/email/_encoded_words.py',
    'ouroboros/email/_header_value_parser.py',
    'ouroboros/email/_policybase.py',
    'ouroboros/email/charset.py',
    'ouroboros/email/contentmanager.py',
    'ouroboros/email/header.py',
    'ouroboros/email/headerregistry.py',
    'ouroboros/email/iterators.py',
    'ouroboros/email/message.py',
    'ouroboros/email/mime/nonmultipart.py',
    'ouroboros/encodings/uu_codec.py',
    'ouroboros/enum.py',
    'ouroboros/filecmp.py',
    'ouroboros/ftplib.py',
    'ouroboros/functools.py',
    'ouroboros/getpass.py',
    'ouroboros/gettext.py',
    'ouroboros/glob.py',
    'ouroboros/heapq.py',
    'ouroboros/http/cookiejar.py',
    'ouroboros/http/server.py',
    'ouroboros/idlelib/EditorWindow.py',
    'ouroboros/idlelib/IOBinding.py',
    'ouroboros/idlelib/MultiCall.py',
    'ouroboros/idlelib/Percolator.py',
    'ouroboros/idlelib/PyParse.py',
    'ouroboros/idlelib/PyShell.py',
    'ouroboros/idlelib/ReplaceDialog.py',
    'ouroboros/idlelib/ScriptBinding.py',
    'ouroboros/idlelib/SearchEngine.py',
    'ouroboros/idlelib/WidgetRedirector.py',
    'ouroboros/idlelib/idle_test/htest.py',
    'ouroboros/idlelib/idle_test/mock_idle.py',
    'ouroboros/idlelib/macosxSupport.py',
    'ouroboros/idlelib/rpc.py',
    'ouroboros/idlelib/run.py',
    'ouroboros/idlelib/tabbedpages.py',
    'ouroboros/imaplib.py',
    'ouroboros/importlib/abc.py',
    'ouroboros/importlib/util.py',
    'ouroboros/inspect.py',
    'ouroboros/io.py',
    'ouroboros/ipaddress.py',
    'ouroboros/itertools.py',
    'ouroboros/json/encoder.py',
    'ouroboros/lib2to3/btm_utils.py',
    'ouroboros/lib2to3/main.py',
    'ouroboros/lib2to3/patcomp.py',
    'ouroboros/lib2to3/pgen2/driver.py',
    'ouroboros/lib2to3/pytree.py',
    'ouroboros/lib2to3/refactor.py',
    'ouroboros/logging/config.py',
    'ouroboros/logging/handlers.py',
    'ouroboros/lzma.py',
    'ouroboros/macpath.py',
    'ouroboros/mailbox.py',
    'ouroboros/mimetypes.py',
    'ouroboros/modulefinder.py',
    'ouroboros/msilib/schema.py',
    'ouroboros/multiprocessing/connection.py',
    'ouroboros/multiprocessing/pool.py',
    'ouroboros/netrc.py',
    'ouroboros/numbers.py',
    'ouroboros/operator.py',
    'ouroboros/optparse.py',
    'ouroboros/os.py',
    'ouroboros/pathlib.py',
    'ouroboros/pickle.py',
    'ouroboros/pkgutil.py',
    'ouroboros/plat-linux/IN.py',
    'ouroboros/plat-sunos5/IN.py',
    'ouroboros/plat-sunos5/STROPTS.py',
    'ouroboros/platform.py',
    'ouroboros/plistlib.py',
    'ouroboros/profile.py',
    'ouroboros/pstats.py',
    'ouroboros/pty.py',
    'ouroboros/pydoc.py',
    'ouroboros/quopri.py',
    'ouroboros/selectors.py',
    'ouroboros/shutil.py',
    'ouroboros/smtpd.py',
    'ouroboros/smtplib.py',
    'ouroboros/sndhdr.py',
    'ouroboros/socketserver.py',
    'ouroboros/sre_compile.py',
    'ouroboros/string.py',
    'ouroboros/tabnanny.py',
    'ouroboros/tarfile.py',
    'ouroboros/timeit.py',
    'ouroboros/tkinter/__init__.py',
    'ouroboros/tkinter/font.py',
    'ouroboros/tkinter/scrolledtext.py',
    'ouroboros/tkinter/ttk.py',
    'ouroboros/trace.py',
    'ouroboros/traceback.py',
    'ouroboros/turtle.py',
    'ouroboros/turtledemo/__main__.py',
    'ouroboros/unittest/case.py',
    'ouroboros/unittest/loader.py',
    'ouroboros/unittest/mock.py',
    'ouroboros/urllib/parse.py',
    'ouroboros/urllib/request.py',
    'ouroboros/urllib/robotparser.py',
    'ouroboros/uu.py',
    'ouroboros/uuid.py',
    'ouroboros/weakref.py',
    'ouroboros/webbrowser.py',
    'ouroboros/wsgiref/handlers.py',
    'ouroboros/xdrlib.py',
    'ouroboros/xml/dom/minicompat.py',
    'ouroboros/xml/dom/minidom.py',
    'ouroboros/xml/dom/xmlbuilder.py',
    'ouroboros/xml/etree/ElementPath.py',
    'ouroboros/xml/etree/ElementTree.py',
    'ouroboros/xml/sax/expatreader.py',
    'ouroboros/xmlrpc/client.py',
    'ouroboros/xmlrpc/server.py',
    'ouroboros/zipfile.py',
]

# This modules are not checked as Java native implementations are provided
MODULE_MANUAL_OVERRIDES = [
    # 'ouroboros/somefiletoignore1.py',
    # 'ouroboros/somefiletoignore2.py',
]


def ouroboros_repo_folder():
    """Return the folder where the ouroboros repo was cloned."""
    path = os.path.join(REPO_ROOT, 'ouroboros-repo')
    if not os.path.isdir(path):
        os.makedirs(path)
    return path


def ouroboros_module_folder():
    """Return the folder where the ouroboros module lives (inside the repo)."""
    return os.path.join(ouroboros_repo_folder(), 'ouroboros')


def ouroboros_compiled_folder(target='java'):
    """Location of the `voc` compiled `*.java` files."""
    return os.path.join(REPO_ROOT, 'build', target)


def module_overrides():
    """"""
    folder_overrides = os.path.join(REPO_ROOT, 'python', 'common', 'python')
    paths = []
    for folder, subfolders, files in os.walk(folder_overrides):
        for fname in files:
            if fname.endswith('.java'):
                module_path = os.path.join('ouroboros',
                                           fname.replace('.java', '.py'))
                module_init_path = os.path.join('ouroboros',
                                           fname.replace('.java', ''),
                                           '__init__.py')
                paths += [module_path, module_init_path]
    paths += MODULE_MANUAL_OVERRIDES
    return list(sorted(paths))


def clone_update_repo():
    """Clone or update the ouroboros repository inside the voc folder."""
    print('\nUPDATING OUROBOROS CODE')
    print('=======================')
    url = 'https://github.com/pybee/ouroboros.git'

    repo_folder = ouroboros_repo_folder()
    if os.path.isdir(os.path.join(repo_folder, '.git')):
        print('Pulling from master on repo: {}\n'.format(url))
        args = ['git', 'pull', 'origin', 'master']
    else:
        print('Cloning repo: {}\n'.format(url))
        args = ['git', 'clone', url, repo_folder]

    p = Popen(args, stdout=PIPE, stderr=PIPE, cwd=repo_folder)
    stdout, stderr = p.communicate()
    stdout = stdout.decode()
    stderr = stderr.decode()
    print('Repo dir: {0}\n'.format(repo_folder))
    print(stdout)
    print(stderr)


def list_files():
    """
    List all valid python files within ouroboros.

    We currently exclude paths including '/test/' or '/tests/' and files
    with extensions different from `.py`.
    """
    overrides = module_overrides()
    paths = []
    repo_folder = ouroboros_repo_folder()
    for folder, subfolders, files in os.walk(ouroboros_module_folder()):
        for fname in files:
            if not fname.startswith('test_') and fname.endswith('.py'):
                path = os.path.join(folder, fname)
                normpath = path.replace(repo_folder , '')
                if (os.sep + 'test' + os.sep not in path and
                        os.sep + 'tests' + os.sep not in path and
                        normpath not in overrides):
                    paths.append(path)

    normal_paths = [p for p in paths if not p.endswith('__init__.py')]
    init_paths = [p for p in paths if p.endswith('__init__.py')]
    return normal_paths + init_paths


def compile_with_voc(args):
    """
    Compile the given (path, queue1, queue2) with voc.

    Save results in the queues passed by pool.map.
    """
    namespace = 'python'
    path, failed_queue, xpassed_queue, target = args
    folder = os.path.dirname(ouroboros_repo_folder())
    norm_path = path.replace(folder + os.sep, '')
    args = ['voc', '-v', path, '-o', ouroboros_compiled_folder(target=target),
            '--prefix', ouroboros_module_folder()]

    p = Popen(args, stdout=PIPE, stderr=PIPE, cwd=os.path.dirname(path))
    stdout, stderr = p.communicate()
    stdout = stdout.decode()
    stderr = stderr.decode()

    check = [i for i in MODULES_NOT_COMPILING if
             path.replace('\\', '/').endswith(i)]

    if stderr and not check:
        # Unexpected failure
        failed_queue.put((norm_path, stdout, stderr))
        print('FAILED: {}'.format(norm_path))
    elif not stderr and check:
        # Unexpected pass
        xpassed_queue.put((norm_path, stdout, stderr))
        print('FAILED: {}'.format(norm_path))
    elif not stderr and not check:
        module_path = norm_path.replace('ouroboros-repo' + os.sep + 'ouroboros', '')
        norm_compiled_path = (os.path.join(ouroboros_compiled_folder(target),
                                           namespace) + module_path)
        norm_compiled_path = norm_compiled_path.replace(REPO_ROOT + os.sep, '')
        norm_compiled_path = norm_compiled_path.replace('.py', '.class')
        print('PASSED: {0} -> {1}'.format(norm_path, norm_compiled_path))
    elif stderr and not not check:
        print('xfail:  {}'.format(norm_path))

    return stdout, stderr


def run_process(paths, target='java'):
    """Run main compilation process on all paths found."""
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    m = multiprocessing.Manager()
    xpassed_queue = m.Queue()
    failed_queue  = m.Queue()
    args = [(path, failed_queue, xpassed_queue, target) for path in paths]

    print('\nSTART VOC COMPILE TESTS')
    print('=======================')

    pool.map(compile_with_voc, args)
    pool.close()
    pool.join()

    xpassed_list = []
    while xpassed_queue.qsize() != 0:
        xpassed_list.append(xpassed_queue.get())

    failed_list = []
    while failed_queue.qsize() != 0:
        failed_list.append(failed_queue.get())

    if failed_list:
        print('\nUNEXPECTED FAILS')
        print('=================')

        for (path, stdout, stderr) in sorted(failed_list):
            print(path)
            print(stderr)
            print('\n')

    if xpassed_list:
        print('\nUNEXPECTED SUCCESS')
        print('=====================')
        for (path, stdout, stderr) in sorted(xpassed_list):
            print(path)

    return failed_list, xpassed_list


def main(target='java'):
    """"""
    start = datetime.now()
    clone_update_repo()
    paths = list_files()

    print('\nFound: {} python files\n'.format(len(paths)))

    failed_list , xpassed_list = run_process(paths)
    n_err = len(failed_list) + len(xpassed_list)
    n_compiled = len(paths) - len(MODULES_NOT_COMPILING)
    percent = round((n_compiled*1.0 / len(paths))*100, 1)

    print('\nProcess duration: {}\n'.format(datetime.now() - start))

    if not failed_list and not xpassed_list:
        print('\nTests completed. {0}/{1} files compiled successfully ({2}%)\n'
              ''.format(n_compiled, len(paths), percent))
    else:
        plural = 's' if n_err != 1 else ''
        raise SystemExit('\n\n{0} failure{1} encountered!!!\n\n'
                         ''.format(n_err, plural))


if __name__ == '__main__':
    main()
