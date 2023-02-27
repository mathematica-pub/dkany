version="v${DKANY_VERSION}"
echo "Tagging "$DKANY_VERSION
git tag $version
git push origin $version