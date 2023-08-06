import os
import yaml
import json
import sys

from shutil import rmtree
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from .utils.config import fix
from .utils.Tools import get_current_path, read_app_yaml


class ExecAppClass(object):
    def __init__(self, cwd, file_path, code_type):
        self.file_path = file_path
        self.cwd = cwd
        self. code_type = code_type

    def run_python_app(self):
        port = input("输入端口:")
        try:
            port = int(port)
        except ValueError:
            return False, "错误: 输入的端口不是整型."

        sys.path.append(self.cwd)
        try:
            from app import app
        except Exception as e:
            return False, f"错误: sipiiii项目路径. {e}"

        app.run(debug=True, port=port)
        return True, "服务器运行正常过，目前服务器已停止..."


class CreateAppTypeClass(object):
    def __init__(self, app_name, app_yaml, app_dir):
        self.app_name = app_name
        self.app_yaml = app_yaml
        self.app_dir = app_dir

    def __create_app_path(self):
        if os.path.exists(self.app_name):
            print(f"{self.app_name} 路径已存在，无法在不删除的情况下创建新项目.")
            is_rm = input("是否需要删除, 不删除则会退出程序(y/n)?")
            is_rm = is_rm.lower()
            if is_rm == "y":
                rmtree(self.app_name)
            elif is_rm == "n":
                return True, "退出"

        path = Path(f"{self.app_name}")
        path.mkdir(parents=True, exist_ok=True)

    def __create_code(self, code_type, app_type):
        status, msg = create_framework_code(
            self.app_dir, self.app_name, self.app_yaml, code_type, app_type)
        if not status:
            return False, "创建框架代码出错, {msg}"
        return True, msg

    def __create_python_requirements(self, app_type):
        requirements = input("输入导入的库(多个库用逗号分隔):")
        if requirements is None or requirements == "":
            requirements = ""

        if requirements.find(",") > -1:
            requirements = requirements.split(",")
        else:
            if requirements == "":
                requirements = []
            else:
                requirements = [requirements]

        if app_type == "fastapi":
            requirements.append('fastapi')
        if app_type == "flask":
            requirements.append('flask')
        if app_type == "openai":
            requirements.append('quart')
            requirements.append('quart_cors')

        status, requirements_file_path = create_requirements(
            self.app_name, requirements)
        if not status:
            return False, requirements_file_path

    def create_flask_app(self, code_type):
        self.__create_app_path()

        if code_type == "python":
            self.__create_python_requirements("flask")

        status, openapi_file_path = create_app_yaml(
            self.app_name, self.app_yaml, "flask")
        if not status:
            return False, openapi_file_path

        ststus, msg = self.__create_code(code_type, "flask")
        if not ststus:
            return False, msg

        return True, f"创建flask框架代码成功, 项目目录: ./{self.app_name}"

    def create_fastapi_app(self, code_type):
        self.__create_app_path()

        if code_type == "python":
            self.__create_python_requirements("fastapi")

        status, openapi_file_path = create_app_yaml(
            self.app_name, self.app_yaml, "fastapi")
        if not status:
            return False, openapi_file_path

        ststus, msg = self.__create_code(code_type, "fastapi")
        if not ststus:
            return False, msg

        return True, f"创建fastapi框架代码成功, 项目目录: ./{self.app_name}"

    def create_openai_app(self, code_type):
        ai_plugin_json = {
            "schema_version": "",
            "name_for_human": "",
            "name_for_model": "",
            "description_for_human": "",
            "description_for_model": "",
            "auth": {
                "type": "none"
            },
            "api": {
                "type": "openapi",
                "url": "!HOSTNAME!/openapi.yaml",
                "is_user_authenticated": False
            },
            "logo_url": "!HOSTNAME!/logo.png",
            "contact_email": "support@example.com",
            "legal_info_url": "https://example.com/legal"
        }

        try:
            ai_plugin_json['schema_version'] = self.app_yaml.get(
                'info', {}).get('version')
            ai_plugin_json['name_for_human'] = self.app_yaml.get(
                'info', {}).get('title')
            ai_plugin_json['name_for_model'] = self.app_yaml.get(
                'info', {}).get('title')
            ai_plugin_json['description_for_human'] = self.app_yaml.get(
                'info', {}).get('description')
            ai_plugin_json['description_for_model'] = self.app_yaml.get(
                'info', {}).get('description')
        except Exception as e:
            return False, str(e)

        self.__create_app_path()

        if code_type == "python":
            self.__create_python_requirements("openai")

        status, openapi_file_path = create_app_yaml(
            self.app_name, self.app_yaml, "openai")
        if not status:
            return False, openapi_file_path

        status, plugin_json_file_path = create_app_config(
            self.app_name, ai_plugin_json, "openai")
        if not status:
            return False, plugin_json_file_path

        ststus, msg = self.__create_code(code_type, "openai")
        if not ststus:
            return False, msg

        return True, f"创建openai框架代码成功, 项目目录: ./{self.app_name}"


def get_app_name(app_name, is_yaml=False):
    if app_name is None:
        while True:
            app_yaml_file = ""
            try:
                app_yaml_file = input("请输入APP yaml文件:")
            except KeyboardInterrupt:
                print("\r\n")
                sys.exit(1)

            if app_yaml_file == "":
                continue
            status, app_name, openapi_yaml, aiapi_dir = yaml_app_info(
                app_yaml_file, None)
            if not status:
                return False, app_name, openapi_yaml, aiapi_dir

            return True, app_name, openapi_yaml, aiapi_dir

    elif app_name.find(".yaml") > -1:
        status, app_name, openapi_yaml, aiapi_dir = yaml_app_info(
            app_name, None)
        if not status:
            return False, app_name, openapi_yaml, aiapi_dir
        return True, app_name, openapi_yaml, aiapi_dir
    else:
        if is_yaml:
            return False, app_name, "", ""
        return True, app_name, "", ""


def get_app_code_type(file_path):
    _fix = ""
    try:
        _fix = os.path.splitext(file_path)[-1].split(".")[-1]
    except Exception as e:
        return False, f"错误: {e}"

    if _fix not in fix.values():
        return False, f"{_fix} 不存在于 {list(fix.keys())}"

    new_fix = {v: k for k, v in fix.items()}
    return True, new_fix[_fix]


def yaml_app_info(yaml_file, app_type):
    openapi_yaml = None
    aiapi_dir = get_current_path()
    if app_type != "openai":
        app_type = "other"
    if yaml_file is None:
        openapi_yaml = read_app_yaml(aiapi_dir, app_type)
    else:
        openapi_yaml = read_app_yaml(yaml_file, app_type)
    if openapi_yaml == "":
        return False, "没找到yaml文件.", None, None
    app_name = ""
    try:
        app_name = openapi_yaml['info']['title']
    except Exception as e:
        return False, str(e), None, None

    if app_name == "":
        return False, "yaml中没有找到 yaml[info][title]", None, None

    app_name = app_name.replace(" ", "")
    return True, app_name, openapi_yaml, aiapi_dir


def create_directory(directory_name):
    current_path = get_current_path()
    new_directory_path = os.path.join(current_path, directory_name)

    if not os.path.exists(new_directory_path):
        os.mkdir(new_directory_path)
        print(f"目录 '{directory_name}' 创建成功!")
        return True, new_directory_path
    else:
        print(f"目录 '{directory_name}' 已存在.")

    return False, ""


def create_requirements(directory_path, requirements):
    if type(requirements) != list:
        return False, "requirements 错误!"

    if not os.path.exists(directory_path):
        return False, f"{directory_path} 没有找到."

    requirements_file_path = os.path.join(directory_path, "requirements.txt")
    requirements_data = ""
    if len(requirements) > 0:
        requirements_data = "\n".join(requirements)

    with open(requirements_file_path, "w") as f:
        f.write(requirements_data)

    return True, requirements_file_path


def create_app_config(directory_path, plugin_json, app_type):
    if type(plugin_json) != dict:
        return False, "应用配置文件错误!"

    if not os.path.exists(directory_path):
        return False, f"{directory_path} 目录没有找到."

    # ai-plugin.json
    if app_type == "openai":
        app_type = "ai-plugin"
    else:
        app_type = "config"

    plugin_json_file_path = os.path.join(directory_path, f"{app_type}.json")
    # plugin_json_data = "\n".join(plugin_json_file_path)
    with open(plugin_json_file_path, encoding="utf-8", mode="w") as f:
        json.dump(plugin_json, f, indent=2)

    return True, plugin_json_file_path


def create_app_yaml(directory_path, openapi_yaml, app_type):
    if not os.path.exists(directory_path):
        return False, f"{directory_path} 目录不存在"

    # openapi_yaml_file_path = os.path.join(directory_path, f"{app_type}.yaml")
    # if app_type is None:
    openapi_yaml_file_path = os.path.join(directory_path, "aiapi.yaml")
    # openapi.yaml
    # openapi_yaml_file_path = os.path.join(directory_path, f"{app_type}.yaml")

    # plugin_json_data = "\n".join(plugin_json_file_path)
    with open(openapi_yaml_file_path, encoding="utf-8", mode="w") as f:
        yaml.dump(openapi_yaml, stream=f, allow_unicode=True)

    return True, openapi_yaml_file_path


def create_framework_code(directory_path, app_path, openapi_yaml, code_type, app_type):
    env = Environment(loader=FileSystemLoader(f"{directory_path}"))
    # template.j2
    # if app_type != "openai":
    #     app_type = "other"
    j2_file = f"{code_type}_{app_type}"
    try:
        template = env.get_template(f'{j2_file}.j2')
        output = template.render(paths=openapi_yaml['paths'])
    except Exception as e:
        return False, str(e)
    _fix = fix.get(code_type, None)
    if _fix is None:
        return False, "没有获取到应用类型"
    # Write the output to a Python file
    app_file = os.path.join(app_path, f"app.{_fix}")
    with open(app_file, 'w', encoding="utf-8") as f:
        f.write(output)

    return True, "创建框架代码成功"
