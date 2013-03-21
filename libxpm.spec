%define major 4
%define libxpm %mklibname xpm %{major}
%define develxpm %mklibname -d xpm

Name:		libxpm
Summary:	X Pixmap Library
Version:	3.5.10
Release:	1
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXpm-%{version}.tar.bz2
Patch0:		libxpm-aatch64.patch

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xt)
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1

%description
The xpm package contains the XPM pixmap library for the X Window
System. The XPM library allows applications to display color,
pixmapped images, and is used by many popular X programs.

%package -n %{libxpm}
Summary:	X Pixmap Library
Group:		Development/X11
Conflicts:	libxorg-x11 < 7.0
Provides:	%{name} = %{version}

%description -n %{libxpm}
The xpm package contains the XPM pixmap library for the X Window
System. The XPM library allows applications to display color,
pixmapped images, and is used by many popular X programs.

%files -n %{libxpm}
%{_libdir}/libXpm.so.%{major}*

%package -n %{develxpm}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libxpm} = %{version}
Requires:	pkgconfig(x11)
Provides:	libxpm-devel = %{version}-%{release}
Provides:	xpm-devel = %{version}-%{release}
Obsoletes:	%{_lib}xpm4-devel < 3.5.10
Obsoletes:	%{_lib}xpm-static-devel < 3.5.10
Conflicts:	libxorg-x11-devel < 7.0

%description -n %{develxpm}
Development files for %{name}

%files -n %{develxpm}
%{_bindir}/cxpm
%{_bindir}/sxpm
%{_libdir}/libXpm.so
%{_libdir}/pkgconfig/xpm.pc
%{_includedir}/X11/xpm.h
%{_mandir}/man1/*

%prep
%setup -qn libXpm-%{version}
%apply_patches

%build
%configure2_5x \
    --x-includes=%{_includedir} \
    --x-libraries=%{_libdir} \
    --disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%changelog
* Thu Mar 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.5.9-5
+ Revision: 783371
- Remove pre scriptlet to correct rpm upgrade moving from /usr/X11R6.

* Tue Dec 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 3.5.9-4
+ Revision: 745641
- rebuild to obsolete orphaned static pkg

* Mon Dec 05 2011 Zé <ze@mandriva.org> 3.5.9-3
+ Revision: 737925
- clean defattr, BR, clean section and mkrel
- disabled static files
- clean .la files

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 3.5.9-2
+ Revision: 660303
- mass rebuild

* Sat Oct 30 2010 Thierry Vignaud <tv@mandriva.org> 3.5.9-1mdv2011.0
+ Revision: 590419
- new release

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 3.5.8-2mdv2010.1
+ Revision: 520323
- rebuild

* Mon Nov 09 2009 Thierry Vignaud <tv@mandriva.org> 3.5.8-1mdv2010.1
+ Revision: 463605
- new release

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 3.5.7-5mdv2010.0
+ Revision: 425932
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 3.5.7-4mdv2009.0
+ Revision: 223081
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert build requires.

* Tue Jan 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 3.5.7-3mdv2008.1
+ Revision: 152806
- Update BuildRequires and rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 3.5.7-1mdv2008.0
+ Revision: 69338
- new release

* Sun Jul 15 2007 Olivier Thauvin <nanardon@mandriva.org> 3.5.6-2mdv2008.0
+ Revision: 52220
- fix requirements
- improve file list

* Thu Jul 12 2007 Funda Wang <fwang@mandriva.org> 3.5.6-1mdv2008.0
+ Revision: 51494
- New version


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 20:17:57 (31598)
- X11R7.1

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 19:54:51 (26912)
- fixed more dependencies

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

