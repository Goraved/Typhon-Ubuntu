import os
import subprocess

import allure

from framework.utilities import Utilities


class BaseMethods:
    properties = False

    def __init__(self):
        # Gather info for Allure environment block
        if not self.properties:
            Utilities.fix_allure_properties()
            self.properties = True

    @staticmethod
    @allure.step('Execute sh command')
    def execute_sh_command(command, root=False):
        err, output = '', ''
        try:
            if root:
                command = f'echo {os.getenv("pass")}|sudo -S {command}'
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, timeout=30,
                                             encoding='utf-8')
        except subprocess.CalledProcessError as exc:
            err = exc.output
            print("Status : FAIL", exc.returncode, err)
        else:
            print("Output: \n{}\n".format(output))
        return {'out': output, 'err': err}

    @staticmethod
    def get_logs(path):
        logs = BaseMethods.execute_sh_command(f'cat {path}')
        if logs['err']:
            raise Exception('Failed to get logs')
        else:
            return logs['out']
