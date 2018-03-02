#! /bin/bash

set -ex

REPONAME="tripleo-ui"
REPO="https://review.openstack.org/p/openstack/$REPONAME"
REVIEW=$(awk '/%global review/ { print $3 }' *spec)
REVIEW2=$(awk '/%global review/ { print substr($3,length($3)-1,2)}' *spec)
PATCHSET=$(awk '/%global patchset/ { print $3 }' *spec)
TARBALL="tripleo-ui-deps-$REVIEW.$PATCHSET.tar.gz"

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

generate_archive
