%define upstream_name    DateTime-Format-DateManip
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:    Perl DateTime extension to convert
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/DateTime/%{upstream_name}-%{upstream_version}.tar.gz
# patch from https://rt.cpan.org/Public/Bug/Display.html?id=55771
Patch0:     perl-DateTime-Format-DateManip-fix_tests.diff

BuildRequires: perl(Carp)
BuildRequires: perl(Date::Manip)
BuildRequires: perl(DateTime)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
DateTime::Format::DateManip is a class that knows how to convert between
'Date::Manip' dates and durations and 'DateTime' and 'DateTime::Duration'
objects. Recurrences are note yet supported.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p0
%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.40.0-2mdv2011.0
+ Revision: 654909
- rebuild for updated spec-helper

* Wed May 05 2010 Michael Scherer <misc@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 542675
- import perl-DateTime-Format-DateManip


* Wed May 05 2010 cpan2dist 0.04-1mdv
- initial mdv release, generated with cpan2dist
