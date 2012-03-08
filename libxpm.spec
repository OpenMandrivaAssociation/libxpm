%define major 4
%define libxpm %mklibname xpm %{major}
%define develxpm %mklibname -d xpm

Name: libxpm
Summary:  X Pixmap Library
Version: 3.5.9
Release: 5
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXpm-%{version}.tar.bz2

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: libxt-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
The xpm package contains the XPM pixmap library for the X Window
System. The XPM library allows applications to display color,
pixmapped images, and is used by many popular X programs.

%package -n %{libxpm}
Summary:  X Pixmap Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxpm}
The xpm package contains the XPM pixmap library for the X Window
System. The XPM library allows applications to display color,
pixmapped images, and is used by many popular X programs.

%files -n %{libxpm}
%{_libdir}/libXpm.so.%{major}*

%package -n %{develxpm}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libxpm} = %{version}
Requires: libx11-devel >= 1.0.0
Provides: libxpm-devel = %{version}-%{release}
Provides: xpm-devel = %{version}-%{release}
Obsoletes: %{_lib}xpm4-devel
Obsoletes: %{_lib}xpm-static-devel
Conflicts: libxorg-x11-devel < 7.0

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

%build
%configure2_5x \
    --x-includes=%{_includedir} \
    --x-libraries=%{_libdir} \
    --disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std

