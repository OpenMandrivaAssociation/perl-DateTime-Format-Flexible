%define upstream_name    DateTime-Format-Flexible
%define upstream_version 0.26
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	A module that try very hard to parse string into DateTime object

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DateTime/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Factory::Util)
BuildRequires:	perl(DateTime)
BuildRequires:	perl(DateTime::Format::Builder)
BuildRequires:	perl(DateTime::Format::Strptime)
BuildRequires:	perl(DateTime::TimeZone)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Module::Pluggable)
BuildRequires:	perl(Test::Simple)
BuildRequires:	perl(Test::MockTime)

BuildArch:	noarch

# not autodetect, for some reason
Requires:	perl(Class::Factory::Util)
Requires:	perl(DateTime::Format::Strptime)

%description
If you have ever had to use a program that made you type in the date a
certain way and thought "Why can't the computer just figure out what date I
wanted?", this module is for you.

DateTime::Format::Flexible attempts to take any string you give it and
parse it into a DateTime object.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml README Changes LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/*



