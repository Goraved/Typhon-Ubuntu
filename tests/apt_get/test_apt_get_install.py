import allure
import pytest
from allure_commons._allure import step

from tests.apt_get import AptGetBase


@allure.suite('Install')
class TestAptGetInstall(AptGetBase):
    new_version = '0.30.0-3ubuntu2'
    old_version = '0.30.0-3ubuntu1'

    @allure.title('Positive installation package')
    @pytest.mark.parametrize('prepare_package', [['gparted']], indirect=True)
    def test_success_install_app(self, prepare_package):
        with step('Install package'):
            result = self.apt_get_methods.install_package(prepare_package[0])
        with step('Check no error present'):
            assert not result['err']
        with step('Check package installed'):
            assert self.apt_get_methods.check_package_installed(prepare_package[0])

    @allure.title('Reinstall app with higher version')
    @pytest.mark.parametrize('prepare_package', [['gparted']], indirect=True)
    def test_install_app_with_higher_version(self, prepare_package):
        with step('Install package'):
            self.apt_get_methods.install_package_with_version(prepare_package[0], self.old_version)
        with step('Reinstall package with higher version'):
            result = self.apt_get_methods.install_package_with_version(prepare_package[0], self.new_version)
        with step('Check no error present'):
            assert not result['err']
        with step('Check package installed'):
            assert self.apt_get_methods.check_package_installed(prepare_package[0], version=self.new_version)

    @allure.title('Reinstall app with lower version')
    @pytest.mark.parametrize('prepare_package', [['gparted']], indirect=True)
    def test_install_app_with_lower_version(self, prepare_package):
        with step('Install package'):
            self.apt_get_methods.install_package_with_version(prepare_package[0], self.new_version)
        with step('Reinstall package with lower version'):
            result = self.apt_get_methods.install_package_with_version(prepare_package[0], self.old_version)
        with step('Check error present without allowing downgrades'):
            assert 'Packages were downgraded and -y was used without --allow-downgrades' in result['err']
        with step('Check no error present with allowing downgrades'):
            result = self.apt_get_methods.install_package_with_flag(
                f'{prepare_package[0]}={self.old_version}', ['allow-downgrades'])
            assert not result['err']
        with step('Check package installed'):
            assert self.apt_get_methods.check_package_installed(prepare_package[0], version=self.old_version)

    @allure.title('Reinstall app with the same version')
    @pytest.mark.parametrize('prepare_package', [['gparted']], indirect=True)
    def test_install_app_with_same_version(self, prepare_package):
        with step('Install package'):
            self.apt_get_methods.install_package_with_version(prepare_package[0], self.new_version)
        with step('Reinstall package with the same version'):
            result = self.apt_get_methods.install_package_with_version(prepare_package[0], self.new_version)
        with step('Check no error present'):
            assert not result['err']
        with step('Check package installed'):
            assert self.apt_get_methods.check_package_installed(prepare_package[0], version=self.new_version)

    @allure.title('Install app with unknown version')
    @pytest.mark.parametrize('prepare_package', [['gparted']], indirect=True)
    def test_install_app_with_unknown_version(self, prepare_package):
        version = '3.66'
        with step('Install package with unknown version'):
            result = self.apt_get_methods.install_package_with_version(prepare_package[0], version)
        with step('Check correct error present'):
            assert f"Version '{version}' for '{prepare_package[0]}' was not found" in result[
                'err'], 'Wrong error message'

    @allure.title('Install unknown package')
    @pytest.mark.parametrize('prepare_package', [['asdzcx']], indirect=True)
    def test_unknown_app(self, prepare_package):
        with step('Install unknown package'):
            result = self.apt_get_methods.install_package(prepare_package[0])
        with step('Check correct error present'):
            assert f'Unable to locate package {prepare_package[0]}' in result['err'], 'Wrong error message'

    @allure.title('Install empty package')
    def test_empty_app(self):
        with step('Install empty package'):
            result = self.apt_get_methods.install_package('')
        with step('Check correct error present'):
            assert '0 newly installed' in result['out'], 'Wrong message'

    @pytest.mark.parametrize('prepare_package', [['gparted', 'gnome-weather']], indirect=True)
    @allure.title('Install several packages at once')
    def test_several_apps(self, prepare_package):
        with step('Install package'):
            result = self.apt_get_methods.install_packages(prepare_package)
        with step('Check no error present'):
            assert not result['err']
        with step('Check package installed'):
            for package in prepare_package:
                assert self.apt_get_methods.check_package_installed(package)

    @pytest.mark.parametrize('prepare_package', [['gparted']], indirect=True)
    @allure.title('Install package with flag')
    def test_app_with_flag(self, prepare_package):
        with step('Install package with flag'):
            result = self.apt_get_methods.install_package_with_flag(prepare_package[0], ['quiet'])
        with step('Check no error present'):
            assert not result['err']
        with step('Check package installed'):
            assert self.apt_get_methods.check_package_installed(prepare_package[0])

    @pytest.mark.parametrize('prepare_package', [['gparted']], indirect=True)
    @allure.title('Install package with wrong flag')
    def test_app_with_wrong_flag(self, prepare_package):
        flag = 'wrong_flag'
        with step('Install package with flag'):
            result = self.apt_get_methods.install_package_with_flag(prepare_package[0], [flag])
        with step('Check correct error present'):
            assert f'Command line option --{flag} is not understood in combination with the other options' \
                   in result['err'], 'Wrong message'
