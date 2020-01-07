import allure

from framework.modules.apt_get.apt_get_methods import AptGetMethods
from tests import TestBase


@allure.feature('apt-get')
class AptGetBase(TestBase):
    def setup(self):
        self.apt_get_methods = AptGetMethods()
