#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Build report with stdlib modules status
"""

from __future__ import print_function, absolute_import, division
import glob
import jinja2

# ugly hack to avoid duplicating code:
import sys, os
sys.path.append(os.path.dirname(__file__))
from compile_stdlib import module_list


TEMPLATE = jinja2.Template(r"""
<html>
<head>
<title>VOC stdlib modules status</title>
<style>
body {
    font: 1.2em "Open Sans", sans-serif;
}
.td {
    padding: 2px 0;
    border: 1px solid #444;
}
.notest {
    background-color: #aaa;
}
.nocompile {
    color: #ddaaaa;
    background-color: #aa1111;
}
.failed {
    background-color: #773333;
    color: #eeaaaa;
}
.ok {
    color: #aaddaa;
    background-color: #11aa11;
}
pre {
    display: none;
}
</style>
</head>
<body>
<table>
<tr>
    <th>Module name</th>
    <th>Compile</th>
    <th>Test</th>
</tr>
{% for info in modules_info %}
<tr>
    <td>{{ info.module }}</td>
    <td class={{ info.compile_status|lower }}>
    {{ info.compile_status }}
    <pre>{{ info.compile_errors }}</pre>
    </td>
    <td class={{ info.test_status|lower }}>
    {{ info.test_status }}
    <pre>{{ info.test_errors }}</pre>
    </td>
</tr>
{% endfor %}
</table>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script>
$(function(){
    $('td pre').each(function() {
        var pre = $(this);
        var pre_text = pre.text();
        if (pre_text.length > 1) {
            var btn = $('<button>expand</button>');
            btn.click(function(){
                pre.toggle();
            })
            btn.insertBefore(pre);
        } else {
            console.log('pre', pre_text);
        }
    });
});
</script>
</body>
</html>
""")


def find_result(mod_name):
    result_files = glob.glob(os.path.join('build', 'java', 'python', mod_name + '.*'))
    result_files = [f for f in result_files
                    if not f.endswith('.class') and not f.endswith(mod_name)]
    if not result_files:
        result_files = glob.glob(os.path.join('build', 'java', 'python', mod_name,
                                              '__init__.*'))
        result_files = [f for f in result_files if not f.endswith('.class')]
    if result_files:
        return sorted(result_files)


def read_file(fpath):
    with open(fpath) as f:
        return f.read()


def build_info(mod_name, result_files):
    result_files = find_result(mod_name)
    compile_status = 'N/A'
    test_status = 'N/A'
    compile_errors = ''
    test_errors = ''

    def build_test_error_mesg():
        def find_file_with_ext(ext):
            files = [f for f in result_files if f.endswith(ext)]
            if files:
                return files[0]

        py_stderr = read_file(find_file_with_ext('.test-fails-py_stderr'))
        py_stdout = read_file(find_file_with_ext('.test-fails-py_stdout'))
        voc_stderr = read_file(find_file_with_ext('.test-fails-voc_stderr'))
        voc_stdout = read_file(find_file_with_ext('.test-fails-voc_stdout'))

        out = ''
        marker = '-' * 20
        if py_stdout or voc_stdout:
            out += (
                'Expected output was:\n{marker}\n{py_stdout}{marker}\n\n'
                'Received output was:\n{marker}\n{voc_stdout}{marker}\n\n'
                .format(marker=marker, py_stdout=py_stdout, voc_stdout=voc_stdout)
            )
        if py_stderr or voc_stderr:
            out += (
                'CPython stderr was:\n{marker}\n{py_stderr}{marker}\n\n'
                'Java/VOC stderr was:\n{marker}\n{voc_stderr}{marker}\n\n'
                .format(marker=marker, py_stderr=py_stderr, voc_stderr=voc_stderr)
            )
        return out

    if result_files:
        if result_files[0].endswith('.compile-stderr'):
            compile_status = 'FAILED'
            compile_errors = read_file(result_files[0])
        else:
            compile_status = 'OK'

        if result_files[0].endswith('.test-works'):
            test_status = 'OK'
        elif result_files[0].endswith('.test-notest'):
            test_status = 'NOTEST'
        elif result_files[0].endswith('.test-compile-stderr'):
            test_status = 'NOCOMPILE'
            test_errors = read_file(result_files[0])
        elif '.test-fails' in result_files[0]:
            test_status = 'FAILED'
            test_errors = build_test_error_mesg()

    return dict(
        module=mod_name,
        result_files=result_files,
        compile_status=compile_status,
        compile_errors=compile_errors,
        test_status=test_status,
        test_errors=test_errors
    )


def run(args):
    modules_info = [
        build_info(mod, find_result(mod))
        for mod in
        sorted(module_list('java', False))
    ]
    if args.html:
        html = TEMPLATE.render(modules_info=modules_info)
        with open('report.html', 'w') as f:
            f.write(html)
    else:
        print('{:17}  {:10}  {:10}'.format('Module', 'Compile', 'Test'))
        for info in modules_info:
            print('{module:17}  {compile_status:10}  {test_status:10}'.format(**info))


if '__main__' == __name__:
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--html', action='store_true')

    args = parser.parse_args()
    run(args)
