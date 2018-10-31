# Created by pyp2rpm-3.2.1
%global pypi_name webencodings

Name:           python-%{pypi_name}
Version:        0.5.1
Release:        2
Summary:        Character encoding aliases for legacy web content
Group:          Development/Python

License:        BSD
URL:            https://github.com/SimonSapin/python-webencodings
Source0:        https://files.pythonhosted.org/packages/source/w/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

BuildRequires:  python3-devel
BuildRequires:  python-setuptools
BuildRequires:  python2-pkg-resources

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

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
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
%setup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
cp -a . %{py3dir}

%build
%{__python2} setup.py build
pushd %{py3dir}
%{__python3} setup.py build
popd

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd

%files -n python2-%{pypi_name}
%doc README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
