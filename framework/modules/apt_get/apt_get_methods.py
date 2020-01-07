from framework.base_methods import BaseMethods


class AptGetMethods(BaseMethods):
    def install_package(self, package_name):
        return self.execute_sh_command(f'apt-get install {package_name} -y')

    def install_packages(self, packages: list):
        package_names = ' '.join([f'{_}' for _ in packages])
        return self.execute_sh_command(f'apt-get install {package_names} -y')

    def install_package_with_flag(self, package_name, flags: list):
        flag_names = ' '.join([f'--{_}' for _ in flags])
        return self.execute_sh_command(f'apt-get install {package_name} {flag_names} -y')

    def install_package_with_version(self, package_name, version):
        return self.execute_sh_command(f'apt-get install {package_name}={version} -y')

    def check_package_installed(self, package, version=''):
        packages = self.get_all_installed_packages()['out']
        return package in packages and version in version in packages

    def get_all_installed_packages(self):
        return self.execute_sh_command('apt list --installed')

    def remove_package(self, package_name):
        return self.execute_sh_command(f'apt-get remove {package_name} -y')
