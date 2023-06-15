if [[ -z $(which python | grep virtual) ]]; then
    echo "Error: not running from virtual env"
    echo "USAGE: pipenv run bash scripts/publish_package.sh"
    exit 1
fi

pipenv sync --dev

python setup.py sdist bdist_wheel

aws codeartifact login --tool twine \
    --domain dil-domain \
    --domain-owner 803461793753 \
    --repository dil-repository

twine upload --repository codeartifact \
    dist/dkany-0.0.12.tar.gz