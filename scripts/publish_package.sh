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

python -m twine upload --repository codeartifact \
    dist/dkany-0.0.12.tar.gz --verbose