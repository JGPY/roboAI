#JsonLou
import paramiko

# def test1():
#     paramiko.util.log_to_file('paramiko.log')
#     s = paramiko.SSHClient()
#     s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     s.connect(hostname=hostname, username=username, password=password)
#
#     stdin, stdout, stderr = s.exec_command('ls -l')
#     '''然后这里就有趣了。这里返回了三个流：stdin（标准输入）、stdout（标准输出）和strerr（标准错误），
#     流是不可以直接读的，得像打开一个文件那样读取，用read()或readlines()。并且，这两个函数都是一次性的，
#     也就是说，read()一次，再次read()时候结果为None，因此，需要有缓存来接住这个流：'''
#     sin, sout, serr = stdin.readlines(), stdout.readlines(), stderr.readlines()
#     print(sout)
#     '''sudo命令。这特么就是个万年大坑，不管是pexpect还是paramiko，我都栽在sudo上面好久。血泪史我就不说了，直接说解决方法吧：
#     首先，sudo后面要加一个-S选项，表示从标准输入接收密码。标准输入？咋么听起来那么耳熟？没错，
#     就是stdin，发送完命令之后要再发个密码；然后，命令的最后要加上’\n’作为命令的结束，如果没有加，
#     那么恭喜你，服务器以为你没有结束命令，还在等待，而你不知道服务器的状态，在等待它给你反馈。于是'''
#
#     stdin, stdout, stderr = s.exec_command('sudo -S %s\n'% cmd)
#     stdin.write('%s\n'% password)
#     stdin.flush()
#     out = stdout.readlines()
#     s.close()


class SshClient:

    def __init__(self):
        self.ssh_client = paramiko.SSHClient()

    def connect(self, host, user, pwd):
        self.password=pwd
        try:
            self.ssh_client.load_system_host_keys()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_client.connect(hostname=host, port=22, username=user, password=pwd)
        except Exception as e:
            print(e)

    def key_connect(self, host, user, key_file_path):
        try:
            # 允许连接不在know_hosts文件中的主机
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            private_key = paramiko.RSAKey.from_private_key_file(key_file_path)
            # 连接服务器
            self.ssh_client.connect(hostname=host, port=22, username=user, key=private_key)
        except Exception as e:
            print(e)

    def command(self, command):
        try:
            std_in, std_out, std_err = self.ssh_client.exec_command(
                command,
                get_pty=True)  # 在command命令最后加上 get_pty=True，执行多条命令 的话用；隔开，另外所有命令都在一个大的单引号范围内引用
            std_in.write(self.password + '\n')  # 执行输入命令，输入sudo命令的密码，会自动执行
            for line in std_out:
                print(line.strip('\n'))
        except Exception as e:
            print(e)
        # finally:
        #     self.ssh_client.close()

    def close(self):
        self.ssh_client.close()


if __name__ == '__main__':
    # hostname = "192.168.31.160"
    # username = "eaibot"
    # password = "eaibot"
    hostname = '192.168.31.155'
    username = 'eaibot'
    password = 'eaibot'
    try:
        Client = SshClient()
        Client.connect(hostname, username, password)
        Client.command('cd audio;python3 AudioPlay.py auidoA')
        # Client.SSHClintComm('cd audio;python3 AudioPlay.py auidoA')
    finally:
        Client.close()


''';cd /audio;sudo ;ls -l;-S python3 AudioPlay.py'''
