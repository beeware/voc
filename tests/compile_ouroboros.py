# -*- coding: utf-8 -*-
"""Check modules from Ouroboros that compile with voc."""

# Standard library imports
from datetime import datetime
from subprocess import Popen, PIPE
import multiprocessing
import os

HERE = os.path.dirname(os.path.realpath(__file__))
MODULES_WHITELIST = [
    'ouroboros/__builtins__.py',
    'ouroboros/__future__.py',
    'ouroboros/__phello__.foo.py',
    'ouroboros/_bootlocale.py',
    'ouroboros/_codecs.py',
    'ouroboros/_compat_pickle.py',
    'ouroboros/_csv.py',
    'ouroboros/_dummy_thread.py',
    'ouroboros/_osx_support.py',
    'ouroboros/_sre.py',
    'ouroboros/antigravity.py',
    'ouroboros/ast.py',
    'ouroboros/asynchat.py',
    'ouroboros/asyncio/compat.py',
    'ouroboros/asyncio/constants.py',
    'ouroboros/asyncio/log.py',
    'ouroboros/asyncio/protocols.py',
    'ouroboros/asyncio/transports.py',
    'ouroboros/asyncio/windows_utils.py',
    'ouroboros/asyncore.py',
    'ouroboros/bdb.py',
    'ouroboros/bisect.py',
    'ouroboros/cProfile.py',
    'ouroboros/calendar.py',
    'ouroboros/cgi.py',
    'ouroboros/cgitb.py',
    'ouroboros/cmath.py',
    'ouroboros/cmd.py',
    'ouroboros/code.py',
    'ouroboros/codeop.py',
    'ouroboros/collections/__main__.py',
    'ouroboros/collections/abc.py',
    'ouroboros/colorsys.py',
    'ouroboros/concurrent/futures/thread.py',
    'ouroboros/configparser.py',
    'ouroboros/copy.py',
    'ouroboros/copyreg.py',
    'ouroboros/crypt.py',
    'ouroboros/csv.py',
    'ouroboros/ctypes/macholib/dyld.py',
    'ouroboros/ctypes/macholib/dylib.py',
    'ouroboros/ctypes/macholib/framework.py',
    'ouroboros/ctypes/util.py',
    'ouroboros/ctypes/wintypes.py',
    'ouroboros/curses/ascii.py',
    'ouroboros/curses/has_key.py',
    'ouroboros/curses/panel.py',
    'ouroboros/dbm/dumb.py',
    'ouroboros/dbm/gnu.py',
    'ouroboros/dbm/ndbm.py',
    'ouroboros/dis.py',
    'ouroboros/distutils/archive_util.py',
    'ouroboros/distutils/bcppcompiler.py',
    'ouroboros/distutils/cmd.py',
    'ouroboros/distutils/command/bdist.py',
    'ouroboros/distutils/command/bdist_dumb.py',
    'ouroboros/distutils/command/bdist_msi.py',
    'ouroboros/distutils/command/bdist_rpm.py',
    'ouroboros/distutils/command/bdist_wininst.py',
    'ouroboros/distutils/command/build.py',
    'ouroboros/distutils/command/build_clib.py',
    'ouroboros/distutils/command/build_ext.py',
    'ouroboros/distutils/command/build_scripts.py',
    'ouroboros/distutils/command/check.py',
    'ouroboros/distutils/command/clean.py',
    'ouroboros/distutils/command/config.py',
    'ouroboros/distutils/command/install.py',
    'ouroboros/distutils/command/install_data.py',
    'ouroboros/distutils/command/install_egg_info.py',
    'ouroboros/distutils/command/install_headers.py',
    'ouroboros/distutils/command/install_lib.py',
    'ouroboros/distutils/command/install_scripts.py',
    'ouroboros/distutils/command/sdist.py',
    'ouroboros/distutils/command/upload.py',
    'ouroboros/distutils/config.py',
    'ouroboros/distutils/core.py',
    'ouroboros/distutils/cygwinccompiler.py',
    'ouroboros/distutils/debug.py',
    'ouroboros/distutils/dep_util.py',
    'ouroboros/distutils/dir_util.py',
    'ouroboros/distutils/errors.py',
    'ouroboros/distutils/extension.py',
    'ouroboros/distutils/file_util.py',
    'ouroboros/distutils/filelist.py',
    'ouroboros/distutils/log.py',
    'ouroboros/distutils/msvc9compiler.py',
    'ouroboros/distutils/msvccompiler.py',
    'ouroboros/distutils/spawn.py',
    'ouroboros/distutils/sysconfig.py',
    'ouroboros/distutils/text_file.py',
    'ouroboros/distutils/unixccompiler.py',
    'ouroboros/distutils/util.py',
    'ouroboros/distutils/version.py',
    'ouroboros/distutils/versionpredicate.py',
    'ouroboros/dummy_threading.py',
    'ouroboros/email/_parseaddr.py',
    'ouroboros/email/base64mime.py',
    'ouroboros/email/encoders.py',
    'ouroboros/email/errors.py',
    'ouroboros/email/feedparser.py',
    'ouroboros/email/generator.py',
    'ouroboros/email/mime/application.py',
    'ouroboros/email/mime/audio.py',
    'ouroboros/email/mime/base.py',
    'ouroboros/email/mime/image.py',
    'ouroboros/email/mime/message.py',
    'ouroboros/email/mime/multipart.py',
    'ouroboros/email/mime/text.py',
    'ouroboros/email/parser.py',
    'ouroboros/email/policy.py',
    'ouroboros/email/quoprimime.py',
    'ouroboros/email/utils.py',
    'ouroboros/encodings/aliases.py',
    'ouroboros/encodings/ascii.py',
    'ouroboros/encodings/base64_codec.py',
    'ouroboros/encodings/big5.py',
    'ouroboros/encodings/big5hkscs.py',
    'ouroboros/encodings/bz2_codec.py',
    'ouroboros/encodings/charmap.py',
    'ouroboros/encodings/cp037.py',
    'ouroboros/encodings/cp1006.py',
    'uroboros/encodings/cp1026.py',
    'ouroboros/encodings/cp1125.py',
    'ouroboros/encodings/cp1140.py',
    'ouroboros/encodings/cp1250.py',
    'ouroboros/encodings/cp1251.py',
    'ouroboros/encodings/cp1252.py',
    'ouroboros/encodings/cp1253.py',
    'ouroboros/encodings/cp1254.py',
    'ouroboros/encodings/cp1255.py',
    'ouroboros/encodings/cp1256.py',
    'ouroboros/encodings/cp1257.py',
    'ouroboros/encodings/cp1258.py',
    'ouroboros/encodings/cp273.py',
    'ouroboros/encodings/cp424.py',
    'ouroboros/encodings/cp437.py',
    'ouroboros/encodings/cp500.py',
    'ouroboros/encodings/cp65001.py',
    'ouroboros/encodings/cp720.py',
    'ouroboros/encodings/cp737.py',
    'ouroboros/encodings/cp775.py',
    'ouroboros/encodings/cp850.py',
    'ouroboros/encodings/cp852.py',
    'ouroboros/encodings/cp855.py',
    'ouroboros/encodings/cp856.py',
    'ouroboros/encodings/cp857.py',
    'ouroboros/encodings/cp858.py',
    'ouroboros/encodings/cp860.py',
    'ouroboros/encodings/cp861.py',
    'ouroboros/encodings/cp862.py',
    'ouroboros/encodings/cp863.py',
    'ouroboros/encodings/cp864.py',
    'ouroboros/encodings/cp865.py',
    'ouroboros/encodings/cp866.py',
    'ouroboros/encodings/cp869.py',
    'ouroboros/encodings/cp874.py',
    'ouroboros/encodings/cp875.py',
    'ouroboros/encodings/cp932.py',
    'ouroboros/encodings/cp949.py',
    'ouroboros/encodings/cp950.py',
    'ouroboros/encodings/euc_jis_2004.py',
    'ouroboros/encodings/euc_jisx0213.py',
    'ouroboros/encodings/euc_jp.py',
    'ouroboros/encodings/euc_kr.py',
    'ouroboros/encodings/gb18030.py',
    'ouroboros/encodings/gb2312.py',
    'ouroboros/encodings/gbk.py',
    'ouroboros/encodings/hex_codec.py',
    'ouroboros/encodings/hp_roman8.py',
    'ouroboros/encodings/hz.py',
    'ouroboros/encodings/idna.py',
    'ouroboros/encodings/iso2022_jp.py',
    'ouroboros/encodings/iso2022_jp_1.py',
    'ouroboros/encodings/iso2022_jp_2.py',
    'ouroboros/encodings/iso2022_jp_2004.py',
    'ouroboros/encodings/iso2022_jp_3.py',
    'ouroboros/encodings/iso2022_jp_ext.py',
    'ouroboros/encodings/iso2022_kr.py',
    'ouroboros/encodings/iso8859_1.py',
    'ouroboros/encodings/iso8859_10.py',
    'ouroboros/encodings/iso8859_11.py',
    'ouroboros/encodings/iso8859_13.py',
    'ouroboros/encodings/iso8859_14.py',
    'ouroboros/encodings/iso8859_15.py',
    'ouroboros/encodings/iso8859_16.py',
    'ouroboros/encodings/iso8859_2.py',
    'ouroboros/encodings/iso8859_3.py',
    'ouroboros/encodings/iso8859_4.py',
    'ouroboros/encodings/iso8859_5.py',
    'ouroboros/encodings/iso8859_6.py',
    'ouroboros/encodings/iso8859_7.py',
    'ouroboros/encodings/iso8859_8.py',
    'ouroboros/encodings/iso8859_9.py',
    'ouroboros/encodings/johab.py',
    'ouroboros/encodings/koi8_r.py',
    'ouroboros/encodings/koi8_u.py',
    'ouroboros/encodings/latin_1.py',
    'ouroboros/encodings/mac_arabic.py',
    'ouroboros/encodings/mac_centeuro.py',
    'ouroboros/encodings/mac_croatian.py',
    'ouroboros/encodings/mac_cyrillic.py',
    'ouroboros/encodings/mac_farsi.py',
    'ouroboros/encodings/mac_greek.py',
    'ouroboros/encodings/mac_iceland.py',
    'ouroboros/encodings/mac_latin2.py',
    'ouroboros/encodings/mac_roman.py',
    'ouroboros/encodings/mac_romanian.py',
    'ouroboros/encodings/mac_turkish.py',
    'ouroboros/encodings/mbcs.py',
    'ouroboros/encodings/palmos.py',
    'ouroboros/encodings/ptcp154.py',
    'ouroboros/encodings/punycode.py',
    'ouroboros/encodings/quopri_codec.py',
    'ouroboros/encodings/raw_unicode_escape.py',
    'ouroboros/encodings/rot_13.py',
    'ouroboros/encodings/shift_jis.py',
    'ouroboros/encodings/shift_jis_2004.py',
    'ouroboros/encodings/shift_jisx0213.py',
    'ouroboros/encodings/tis_620.py',
    'ouroboros/encodings/undefined.py',
    'ouroboros/encodings/unicode_escape.py',
    'ouroboros/encodings/unicode_internal.py',
    'ouroboros/encodings/utf_16.py',
    'ouroboros/encodings/utf_16_be.py',
    'ouroboros/encodings/utf_16_le.py',
    'ouroboros/encodings/utf_32.py',
    'ouroboros/encodings/utf_32_be.py',
    'ouroboros/encodings/utf_32_le.py',
    'ouroboros/encodings/utf_7.py',
    'ouroboros/encodings/utf_8.py',
    'ouroboros/encodings/utf_8_sig.py',
    'ouroboros/encodings/zlib_codec.py',
    'ouroboros/ensurepip/__main__.py',
    'ouroboros/ensurepip/_uninstall.py',
    'ouroboros/fileinput.py',
    'ouroboros/fnmatch.py',
    'ouroboros/formatter.py',
    'ouroboros/fractions.py',
    'ouroboros/genericpath.py',
    'ouroboros/getopt.py',
    'ouroboros/gzip.py',
    'ouroboros/hashlib.py',
    'ouroboros/hmac.py',
    'ouroboros/html/entities.py',
    'ouroboros/html/parser.py',
    'ouroboros/http/client.py',
    'ouroboros/http/cookies.py',
    'ouroboros/idlelib/AutoComplete.py',
    'ouroboros/idlelib/AutoCompleteWindow.py',
    'ouroboros/idlelib/AutoExpand.py',
    'ouroboros/idlelib/Bindings.py',
    'ouroboros/idlelib/CallTipWindow.py',
    'ouroboros/idlelib/CallTips.py',
    'ouroboros/idlelib/ClassBrowser.py',
    'ouroboros/idlelib/CodeContext.py',
    'ouroboros/idlelib/ColorDelegator.py',
    'ouroboros/idlelib/Debugger.py',
    'ouroboros/idlelib/Delegator.py',
    'ouroboros/idlelib/FileList.py',
    'ouroboros/idlelib/FormatParagraph.py',
    'ouroboros/idlelib/GrepDialog.py',
    'ouroboros/idlelib/HyperParser.py',
    'ouroboros/idlelib/IdleHistory.py',
    'ouroboros/idlelib/MultiStatusBar.py',
    'ouroboros/idlelib/ObjectBrowser.py',
    'ouroboros/idlelib/OutputWindow.py',
    'ouroboros/idlelib/ParenMatch.py',
    'ouroboros/idlelib/PathBrowser.py',
    'ouroboros/idlelib/RemoteDebugger.py',
    'ouroboros/idlelib/RemoteObjectBrowser.py',
    'ouroboros/idlelib/RstripExtension.py',
    'ouroboros/idlelib/ScrolledList.py',
    'ouroboros/idlelib/SearchDialog.py',
    'ouroboros/idlelib/SearchDialogBase.py',
    'ouroboros/idlelib/StackViewer.py',
    'ouroboros/idlelib/ToolTip.py',
    'ouroboros/idlelib/TreeWidget.py',
    'ouroboros/idlelib/UndoDelegator.py',
    'ouroboros/idlelib/WindowList.py',
    'ouroboros/idlelib/ZoomHeight.py',
    'ouroboros/idlelib/__main__.py',
    'ouroboros/idlelib/aboutDialog.py',
    'ouroboros/idlelib/configDialog.py',
    'ouroboros/idlelib/configHandler.py',
    'ouroboros/idlelib/configHelpSourceEdit.py',
    'ouroboros/idlelib/configSectionNameDialog.py',
    'ouroboros/idlelib/dynOptionMenuWidget.py',
    'ouroboros/idlelib/help.py',
    'ouroboros/idlelib/idle.py',
    'ouroboros/idlelib/idlever.py',
    'ouroboros/idlelib/keybindingDialog.py',
    'ouroboros/idlelib/testcode.py',
    'ouroboros/idlelib/textView.py',
    'ouroboros/idlelib/idle_test/mock_tk.py',
    'ouroboros/imghdr.py',
    'ouroboros/imp.py',
    'ouroboros/importlib/_bootstrap.py',
    'ouroboros/importlib/machinery.py',
    'ouroboros/json/decoder.py',
    'ouroboros/json/scanner.py',
    'ouroboros/json/tool.py',
    'ouroboros/keyword.py',
    'ouroboros/lib2to3/__main__.py',
    'ouroboros/lib2to3/btm_matcher.py',
    'ouroboros/lib2to3/fixer_base.py',
    'ouroboros/lib2to3/fixer_util.py',
    'ouroboros/lib2to3/fixes/fix_apply.py',
    'ouroboros/lib2to3/fixes/fix_asserts.py',
    'ouroboros/lib2to3/fixes/fix_basestring.py',
    'ouroboros/lib2to3/fixes/fix_buffer.py',
    'ouroboros/lib2to3/fixes/fix_callable.py',
    'ouroboros/lib2to3/fixes/fix_dict.py',
    'ouroboros/lib2to3/fixes/fix_except.py',
    'ouroboros/lib2to3/fixes/fix_exec.py',
    'ouroboros/lib2to3/fixes/fix_execfile.py',
    'ouroboros/lib2to3/fixes/fix_exitfunc.py',
    'ouroboros/lib2to3/fixes/fix_filter.py',
    'ouroboros/lib2to3/fixes/fix_funcattrs.py',
    'ouroboros/lib2to3/fixes/fix_future.py',
    'ouroboros/lib2to3/fixes/fix_getcwdu.py',
    'ouroboros/lib2to3/fixes/fix_has_key.py',
    'ouroboros/lib2to3/fixes/fix_idioms.py',
    'ouroboros/lib2to3/fixes/fix_import.py',
    'ouroboros/lib2to3/fixes/fix_imports.py',
    'ouroboros/lib2to3/fixes/fix_imports2.py',
    'ouroboros/lib2to3/fixes/fix_input.py',
    'ouroboros/lib2to3/fixes/fix_intern.py',
    'ouroboros/lib2to3/fixes/fix_isinstance.py',
    'ouroboros/lib2to3/fixes/fix_itertools.py',
    'ouroboros/lib2to3/fixes/fix_itertools_imports.py',
    'ouroboros/lib2to3/fixes/fix_long.py',
    'ouroboros/lib2to3/fixes/fix_map.py',
    'ouroboros/lib2to3/fixes/fix_metaclass.py',
    'ouroboros/lib2to3/fixes/fix_methodattrs.py',
    'ouroboros/lib2to3/fixes/fix_ne.py',
    'ouroboros/lib2to3/fixes/fix_next.py',
    'ouroboros/lib2to3/fixes/fix_nonzero.py',
    'ouroboros/lib2to3/fixes/fix_numliterals.py',
    'ouroboros/lib2to3/fixes/fix_operator.py',
    'ouroboros/lib2to3/fixes/fix_paren.py',
    'ouroboros/lib2to3/fixes/fix_print.py',
    'ouroboros/lib2to3/fixes/fix_raise.py',
    'ouroboros/lib2to3/fixes/fix_raw_input.py',
    'ouroboros/lib2to3/fixes/fix_reduce.py',
    'ouroboros/lib2to3/fixes/fix_reload.py',
    'ouroboros/lib2to3/fixes/fix_renames.py',
    'ouroboros/lib2to3/fixes/fix_repr.py',
    'ouroboros/lib2to3/fixes/fix_set_literal.py',
    'ouroboros/lib2to3/fixes/fix_standarderror.py',
    'ouroboros/lib2to3/fixes/fix_sys_exc.py',
    'ouroboros/lib2to3/fixes/fix_throw.py',
    'ouroboros/lib2to3/fixes/fix_tuple_params.py',
    'ouroboros/lib2to3/fixes/fix_types.py',
    'ouroboros/lib2to3/fixes/fix_unicode.py',
    'ouroboros/lib2to3/fixes/fix_urllib.py',
    'ouroboros/lib2to3/fixes/fix_ws_comma.py',
    'ouroboros/lib2to3/fixes/fix_xrange.py',
    'ouroboros/lib2to3/fixes/fix_xreadlines.py',
    'ouroboros/lib2to3/fixes/fix_zip.py',
    'ouroboros/lib2to3/pgen2/conv.py',
    'ouroboros/lib2to3/pgen2/grammar.py',
    'ouroboros/lib2to3/pgen2/literals.py',
    'ouroboros/lib2to3/pgen2/parse.py',
    'ouroboros/lib2to3/pgen2/pgen.py',
    'ouroboros/lib2to3/pgen2/token.py',
    'ouroboros/lib2to3/pgen2/tokenize.py',
    'ouroboros/lib2to3/pygram.py',
    'ouroboros/linecache.py',
    'ouroboros/locale.py',
    'ouroboros/macurl2path.py',
    'ouroboros/mailcap.py',
    'ouroboros/msilib/sequence.py',
    'ouroboros/msilib/text.py',
    'ouroboros/multiprocessing/context.py',
    'ouroboros/multiprocessing/dummy/connection.py',
    'ouroboros/multiprocessing/forkserver.py',
    'ouroboros/multiprocessing/heap.py',
    'ouroboros/multiprocessing/managers.py',
    'ouroboros/multiprocessing/popen_fork.py',
    'ouroboros/multiprocessing/popen_forkserver.py',
    'ouroboros/multiprocessing/popen_spawn_posix.py',
    'ouroboros/multiprocessing/popen_spawn_win32.py',
    'ouroboros/multiprocessing/process.py',
    'ouroboros/multiprocessing/queues.py',
    'ouroboros/multiprocessing/reduction.py',
    'ouroboros/multiprocessing/resource_sharer.py',
    'ouroboros/multiprocessing/semaphore_tracker.py',
    'ouroboros/multiprocessing/sharedctypes.py',
    'ouroboros/multiprocessing/spawn.py',
    'ouroboros/multiprocessing/synchronize.py',
    'ouroboros/multiprocessing/util.py',
    'ouroboros/nntplib.py',
    'ouroboros/ntpath.py',
    'ouroboros/nturl2path.py',
    'ouroboros/opcode.py',
    'ouroboros/pdb.py',
    'ouroboros/pickletools.py',
    'ouroboros/pipes.py',
    'ouroboros/plat-aix4/IN.py',
    'ouroboros/plat-darwin/IN.py',
    'ouroboros/plat-freebsd4/IN.py',
    'ouroboros/plat-freebsd5/IN.py',
    'ouroboros/plat-freebsd6/IN.py',
    'ouroboros/plat-freebsd7/IN.py',
    'ouroboros/plat-freebsd8/IN.py',
    'ouroboros/plat-linux/CDROM.py',
    'ouroboros/plat-linux/DLFCN.py',
    'ouroboros/plat-linux/TYPES.py',
    'ouroboros/plat-netbsd1/IN.py',
    'ouroboros/plat-sunos5/CDIO.py',
    'ouroboros/plat-sunos5/DLFCN.py',
    'ouroboros/plat-sunos5/TYPES.py',
    'ouroboros/plat-unixware7/IN.py',
    'ouroboros/plat-unixware7/STROPTS.py',
    'ouroboros/poplib.py',
    'ouroboros/posixpath.py',
    'ouroboros/pprint.py',
    'ouroboros/py_compile.py',
    'ouroboros/pyclbr.py',
    'ouroboros/pydoc_data/topics.py',
    'ouroboros/queue.py',
    'ouroboros/random.py',
    'ouroboros/re.py',
    'ouroboros/reprlib.py',
    'ouroboros/rlcompleter.py',
    'ouroboros/runpy.py',
    'ouroboros/sched.py',
    'ouroboros/shelve.py',
    'ouroboros/shlex.py',
    'ouroboros/site.py',
    'ouroboros/socket.py',
    'ouroboros/sqlite3/dbapi2.py',
    'ouroboros/sqlite3/dump.py',
    'ouroboros/sre_constants.py',
    'ouroboros/sre_parse.py',
    'ouroboros/ssl.py',
    'ouroboros/stat.py',
    'ouroboros/statistics.py',
    'ouroboros/stringprep.py',
    'ouroboros/struct.py',
    'ouroboros/subprocess.py',
    'ouroboros/sunau.py',
    'ouroboros/symbol.py',
    'ouroboros/symtable.py',
    'ouroboros/sysconfig.py',
    'ouroboros/telnetlib.py',
    'ouroboros/tempfile.py',
    'ouroboros/textwrap.py',
    'ouroboros/this.py',
    'ouroboros/threading.py',
    'ouroboros/tkinter/__main__.py',
    'ouroboros/tkinter/_fix.py',
    'ouroboros/tkinter/colorchooser.py',
    'ouroboros/tkinter/commondialog.py',
    'ouroboros/tkinter/constants.py',
    'ouroboros/tkinter/dialog.py',
    'ouroboros/tkinter/dnd.py',
    'ouroboros/tkinter/filedialog.py',
    'ouroboros/tkinter/messagebox.py',
    'ouroboros/tkinter/simpledialog.py',
    'ouroboros/tkinter/tix.py',
    'ouroboros/token.py',
    'ouroboros/tokenize.py',
    'ouroboros/tracemalloc.py',
    'ouroboros/tty.py',
    'ouroboros/turtledemo/bytedesign.py',
    'ouroboros/turtledemo/chaos.py',
    'ouroboros/turtledemo/clock.py',
    'ouroboros/turtledemo/colormixer.py',
    'ouroboros/turtledemo/forest.py',
    'ouroboros/turtledemo/fractalcurves.py',
    'ouroboros/turtledemo/lindenmayer.py',
    'ouroboros/turtledemo/minimal_hanoi.py',
    'ouroboros/turtledemo/nim.py',
    'ouroboros/turtledemo/paint.py',
    'ouroboros/turtledemo/peace.py',
    'ouroboros/turtledemo/penrose.py',
    'ouroboros/turtledemo/planet_and_moon.py',
    'ouroboros/turtledemo/round_dance.py',
    'ouroboros/turtledemo/tree.py',
    'ouroboros/turtledemo/two_canvases.py',
    'ouroboros/turtledemo/wikipedia.py',
    'ouroboros/turtledemo/yinyang.py',
    'ouroboros/types.py',
    'ouroboros/unittest/__main__.py',
    'ouroboros/unittest/main.py',
    'ouroboros/unittest/result.py',
    'ouroboros/unittest/runner.py',
    'ouroboros/unittest/signals.py',
    'ouroboros/unittest/suite.py',
    'ouroboros/unittest/test/__main__.py',
    'ouroboros/unittest/test/_test_warnings.py',
    'ouroboros/unittest/test/dummy.py',
    'ouroboros/unittest/test/support.py',
    'ouroboros/unittest/util.py',
    'ouroboros/urllib/error.py',
    'ouroboros/urllib/response.py',
    'ouroboros/venv/__main__.py',
    'ouroboros/warnings.py',
    'ouroboros/wave.py',
    'ouroboros/wsgiref/headers.py',
    'ouroboros/wsgiref/simple_server.py',
    'ouroboros/wsgiref/util.py',
    'ouroboros/wsgiref/validate.py',
    'ouroboros/xml/dom/NodeFilter.py',
    'ouroboros/xml/dom/domreg.py',
    'ouroboros/xml/dom/expatbuilder.py',
    'ouroboros/xml/dom/pulldom.py',
    'ouroboros/xml/etree/ElementInclude.py',
    'ouroboros/xml/etree/cElementTree.py',
    'ouroboros/xml/parsers/expat.py',
    'ouroboros/xml/sax/_exceptions.py',
    'ouroboros/xml/sax/handler.py',
    'ouroboros/xml/sax/saxutils.py',
    'ouroboros/xml/sax/xmlreader.py',
]


def ouroboros_folder():
    """Return the folder where the ouroboros repo was cloned."""
    os.chdir(HERE)
    os.chdir('../')
    return os.path.join(os.getcwd(), 'ouroboros', 'ouroboros')


def clone_update_repo():
    """Clone or update the ouroboros repository inside the voc folder."""
    print('\nUPDATING OUROBOROS CODE')
    print('=======================')
    url = 'https://github.com/pybee/ouroboros.git'

    repo_folder = ouroboros_folder()
    if os.path.isdir(repo_folder):
        print('Pulling from master on repo: {}\n'.format(url))
        args = ['git', 'pull', 'origin', 'master']
    else:
        print('Cloning repo: {}\n'.format(url))
        args = ['git', 'clone', url]

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
    count = 0
    paths = {}
    repo_folder = ouroboros_folder()
    for folder, subfolders, files in os.walk(repo_folder ):
        for fname in files:
            if not fname.startswith('test_') and fname.endswith('.py'):
                count += 1
                path = os.path.join(folder, fname)

                if '/test/' not in path and '/tests/' not in path:
                    paths[count] = path
    return paths


def compile_with_voc(args):
    """
    Compile the given (path, queue1, queue2) with voc.

    Save results in the queues passed by pool.map.
    """
    path, failed_queue, xpassed_queue = args
    folder = ouroboros_folder()
    norm_path = 'ouroboros' + path.replace(folder, '')
    args = ['voc', '-v', path]

    p = Popen(args, stdout=PIPE, stderr=PIPE, cwd=os.path.dirname(path))
    stdout, stderr = p.communicate()
    stdout = stdout.decode()
    stderr = stderr.decode()

    check = [i for i in MODULES_WHITELIST if path.endswith(i)]

    if stderr and check:
        # Unexpected failure
        failed_queue.put((norm_path, stdout, stderr))
        print('FAILED: {}'.format(norm_path))
    elif not stderr and not check:
        # Unexpected pass
        xpassed_queue.put((norm_path, stdout, stderr))
        print('FAILED: {}'.format(norm_path))
    elif not stderr and check:
        print('PASSED: {}'.format(norm_path))
    elif stderr and not check:
        print('xfail:  {}'.format(norm_path))
 
    return stdout, stderr


def run_process(paths):
    """Run main compilation process on all paths found."""
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    m = multiprocessing.Manager()
    xpassed_queue = m.Queue()
    failed_queue  = m.Queue()
    args = [(val, failed_queue, xpassed_queue) for key, val in paths.items()]

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


if __name__ == '__main__':
    start = datetime.now()
    clone_update_repo()
    paths = list_files()

    print('\nFound: {} files\n\n'.format(len(paths)))
    failed_list , xpassed_list = run_process(paths)
    n_err = len(failed_list) + len(xpassed_list)
    print('\nProcess duration: {}\n'.format(datetime.now() - start))
    if not failed_list and not xpassed_list:
        print("\nCompleted!\n\n")
    else:
        plural = 's' if n_err != 1 else ''
        raise SystemExit('\n\n{0} failure{1} encountered!!!\n\n'
                         ''.format(n_err, plural))
