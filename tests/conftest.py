import pytest

from framework.modules.apt_get.apt_get_methods import AptGetMethods


@pytest.fixture(scope='function', autouse=False)
def prepare_package(request):
    apt_get_methods = AptGetMethods()
    if not request.param:
        raise Exception('Empty package attribute')
    packages = request.param
    yield packages
    for package in packages:
        apt_get_methods.remove_package(package)
