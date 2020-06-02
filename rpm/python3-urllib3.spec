Name:       python3-urllib3
Summary:    Powerful, sanity-friendly HTTP client for Python
Version:    1.25.9
Release:    1
License:    MIT
URL:        https://pypi.org/project/urllib3/
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.bz2
Requires:   python3-base
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
urllib3 is a powerful, sanity-friendly HTTP client for Python. Much of the Python ecosystem already uses urllib3 and you should too. urllib3 brings many critical features that are missing from the Python standard libraries.

%prep
%setup -q -n %{name}-%{version}/urllib3

%build
%{py3_build}

%install
rm -rf %{buildroot}
%{py3_install}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/urllib3
%{python3_sitelib}/urllib3-*.egg-info
