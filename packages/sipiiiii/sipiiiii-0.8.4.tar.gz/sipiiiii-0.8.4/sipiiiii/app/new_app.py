import os
import multiprocessing
import prettytable as pt
import sys
import time
import yaml

from requests_toolbelt.multipart.encoder import MultipartEncoder
from pathlib import Path
from shutil import copyfile

from .core import CreateAppTypeClass, yaml_app_info, ExecAppClass, get_app_code_type, get_app_name

from .utils.PPI import ProgPercent
from .utils.ZipFileTool import zip_folder
from .utils.HttpSDK import https_get, https_post, https_file
from .utils.Tools import get_outside_ip, is_encomm_char, write_new_yaml, get_current_path
from .utils.config import app_all_types, server_host, fix


def process_update_outside_ip(domain, _token):
    while True:
        time.sleep(60 * 30)
        outside_ip = get_outside_ip()
        headers = {
            "Content-type": "application/json",
            "authorization": _token
        }
        url = f"{server_host}/system/openapi/app/stop"
        data = {
            "domain": domain,
            "ip": outside_ip
        }
        response = https_post(url, json_data=data, headers=headers)
        if not response.success:
            print(f"更新域名错误: {response.msg}")
        else:
            print(f"域名IP已更新: {domain} -> {outside_ip}")


def get_token():
    _token = ""
    home_dir_file = os.path.join(Path.home(), ".sipitoken")
    if os.path.exists(home_dir_file):
        with open(home_dir_file, 'r', encoding='utf8') as f:
            _token = f.read()
    if _token == "":
        return False, "请登录 sipiiiii."

    return True, _token


# 创建项目
def create_app_project():
    status, _token = get_token()
    if not status:
        return False, _token, ""

    print("""
    *** 应用名称必须英文
    *** 可以使用向导模式创建应用和使用模版创建应用
        """)

    while True:
        is_ai_create = input("是否使用向导创建应用(y/n):")
        is_ai_create = is_ai_create.lower()

        if is_ai_create == "y":
            app_name = input("请输入应用名:")
            if app_name == "":
                return False, "项目名不能为空", ""
            if not is_encomm_char(app_name):
                return False, "项目名必须是英文", ""

            app_desc = input("请输入应用说明:")
            app_version = input("请输入应用版本(不输入默认 v1.0):")
            if app_version == "":
                app_version = "v1.0"
            print(f"项目名: {app_name}, 项目说明: {app_desc}, 项目版本: {app_version}")
            status, yaml_data = create_yaml(
                app_name, app_version, app_desc)
            if not status:
                print(yaml_data)

            with open(f"{os.getcwd()}{os.sep}aiapi.yaml", "w", encoding="utf-8") as f:
                f.write(yaml_data)

            status, msg, app_name = create_app(
                f"{os.getcwd()}{os.sep}aiapi.yaml")
            if status:
                write_new_yaml(f"{msg}{os.sep}aiapi.yaml")

            os.remove(f"{os.getcwd()}{os.sep}aiapi.yaml")
            return status, msg, app_name
        elif is_ai_create == "n":
            status, msg, app_name = create_app(None)
            # if status:
            #     write_new_yaml(f"{msg}{os.sep}aiapi.yaml")
            break

    return status, msg, app_name


# 创建yaml模版
def create_yaml(app_name, app_version, app_desc):
    status, _token = get_token()
    if not status:
        return False, _token

    # yaml_name = input("请输入Yaml文件名:")
    # if not is_encomm_char(yaml_name):
    #     return False, "yaml文件名必须是英文"
    route_num = input("请输入有多少个接口(输入数字,不输入则1个):")
    if route_num == "":
        route_num = 1

    try:
        route_num = int(route_num)
    except Exception as _:
        return False, "请输入数字"

    route_json = {
        "swagger": "2.0",
        "info": {
            "title": app_name,
            "description": app_desc,
            "version": app_version
        },
        "paths": {}
    }
    for i in range(route_num):
        i = i + 1
        api_method = input(f"第{i}个接口的请求方式(get, post, put, delete):")
        api_name = input(f"第{i}个接口的名字,请用英文:")
        api_dec = input(f"第{i}个接口的描述:")
        parameters_end = False
        params_list = []
        while parameters_end:
            params_name = input("请输入参数名:")
            params_type = input("请输入参数类型(float, int, string):")
            params_list.append({
                "name": params_name,
                "in": "query",
                "schema": {
                    "type": params_type
                }
            })
            parameters_end = input("是否继续录入参数(y/n):")
            parameters_end = parameters_end.lower()
            if parameters_end == "y":
                parameters_end = True
            else:
                parameters_end = False
        route_json['paths'][f"/{api_name}"] = {
            api_method: {
                "summary": api_dec,
                # "parameters": params_list,
                "responses": {
                    "200": "OK"
                }
            }
        }
    yaml_data = yaml.dump(route_json, allow_unicode=True)

    return True, yaml_data

# 通过yaml直接创建APP


def create_app(yaml_file=None):
    status, _token = get_token()
    if not status:
        return False, _token, ""

    code_type = input(
        f"请输入创建编程语言{list(fix.keys())}: "
    )

    _code_type = app_all_types.get(code_type, None)
    if _code_type is None:
        return False, f"输入的编程语言的范围: {list(fix.keys())}", ""

    app_type = input(
        f"请创建应用程序类型({', '.join(app_all_types[code_type])}): "
    )

    if app_type not in app_all_types[code_type]:
        return False, f"输入应用程序的范围: {app_all_types[code_type]}", ""

    status, app_name, app_yaml, app_dir = yaml_app_info(yaml_file, app_type)
    if not status:
        return False, app_name, ""

    catc = CreateAppTypeClass(app_name, app_yaml, app_dir)
    method_of_catc = getattr(catc, f"create_{app_type}_app")
    status, msg = method_of_catc(code_type)
    return status, msg, app_name


def dev_app():
    print("测试运行....\r\n")
    run_main = input("请输入APP运行文件:")
    cwd = os.getcwd()
    # file_path = os.path.join(cwd, "ai-plugin.json")
    # file_path = Path(f'{file_path}')
    # if not file_path.exists():
    #     print("Error: dont sipiiiii project path.")
    #     sys.exit(1)

    # file_path = os.path.join(cwd, "openapi.yaml")
    # file_path = Path(f'{file_path}')
    # if not file_path.exists():
    #     return False, "Error: dont sipiiiii project path."

    file_path = os.path.join(cwd, run_main)
    file_path = Path(f'{file_path}')
    if not file_path.exists():
        return False, "错误: 不存在sipiiiii项目路径"

    status, code_type = get_app_code_type(file_path)
    if not status:
        return False, code_type

    eac = ExecAppClass(cwd, file_path, code_type)

    method_of_catc = getattr(eac, f"run_{code_type}_app")
    status, msg = method_of_catc()

    return status, msg


def localdepl(yaml_file_name):
    status, _token = get_token()
    if not status:
        return False, _token

    status, app_name, app_yaml, _ = get_app_name(yaml_file_name, True)
    if not status:
        return False, "获取应用名错误"

    app_cn_name = input("请输出应用别名:")
    if app_cn_name == "":
        app_cn_name = app_name

    print(f"本地部署: {app_name} 项目\r\n")

    description = ""
    try:
        description = app_yaml.get(
            'info', {}).get('description')
    except Exception as e:
        return False, str(e)

    outside_ip = get_outside_ip()
    if outside_ip == "":
        return False, "你无法访问互联网"

    print(f"你的外网IP: {outside_ip}")
    status, _token = get_token()
    if not status:
        return False, _token

    run_main = input("请输入APP运行文件:")

    if run_main.find(".") == 0:
        return False, "APP运行文件必须是文件名加文件后缀"

    run_main_fix = run_main.split(".")
    if len(run_main_fix) != 2:
        return False, "APP运行文件输入不合法"

    if run_main_fix[-1] not in list(fix.keys()):
        return False, f"APP运行文件不在允许的列表范围内: {list(fix.keys())}"

    app_language = [k for k, v in fix.items() if v == run_main_fix[-1]][0]

    '''
    需要两个接口
    1）本地部署上传应用信息，并且申请个二级域名
    2）通过应用名和用户EMAIL对二级域名的IP进行更新IP地址
    '''
    url = f"{server_host}/system/openapi/app/local/deployment"
    headers = {
        "Content-type": "application/json",
        "authorization": _token
    }
    data = {
        "app_name": app_name,
        "app_dock": "app",
        "app_cn_name": app_cn_name,
        "ip": outside_ip,
        "description": description,
        "app_language": app_language
    }

    response = https_post(url, json_data=data, headers=headers)
    if response.code != 200:
        return False, "内部服务器错误，请稍后再试"

    if not response.success:
        return False, response.msg

    p = multiprocessing.Process(
        target=process_update_outside_ip, args=(response.domain, _token), daemon=True)
    p.start()

    cwd = os.getcwd()
    file_path = os.path.join(cwd, run_main)
    file_path = Path(f'{file_path}')
    if not file_path.exists():
        return False, "错误: 不存在sipiiiii项目路径"

    status, code_type = get_app_code_type(file_path)
    if not status:
        return False, code_type

    eac = ExecAppClass(cwd, file_path, code_type)

    method_of_catc = getattr(eac, f"run_{code_type}_app")
    status, msg = method_of_catc()

    return status, msg


def stop_app(app_name=None):
    status, app_name, _, _ = get_app_name(app_name)
    if not status:
        return False, "获取应用名错误"

    data = {"app_name": app_name}

    status, _token = get_token()
    if not status:
        return False, _token

    headers = {
        "Content-type": "application/json",
        "authorization": _token
    }
    url = f"{server_host}/system/openapi/app/stop"
    response = https_post(url, json_data=data, headers=headers)
    if not response.success:
        return False, response.msg

    return True, response.msg


def deployed():
    status, _token = get_token()
    if not status:
        return False, _token

    headers = {
        "Content-type": "application/json",
        "authorization": _token
    }

    url = f"{server_host}/system/openapi/users/check/token"
    # response = requests.get(url,headers=headers, timeout=20)
    response = https_get(url, headers=headers)

    if not response.success:
        return False, "用户令牌无效，请登录sipiiiiii."

    if not response.data["exist"]:
        return False, "用户令牌无效或超时，请登录sipiiiiii."

    app_cn_name = input("请输入APP别名:")
    # input("please input APP docking party(chatgpt, other):")
    app_dock = "other"
    run_main = input("请输入APP运行文件:")
    # is_run_params = input("Whether there are operating parameters(y/n):")
    # is_run_params = is_run_params.lower()
    # run_params = ""
    # if is_run_params == "y":
    #     run_params = input("Please enter operating parameters")

    if app_cn_name == "" or run_main == "":
        return False, "APP别名 或者 APP运行文件的不能为空."

    if run_main.find(".") == 0:
        return False, "APP运行文件必须是文件名加文件后缀"

    run_main_fix = run_main.split(".")
    if len(run_main_fix) != 2:
        return False, "APP运行文件输入不合法"

    if run_main_fix[-1] not in list(fix.values()):
        return False, f"APP运行文件不在允许的列表范围内: {list(fix.keys())}"

    app_language = [k for k, v in fix.items() if v == run_main_fix[-1]][0]

    app_dir = os.getcwd()
    zip_file_path = zip_folder(app_dir)
    if zip_file_path is None:
        return False, "应用程序打包失败。请检查应用程序目录中是否存在异常文件或文件夹"
    filename = os.path.basename(app_dir)
    print(f"远程部署: {filename} 项目\r\n")
    # filename = ""#os.path.basename(zip_file_path)
    files = MultipartEncoder(fields={
        'file': (f"{filename}.zip", open(zip_file_path, 'rb'), 'application/octet-stream'),
    })

    url = f"{server_host}/system/openapi/app/upload"
    response = https_file(url, files=files, headers=headers)
    # response = requests.post(url, data=files, headers=headers, timeout=300)
    # print(response)
    if response['code'] != 200:
        return False, "内部服务器错误，请稍后再试"

    if not response['success']:
        return False, response['msg']

    url = f"{server_host}/system/openapi/app/deployment"
    data = {
        "file_uuid": response['data']['file_uuid'],
        "app_cn_name": app_cn_name,
        "app_language": app_language,
        "app_dock": app_dock,
        "run_main": run_main
    }
    headers['Content-type'] = "application/json"
    # headers['accept'] = 'application/json'

    response = https_post(url, json_data=data, headers=headers)
    # response = requests.post(url, data=files, headers=headers, timeout=300)
    # print(response)
    if response.code != 200:
        return False, "内部服务器错误，请稍后再试"

    if not response.success:
        return False, response.msg

    # return True, "ok"

    status, info_json, _ = get_app_info(filename)
    if not status:
        return False, "部署成功，状态获取失败"

    bar = ProgPercent(50, monitor=True)
    print("正在远程部署...\r\n")
    while True:
        status, info_json, _ = get_app_info(filename)
        if not status:
            bar.update(50)
            return False, "\r\n部署成功，状态获取失败"
        if info_json['ServerStatus'] == "close" or info_json['ServerStatus'] == "exited":
            bar.update(50)
            return True, f"\r\n应用程序部署出错，日志: \r\n{info_json['Log']}"

        if info_json['ServerStatus'] == "created" or info_json['ServerStatus'] == "running":
            bar.update(50)
            return True, f"\r\n部署成功, \r\n域名: {info_json['Domain']}"

    return True, response.data


def login(email, password):
    url = f"{server_host}/system/openapi/users/login"
    headers = {
        "Content-type": "application/json"
    }
    data = {
        "email": email,
        "password": password
    }
    # response = requests.post(url, json=data, headers=headers, timeout=20)
    response = https_post(url, json_data=data, headers=headers)
    if response.code != 200:
        return False, "服务器错误."
    if not response.success:
        return False, response.msg

    home_dir_file = os.path.join(Path.home(), ".sipitoken")
    with open(home_dir_file, 'w', encoding='utf-8') as f:
        f.write(response.data['token'])

    status, tally = get_tally()
    if status:
        return True, f"登录成功, 登录有效期3天, 剩余积分: {tally}"

    return False, "登录成功, 登录有效期3天, 获取积分失败."


def init_framework():
    aiapi_dir = get_current_path()

    # Replace 'template/template.yaml' with the path to the file you want to copy
    # src_file = f'sipiiiii{os.sep}template/template.yaml'
    src_dir = os.path.join("sipiiiii", "template")

    template_files = os.listdir(src_dir)
    for tFIle in template_files:
        src_file = os.path.join(src_dir, tFIle)

        # Use Path().resolve() to get the absolute path of the source file
        src_path = Path(src_file).resolve()

        # Use Path().joinpath() to get the destination path
        dest_path = Path(aiapi_dir).joinpath(tFIle)
        # Use Path().replace() to copy the file
        try:
            copyfile(src_path, dest_path)
        except Exception as e:
            print(str(e))
            continue

        # Check if the file was copied successfully
        if not dest_path.exists():
            continue

    return True, "初始化成功"


def get_tally():
    status, _token = get_token()
    if not status:
        return False, _token

    url = f"{server_host}/system/openapi/user/tally"
    headers = {
        "Content-type": "application/json",
        "authorization": _token
    }
    response = https_get(url, headers=headers)
    # response = requests.get(url, headers=headers, timeout=20)
    if response.code != 200:
        return False, "服务器错误."

    if not response.success:
        return False, response.msg

    return True, response.data['tally']


def restart_app(app_name):
    status, _token = get_token()
    if not status:
        return False, _token

    url = f"{server_host}/system/openapi/app/restart"
    headers = {
        "Content-type": "application/json",
        "authorization": _token
    }
    status, app_name, _, _ = get_app_name(app_name)
    if not status:
        return False, "获取应用名错误"

    response = https_post(
        url, json_data={"app_name": app_name}, headers=headers)
    if response.code != 200:
        return False, "服务器错误."

    if not response.success:
        return False, response.msg

    return True, response.msg


def delete_app(app_name):
    status, app_name, _, _ = get_app_name(app_name)
    if not status:
        return False, "获取应用名错误"

    data = {"app_name": app_name}
    status, _token = get_token()
    if not status:
        return False, _token

    headers = {
        "Content-type": "application/json",
        "authorization": _token
    }
    url = f"{server_host}/system/openapi/app/del"
    response = https_post(url, json_data=data, headers=headers)
    if not response.success:
        return False, response.msg

    return True, response.msg


def get_app_info(app_name=None):
    status, _token = get_token()
    if not status:
        return False, {}, _token

    url = f"{server_host}/system/openapi/app/status"
    headers = {
        "Content-type": "application/json",
        "authorization": _token
    }
    status, app_name, _, _ = get_app_name(app_name)
    if not status:
        return False, {}, "获取应用名错误"

    data = {"app_name": app_name}

    response = https_post(url, json_data=data, headers=headers)
    if response.code != 200:
        return False, {}, "服务器错误."

    if not response.success:
        return False, {}, response.msg

    app_info = response.data
    app_info = app_info['data']
    app_info_str = f"""
应用名称       : {app_info['AppName']}
应用别名       : {app_info['AppCnName']}
应用启动文件   : {app_info['AppRun']}
域名           : {app_info['Domain']}
应用状态       : {app_info['ServerStatus']}
创建时间       : {app_info['CreateTime']}
"""
    return True, app_info, app_info_str


def show_list():
    status, _token = get_token()
    if not status:
        return False, _token

    url = f"{server_host}/system/openapi/app/list"
    headers = {
        "Content-type": "application/json",
        "authorization": _token
    }

    #response = requests.get(url, headers=headers, timeout=20)
    response = https_get(url, headers=headers)
    if response.code != 200:
        return False, "服务器错误."

    if not response.success:
        return False, response.msg

    app_list = response.data['data']
    table = pt.PrettyTable(
        ['应用名', '应用别名', '域名', '服务状态', '应用状态', '创建时间'])
    for app in app_list:
        table.add_row((app['AppName'], app['AppCnName'], app['Domain'],
                      app['ServerStatus'], app['AppStast'], app['CreateTime']))

    return True, table


def get_cli_server_version():
    return "0.8.4"


def update_template():
    pass


def activate_account():
    status, _token = get_token()
    if not status:
        return False, _token

    headers = {
        "Content-type": "application/json",
        "authorization": _token
    }

    url = f"{server_host}/system/openapi/user/verify/code"

    response = https_get(url, headers=headers)
    if response.code != 200:
        return False, "服务器连接异常"

    if not response.success:
        return False, f"获取验证码异常: {response.msg}"

    verify_code = ""
    while True:
        try:
            verify_code = input("请输出邮件中的 6位 验证码:")
            verify_code = int(verify_code)
        except KeyboardInterrupt:
            print("\r\n")
            sys.exit(1)
        except ValueError:
            print("验证码为纯6位数字")
            continue
        if verify_code == "":
            continue
        break

    url = f"{server_host}/system/openapi/user/verify/code"

    response = https_post(
        url, json_data={"code": verify_code}, headers=headers)
    if response.code != 200:
        return False, "服务器连接异常"

    if not response.success:
        return False, f"获取验证码异常: {response.msg}"

    return True, response.msg


def register(username, email, password):
    headers = {
        "Content-type": "application/json",
    }
    url = f"{server_host}/system/openapi/user/register"

    data = {
        "username": username,
        "password": password,
        "email": email
    }

    response = https_post(url, json_data=data, headers=headers)

    if response.code != 200:
        return False, "服务器连接异常"

    if not response.success:
        return False, f"注册异常: {response.msg}"

    print(f"用户: {username} 注册成功, 注册后需要接受邮件验证码并且输入验证码后才能使用")
    print("验证码也可以之后使用 -V 进行重新验证")

    home_dir_file = os.path.join(Path.home(), ".sipitoken")
    with open(home_dir_file, 'w', encoding='utf-8') as f:
        f.write(response.data['token'])

    headers["authorization"] = response.data['token']
    url = f"{server_host}/system/openapi/user/verify/code"

    response = https_get(url, headers=headers)
    if response.code != 200:
        return False, "服务器连接异常"

    if not response.success:
        return False, f"获取验证码异常: {response.msg}"

    ststus, msg = activate_account()

    return ststus, msg
