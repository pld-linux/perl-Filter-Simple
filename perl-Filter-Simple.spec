%include	/usr/lib/rpm/macros.perl
%define		pdir	Filter
%define		pnam	Simple
Summary:	Filter::Simple Perl module - simplified source filtering
Summary(pl):	Modu³ Perla Filter::Simple - uproszczone filtrowanie
Name:		perl-Filter-Simple
Version:	0.78
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Filter
BuildRequires:	perl-Parse-RecDescent
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Filter::Simple module provides a simplified interface to
Filter::Util::Call; one that is sufficient for most common cases.
	
%description -l pl
Modu³ Filter::Simple daje uproszczony interfejs do Filter::Util::Call,
wystarczaj±cy w wiêkszo¶ci przypadków.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

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
%doc Changes README
%dir %{perl_vendorlib}/Filter
%{perl_vendorlib}/Filter/Simple.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
