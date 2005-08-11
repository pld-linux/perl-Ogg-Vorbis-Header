#
# Conditional build:
%bcond_without	tests           # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Ogg
%define	pnam	Vorbis-Header
Summary:	Ogg::Vorbis::Header - an object-oriented interface to Ogg Vorbis information and comment fields
Summary(pl):	Ogg::Vorbis::Header - zorientowany obiektowo interfejs do pól informacji i komentarza Ogg Vorbis
Name:		perl-Ogg-Vorbis-Header
Version:	0.03
Release:	1
License:	GPL v2+ / LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d1c435e79d3f019147be734281e8a908
URL:		http://www.cpan.org/modules/by-module/Ogg/
BuildRequires:	perl-Inline-C
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module presents an object-oriented interface to Ogg Vorbis files
which allows user to view Vorbis info and comments and to modify or
add comments.

%description -l pl
Modu³ ten dostarcza zorientowanego obiektowo interfejsu do plików Ogg
Vorbis. Pozwala u¿ytkownikowi na odczyt/modyfikacjê pól informacji
i komentarzy plików Ogg Vorbis.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Ogg/Vorbis/Header.pm
%{_mandir}/man3/*
