DKANY_VERSION='0.0.8'
version="v${DKANY_VERSION}"
echo "Tagging "$DKANY_VERSION
git tag $version
git push origin $version