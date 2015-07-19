%define major 4
%define libname %mklibname xpm %{major}
%define devname %mklibname -d xpm

Summary:	X Pixmap Library
Name:		libxpm
Version:	3.5.11
Release:	9
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXpm-%{version}.tar.bz2
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xt)

%description
The xpm package contains the XPM pixmap library for the X Window
System. The XPM library allows applications to display color,
pixmapped images, and is used by many popular X programs.

%package -n %{libname}
Summary:	X Pixmap Library
Group:		Development/X11
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
The xpm package contains the XPM pixmap library for the X Window
System. The XPM library allows applications to display color,
pixmapped images, and is used by many popular X programs.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	xpm-devel = %{version}-%{release}

%description -n %{devname}
Development files for %{name}

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
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXpm.so.%{major}*

%files -n %{devname}
%{_bindir}/cxpm
%{_bindir}/sxpm
%{_libdir}/libXpm.so
%{_libdir}/pkgconfig/xpm.pc
%{_includedir}/X11/xpm.h
%{_mandir}/man1/*

