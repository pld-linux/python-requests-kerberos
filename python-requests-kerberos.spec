#
# Conditional build:
%bcond_with	tests	# unit tests (not in sdist)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Kerberos authentication handler for python-requests
Summary(pl.UTF-8):	Obsługa uwierzytelniania Kerberos dla python-requests
Name:		python-requests-kerberos
# keep 0.12.x here for python2 support
Version:	0.12.0
Release:	1
License:	ISC
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/requests-kerberos/
Source0:	https://files.pythonhosted.org/packages/source/r/requests-kerberos/requests-kerberos-%{version}.tar.gz
# Source0-md5:	51060bc1a7ea8bb2816194619efd7003
Patch0:		requests-kerberos-requires.patch
URL:		https://pypi.org/project/requests-kerberos/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-cryptography >= 1.3
BuildRequires:	python-kerberos >= 1.1.8
BuildRequires:	python-kerberos < 2
BuildRequires:	python-mock
BuildRequires:	python-requests >= 1.1.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-cryptography >= 1.3
BuildRequires:	python3-kerberos >= 1.1.8
BuildRequires:	python3-kerberos < 2
BuildRequires:	python3-requests >= 1.1.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Requests is an HTTP library, written in Python, for human beings. This
library adds optional Kerberos/GSSAPI authentication support and
supports mutual authentication.

%description -l pl.UTF-8
Requests to biblioteka HTTP, napisana w Pythonie dla ludzi. Niniejsza
biblioteka dodaje opcjonalną obsługę uwierzytelniania Kerberos/GSSAPI
i obsługuje wzajemne uwierzytelnianie.

%package -n python3-requests-kerberos
Summary:	Kerberos authentication handler for python3-requests
Summary(pl.UTF-8):	Obsługa uwierzytelniania Kerberos dla python3-requests
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-requests-kerberos
Requests is an HTTP library, written in Python, for human beings. This
library adds optional Kerberos/GSSAPI authentication support and
supports mutual authentication.

%description -n python3-requests-kerberos -l pl.UTF-8
Requests to biblioteka HTTP, napisana w Pythonie dla ludzi. Niniejsza
biblioteka dodaje opcjonalną obsługę uwierzytelniania Kerberos/GSSAPI
i obsługuje wzajemne uwierzytelnianie.

%prep
%setup -q -n requests-kerberos-%{version}
%patch -P0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m unittest discover -s test_requests_kerberos
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s test_requests_kerberos
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS HISTORY.rst LICENSE README.rst
%{py_sitescriptdir}/requests_kerberos
%{py_sitescriptdir}/requests_kerberos-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-requests-kerberos
%defattr(644,root,root,755)
%doc AUTHORS HISTORY.rst LICENSE README.rst
%{py3_sitescriptdir}/requests_kerberos
%{py3_sitescriptdir}/requests_kerberos-%{version}-py*.egg-info
%endif
