#! /bin/bash

set -ex

REPONAME="tripleo-ui"
REPO="https://review.openstack.org/p/openstack/$REPONAME"
REVIEW=$(awk '/%global review/ { print $3 }' *spec)
REVIEW2=$(awk '/%global review/ { print substr($3,length($3)-1,2)}' *spec)
PATCHSET=$(awk '/%global patchset/ { print $3 }' *spec)
TARBALL="tripleo-ui-deps-$REVIEW.$PATCHSET.tar.gz"
NPM_VERSION=$(npm --version)
REQUIRED_NPM_VERSION="5.6.0"

function generate_archive() {
    rm -rf $REPONAME
    git clone $REPO
    pushd $REPONAME
        git fetch origin refs/changes/$REVIEW2/$REVIEW/$PATCHSET
        git checkout FETCH_HEAD
        npm install
        tar czf $TARBALL node_modules
        mv $TARBALL ..
    popd
}

function assert_correct_npm_version() {
    if [ $NPM_VERSION != $REQUIRED_NPM_VERSION ]; then
        echo 'ERROR: Wrong version of npm detected.'
        echo "ERROR: version required $REQUIRED_NPM_VERSION"
        echo "ERROR: actual version $NPM_VERSION"
        exit 1;
    fi
}

assert_correct_npm_version
generate_archive
