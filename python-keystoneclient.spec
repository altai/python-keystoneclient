%define mod_name keystoneclient

%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

%global os_release essex

Name:             python-keystoneclient-%{os_release}
Version:          2012.1
Release:          1%{?dist}
Epoch:            1
Summary:          OpenStack Keystone Client

Group:            Development/Languages
License:          Apache 2.0
Vendor:           Grid Dynamics Consulting Services, Inc.
URL:              http://www.openstack.org
Source0:          %{name}-%{version}.tar.gz

BuildRoot:        %{_tmppath}/%{name}-%{version}

BuildArch:        noarch
BuildRequires:    python-setuptools
BuildRequires:    python-sphinx make
Requires:         python-httplib2
Requires:         python-prettytable

Requires:         python-simplejson
Requires:         python-argparse

Conflicts:        python-keystoneclient

%description
This is a client for the OpenStack Keystone API. There is a Python API (the
keystoneclient module), and a command-line script (keystone).


%package doc
Summary:        Documentation for %{name}
Group:          Documentation
Requires:       %{name} = %{epoch}:%{version}-%{release}


%description doc
Documentation for %{name}.


%prep
%setup -q -n %{name}-%{version}


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}

%{__python} setup.py install -O1 --skip-build --root %{buildroot}

make -C docs html PYTHONPATH=%{buildroot}%{python_sitelib}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README.rst LICENSE AUTHORS HACKING
%{python_sitelib}/%{mod_name}*
%{python_sitelib}/python_keystoneclient*.egg-info
%{_usr}/bin/*


%files doc
%defattr(-,root,root,-)
%doc docs/_build/html


%changelog
* Wed Jan 04 2012 Alessio Ababilov <aababilov@griddynamics.com> - 2.7
- Initial release: spec created
