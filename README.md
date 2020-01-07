# ubuntu_test
Basic test framework to test Ubuntu

## Tests execution
### Docker
To execute tests through docker, just turn on Docker on your machine and launch `run_docker.sh` file

### Local ubuntu run
To run tests on local ubuntu machine you need to set environment variable `pass` with you sudo password (like `export pass={sudo password}` or using `Run/Debug Configurations` in PyCharm) and switch `root` 
attribute from `False` to `True` for the `execute_sh_command` method `framework/base_methods.py`

### Framework uses Allure reports so need to install it
[Allure instruction](https://docs.qameta.io/allure/#_installing_a_commandline)

### Examples
[Video of running](https://drive.google.com/open?id=1UeT2rl0ZjVL3e2ahZB3tMcIFV6rZKOYB)

![Main page](https://drive.google.com/uc?id=1vwVTZSe_kAH6q8Jp8FPXQQsoUNoRWNG4)
![Behavior page](https://drive.google.com/uc?id=12PwW3bLnbWHmwIeMQmDNKTXfmb5KKC-U)