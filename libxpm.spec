%define major 4
%define libxpm %mklibname xpm %{major}
%define develxpm %mklibname -d xpm
%define staticdevelxpm %mklibname -d -s xpm

Name: libxpm
Summary:  X Pixmap Library
Version: 3.5.7
Release: %mkrel 3
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXpm-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: libxt-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
The xpm package contains the XPM pixmap library for the X Window
System. The XPM library allows applications to display color,
pixmapped images, and is used by many popular X programs.

#-----------------------------------------------------------

%package -n %{libxpm}
Summary:  X Pixmap Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxpm}
The xpm package contains the XPM pixmap library for the X Window
System. The XPM library allows applications to display color,
pixmapped images, and is used by many popular X programs.

#-----------------------------------------------------------

%package -n %{develxpm}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libxpm} = %{version}
Requires: libx11-devel >= 1.0.0
Provides: libxpm-devel = %{version}-%{release}
Provides: xpm-devel = %{version}-%{release}
Obsoletes: %{libxpm}-devel

Conflicts: libxorg-x11-devel < 7.0

%description -n %{develxpm}
Development files for %{name}

%pre -n %{develxpm}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{develxpm}
%defattr(-,root,root)
%{_bindir}/cxpm
%{_bindir}/sxpm
%{_libdir}/libXpm.so
%{_libdir}/libXpm.la
%{_libdir}/pkgconfig/xpm.pc
%{_includedir}/X11/xpm.h
%{_mandir}/man1/*

#-----------------------------------------------------------

%package -n %{staticdevelxpm}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develxpm} >= %{version}
Provides: libxpm-static-devel = %{version}-%{release}
Provides: xpm-static-devel = %{version}-%{release}
Obsoletes: %{libxpm}-static-devel

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{staticdevelxpm}
Static development files for %{name}

%files -n %{staticdevelxpm}
%defattr(-,root,root)
%{_libdir}/libXpm.a

#-----------------------------------------------------------

%prep
%setup -q -n libXpm-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -n %{libxpm} -p /sbin/ldconfig
%postun -n %{libxpm} -p /sbin/ldconfig

%files -n %{libxpm}
%defattr(-,root,root)
%{_libdir}/libXpm.so.%{major}*
