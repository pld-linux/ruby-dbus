%define pkgname dbus
Summary:	Ruby module for interaction with D-Bus
Summary(pl.UTF-8):	Moduł języka Ruby do współpracy z D-Bus
Name:		ruby-%{pkgname}
Version:	0.25.0
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages
Source0:	https://rubygems.org/downloads/ruby-%{pkgname}-%{version}.gem
# Source0-md5:	69aae2c116fd92887d742446f2b4f2b7
URL:		https://github.com/mvidner/ruby-dbus
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
Requires:	ruby-logger
Requires:	ruby-rexml
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby module for interaction with D-Bus.

%description -l pl.UTF-8
Moduł języka Ruby do współpracy z D-Bus.

%prep
%setup -q -n ruby-%{pkgname}-%{version}

%build
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p ruby-%{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{ruby_vendorlibdir}/dbus.rb
%{ruby_vendorlibdir}/dbus
%{ruby_specdir}/ruby-%{pkgname}-%{version}.gemspec
