
import setuptools
import sys

from sipiiiii.app.version import version
from sipiiiii.app.new_app import init_framework

with open("README.md", "r") as fh:
    long_description = fh.read()

status, msg = init_framework()
if not status:
    print(msg)
    sys.exit(1)

setuptools.setup(
    # 包的分发名称，使用字母、数字、_、-
    name="sipiiiii",
    # 版本号, 版本号规范：https://www.python.org/dev/peps/pep-0440/
    version=version,
    # 作者名
    author="sipiiiii@admin",
    # 作者邮箱
    author_email="j0hn.wahahaha@gmail.com",
    # 包的简介描述
    description="depl sipiiiii, App Development Framework",
    # 包的详细介绍(一般通过加载README.md)
    long_description=long_description,
    # 和上条命令配合使用，声明加载的是markdown文件
    long_description_content_type="text/markdown",
    # 项目开源地址
    url="http://www.depl.run/",
    # 如果项目由多个文件组成，我们可以使用find_packages()自动发现所有包和子包，而不是手动列出每个包，在这种情况下，包列表将是example_pkg
    packages=setuptools.find_packages(),
    install_requires=[
        'httpx',
        'prettytable',
        'jinja2',
        'requests',
        'yaml',
        'shutil',
        'requests_toolbelt',
        'xmltodict',
        'validators',
        'pathlib',
        'jsonpath'
    ],
    entry_points={
        'console_scripts': [
            'sipiiiii = sipiiiii.main:main'
        ]
    },
    # 关于包的其他元数据(metadata)
    classifiers=[
        # 该软件包仅与Python3兼容
        "Programming Language :: Python :: 3",
        # 根据MIT许可证开源
        "License :: OSI Approved :: MIT License",
        # 与操作系统无关
        "Operating System :: OS Independent",
    ],
)
