#!/bin/bash
#
# Perform code style checks of the Python code.
export PIPENV_VERBOSITY=-1
set -e

echo "--- black ---"
pipenv run black --line-length 88 --check python/src/easy-learn/
pipenv run black --line-length 88 --check python/src/test/
echo "--- isort ---"
pipenv run isort python/src/easy-learn/ --multi-line 3 --profile black --check
pipenv run isort python/src/test/ --multi-line 3 --profile black --check
echo "--- flake8 ---"
pipenv run flake8 python/src/easy-learn/
pipenv run flake8 python/src/test/
echo "--- pytest ---"
if [[ "$OSTYPE" == "msys" ]]; then
  PYTHONPATH="./python/src/main;$PYTHONPATH" pipenv run pytest python/src/test/
else
  PYTHONPATH=./python/src/main:$PYTHONPATH pipenv run pytest python/src/test/
fi
