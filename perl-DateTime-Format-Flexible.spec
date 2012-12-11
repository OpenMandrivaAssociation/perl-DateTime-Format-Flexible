%define upstream_name    DateTime-Format-Flexible
%define upstream_version 0.19

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	A module that try very hard to parse string into DateTime object
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
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


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.190.0-3mdv2011.0
+ Revision: 657774
- rebuild for updated spec-helper
- rebuild for updated spec-helper

* Sat Jan 08 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.190.0-1mdv2011.0
+ Revision: 630621
- update to new version 0.19

* Sun Jan 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.180.0-1mdv2011.0
+ Revision: 627501
- update to new version 0.18

* Mon Nov 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.170.0-1mdv2011.0
+ Revision: 595098
- update to new version 0.17

* Sat Aug 28 2010 Jérôme Quelin <jquelin@mandriva.org> 0.160.0-1mdv2011.0
+ Revision: 573855
- adding missing buildrequires:
- update to 0.16

* Thu May 06 2010 Michael Scherer <misc@mandriva.org> 0.150.0-3mdv2011.0
+ Revision: 543061
- fix Requires

* Thu May 06 2010 Michael Scherer <misc@mandriva.org> 0.150.0-2mdv2010.1
+ Revision: 543037
- fix Requires

* Thu May 06 2010 Michael Scherer <misc@mandriva.org> 0.150.0-1mdv2010.1
+ Revision: 542953
- fix BR, missing for test, 2nd
- fix BR, missing for test
- import perl-DateTime-Format-Flexible


* Thu May 06 2010 cpan2dist 0.15-1mdv
- initial mdv release, generated with cpan2dist
