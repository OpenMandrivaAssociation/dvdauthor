Summary:	A simple set of tools to help you author a DVD
Name:		dvdauthor
Version:	0.6.18
Release:	%mkrel 1
License:	GPLv2
Group:		Video
Url:		http://dvdauthor.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/dvdauthor/dvdauthor/%{version}/%{name}-%{version}.tar.gz
Source1:	http://www.joonet.de/dvdauthor/ftp/%{name}-doc-0.6.17.tar.gz
Patch0:		dvdauthor-imagemagick-0.6.18.patch
BuildRequires:	libxml2-devel >= 2.6.0
BuildRequires:	freetype2-devel
BuildRequires:	fribidi-devel
BuildRequires:	bison flex
BuildRequires:	png-devel
BuildRequires:	zlib-devel
BuildRequires:	imagemagick-devel
BuildRequires:	libdvdread-devel
BuildRequires:	autoconf automake gettext-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A simple set of tools to help you author a DVD. The idea is to be able to
create menus, buttons, chapters, etc. But for now you can just take an mpeg
stream (as created by mplex -f 8 from mjpegtools 1.6.0) and write it to DVD.

%prep

%setup -q -n %{name} -a 1
%patch0 -p0

autoreconf -fi

mv %{name}-doc-0.6.17/html .

%build
%configure2_5x --disable-rpath
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS README ChangeLog COPYING INSTALL TODO html
%{_bindir}/dvdauthor
%{_bindir}/dvddirdel
%{_bindir}/dvdunauthor
%{_bindir}/mpeg2desc
%{_bindir}/spumux
%{_bindir}/spuunmux
%{_mandir}/man1/*
%{_datadir}/%{name}
