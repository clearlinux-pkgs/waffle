#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : waffle
Version  : 1.7.0
Release  : 5
URL      : https://gitlab.freedesktop.org/mesa/waffle/-/archive/v1.7.0/waffle-v1.7.0.tar.gz
Source0  : https://gitlab.freedesktop.org/mesa/waffle/-/archive/v1.7.0/waffle-v1.7.0.tar.gz
Summary  : a library for selecting an OpenGL API and window system at runtime
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause BSL-1.0
Requires: waffle-bin = %{version}-%{release}
Requires: waffle-data = %{version}-%{release}
Requires: waffle-lib = %{version}-%{release}
Requires: waffle-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-egl)
BuildRequires : pkgconfig(wayland-protocols)

%description
CMOCKA
=======
cmocka is a fork for Google's cmockery unit testing framework to fix bugs and
support it in future.
See https://code.google.com/p/cmockery/

%package bin
Summary: bin components for the waffle package.
Group: Binaries
Requires: waffle-data = %{version}-%{release}
Requires: waffle-license = %{version}-%{release}

%description bin
bin components for the waffle package.


%package data
Summary: data components for the waffle package.
Group: Data

%description data
data components for the waffle package.


%package dev
Summary: dev components for the waffle package.
Group: Development
Requires: waffle-lib = %{version}-%{release}
Requires: waffle-bin = %{version}-%{release}
Requires: waffle-data = %{version}-%{release}
Provides: waffle-devel = %{version}-%{release}
Requires: waffle = %{version}-%{release}

%description dev
dev components for the waffle package.


%package doc
Summary: doc components for the waffle package.
Group: Documentation

%description doc
doc components for the waffle package.


%package lib
Summary: lib components for the waffle package.
Group: Libraries
Requires: waffle-data = %{version}-%{release}
Requires: waffle-license = %{version}-%{release}

%description lib
lib components for the waffle package.


%package license
Summary: license components for the waffle package.
Group: Default

%description license
license components for the waffle package.


%prep
%setup -q -n waffle-v1.7.0
cd %{_builddir}/waffle-v1.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1615935978
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/waffle
cp %{_builddir}/waffle-v1.7.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/waffle/0e246ef78dd737260342ed614266ee175827fcba
cp %{_builddir}/waffle-v1.7.0/third_party/cmocka/COPYING %{buildroot}/usr/share/package-licenses/waffle/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/waffle-v1.7.0/third_party/cmocka/cmake/Modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/waffle/ff3ed70db4739b3c6747c7f624fe2bad70802987
cp %{_builddir}/waffle-v1.7.0/third_party/getopt/LICENSE %{buildroot}/usr/share/package-licenses/waffle/56e79db23f145740b0801606cfce363eb0f10284
cp %{_builddir}/waffle-v1.7.0/third_party/threads/LICENSE %{buildroot}/usr/share/package-licenses/waffle/93b512a1720f0df65d3908744080a92813893add
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/wflinfo

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/wflinfo

%files dev
%defattr(-,root,root,-)
/usr/include/waffle-1/waffle.h
/usr/include/waffle-1/waffle_gbm.h
/usr/include/waffle-1/waffle_glx.h
/usr/include/waffle-1/waffle_version.h
/usr/include/waffle-1/waffle_wayland.h
/usr/include/waffle-1/waffle_x11_egl.h
/usr/lib64/cmake/Waffle/WaffleConfig.cmake
/usr/lib64/cmake/Waffle/WaffleConfigVersion.cmake
/usr/lib64/libwaffle-1.so
/usr/lib64/pkgconfig/waffle-1.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/waffle1/HACKING.txt
/usr/share/doc/waffle1/LICENSE-threads.txt
/usr/share/doc/waffle1/LICENSE.txt
/usr/share/doc/waffle1/README.md
/usr/share/doc/waffle1/examples/Makefile.example
/usr/share/doc/waffle1/examples/gl_basic.c
/usr/share/doc/waffle1/examples/simple-x11-egl.c
/usr/share/doc/waffle1/release-notes/waffle-0.1.txt
/usr/share/doc/waffle1/release-notes/waffle-0.2.txt
/usr/share/doc/waffle1/release-notes/waffle-0.3.0.txt
/usr/share/doc/waffle1/release-notes/waffle-0.3.1.txt
/usr/share/doc/waffle1/release-notes/waffle-1.0.0.txt
/usr/share/doc/waffle1/release-notes/waffle-1.0.1.txt
/usr/share/doc/waffle1/release-notes/waffle-1.1.0.txt
/usr/share/doc/waffle1/release-notes/waffle-1.1.1.txt
/usr/share/doc/waffle1/release-notes/waffle-1.1.2.txt
/usr/share/doc/waffle1/release-notes/waffle-1.2.0.txt
/usr/share/doc/waffle1/release-notes/waffle-1.2.1.txt
/usr/share/doc/waffle1/release-notes/waffle-1.2.2.txt
/usr/share/doc/waffle1/release-notes/waffle-1.3.0.txt
/usr/share/doc/waffle1/release-notes/waffle-1.4.0.txt
/usr/share/doc/waffle1/release-notes/waffle-1.4.1.txt
/usr/share/doc/waffle1/release-notes/waffle-1.4.2.txt
/usr/share/doc/waffle1/release-notes/waffle-1.4.3.txt
/usr/share/doc/waffle1/release-notes/waffle-1.4.4.txt
/usr/share/doc/waffle1/release-notes/waffle-1.5.0.txt
/usr/share/doc/waffle1/release-notes/waffle-1.5.1.txt
/usr/share/doc/waffle1/release-notes/waffle-1.5.2.txt
/usr/share/doc/waffle1/release-notes/waffle-1.6.0.md
/usr/share/doc/waffle1/release-notes/waffle-1.6.1.md
/usr/share/doc/waffle1/release-notes/waffle-1.6.2.md
/usr/share/doc/waffle1/release-notes/waffle-1.6.3.md

%files lib
%defattr(-,root,root,-)
/usr/lib64/libwaffle-1.so.0
/usr/lib64/libwaffle-1.so.0.7.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/waffle/0e246ef78dd737260342ed614266ee175827fcba
/usr/share/package-licenses/waffle/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/waffle/56e79db23f145740b0801606cfce363eb0f10284
/usr/share/package-licenses/waffle/93b512a1720f0df65d3908744080a92813893add
/usr/share/package-licenses/waffle/ff3ed70db4739b3c6747c7f624fe2bad70802987
