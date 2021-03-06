import traceback
from .base import BasePlugin
from lib.response import BaseResponse


# 获取主机信息
class BasicPlugin(BasePlugin):
    def os_platform(self):
        if self.test_mode:
            output = 'linux'
        else:
            output = self.exec_shell_cmd('uname')
        return output.strip()

    def os_version(self):
        if self.test_mode:
            output = "CentOS release 7.4"
        else:
            output = self.exec_shell_cmd('cat /etc/issue')
        result = output.strip().split('\n')[0]
        return result

    def os_hostname(self):
        if self.test_mode:
            output = 'c1.com'
        else:
            output = self.exec_shell_cmd('hostname')
        return output

    def linux(self):
        response = BaseResponse()
        try:
            ret = {
                'os_platform': self.os_platform(),
                'os_version': self.os_version(),
                'hostname': self.os_hostname(),
            }
            response.data = ret
        except Exception as e:
            msg = '%s BasicPlugin Error:%s'
            self.logger.log(msg % (self.hostname, traceback.format_exc()), False)
            response.status = False
            response.error = msg % (self.hostname, traceback.format_exc())

        return response
