import paramiko
import logging


class ClientSSH:

    def __init__(self, host, port, login, passwd: str):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.port = port
        self.host = host
        self.login = login
        self.passwd = passwd

    def connect(self):
        logging.info('Connect')
        self.ssh.connect(self.host, username=self.login, password=self.passwd, port=self.port)

    def exec_command(self, str_command):
        logging.info(f'exec_command: {str_command}')
        stin, stout, ster = self.ssh.exec_command(str_command)
        return stin, stout, ster

    def close(self):
        if self.ssh is not None:
            # Needs to prevent gc error
            # https://github.com/paramiko/paramiko/issues/1078
            self.ssh.close()
        #    del ssh, stin
