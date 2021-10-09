Summary:	A simple set of tools to help you author a DVD
Name:		dvdauthor
Version:	0.7.2
Release:	6
License:	GPLv2
Group:		Video
Url:		http://dvdauthor.sourceforge.net/
Source0:	https://github.com/ldo/dvdauthor/archive/%{version}.tar.gz
Source1:	http://www.joonet.de/dvdauthor/ftp/%{name}-doc-0.6.17.tar.gz
Patch0:		dvdauthor-0.7.2-compile.patch

BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	docbook-utils docbook-dtds
BuildRequires:	pkgconfig(dvdread)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(fribidi)
BuildRequires:	pkgconfig(ImageMagick) > 7.0
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(zlib)

%description
A simple set of tools to help you author a DVD. The idea is to be able to
create menus, buttons, chapters, etc. But for now you can just take an mpeg
stream (as created by mplex -f 8 from mjpegtools 1.6.0) and write it to DVD.

N.B. The system-wide default video format is NTSC, to change it modify 
/etc/video_format; for per user specific settings creat ~/.config/video_format
and put the video format you want (NTSC or PAL) there.

%prep
%setup -q -a 1
%autopatch -p1

mv %{name}-doc-0.6.17/html .

mkdir autotools
cp %{_datadir}/gettext/config.rpath autotools/
autoreconf -fi

%build
%configure
%make_build

%install
%make_install

# (ahmad) Starting from 0.7, dvdauthor doesn't specify a default video format
# previoulsy it defaulted to NTSC
mkdir -p %{buildroot}%{_sysconfdir}
cat > %{buildroot}%{_sysconfdir}/video_format << EOF
NTSC
EOF

%files
%doc AUTHORS README ChangeLog COPYING INSTALL TODO html
%{_sysconfdir}/video_format
%{_bindir}/dvdauthor
%{_bindir}/dvddirdel
%{_bindir}/dvdunauthor
%{_bindir}/mpeg2desc
%{_bindir}/spumux
%{_bindir}/spuunmux
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_mandir}/man7/*
