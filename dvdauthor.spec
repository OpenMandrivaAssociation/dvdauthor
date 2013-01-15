Summary:	A simple set of tools to help you author a DVD
Name:		dvdauthor
Version:	0.7.1
Release:	1
License:	GPLv2
Group:		Video
Url:		http://dvdauthor.sourceforge.net/
Source0:	http://heanet.dl.sourceforge.net/project/dvdauthor/dvdauthor/%version/dvdauthor-%version.tar.gz
Source1:	http://www.joonet.de/dvdauthor/ftp/%{name}-doc-0.6.17.tar.gz
Patch0:		dvdauthor-imagemagick-0.7.0.patch
Patch1:		dvdauthor-0.7.1-automake-1.13.patch
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(fribidi)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	zlib-devel
BuildRequires:	pkgconfig(ImageMagick)
BuildRequires:	pkgconfig(dvdread)
BuildRequires:	gettext-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex

%track
prog %name = {
	url = http://sourceforge.net/projects/dvdauthor/files/
	regex = %name-(__VER__)\.tar\.gz
	version = %version
}

%description
A simple set of tools to help you author a DVD. The idea is to be able to
create menus, buttons, chapters, etc. But for now you can just take an mpeg
stream (as created by mplex -f 8 from mjpegtools 1.6.0) and write it to DVD.

N.B. The system-wide default video format is NTSC, to change it modify 
/etc/video_format; for per user specific settings creat ~/.config/video_format
and put the video format you want (NTSC or PAL) there.

%prep
%setup -q -n %{name} -a 1
%patch0 -p0
%patch1 -p1 -b .automake113~

autoreconf -fi

mv %{name}-doc-0.6.17/html .

%build
%configure2_5x --disable-rpath
%make

%install
%makeinstall_std

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
%{_mandir}/man1/*
%{_datadir}/%{name}


%changelog
* Sun Nov 13 2011 Oden Eriksson <oeriksson@mandriva.com> 0.7.0-3mdv2012.0
+ Revision: 730470
- sync with fedora

* Wed Nov 10 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.7.0-2mdv2011.0
+ Revision: 595688
- Starting from 0.7, dvdauthor doesn't specify a default video format (previoulsy
  it defaulted to NTSC), so we set the default format to NTSC in /etc/video_format.
  o The user can modify /etc/video_format to change the system-wide value
  o The user can use ~/.config/video_format to set per user settings

* Mon Oct 25 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.7.0-1mdv2011.0
+ Revision: 589275
- update to 0.7.0
- rediff patch0

* Sat Jul 10 2010 Funda Wang <fwang@mandriva.org> 0.6.18-2mdv2011.0
+ Revision: 550004
- rebuild for new imagemagick

* Thu Mar 18 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.6.18-1mdv2010.1
+ Revision: 524957
- new upstream release 0.6.18
- drop FriBidi patches, merged upstream
- rediff imagemagick patch
- back to sourceforge url, now it's up-to-date

* Thu Jan 14 2010 Funda Wang <fwang@mandriva.org> 0.6.17-2mdv2010.1
+ Revision: 491444
- rebuild for new imagemagick

* Tue Jan 05 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.6.17-1mdv2010.1
+ Revision: 486421
- update to 0.6.17
- switch to new "unofficial" upstream http://www.joonet.de/dvdauthor/
- clean spec
- fix license
- add patches to fix build with FriBidi-0.19.x
- add html docs in package

* Wed Jan 28 2009 Götz Waschk <waschk@mandriva.org> 0.6.14-9mdv2009.1
+ Revision: 335005
- rebuild for new libmagick

* Mon Sep 01 2008 Götz Waschk <waschk@mandriva.org> 0.6.14-8mdv2009.0
+ Revision: 278246
- rebuild for new libdvdread

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.6.14-7mdv2009.0
+ Revision: 244562
- rebuild

* Thu Feb 14 2008 Oden Eriksson <oeriksson@mandriva.com> 0.6.14-5mdv2008.1
+ Revision: 167713
- fix build
- added a patch to make it compile
- rebuilt against new imagemagick libs

* Tue Jan 08 2008 Oden Eriksson <oeriksson@mandriva.com> 0.6.14-4mdv2008.1
+ Revision: 146497
- rebuilt against new imagemagick libs (6.3.7)

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jun 07 2007 Anssi Hannula <anssi@mandriva.org> 0.6.14-3mdv2008.0
+ Revision: 36143
- rebuild with correct optflags

* Mon May 07 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.6.14-1mdv2008.0
+ Revision: 24817
- Updated to 0.6.14.


* Sat Feb 24 2007 Emmanuel Andry <eandry@mandriva.org> 0.6.13-2mdv2007.0
+ Revision: 125334
- rebuild for latest ImageMagick

* Fri Feb 09 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.13-1mdv2007.1
+ Revision: 118333
- Import dvdauthor

