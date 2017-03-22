%global sname openstack-tripleo-ui-deps
%global commit ad6314526b80f656b4807ed0f537f3a089c9b87c
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           %{sname}
Version:        7
Release:        1%{?dist}
Summary:        Source dependencies for TripleO UI
License:        ASL 2.0
URL:            http://tripleo.org

# The source for this package was pulled from git.  Use the following commands
# to generate the tarball.
#
#   $ git clone https://github.com/openstack/tripleo-ui.git
#   $ cd tripleo-ui
#   $ git checkout %{commit}
#   $ npm install
#   $ tar czf tripleo-ui-deps-%{shortcommit}.tar.gz node_modules
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
