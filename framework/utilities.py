import gevent as gevent

from base_definitions import os, ROOT_DIR
from configuration.config_parse import GITHUB, OS_NAME, OS_ARCHITECTURE, OS_PLATFORM, PYTHON_VERSION


class Utilities:
    @staticmethod
    def fix_allure_properties():
        if os.path.isdir(f"{ROOT_DIR}/allure-results"):
            if os.path.exists(f"{ROOT_DIR}/allure-results/environment.properties"):
                remove_cycles = 10
                wait_interval = 1
                for _ in range(remove_cycles):
                    try:
                        os.remove(f"{ROOT_DIR}/allure-results/environment.properties")
                        break
                    except FileNotFoundError:
                        gevent.sleep(wait_interval)  # will be useful in parallel mode
        else:
            os.mkdir(f"{ROOT_DIR}/allure-results")
        f = open(f"{ROOT_DIR}/allure-results/environment.properties", "w+")
        f.write(f"Git {GITHUB}\n")
        f.write(f"OS_NAME {OS_NAME}\n")
        f.write(f"OS_ARCHITECTURE {OS_ARCHITECTURE}\n")
        f.write(f"OS_PLATFORM {OS_PLATFORM}\n")
        f.write(f"Python {PYTHON_VERSION}\n")
