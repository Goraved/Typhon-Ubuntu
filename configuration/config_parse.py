import configparser
import platform

from base_definitions import os, ROOT_DIR

global_config = configparser.ConfigParser()
global_config.read_file(open(f'{os.path.dirname(os.path.abspath(__file__))}/global.ini'))

# Environment settings
OS_NAME = platform.system()
OS_VERSION = platform.version()
OS_ARCHITECTURE = platform.architecture()
PROJECT = global_config.get('ENVIRONMENT', 'project')
LINK_TYPE_TEST_CASE = global_config.get('ENVIRONMENT', 'link_type_test_case')
LINK_TYPE_LINK = global_config.get('ENVIRONMENT', 'link_type_link')
TEST_CASE = global_config.get('ENVIRONMENT', 'test_case')
BUG = global_config.get('ENVIRONMENT', 'bug')
GITHUB = global_config.get('ENVIRONMENT', 'git_path')
