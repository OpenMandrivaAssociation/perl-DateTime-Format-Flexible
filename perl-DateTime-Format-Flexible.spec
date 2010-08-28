%define upstream_name    DateTime-Format-Flexible
%define upstream_version 0.16

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A module that try very hard to parse string into DateTime object
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/DateTime/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::Factory::Util)
BuildRequires: perl(DateTime)
BuildRequires: perl(DateTime::Format::Builder)
BuildRequires: perl(DateTime::Format::Strptime)
BuildRequires: perl(DateTime::TimeZone)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Module::Pluggable)
BuildRequires: perl(Test::Simple)
BuildRequires: perl(Test::MockTime)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

# not autodetect, for some reason
Requires:  perl(Class::Factory::Util)
Requires:  perl(DateTime::Format::Strptime)

%description
If you have ever had to use a program that made you type in the date a
certain way and thought "Why can't the computer just figure out what date I
wanted?", this module is for you.

DateTime::Format::Flexible attempts to take any string you give it and
parse it into a DateTime object.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%doc META.yml README Changes LICENSE
%{_mandir}/man3/*
%perl_vendorlib/*
