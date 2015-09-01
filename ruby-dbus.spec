#
# Conditional build:
%bcond_with	tests	# "rake test"
%bcond_without	doc	# ri/rdoc documentation

Summary:        Ruby module for interaction with D-Bus
Summary(pl.UTF-8):	Moduł języka Ruby do współpracy z D-Bus
Name:		ruby-dbus
Version:	0.11.0
Release:	2
License:	LGPL v2.1+
Source0:	https://github.com/mvidner/ruby-dbus/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d53e2a07d65bff1eb65910db836cd1f2
Group:		Development/Languages
URL:		https://trac.luon.net/ruby-dbus/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildRequires:	ruby >= 1:1.9.3
%{?with_tests:BuildRequires:	ruby-rspec-core-rake_task}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby module for interaction with D-Bus.

%description -l pl.UTF-8
Moduł języka Ruby do współpracy z D-Bus.

%package rdoc
Summary:	HTML documentation for ruby-dbus
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla pakietu ruby-dbus
Group:		Documentation
Requires:	ruby >= 1:1.9.3

%description rdoc
HTML documentation for ruby-dbus.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla pakietu ruby-dbus.

%package ri
Summary:	ri documentation for ruby-dbus
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla pakietu ruby-dbus
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for ruby-dbus.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla pakietu ruby-dbus.

%prep
%setup -q

%build
# make gemspec self-contained
ruby -r rubygems -e 'spec = eval(File.read("ruby-dbus.gemspec"))
	File.open("ruby-dbus-%{version}.gemspec", "w") do |file|
	file.puts spec.to_ruby_for_cache
end'

%if %{with doc}
rdoc --ri --op ri lib
rdoc --op rdoc lib
%endif

%if %{with tests}
rake test TESTOPTS=-v
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_ridir},%{ruby_rdocdir}/%{name}-%{version}}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
%if %{with doc}
cp -a ri/DBus $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc/* $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}
%endif

install -Dp ruby-dbus-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}/ruby-dbus-%{version}.gemspec

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README.md
%{ruby_vendorlibdir}/dbus.rb
%{ruby_vendorlibdir}/dbus
%{ruby_specdir}/ruby-dbus-%{version}.gemspec

%if %{with doc}
%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/DBus
%endif
