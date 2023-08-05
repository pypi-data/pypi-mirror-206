#!/usr/bin/env python3
"""
Example of program which uses [options] shortcut in pattern.

Usage:
  lesscode_tool (new -d dir [-p project]|sqlacodegen -u url [-t table][-f file])

Options:
  -h, --help                查看帮助
  -v, --version            展示版本号
  -d, --dir dir            项目目录
  -u, --url url            数据库连接
  -f, --file file          表结构类输出文件
  -p, --project project    项目模板名
  -t, --table table        表名
"""
from docopt import docopt

from tool.new import create_lesscode_project
from tool.sqlacodegen import sqlacodegen
from version import __version__


def main():
    arguments = docopt(__doc__, version=__version__)
    new_command_flag = arguments.get("new")
    sqlacodegen_command_flag = arguments.get("sqlacodegen")
    if new_command_flag:
        project = arguments.get("--project")
        project_dir = arguments.get("--dir")
        if project is None:
            project = "lesscode-py"
        if project == "lesscode-py":
            create_lesscode_project(project_dir)
    if sqlacodegen_command_flag:
        url = arguments.get("--url")
        file = arguments.get("--file")
        table = arguments.get("--table")
        sqlacodegen(url, table, file)


if __name__ == '__main__':
    main()
