#!/usr/bin/env bash

. /opt/venv/bin/activate
_now=$(date +%Y-%m-%d_%H:%M:%S)
dir=$(pwd)

# Parameters
RUN_TESTS=${RUN_TESTS:=apt_get}
echo "Test run folder - $RUN_TESTS"

mkdir -p allure-results
mkdir -p allure-results/archive
mkdir -p allure-results/history

# Run The tests in project folder
echo "Running tests"
# Regular run
python3 -m py.test ${dir}/tests/${RUN_TESTS} --alluredir ${dir}/allure-results/archive/${_now}
echo "Test run finished"

## Environments settings
cp ${dir}/allure-results/environment.properties ${dir}/allure-results/archive/${_now}

## Copy previous history
mkdir ${dir}/allure-results/archive/${_now}/history
cp ${dir}/allure-results/history/*.json ${dir}/allure-results/archive/${_now}/history

## Generate allure report folder
allure generate ${dir}/allure-results/archive/${_now} -o ${dir}/allure-results/archive/${_now}/generated-report

## Saving current test run to history
rm ${dir}/allure-results/history/*
cp -r ${dir}/allure-results/archive/${_now}/generated-report/history/*.json ${dir}/allure-results/history
find . | grep -E "(__pycache__|\.pyc|\.pyo$|.pytest_cache)" | xargs rm -rf
