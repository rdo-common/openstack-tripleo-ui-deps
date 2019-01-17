#! /bin/bash

set -ex

REPONAME="tripleo-ui"
REPO="https://review.openstack.org/p/openstack/$REPONAME"
REVIEW=$(awk '/%global review/ { print $3 }' *spec)
REVIEW2=$(awk '/%global review/ { print substr($3,length($3)-1,2)}' *spec)
PATCHSET=$(awk '/%global patchset/ { print $3 }' *spec)
TARBALL="tripleo-ui-deps-$REVIEW.$PATCHSET.tar.gz"
USER_ID=$(id -u)


function generate_archive() {
    rm -rf $REPONAME
    git clone $REPO
    cat <<-EOF > Dockerfile
FROM centos:centos7
RUN curl -o /etc/yum.repos.d/deps.repo https://trunk.rdoproject.org/centos7-rocky/delorean-deps.repo
RUN yum -y install npm
WORKDIR /src
RUN chown -R $USER_ID:0 /src  && chmod -R ug+rwX /src
CMD npm install && tar czf $TARBALL node_modules
USER $USER_ID
EOF
    # Configure cache settings not write outside our workdir
    cp npmrc $PWD/$REPONAME/.npmrc
    # Fix SELinux context so we can write in the mounted
    # volume within the container
    chcon -Rt svirt_sandbox_file_t $PWD/$REPONAME
    sudo docker build -t ooouideps .
    sudo docker run -v $PWD/$REPONAME:/src ooouideps
    mv $PWD/$REPONAME/$TARBALL .
}

generate_archive
