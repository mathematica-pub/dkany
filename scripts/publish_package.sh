if [[ -z $(which python | grep virtual) ]]; then
    echo "Error: not running from virtual env"
    echo "USAGE: pipenv run bash scripts/publish_package.sh"
    exit 1
fi

pipenv sync --dev

python setup.py sdist bdist_wheel

aws codeartifact login --tool twine \
    --domain shared-package-domain \
    --domain-owner 922539530544 \
    --repository shared-package-repository

twine upload --repository codeartifact \
    dist/dkany-0.0.12.tar.gz --verbose