# This package won't generate useful debuginfo
%global debug_package %{nil}
%global sname openstack-tripleo-ui-deps
%global commit f2820bd0cc6560cf9467cca92ff2f7d749a43fe1
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           %{sname}
Version:        8
Release:        3%{?dist}
Summary:        Source dependencies for TripleO UI
License:        ASL 2.0
URL:            http://tripleo.org

# See companion script create_tarball.sh to generate
# source tarball
Source0:        tripleo-ui-deps-%{shortcommit}.tar.gz

# Cannot build as noarch until nodejs is built from aarch64 in CBS
ExclusiveArch: x86_64

BuildRequires:  nodejs
BuildRequires:  git
Requires:       %{sname}-babel = %{version}-%{release}
Requires:       %{sname}-webpack = %{version}-%{release}

%description
Source dependencies for TripleO UI

%package babel
Summary:        Source dependencies for TripleO UI (babel)

%description babel
Source dependencies for TripleO UI (babel)

%package webpack
Summary:        Source dependencies for TripleO UI (webpack)

%description webpack
Source dependencies for TripleO UI (webpack)

%prep
%autosetup -n node_modules -S git

%build

%install
mkdir -p %{buildroot}/opt/%{name}/
cp -rf %{_builddir}/node_modules %{buildroot}/opt/%{name}/

%files
/opt/%{name}/
%exclude /opt/%{name}/node_modules/babel*
%exclude /opt/%{name}/node_modules/webpack*

%files babel
/opt/%{name}/node_modules/babel*

%files webpack
/opt/%{name}/node_modules/webpack*

%changelog
* Mon Jan 08 2018 Javier Peña <jpena@redhat.com> 8-3
- Re-created tarball using npm 3.x

* Mon Dec 4 2017 Honza Pokorny <honza@redhat.com> 8-2
- Sync w/upstream
- Upgrade react-bootstrap (stays MIT)
- Add react-overlays (MIT)
- Add react-transition-group (BSD 3-Clause)

* Thu Oct 12 2017 Honza Pokorny <honza@redhat.com> 8-1
- Sync w/upstream
- Add uuid (MIT)
- Add patternfly-react (MIT)
- Add redux-form-validators (MIT)
- Add redux-mock-store (MIT)

* Wed Aug 02 2017 Honza Pokorny <honza@redhat.com> 7-6
- Sync w/upstream
- Add eslint-plugin-prettier (MIT)
- Add axios (MIT)
- Add es6-error (MIT)

* Tue May 30 2017 Honza Pokorny <honza@redhat.com> 7-5
- Sync w/upstream
- Add react-router-dom (MIT)
- Add webpack-merge (MIT)

* Wed May 10 2017 Honza Pokorny <honza@redhat.com> 7-4
- Sync w/upstream
- Upgrade patternfly
- Upgrade React
- Add prettier (MIT)
- Add eslint-config-prettier (MIT)

* Fri Apr 7 2017 Honza Pokorny <honza@redhat.com> 7-3
- Sync w/upstream
- Upgrade webpack
- Upgrade redux-forms
- Add react-bootstrap (MIT)
- Add favicons webpack plugin (MIT)

* Wed Mar 22 2017 Honza Pokorny <honza@redhat.com> 7-2
- Sync w/upstream
- Remove karma, jasmine, phantomjs
- Add redux-form (MIT)

* Wed Mar 8 2017 Honza Pokorny <honza@redhat.com> 7-1
- Sync w/upstream
- jest (BSD-3) and babel-jest (BSD-3)

* Thu Feb 9 2017 Honza Pokorny <honza@redhat.com> 3-4
- Sync w/upstream
- Add html-webpack-plugin (MIT)

* Thu Jan 19 2017 Honza Pokorny <honza@redhat.com> 3-3
- Sync w/upstream
- Add js-yaml (MIT)

* Wed Jan 18 2017 Honza Pokorny <honza@redhat.com> 3-2
- Sync w/upstream
- Add react-cookie (MIT)

* Mon Dec 19 2016 Honza Pokorny <honza@redhat.com> 3-1
- Sync w/upstream
- Add babel-plugin-react-intl, json-loader, react-intl-po (BSD-3, MIT)

* Fri Sep 23 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 2-1
- Sync w/ upstream
- Add react-motion and react-portal (MIT)

* Thu Sep 15 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 1-3
- Use system phantomjs

* Tue Jul 26 2016 Honza Pokorny <honza@redhat.com> 1-2
- First RPM
