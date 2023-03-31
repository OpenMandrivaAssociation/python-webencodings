%global pypi_name webencodings

Name:           python-%{pypi_name}
Version:        0.5.1
Release:        5
Summary:        Character encoding aliases for legacy web content
Group:          Development/Python

License:        BSD
URL:            https://github.com/SimonSapin/python-webencodings
Source0:        https://files.pythonhosted.org/packages/source/w/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python-setuptools

%description
python-webencodings
===================

This is a Python implementation of the
`WHATWG Encoding standard
<http://encoding.spec.whatwg.org/>`_.

* Latest
documentation: http://packages.python.org/webencodings/
* Source code and issue
tracker:
  https://github.com/gsnedders/python-webencodings
* PyPI releases:
http://pypi.python.org/pypi/webencodings
* License: BSD
* Python 2.6+ and 3.3+
In ...

%prep
%autosetup -p1
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
python setup.py build

%install
python setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info
