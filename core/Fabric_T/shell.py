from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm
from fabric.contrib.files import *
from fabric.contrib.project import rsync_project
import fabric.operations
import time, os
import logging
import base64
from getpass import getpass

# 如果需要打印log，取消下行的注释
#logging.basicConfig(level=logging.DEBUG)

# 定义三台服务器
eaibot="liu@192.168.137.203:22"


# 定义三台服务器的密码
env.passwords = {
  "eaibot": '123456',

}

# 定义一些环境变量，没有也无所谓，小细节
env.sdir="/data/soft/soft/"
env.disable_known_hosts=True
env.abort_on_prompts=True
env.skip_bad_hosts = True
env.remote_interupt = True
env.warn_only = True
env.eagerly_disconnect = True
env.gateway="liu@192.168.137.203:22"
#env.gateway="root@192.168.0.17:22"
#env.parallel=10

@task
def shell(cmd=None):
  myhost=eval(env.host)
  env.host_string=myhost
  env.password=env.passwords[myhost]
  if cmd is None:
    print("即将登陆服务器: %s"%(env.host_string))
    fabric.operations.open_shell()
  else:
    print("即将在服务器执行命令: %s"%(env.host_string))
    run(cmd)
