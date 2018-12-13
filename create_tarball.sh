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
    cat <<-EOF > Dockerfile
    FROM centos:centos7
    RUN curl -o /etc/yum.repos.d/deps.repo https://trunk.rdoproject.org/centos7-rocky/delorean-deps.repo
    RUN yum -y install npm
    VOLUME ["/src"]
    WORKDIR /src
    CMD ["npm","install"]
    EOF
    pushd $REPONAME
        git fetch origin refs/changes/$REVIEW2/$REVIEW/$PATCHSET
        git checkout FETCH_HEAD
        sudo docker build -t ooouideps ..
        # npm install in a centos7 container
        # FIXME with SELinux enforcing fails with
        # Error: EACCES: permission denied, scandir '/src'
        sudo docker run -v $PWD:/src ooouideps
        tar czf $TARBALL node_modules
        mv $TARBALL ..
    popd
}

generate_archive
