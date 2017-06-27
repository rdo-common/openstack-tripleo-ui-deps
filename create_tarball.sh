#! /bin/bash

set -ex

ARCH=$(uname --hardware-platform)
REPONAME="tripleo-ui"
REPO="https://github.com/openstack/$REPONAME"
COMMIT=`awk '/%global commit/ { print $3 }' *spec`
SHORT_COMMIT=${COMMIT:0:7}
TARBALL="tripleo-ui-deps-$SHORT_COMMIT-$ARCH.tar.gz"

function generate_archive() {
    rm -rf $REPONAME
    git clone $REPO
    pushd $REPONAME
        git checkout $SHORT_COMMIT
        npm install
        tar czf $TARBALL node_modules
        mv $TARBALL ..
    popd
}

generate_archive
