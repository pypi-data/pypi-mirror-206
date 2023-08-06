# encoding:utf-8
from setuptools import find_packages
from setuptools import setup

from pkg.version import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lesscode_tool",
    version=__version__,
    description="低代码生成工具",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="navysummer",
    author_email="navysummer@yeah.net",
    packages=find_packages(),
    url="https://gitee.com/navysummer/lesscodeTool",
    platforms="any",
    include_package_data=True,
    # include_dirs=["pkg/lesscode"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # "SQLAlchemy~=2.0.12",
        "docopt~=0.6.2"],
    entry_points={"console_scripts": ['lesscodeTool = pkg.lesscode_tool:main']}
)
