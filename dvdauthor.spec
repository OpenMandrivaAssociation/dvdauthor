Summary:	A simple set of tools to help you author a DVD
Name:		dvdauthor
Version:	0.6.14
Release:	%mkrel 4
License:	GPL
Group:		Video
Url:		http://dvdauthor.sourceforge.net/
Source0:	http://downloads.sourceforge.net/dvdauthor/dvdauthor-%{version}.tar.gz
BuildRequires:	libxml2-devel >= 2.6.0
BuildRequires:	freetype2-devel
BuildRequires:	fribidi-devel
BuildRequires:	bison flex
BuildRequires:	png-devel
BuildRequires:	zlib-devel
BuildRequires:	imagemagick-devel
BuildRequires:	libdvdread-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A simple set of tools to help you author a DVD.
The idea is to be able to create menus, buttons, chapters, etc.
But for now you can just take an mpeg stream 
(as created by mplex -f 8 from mjpegtools 1.6.0) and write it to DVD.

%prep
%setup -q

%configure2_5x \
	--disable-rpath

%build
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dvd*
%attr(755,root,root) %{_bindir}/mpeg2desc
%attr(755,root,root) %{_bindir}/spu*
%{_mandir}/man1/*
%{_datadir}/%{name}


