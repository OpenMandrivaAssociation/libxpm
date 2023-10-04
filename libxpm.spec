# libXpm is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif

%define major 4
%define libname %mklibname xpm %{major}
%define devname %mklibname -d xpm
%define lib32name libxpm%{major}
%define dev32name libxpm-devel

Summary:	X Pixmap Library
Name:		libxpm
Version:	3.5.17
Release:	1
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXpm-%{version}.tar.xz
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	gzip
BuildRequires:	ncompress
%if %{with compat32}
BuildRequires:	libc6
BuildRequires:	devel(libX11)
BuildRequires:	devel(libXext)
BuildRequires:	devel(libXt)
BuildRequires:	devel(libxcb)
BuildRequires:	devel(libXau)
BuildRequires:	devel(libXdmcp)
%endif

%description
The xpm package contains the XPM pixmap library for the X Window
System. The XPM library allows applications to display color,
pixmapped images, and is used by many popular X programs.

%package -n %{libname}
Summary:	X Pixmap Library
Group:		Development/X11

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
Development files for %{name}.

%package -n %{lib32name}
Summary:	X Pixmap Library (32-bit)
Group:		Development/X11

%description -n %{lib32name}
The xpm package contains the XPM pixmap library for the X Window
System. The XPM library allows applications to display color,
pixmapped images, and is used by many popular X programs.

%package -n %{dev32name}
Summary:	Development files for %{name} (32-bit)
Group:		Development/X11
Requires:	%{lib32name} = %{version}-%{release}
Requires:	%{devname} = %{version}-%{release}

%description -n %{dev32name}
Development files for %{name}.

%prep
%autosetup -n libXpm-%{version} -p1
export CONFIGURE_TOP="$(pwd)"

%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif

mkdir build
cd build
%configure

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

%files -n %{libname}
%{_libdir}/libXpm.so.%{major}*

%files -n %{devname}
%{_bindir}/cxpm
%{_bindir}/sxpm
%{_libdir}/libXpm.so
%{_libdir}/pkgconfig/xpm.pc
%{_includedir}/X11/xpm.h
%doc %{_mandir}/man?/*

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libXpm.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/libXpm.so
%{_prefix}/lib/pkgconfig/xpm.pc
%endif
