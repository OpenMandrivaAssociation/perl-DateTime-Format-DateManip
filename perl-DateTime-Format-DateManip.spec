%define upstream_name    DateTime-Format-DateManip
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

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

