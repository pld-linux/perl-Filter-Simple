#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Filter
%define		pnam	Simple
Summary:	Filter::Simple Perl module - simplified source filtering
Summary(pl.UTF-8):	Moduł Perla Filter::Simple - uproszczone filtrowanie
Name:		perl-Filter-Simple
Version:	0.82
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3defebcbbc969a5b05f1d37422f86a3a
%if %{with tests}
BuildRequires:	perl-Filter
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Filter::Simple module provides a simplified interface to
Filter::Util::Call; one that is sufficient for most common cases.

%description -l pl.UTF-8
Moduł Filter::Simple daje uproszczony interfejs do Filter::Util::Call,
wystarczający w większości przypadków.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/Filter
%{perl_vendorlib}/Filter/Simple.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
