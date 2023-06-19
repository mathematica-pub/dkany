#!/bin/bash

if [[ -z $(which python | grep virtual) ]]; then
    echo "Error: not running from virtual env"
    echo "USAGE: pipenv run bash scripts/publish_package.sh"
    exit 1
fi

aws_profile=$(aws configure list-profiles | grep devops)
if [ -z "$aws_profile" ]
then
    echo "The profile ${aws_profile} has not been established.  Using default."
    aws_profile="default"
else
    echo "AWS_PROFILE=${aws_profile}"
fi

pipenv sync --dev

python setup.py sdist bdist_wheel

# note: you may have to configure a region as well. add the following to ~/.aws/config
# [profile devops]
# region = us-east-1

AWS_PROFILE=$aws_profile aws codeartifact login --tool twine \
    --domain shared-package-domain \
    --domain-owner 922539530544 \
    --repository shared-package-repository

# lists all compiled distributions, parses the version, sorts, and only keeps the last result.
latest_distribution=$(ls dist/dkany-*.tar.gz | awk -F"-" '{print $NF, $0}' | sort -V | tail -n 1 | awk '{print $2}')

python -m twine upload --repository codeartifact $latest_distribution --verbose