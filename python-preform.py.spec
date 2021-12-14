# Based on spec created by pyp2rpm-3.3.7
%global pypi_name preform.py
%global pypi_version 1.1.3

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        PreForM.py, Preprocessor for Fortran poor Men

License:        GPLv3
URL:            https://github.com/szaghi/PreForM
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/PreForM.py-%{pypi_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
A very simple and stupid preprocessor for modern Fortran projects. PreForM.py
supports the most used cpp pre-processing directives and provides advanced
features typical of templating systems. Even if PreForM.py is currently
Fortran- agnostic (it being usable within any programming languages) it is
focused on Fortran programming language.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-setuptools
%description -n python3-%{pypi_name}
A very simple and stupid preprocessor for modern Fortran projects. PreForM.py
supports the most used cpp pre-processing directives and provides advanced
features typical of templating systems. Even if PreForM.py is currently
Fortran- agnostic (it being usable within any programming languages) it is
focused on Fortran programming language.

%prep
%autosetup -n PreForM.py-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# prevent trying to automatically add python3-argparse R
sed -i "/install_requires/d" setup.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%{_bindir}/PreForM.py
%{python3_sitelib}/PreForM
%{python3_sitelib}/PreForM.py-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Dec 14 2021 Frédéric Pierret (fepitre) <frederic@invisiblethingslab.com> - 1.1.3-1
- Initial package.
