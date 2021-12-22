%global     plugin_name build-flow-test-aggregator
%global     debug_package %{nil}
Name:       jenkins-in-house-plugins-%{plugin_name}
Version:    1.3
Release:    4%{?dist}
Summary:    A jenkins in-house plugins %{plugin_name}.hpi
Obsoletes:  jenkins-upstream-plugins-%{plugin_name} <= %{version}
Requires:   jenkins
Group:      Development/Libraries
License:    BSD
URL:        https://github.com/gooddata/%{plugin_name}
Source0:    %{name}.tar.gz

BuildRequires: java
BuildRequires: maven

%description
Packaged jenkins-in-house-plugin-%{plugin_name} %{plugin_name}.hpi file

%prep
%setup -n %{name} -c

%build
mvn versions:set -DnewVersion=%{version}
mvn versions:commit
mvn package

%install
%{__mkdir_p} %{buildroot}%{_sharedstatedir}/juseppe
%{__cp} target/%{plugin_name}.hpi %{buildroot}%{_sharedstatedir}/juseppe/

%files
%defattr(-,root,root,-)
%dir %{_sharedstatedir}/juseppe
%{_sharedstatedir}/juseppe/%{plugin_name}.hpi

%changelog
* Wed Dec 22 2021 +0700 Manh Ha <manh.ha@gooddata.com> - 1.3-4
- CONFIG: SETI-6576 support el8
- Added repositories and pluginRepositories config for pom.xml
- Bump version for build-flow-test-aggregator to 4 to override previous version

* Thu Apr 23 2020 +0700 Hien Tran <hien.tran@gooddata.com> - 1.3-3
- CONFIG: SETI-4077 remove obsoletes package in spec file

* Mon Apr 13 2020 +0700 Hien Tran <hien.tran@gooddata.com> - 1.3-2
- CONFIG: SETI-4077 add build-flow-test-aggregator.spec and Makefile

* Fri Sep 8 2017 +0700 Hung Cao Hiep <hung.cao@gooddata.com> - 1.3-1
- CONFIG: PAAS-11278 Add build-flow-test-aggregator plugin
