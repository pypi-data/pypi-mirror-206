import argparse
import getpass
import sys
from .app.version import version
from .app.new_app import *


def echo_help():
    # 显示一个帮助信息
    _log = f'''
  _____ _____ _____ _____ _____ _____ _____ _____ 
 / ____|_   _|  __ \_   _|_   _|_   _|_   _|_   _|
| (___   | | | |__) || |   | |   | |   | |   | |  
 \___ \  | | |  ___/ | |   | |   | |   | |   | |  
 ____) |_| |_| |    _| |_ _| |_ _| |_ _| |_ _| |_ 
|_____/|_____|_|   |_____|_____|_____|_____|_____|

/* 专业应用托管服务平台 */

本地客户端版本: {version}, 最新客户端版本: {get_cli_server_version()}:

用法: sipiiiii [选项]

  显示帮助信息:
    sipiiiii -h 或 --help

  账号管理:
    登录你的sipiiiii账号, 登录后token有消息为3天:
      sipiiiii -L 或 --login

    注册一个sipiiiii账号:
      sipiiiii -S 或 --register

    邮件激活你的sipiiiii账号, 每个激活后的账号将赠送10积分:
      sipiiiii -A 或 --activate

    查看你的剩余积分:
      sipiiiii -t 或 --tally

  应用部署:
    运行应用(非部署)，在应用目录下直接运行:
      sipiiiii -d 或 --dev

    本地化部署应用，不需要上传代码到我们的部署服务器，在本地部署一个应用，并且我们提供一个二级域名解析到你的外网IP
    每部署一个本地应用将消耗5积分, 一个应用名只扣除一次积分:
      sipiiiii -LD <app name> 或 --localdepl <app name>
      sipiiiii -LD <test.yaml> 或 --localdepl <test.yaml>

    部署你的应用，将在我们的部署服务器中运行，并且我们提供一个二级域名解析
    每部署一个远程应用将消耗20积分, 一个应用名只扣除一次积分:
      sipiiiii -D 或 --deployed

  应用生成:
    根据 yaml 模版和选项创建一个应用框架
    有三种方式创建应用
    1) 根据自己提供的yaml文件创建应用
    2) 使用aiapi的模版创建应用
    3) 使用向导模式创建应用
      sipiiiii -n <test.yaml> 或 --new <test.yaml>

  应用管理:
    列出你的应用列表:
      sipiiiii -l 或 --list

    查看你的应用详情:
      sipiiiii -i <app name> 或 --info <app name>
      sipiiiii -i <test.yaml> 或 --info <test.yaml>

    停止你正在运行的应用(非本地部署):
      sipiiiii -s <app name> 或 --stop <app name>
      sipiiiii -s <test.yaml> 或 --stop <test.yaml>

    重启你的应用(非本地部署):
      sipiiiii -r <app name> 或 --restart <app name>
      sipiiiii -r <test.yaml> 或 --restart <test.yaml>
      
    删除你的应用(非本地部署):
      sipiiiii -DE <app name> 或 --delete <app name>
      sipiiiii -DE <test.yaml> 或 --delete <test.yaml>

  示例:
    sipiiiii -n test.yaml
    sipiiiii -LD test.yaml
    sipiiiii -LD your-app-name
    sipiiiii -D
    sipiiiii -L
    sipiiiii -i your-app-name

'''
    return _log


def main():
    parser = argparse.ArgumentParser(description='说明', add_help=False)
    parser.add_argument('-h', '--help', help='说明文档',
                        required=False, nargs='?', const='default_value')
    parser.add_argument('-n', '--new', help='根据应用模版创建应用',
                        required=False, nargs='?', const='default_value')
    parser.add_argument('-d', '--dev', help='运行应用(非部署)',
                        required=False, nargs='?', const='default_value')
    parser.add_argument('-D', '--deployed', help='部署应用',
                        required=False, nargs='?', const='default_value')
    parser.add_argument('-L', '--login', help='登录',
                        required=False, nargs='?', const='default_value')
    parser.add_argument('-R', '--register', help='注册',
                        required=False, nargs='?', const='default_value')
    parser.add_argument('-A', '--activate', help='激活账号',
                        required=False, nargs='?', const='default_value')
    parser.add_argument('-l', '--list', help='获取你的应用列表',
                        required=False, nargs='?', const='default_value')
    parser.add_argument('-t', '--tally', help='查看积分',
                        required=False, nargs='?', const='default_value')
    parser.add_argument('-i', '--info', help='显示应用信息',
                        required=False, nargs='?', const='default_value')
    parser.add_argument('-s', '--stop', help='停止应用',
                        required=False, nargs='?', const='default_value')
    parser.add_argument('-r', '--restart', help='重启应用',
                        required=False, nargs='?', const='default_value')
    parser.add_argument('-DE', '--delete', help='删除应用',
                        required=False, nargs='?', const='default_value')
    parser.add_argument('-LD', '--localdepl', help='本地部署应用',
                        required=False, nargs='?', const='default_value')
    args = vars(parser.parse_args())

    if args is None:
        print(echo_help())
        if version != get_cli_server_version():
            print("pip install sipiiiii")
        sys.exit(1)

    if args['deployed']:
        # execute deployed code here
        _, msg = deployed()
        print(msg)

    elif args['dev']:
        # execute dev code here
        _, msg = dev_app()
        print(msg)

    elif args['new']:
        # execute new code here
        status = False
        msg = ""
        if args['new'] == "default_value":
            status, msg = create_app_project()
        else:
            status, msg = create_app(args['new'])

        print(msg)

    elif args['login']:
        email = input("输入你的email:")
        password = getpass.getpass('输入你的密码:')
        if email == "" or email is None:
            print("没有输入email.")
            sys.exit(1)
        if password == "" or password is None:
            print("没有输入密码.")
            sys.exit(1)

        _, msg = login(email, password)
        print(msg)
    elif args['register']:
        username = input("请输入你的用户名:")
        email = input("输入你的email:")
        password = getpass.getpass('输入你的密码:')
        if username == "" or username is None:
            print("没有输入用户名.")
            sys.exit(1)
        if email == "" or email is None:
            print("没有输入email.")
            sys.exit(1)
        if password == "" or password is None:
            print("没有输入密码.")
            sys.exit(1)
        _, msg = register(username, email, password)

        print(msg)
    elif args['activate']:
        _, msg = activate_account()
        print(msg)

    elif args['list']:
        _, apps = show_list()
        print(apps)
    elif args['tally']:
        status, tally = get_tally()
        if not status:
            print(tally)
        else:
            print(f"你的积分: {tally}")

    elif args['info']:
        status = False
        app_info = ""
        if args['info'] == "default_value":
            status, _, app_info = get_app_info()
        else:
            status, _, app_info = get_app_info(args['info'])

        print(app_info)
    elif args['stop']:
        status = False
        msg = ""
        if args['stop'] == "default_value":
            status, msg = stop_app(None)
        else:
            status, msg = stop_app(args['stop'])

        print(msg)
    elif args['restart']:
        status = False
        msg = ""
        if args['restart'] == "default_value":
            status, msg = restart_app(None)
        else:
            status, msg = restart_app(args['restart'])

        print(msg)
    elif args['delete']:
        status = False
        msg = ""
        if args['delete'] == "default_value":
            status, msg = delete_app(None)
        else:
            status, msg = delete_app(args['delete'])

        print(msg)
    elif args['localdepl']:
        status = False
        msg = ""
        if args['localdepl'] == "default_value":
            status, msg = localdepl(None)
        else:
            status, msg = localdepl(args['localdepl'])

        print(msg)

    elif args['help']:
        print(echo_help())
    else:
        print(echo_help())
        if version != get_cli_server_version():
            print("\r\npip install sipiiiii")


if __name__ == "__main__":
    main()
